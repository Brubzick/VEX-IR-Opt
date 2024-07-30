import angr
from whole_process_3 import VexOptHash3

proj = angr.Project('./C_files/dfs', auto_load_libs=False)


hashedSet = VexOptHash3(proj)

print(len(hashedSet),len(set(hashedSet)))
