import json
from longest_common_part import FindComPart
from filter import Filter

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


for fileIndex in range(5,len(sSetList)):
    sSet1 = sSetList[fileIndex]
    filteredListIndex = Filter(sSet1, sSetList)

    n = len(filteredListIndex)

    if n == 0:
        print('No files similar to ' + projName[fileIndex] + ' is found.')
    else:
        simVector = [0]*(n+1) # 最后一位用来储存当前的fileIndex

        for i in range(0, n):
            index = filteredListIndex[i]
            sSet2 = sSetList[index]
            simScore = Compare(sSet1, sSet2, 'small')
            simVector[i] = (simScore, index) # Index也要储存

            print('file1:',projName[fileIndex],'file2:',projName[index],'L1:',len(sSetList[fileIndex]),'L2:',len(sSetList[index]),'Sim:',simScore)
        
        simVector[-1] = fileIndex # 该二进制的index
        # 每一个二进制文件在projName, sSetList和vexOptProjs这三个列表中的index都相同，所以保留index可以便于后续分析
        # output data
        file = 'large_test_data/simResult/' + projName[fileIndex] + '_simScore_noBase.json'
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(simVector, f)
