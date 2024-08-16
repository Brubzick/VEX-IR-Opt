import json
from openpyxl import Workbook

with open('large_test_data/projName.json', 'r') as f:
    projName = json.load(f)

with open('large_test_data/sSetList.json', 'r') as f:
    sSetList = json.load(f)

with open('large_test_data/ac_arm_simScore_noBase.json', 'r') as f:
    simVector = json.load(f)

wb = Workbook()
ws = wb.active

fileIndex = simVector[-1]

head = ['File name']
sim = [projName[fileIndex]]
lengthes = ['ComNode nums']
ratio1 = ['Ratio1']
ratio2 = ['Ratio2']
comp = ['Comp score']

for i in range(len(simVector)-1):
    t = simVector[i]
    head.append(projName[t[1]])
    sim.append(t[0])
    lengthes.append(len(sSetList[t[1]]))
    r1 = t[0]/len(sSetList[fileIndex])
    r2 = t[0]/len(sSetList[t[1]])
    ratio1.append(r1)
    ratio2.append(r2)
    comp.append((r1+r2)/2)

toWrite = [head, sim, lengthes, ratio1, ratio2, comp]

for i in range(len(toWrite)):
    for j in range(len(head)):
        ws.cell(row=j+1,column=i+1,value=toWrite[i][j])

wb.save(projName[fileIndex] + '_simVec.xlsx')
