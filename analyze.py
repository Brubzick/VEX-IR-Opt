import json
from openpyxl import Workbook
import os

with open('large_test_data/projName.json', 'r') as f:
    projName = json.load(f)

with open('large_test_data/sSetList.json', 'r') as f:
    sSetList = json.load(f)

resultsPath = 'large_test_data/simResult'
results = os.listdir(resultsPath)

for result in results:
    resultPath = os.path.join(resultsPath, result)
    with open(resultPath, 'r') as f:
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

    wb.save('large_test_data/simExcel/'+projName[fileIndex] + '_simVec.xlsx')
