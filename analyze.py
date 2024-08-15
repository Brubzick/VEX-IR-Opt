import json
from longest_common_part import FindComPart

def Compare(sSet1, sSet2, mode='normal', base=None):
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

with open('large_test_data/projName.json', 'r') as f:
    projName = json.load(f)

with open('large_test_data/sSetList.json', 'r') as f:
    sSetList = json.load(f)

n = len(sSetList)
simMatrix = [['x']*n]*n
for i in range(n):
    for j in range(i, n):
        sSet1 = sSetList[i]
        sSet2 = sSetList[j]
        simScore = Compare(sSet1, sSet2, 'small')
        simMatrix[i][j] = simScore

        print('file1:',projName[i],'file2:',projName[j],'L1:',len(sSetList[i]),'L2:',len(sSetList[j]),'Sim:',simScore)

# output data
with open('large_test_data/simMatrix_noBase.json', 'w', encoding='utf-8') as f:
    json.dump(simMatrix, f)