import angr
from whole_process import VexOptHash

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

hashedSet1 = VexOptHash(proj1)
hashedSet2 = VexOptHash(proj2)
hashedSet3 = VexOptHash(proj3)
hashedSet4 = VexOptHash(proj4)
hashedSet5 = VexOptHash(proj5)
hashedSet6 = VexOptHash(proj6)
hashedSet7 = VexOptHash(proj7)
hashedSet8 = VexOptHash(proj8)
hashedSet9 = VexOptHash(proj9)

allTarSet = [hashedSet2,hashedSet3,hashedSet4,hashedSet5,hashedSet6,hashedSet7,hashedSet8,hashedSet9]

# Compare 1 and 2
intersection = set(hashedSet1).intersection(set(hashedSet2))

# simScore
simScore = 0
for strand in intersection:
    count = 0
    for hashedSet in allTarSet:
        count += hashedSet.count(strand)
    
    simScore += 8/count # number of targets divided by strand frequency

print(simScore)
print(len(set(hashedSet1)), len(set(hashedSet2)))



