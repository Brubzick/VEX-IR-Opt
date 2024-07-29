import pyvex

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
            
            # add mapping
            if stmt.data.tag == 'Iex_Load':
                loadAddr = stmt.data.addr
                if (loadedMapping.get(loadAddr)):
                    tmpMapping[wrTmp] = loadedMapping[loadAddr]
                    block.remove(block[i])
                    delFlag = True
                else:
                    loadedMapping[loadAddr] = wrTmp
            else:
                if stmt.data.tag == 'Iex_Rdtmp':
                    if (tmpMapping.get(stmt.data)):
                        block[i].data = tmpMapping[stmt.data]
                elif ((stmt.data.tag == 'Iex_Unop') | (stmt.data.tag == 'Iex_Binop') | (stmt.data.tag == 'Iex_Triop') | (stmt.data.tag == 'Iex_Qop') | (stmt.data.tag == 'Iex_CCall')):
                    args = stmt.data.args
                    for j in range(0, len(args)):
                        if (tmpMapping.get(args[j])):
                            block[i].data.args[j] = tmpMapping[args[j]]
                    
                # delete mapping
                if (tmpMapping.get(wrTmp)):
                    del tmpMapping[wrTmp]
                if (wrTmp in loadedMapping.values()):
                    for key in loadedMapping.keys():
                        if loadedMapping[key] == wrTmp:
                            del loadedMapping[key]
                            break

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