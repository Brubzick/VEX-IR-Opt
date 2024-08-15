import angr
import os
from process_strands import VexOptStrands
from longest_common_part import FindComPart
import json

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

maxSize = 1024 * 800 # maximum size (b) of file that would be loaded

def is_ELF(filePath):
    f = open(filePath, 'rb')
    head = f.read(4)
    f.close()
    headList = [head[0], head[1], head[2], head[3]]
    if headList == [127,69,76,70]:
        return True
    return False

folderPathList = ['../bin_range/arm', '../bin_range/file', '../bin_range/openssl', '../bin_range/ssh', '../bin_range/unzip', '../bin_range/wget', '../bin_range/x86']

projNameDict = {} # map the proj to its file name
for foldPath in folderPathList:
    all_files = os.listdir(foldPath)
    
    for file in all_files:
        filePath = os.path.join(foldPath, file)
        if is_ELF(filePath):
            if (os.path.getsize(filePath) <= maxSize):
                proj = angr.Project(filePath, auto_load_libs=False)
                projNameDict[proj] = file

print('all projs are loaded.')

vexOptProjs = []
sSetList = []
projName = [] # map an unique index to the proj name

for proj in projNameDict:
    projName.append(projNameDict[proj])
    blockList = VexOptStrands(proj)
    vexOptProjs.append(blockList)

print('vex opt done.')

n = len(vexOptProjs)

for i in range(n):
    blockList = vexOptProjs[i]
    sSet = []
    for block in blockList:
        if (block not in sSet):
            sSet.append(block)
    sSetList.append(sSet)

simMatrix = [[0]*n]*n
print('Comparing...')
for i in range(n):
    for j in range(n):
        sSet1 = sSetList[i]
        sSet2 = sSetList[j]
        simScore = Compare(sSet1, sSet2, 'small', vexOptProjs)
        simMatrix[i][j] = simScore

        print('file1:',projName[i],'file2:',projName[j],'L1:',len(sSet1),'L2:',len(sSet2),'Sim:',simScore)

# output data
with open('sSetList.json', 'w', encoding='utf-8') as f:
    json.dump(sSetList, f) # for reference
with open('projName.json', 'w', encoding='utf-8') as f:
    json.dump(projName, f)
with open('simMatrix.json', 'w', encoding='utf-8') as f:
    json.dump(simMatrix, f)



