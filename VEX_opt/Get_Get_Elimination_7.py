import pyvex

def GGEliminate(block):
    i = 0

    while (i < len(block)):
        stmt = block[i]
        delIndex = []

        if stmt.tag == 'Ist_WrTmp':
            if stmt.data.tag == 'Iex_Get':
                regOffset = stmt.data.offset
                wrTmp = pyvex.expr.RdTmp.get_instance(stmt.tmp)
                used = False

                for j in range(i+1, len(block)):
                    subStmt = block[j]
                    if subStmt.tag == 'Ist_WrTmp':
                        subWrTmp = pyvex.expr.RdTmp.get_instance(subStmt.tmp)
                        if subStmt.data.tag == 'Iex_Get':
                            if subWrTmp == wrTmp:
                                if regOffset == subStmt.data.offset:
                                    delIndex.append(j)
                            else:
                                if (not used):
                                    if (i not in delIndex): delIndex.append(i)
                        # 还有一种只有offset相同的情况，暂时先不考虑

                        elif subWrTmp == wrTmp:
                            break

                        else:
                            if (str(wrTmp) in str(subStmt.data)): used = True
                    else:
                        if (str(wrTmp) in str(subStmt)): used = True

        delIndex.sort(reverse=True)
        for index in delIndex:
            block.remove(block[index])
        
        i += (1 - len(delIndex))
    
    return block

