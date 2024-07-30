import angr
from whole_process_3 import VexOptHash3

proj1 = angr.Project('./C_files/dfs', auto_load_libs=False)
proj2 = angr.Project('./C_files/hello3', auto_load_libs=False)

hashedSet1 = VexOptHash3(proj1)
hashedSet2 = VexOptHash3(proj2)

sim = set(hashedSet1).intersection(set(hashedSet2))

print(len(sim),len(set(hashedSet1)),len(set(hashedSet2)))





