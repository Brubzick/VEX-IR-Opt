# Remove IMark and AbiHint
def RmUnrelated(block): # block is a list of IR stmt
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