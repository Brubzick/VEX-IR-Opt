import angr
from process_longest_path import VexOptStrands
from longest_common_part import FindComPart

proj1 = angr.Project('../bin_range/file/file_5.38_x86', auto_load_libs=False)
proj2 = angr.Project('../bin_range/file/file_5.38_arm', auto_load_libs=False)

# Compare the Query with 1 Target
strands1 = VexOptStrands(proj1)
strands2 = VexOptStrands(proj2)
print('vex ok')
sSet1 = []
sSet2 = []

for s in strands1:
    if (s not in sSet1):
        sSet1.append(s)
for s in strands2:
    if (s not in sSet2):
        sSet2.append(s)

simScore = 0
count = 0
for s2 in sSet2:
    count+=1
    print(count)
    mp = 0
    for s1 in sSet1:
        comPart = FindComPart(s1, s2)
        tp = len(comPart)/len(s2)
        if tp > mp:
            mp = tp
        if mp == 1:
            break
    simScore += mp

print(simScore)
print(len(sSet1), len(sSet2))

