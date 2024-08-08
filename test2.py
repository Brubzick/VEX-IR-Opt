import angr
from whole_process_2 import VexOptHash2

proj1 = angr.Project('./C_files/dfs', auto_load_libs=False)
proj2 = angr.Project('./C_files/dfs3', auto_load_libs=False)

hashedSet1 = VexOptHash2(proj1)
hashedSet2 = VexOptHash2(proj2)

sim = set(hashedSet1).intersection(set(hashedSet2))

print(len(sim),len(set(hashedSet1)),len(set(hashedSet2)))





