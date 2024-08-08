import angr
from whole_process import VexOptStrands

# Query
proj1 = angr.Project('./C_files/dfs', auto_load_libs=False)
# Target
proj2 = angr.Project('./C_files/dfs3', auto_load_libs=False)
proj3 = angr.Project('./C_files/bfs', auto_load_libs=False)
proj4 = angr.Project('./C_files/bfs3', auto_load_libs=False)
proj5 = angr.Project('./C_files/hello', auto_load_libs=False)
proj6 = angr.Project('./C_files/hello3', auto_load_libs=False)
proj7 = angr.Project('./C_files/insert_sort', auto_load_libs=False)
proj8 = angr.Project('./C_files/shell_sort', auto_load_libs=False)
proj9 = angr.Project('./C_files/whatever', auto_load_libs=False)
proj10 = angr.Project('./C_files/insert_sort3',auto_load_libs=False)
proj11 = angr.Project('./C_files/shell_sort3',auto_load_libs=False)
proj12 = angr.Project('./C_files/dfs2',auto_load_libs=False)

strands1 = VexOptStrands(proj1)
strands2 = VexOptStrands(proj2)
strands3 = VexOptStrands(proj3)
strands4 = VexOptStrands(proj4)
strands5 = VexOptStrands(proj5)
strands6 = VexOptStrands(proj6)
strands7 = VexOptStrands(proj7)
strands8 = VexOptStrands(proj8)
strands9 = VexOptStrands(proj9)
strands10 = VexOptStrands(proj10)
strands11 = VexOptStrands(proj11)
strands12 = VexOptStrands(proj12)

allTarStrands = [strands2,strands3,strands4,strands5,strands6,strands7,strands8,strands9,strands10,strands11,strands12]

# Compare the Query with 1 Target
sSet1 = set(strands1)
sSet2 = set(strands2)

simScore = 0
for s2 in sSet2:
    mp = 0
    for s1 in sSet1:
        if s2 == s1:
            mp = 1
            break
        else:
            if s1 in s2:
                tp = len(s1)/len(s2)
                if tp > mp:
                    mp = tp
            elif s2 in s1:
                tp = len(s2)/len(s1)
                if tp > mp:
                    mp = tp
    
    count = 0
    for strands in allTarStrands:
        for strand in strands:
            if s2 == strand:
                count += 1
            elif s2 in strand:
                count += len(s2)/len(strand)
            elif strand in s2:
                count += len(strand)/len(s2)
    
    simScore += mp*len(allTarStrands)/count

print(simScore)
print(len(sSet1), len(sSet2))


