import pyvex

bitwidthOp = {'Iop_8Uto16','Iop_8Uto32','Iop_8Uto64','Iop_16Uto32', 'Iop_16Uto64','Iop_32Uto64','Iop_8Sto16', 'Iop_8Sto32','Iop_8Sto64','Iop_16Sto32', 'Iop_16Sto64','Iop_32Sto64',
            'Iop_64to8','Iop_32to8','Iop_64to16','Iop_16to8','Iop_16HIto8','Iop_8HLto16','Iop_32to16','Iop_32HIto16','Iop_16HLto32','Iop_64to32','Iop_64HIto32','Iop_32HLto64',
            'Iop_128to64','Iop_128HIto64','Iop_64HLto128','Iop_Not1','Iop_32to1','Iop_64to1','Iop_1Uto8','Iop_1Uto32','Iop_1Uto64','Iop_1Sto8','Iop_1Sto16','Iop_1Sto32','Iop_1Sto64'}


# Remove IMark and AbiHint
def ClearMinus(block): # block is a list of IR stmt
    i = 0
    while (i < len(block)):
        stmt = block[i]
        delFlag = False
        if ((stmt.tag == 'Ist_IMark') | (stmt.tag == 'Ist_AbiHint')):
            block.remove(block[i])
            delFlag = True
        if (not delFlag):
            i += 1
    
    return block

# Remove redundant write to the same reg
def RemoveRedunantWrite(block): # block is a list of IR stmt
    block.reverse()
    i = 0
    for stmt in block:
        i += 1
        if stmt.tag == 'Ist_Put':
            reg = stmt.offset
            getSet = set()
            subBlock = block[i:]

            for preStmt in subBlock:

                if preStmt.tag == 'Ist_WrTmp':
                    if preStmt.data.tag == 'Iex_Get':
                        getSet.add(preStmt.data.offset)

                elif preStmt.tag == 'Ist_Put':
                    if preStmt.offset == reg:
                        if (reg in getSet):
                            break
                        else:
                            block.remove(preStmt)
                            continue
    
    block.reverse()
    return block

# Combine same operations (add32, add64, ...) (optional)



# Remove bitwidth and endianness operation
def RemoveBitwidth(block):
    for i in range(0, len(block)):
        stmt = block[i]
        if stmt.tag == 'Ist_WrTmp':
            if stmt.data.tag == 'Iex_Unop':
                if (stmt.data.op in bitwidthOp):
                    block[i].data = stmt.data.args[0]
    
    return block

# Copy Propagation
def RemoveCopy(block):
    copyDict = {}
    i = 0

    while (i < len(block)):
        stmt = block[i]
        delFlag = False

        if stmt.tag == 'Ist_WrTmp':
            wrTmp = pyvex.expr.RdTmp.get_instance(stmt.tmp)

            # delete the copy link
            if (copyDict.get(wrTmp)): 
                del copyDict[wrTmp]

            # add the copy link and remove the copy stmt
            if (stmt.data.tag == 'Iex_RdTmp'):
                refTmp = stmt.data
                while(copyDict.get(refTmp)):
                    refTmp = copyDict.get(refTmp)
                copyDict[wrTmp] = refTmp
                block.remove(block[i])
                delFlag = True
            # replace the copied tmp for WrTmp
            elif ((stmt.data.tag == 'Iex_Unop') | (stmt.data.tag == 'Iex_Binop') | (stmt.data.tag == 'Iex_Triop') | (stmt.data.tag == 'Iex_Qop') | (stmt.data.tag == 'Iex_CCall')):
                args = stmt.data.args
                for j in range(0, len(args)):
                    if (copyDict.get(args[j])):
                        block[i].data.args[j] = copyDict[args[j]]
            # replace the copied tmp for Load
            elif stmt.data.tag == 'Iex_Load':
                tmp = stmt.data.addr
                if (copyDict.get(tmp)):
                    block[i].data.addr = copyDict[tmp]

            # GET
            elif stmt.data.tag == 'Iex_Get':
                refTmp = stmt.data.offset
                while(copyDict.get(refTmp)):
                    refTmp = copyDict.get(refTmp)
                copyDict[wrTmp] = refTmp
                block.remove(block[i])
                delFlag = True

        # replace the copied tmp for Store
        elif stmt.tag == 'Ist_Store':
            tmp = stmt.addr
            if (copyDict.get(tmp)):
                block[i].addr = copyDict[tmp]

        # Put
        elif (stmt.tag == 'Ist_Put'):
            regOffset = stmt.offset
            # delete the copy link
            if (copyDict.get(regOffset)):
                del copyDict[regOffset]
            
            # add link
            if stmt.data.tag == 'Iex_RdTmp':
                refTmp = stmt.data
                while(copyDict.get(refTmp)):
                    refTmp = copyDict.get(refTmp)
                copyDict[regOffset] = refTmp
                block.remove(block[i])
                delFlag = True
    
        # replace the copied tmp for Exit
        elif stmt.tag == 'Ist_Exit':
            if stmt.guard.tag == 'Iex_RdTmp':
                if (copyDict.get(stmt.guard)):
                    block[i].guard = copyDict[stmt.guard]

        if (not delFlag):
            i += 1
    
    return block

# Constant folding
def ConstFolding(block):
    constMapping = {}
    i = 0

    while (i < len(block)):
        stmt = block[i]
        delFlag = False

        # Put
        if (stmt.tag == 'Ist_Put'):
            regOffset = stmt.offset
            if stmt.data.tag == 'Iex_Const':
                constMapping[regOffset] = stmt.data
                block.remove(block[i])
                delFlag = True
            elif stmt.data.tag == 'Iex_RdTmp':
                if (constMapping.get(stmt.data)):
                    constMapping[regOffset] = constMapping[stmt.data]
                    block.remove(block[i])
                    delFlag = True

        elif stmt.tag == 'Ist_WrTmp':
            wrTmp = pyvex.expr.RdTmp.get_instance(stmt.tmp)

            # delete mapping
            if (constMapping.get(wrTmp)):
                del constMapping[wrTmp]

            # add mapping
            if stmt.data.tag == 'Iex_Const':
                constMapping[wrTmp] = stmt.data
                block.remove(block[i])
                delFlag = True
            
            # replace tmp with const for WrTmp
            elif stmt.data.tag == 'Iex_RdTmp':
                if (constMapping.get(stmt.data)):
                    block[i].data = constMapping[stmt.data]
            elif ((stmt.data.tag == 'Iex_Unop') | (stmt.data.tag == 'Iex_Binop') | (stmt.data.tag == 'Iex_Triop') | (stmt.data.tag == 'Iex_Qop') | (stmt.data.tag == 'Iex_CCall')):
                args = stmt.data.args
                for j in range(0, len(args)):
                    if (constMapping.get(args[j])):
                        block[i].data.args[j] = constMapping[args[j]]
            elif stmt.data.tag == 'Iex_Load':
                addr = stmt.data.addr
                if (constMapping.get(addr)):
                    block[i].data.addr = constMapping[addr]

        # replace tmp for Store
        elif stmt.tag == 'Ist_Store':
            if (constMapping.get(stmt.addr)):
                block[i].addr = constMapping[stmt.addr]
            if (constMapping.get(stmt.data)):
                block[i].data = constMapping[stmt.data]

        # replace tmp for Exit
        elif stmt.tag == 'Ist_Exit':
            if stmt.guard.tag == 'Iex_RdTmp':
                if (constMapping.get(stmt.guard)):
                    block[i].guard = constMapping[stmt.guard]

        if (not delFlag):
            i += 1

    return block

# Get-Get Elimination (maybe?)

# Load-Load Elimination
def LLEliminate(block):
    loadedMapping = {}
    tmpMapping = {}
    i = 0

    while(i < len(block)):
        delFlag = False
        stmt = block[i]

        if stmt.tag == 'Ist_WrTmp':
            wrTmp = pyvex.expr.RdTmp.get_instance(stmt.tmp)

            # delete mapping
            if (tmpMapping.get(wrTmp)):
                del tmpMapping[wrTmp]
            if (wrTmp in loadedMapping.values()):
                for key in loadedMapping.keys():
                    if loadedMapping[key] == wrTmp:
                        del loadedMapping[key]
                        break
            
            # add mapping
            if stmt.data.tag == 'Iex_Load':
                loadAddr = stmt.data.addr
                if (loadedMapping.get(loadAddr)):
                    tmpMapping[wrTmp] = loadedMapping[loadAddr]
                    block.remove(block[i])
                    delFlag = True
                else:
                    loadedMapping[loadAddr] = wrTmp

            elif stmt.data.tag == 'Iex_Rdtmp':
                if (tmpMapping.get(stmt.data)):
                    block[i].data = tmpMapping[stmt.data]
            elif ((stmt.data.tag == 'Iex_Unop') | (stmt.data.tag == 'Iex_Binop') | (stmt.data.tag == 'Iex_Triop') | (stmt.data.tag == 'Iex_Qop') | (stmt.data.tag == 'Iex_CCall')):
                args = stmt.data.args
                for j in range(0, len(args)):
                    if (tmpMapping.get(args[j])):
                        block[i].data.args[j] = tmpMapping[args[j]]

        #replace tmp for store
        elif stmt.tag == 'Ist_Store':
            if (tmpMapping.get(stmt.addr)):
                block[i].addr = tmpMapping[stmt.addr]
            if (tmpMapping.get(stmt.data)):
                block[i].data = tmpMapping[stmt.data]

        # replace tmp for put
        elif (stmt.tag == 'Ist_Put'):
            if stmt.data.tag == 'Iex_RdTmp':
                if (tmpMapping.get(stmt.data)):
                    block[i].data = tmpMapping[stmt.data]

        # replace tmp for Exit
        elif stmt.tag == 'Ist_Exit':
            if stmt.guard.tag == 'Iex_RdTmp':
                if (tmpMapping.get(stmt.guard)):
                    block[i].guard = tmpMapping[stmt.guard]

        if (not delFlag):
            i += 1

    return block

# Load-Store Elimination
def LSEliminate(block):
    i = 0
    loadedSet = set()

    while (i < len(block)):
        delFlag = False
        stmt = block[i]

        if stmt.tag == 'Ist_WrTmp':
            wrTmp = pyvex.expr.RdTmp.get_instance(stmt.tmp)

            if (wrTmp in loadedSet):
                loadedSet.remove(wrTmp)
            
            if stmt.data.tag == 'Iex_Load':
                loadedSet.add(wrTmp)
        
        elif stmt.tag == 'Ist_Store':
            if (stmt.data in loadedSet):
                block.remove(block[i])
                delFlag = True
        
        if (not delFlag):
            i += 1
    
    return block

# Store-Store Elimination
def SSEliminate(block):
    i = 0
    storedAddr = {}

    while (i < len(block)):
        stmt = block[i]
        delFlag = False

        if stmt.tag == 'Ist_Store':
            tAddr = stmt.addr
            if (tAddr in storedAddr):
                block.remove(storedAddr[tAddr])
                delFlag = True
            storedAddr[tAddr] = stmt

        elif stmt.tag =='Ist_WrTmp':
            if stmt.data.tag == 'Iex_Load':
                tAddr = stmt.data.addr
                if (tAddr in storedAddr):
                    del storedAddr[tAddr]
        
        if (not delFlag):
            i += 1

    return block

# Combine together
def VEXOpt(block):
    block = ClearMinus(block)
    block = RemoveRedunantWrite(block)
    block = RemoveBitwidth(block)
    block = RemoveCopy(block)
    block = ConstFolding(block)
    block = LLEliminate(block)
    block = LSEliminate(block)
    block = SSEliminate(block)
    return block
