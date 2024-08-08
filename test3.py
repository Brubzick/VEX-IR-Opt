import angr
from find_longest_path import FindLongest

p = angr.Project('./C_files/dfs2', auto_load_libs = False)

cfg = p.analyses.CFGFast(normalize=True)

for node in cfg.nodes():
    if node.successors == []:
        print(node)

lP = FindLongest(cfg)

print(lP)
