def Filter(tarSet, sSetList): # 筛掉节点数量相差太大的二进制文件
    tarLen = len(tarSet)

    filteredListIndex = []

    for sSet in sSetList:
        sLen = len(sSet)
        if ((sLen > 0.6*tarLen) & (sLen < 1.4*tarLen)):
            filteredListIndex.append(sSetList.index(sSet))
        
    return filteredListIndex
    # 返回的是目标在sSetList中的index
