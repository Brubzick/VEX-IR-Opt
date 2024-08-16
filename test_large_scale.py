import angr
import os
from process_strands import VexOptStrands
from longest_common_part import FindComPart
import json

maxSize = 1024 * 500 # maximum size (b) of file that would be loaded

def is_ELF(filePath):
    f = open(filePath, 'rb')
    head = f.read(4)
    f.close()
    headList = [head[0], head[1], head[2], head[3]]
    if headList == [127,69,76,70]:
        return True
    return False

folderPathList = ['../bin_range/arm', '../bin_range/file', '../bin_range/unzip', '../bin_range/x86']

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

with open('large_test_data/vexOptProjs.json', 'w', encoding='utf-8') as f:
    json.dump(vexOptProjs, f)
with open('large_test_data/projName.json', 'w', encoding='utf-8') as f:
    json.dump(projName, f)
print('vex opt done.')

n = len(vexOptProjs)

for i in range(n):
    blockList = vexOptProjs[i]
    sSet = []
    for block in blockList:
        if (block not in sSet):
            sSet.append(block)
    sSetList.append(sSet)

with open('large_test_data/sSetList.json', 'w', encoding='utf-8') as f:
    json.dump(sSetList, f) # for reference

# simMatrix = [['x']*n]*n
# print('Comparing...')
# for i in range(n):
#     for j in range(i, n):
#         sSet1 = sSetList[i]
#         sSet2 = sSetList[j]
#         simScore = Compare(sSet1, sSet2, 'small', vexOptProjs)
#         simMatrix[i][j] = simScore

#         print('file1:',projName[i],'file2:',projName[j],'L1:',len(sSet1),'L2:',len(sSet2),'Sim:',simScore)

# # output data
# with open('large_test_data/simMatrix.json', 'w', encoding='utf-8') as f:
#     json.dump(simMatrix, f)



