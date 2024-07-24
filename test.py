import angr
from IR_opt import VEXOpt

proj = angr.Project('./dfs', auto_load_libs=False)

cfg = proj.analyses.CFGFast(normalize=True)

nodes = list(cfg.nodes())

node = nodes[0]

node.block.vex.pp()

block = node.block.vex.statements
block = VEXOpt(block)
for stmt in block:
    print(stmt)
