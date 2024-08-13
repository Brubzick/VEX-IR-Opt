import angr
from whole_process import VexOptStrands
from longest_common_part import FindComPart

proj1 = angr.Project('../C_bin/dfs_gcc_O0', auto_load_libs=False)
proj2 = angr.Project('../C_bin/dfs_gcc_O1', auto_load_libs=False)
# proj3 = angr.Project('../C_bin/dfs_gcc_O2', auto_load_libs=False)
# proj4 = angr.Project('../C_bin/dfs_gcc_O3', auto_load_libs=False)
proj5 = angr.Project('../C_bin/bfs_gcc_O0', auto_load_libs=False)
# proj6 = angr.Project('../C_bin/bfs_gcc_O1', auto_load_libs=False)
# proj7 = angr.Project('../C_bin/bfs_gcc_O2', auto_load_libs=False)
# proj8 = angr.Project('../C_bin/bfs_gcc_O3', auto_load_libs=False)
# proj9 = angr.Project('../C_bin/dfs_clang_O0', auto_load_libs=False)
# proj10 = angr.Project('../C_bin/dfs_clang_O1',auto_load_libs=False)
# proj11 = angr.Project('../C_bin/dfs_clang_O2',auto_load_libs=False)
# proj12 = angr.Project('../C_bin/dfs_clang_O3',auto_load_libs=False)
# proj13 = angr.Project('../C_bin/bfs_clang_O0',auto_load_libs=False)
# proj14 = angr.Project('../C_bin/bfs_clang_O1',auto_load_libs=False)
proj15 = angr.Project('../C_bin/bfs_clang_O2',auto_load_libs=False)
# proj16 = angr.Project('../C_bin/bfs_clang_O3',auto_load_libs=False)
proj17 = angr.Project('../C_bin/dfs_gcc2_O0', auto_load_libs=False)
proj18 = angr.Project('../C_bin/dfs_gcc2_O1', auto_load_libs=False)
proj19 = angr.Project('../C_bin/dfs_gcc2_O2', auto_load_libs=False)
proj20 = angr.Project('../C_bin/dfs_gcc2_O3', auto_load_libs=False)
proj21 = angr.Project('../C_bin/other_source/hello_gcc_O0', auto_load_libs=False)
# proj22 = angr.Project('../C_bin/other_source/hello_gcc_O1', auto_load_libs=False)
# proj23 = angr.Project('../C_bin/other_source/hello_gcc_O2', auto_load_libs=False)
# proj24 = angr.Project('../C_bin/other_source/hello_gcc_O3', auto_load_libs=False)
# proj25 = angr.Project('../C_bin/other_source/hello_clang_O0', auto_load_libs=False)
# proj26 = angr.Project('../C_bin/other_source/hello_clang_O1', auto_load_libs=False)
# proj27 = angr.Project('../C_bin/other_source/hello_clang_O2', auto_load_libs=False)
# proj28 = angr.Project('../C_bin/other_source/hello_clang_O3', auto_load_libs=False)
proj29 = angr.Project('../C_bin/other_source/is_gcc_O0', auto_load_libs=False)
proj30 = angr.Project('../C_bin/other_source/is_gcc_O1', auto_load_libs=False)
# proj31 = angr.Project('../C_bin/other_source/is_gcc_O2', auto_load_libs=False)
# proj32 = angr.Project('../C_bin/other_source/is_gcc_O3', auto_load_libs=False)
# proj33 = angr.Project('../C_bin/other_source/is_gcc2_O0', auto_load_libs=False)
# proj34 = angr.Project('../C_bin/other_source/is_gcc2_O1', auto_load_libs=False)
# proj35 = angr.Project('../C_bin/other_source/is_gcc2_O2', auto_load_libs=False)
# proj36 = angr.Project('../C_bin/other_source/is_gcc2_O3', auto_load_libs=False)
proj37 = angr.Project('../C_bin/other_source/whatever_gcc_O0', auto_load_libs=False)
proj38 = angr.Project('../C_bin/other_source/whatever_gcc_O1', auto_load_libs=False)
# proj39 = angr.Project('../C_bin/other_source/whatever_gcc_O2', auto_load_libs=False)
# proj40 = angr.Project('../C_bin/other_source/whatever_gcc_O3', auto_load_libs=False)
# proj41 = angr.Project('../C_bin/other_source/whatever_gcc2_O0', auto_load_libs=False)
# proj42 = angr.Project('../C_bin/other_source/whatever_gcc2_O1', auto_load_libs=False)
# proj43 = angr.Project('../C_bin/other_source/whatever_gcc2_O2', auto_load_libs=False)
# proj44 = angr.Project('../C_bin/other_source/whatever_gcc2_O3', auto_load_libs=False)

# strands1 = VexOptStrands(proj1)
# strands2 = VexOptStrands(proj2)
# strands3 = VexOptStrands(proj3)
# strands4 = VexOptStrands(proj4)
# strands5 = VexOptStrands(proj5)
# strands6 = VexOptStrands(proj6)
# strands7 = VexOptStrands(proj7)
# strands8 = VexOptStrands(proj8)
# strands9 = VexOptStrands(proj9)
# strands10 = VexOptStrands(proj10)
# strands11 = VexOptStrands(proj11)
# strands12 = VexOptStrands(proj12)
# strands13 = VexOptStrands(proj13)
# strands14 = VexOptStrands(proj14)
# strands15 = VexOptStrands(proj15)
# strands16 = VexOptStrands(proj16)
# strands17 = VexOptStrands(proj17)
# strands20 = VexOptStrands(proj20)
# strands21 = VexOptStrands(proj21)
# strands22 = VexOptStrands(proj22)
# strands23 = VexOptStrands(proj23)
# strands24 = VexOptStrands(proj24)
# strands25 = VexOptStrands(proj25)
# strands26 = VexOptStrands(proj26)
# strands27 = VexOptStrands(proj27)

# allTarStrands = [strands21,strands22,strands23,strands24,strands25,strands26,strands27]

# Compare the Query with 1 Target
strands1 = VexOptStrands(proj37)
strands2 = VexOptStrands(proj1)

# if (strand1 not in allTarStrands):
#     allTarStrands.append(strand1)
# if (strand2 not in allTarStrands):
#     allTarStrands.append(strand2)

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
    # count = 0
    # for strands in allTarStrands:
    #     for strand in strands:
    #         if strand == s2:
    #             count += 1
    #         elif strand in s2:
    #             count += len(strand)/len(s2)
    #         elif s2 in strand:
    #             count += len(s2)/len(strand)
    # if count == 0: count = 1
    # simScore += mp*len(allTarStrands)/count
    simScore += mp

print(simScore)
print(len(sSet1), len(sSet2))


    
        

