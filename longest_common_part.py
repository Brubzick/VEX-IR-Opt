def FindComPart(strand1, strand2): # 用strand2去比strand1,找最长公共部分
    l2 = len(strand2)
    maxL = min(len(strand1),l2)
    # padding strand1
    padding = [0]*(l2-1)
    strand1 = padding + strand1 + padding
    l1 = len(strand1)

    lcp = []
    for i in range(l1 - l2 + 1):
        comStr = []
        for j in range(l2):
            if (strand1[i + j] == strand2[j]):
                comStr.append(strand2[j])
            else:
                if (len(comStr) > len(lcp)):
                    lcp = comStr
                    comStr = []
        
        if len(lcp) == maxL:
            break
    
    return lcp