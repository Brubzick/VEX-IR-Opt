import angr
import pyvex
from Vex_opt import VexOpt

proj = angr.Project('./C_files/dfs', auto_load_libs=False)

cfg = proj.analyses.CFGFast(normalize=True)

nodeList = list(cfg.nodes())

allStmt = []

# for node in cfg.nodes():
#     if (not node.is_simprocedure):
#         node.block.vex.pp()

statements = nodeList[0].block.vex.statements


put = statements[2]
get = statements[4]
print(get.data.tag)
get.data = put.data
print(get.data.tag)
