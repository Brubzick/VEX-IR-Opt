from longest_common_part import FindComPart

def Compare(strands1, strands2, mode = 'normal', base = None):
    '''
    mode: 'small'或'normal'.
        'small': sSet1和sSet2中长度更短的来比更长的
        'normal': 使用sSet2比sSet1
    base: 比较时使用的基准(包含数个proj, 每个proj又包含数个blocks), 默认为None. 若不为None, 在计算分数时, 会根据当前比较的主体(block)在base中出现的频率用TFIDF进行计算.
    '''
    sSet1 = []
    sSet2 = []

    for s in strands1:
        if (s not in sSet1):
            sSet1.append(s)
    for s in strands2:
        if (s not in sSet2):
            sSet2.append(s)

    l1 = sSet1
    l2 = sSet2

    if mode == 'small':
        if len(sSet1) < len(sSet2):
            t = sSet2
            sSet2 = sSet1
            sSet1 = t

    simScore = 0
    for s2 in sSet2:
        mp = 0
        for s1 in sSet1:
            comPart = FindComPart(s1, s2)
            tp = len(comPart)/len(s2)
            if tp > mp:
                mp = tp
            if mp == 1:
                break
        
        if base:
            count = 0
            for proj in base:
                for block in proj:
                    for j in range(0, len(block)-len(s2)+1):
                        if (block[j:j+len(s2)] == s2):
                            count += 1
                            break
            #if count == 0: count = 1 # normally base should contain the proj that is comparing
            simScore += mp*len(base)/count
        else:
            simScore += mp
        
    return simScore