import angr
from find_longest_path import FindLongest

p = angr.Project('../C_bin/dfs_gcc_O0', auto_load_libs=False)

cfg = p.analyses.CFGFast(normalize=True)

lP = FindLongest(cfg)

print(len(lP))