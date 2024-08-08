import angr
from whole_process import VexOptHash
from whole_process_2 import VexOptHash2
from whole_process_3 import VexOptHash3

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

hashedSet1 = VexOptHash2(proj1)
hashedSet2 = VexOptHash2(proj2)
hashedSet3 = VexOptHash2(proj3)
hashedSet4 = VexOptHash2(proj4)
hashedSet5 = VexOptHash2(proj5)
hashedSet6 = VexOptHash2(proj6)
hashedSet7 = VexOptHash2(proj7)
hashedSet8 = VexOptHash2(proj8)
hashedSet9 = VexOptHash2(proj9)
hashedSet10 = VexOptHash2(proj10)
hashedSet11 = VexOptHash2(proj11)
hashedSet12 = VexOptHash2(proj12)

allTarSet = [hashedSet2,hashedSet3,hashedSet4,hashedSet5,hashedSet6,hashedSet7,hashedSet8,hashedSet9,hashedSet10,hashedSet11,hashedSet12]

# Compare 1 and 2
intersection = set(hashedSet1).intersection(set(hashedSet2))

# simScore
simScore = 0
for strand in intersection:
    count = 0
    for hashedSet in allTarSet:
        count += hashedSet.count(strand)

    simScore += len(allTarSet)/count # number of targets divided by strand frequency

print(simScore)
print(len(intersection))



