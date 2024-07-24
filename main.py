import angr
from IR_opt import VEXOpt
from get_strands import GetAllStrandsNorm
from hash import GetHashedStrands

proj1 = angr.Project('./dfs', auto_load_libs=False)
proj2 = angr.Project('./dfs3', auto_load_libs=False)

cfg1 = proj1.analyses.CFGFast(normalize=True)
cfg2 = proj2.analyses.CFGFast(normalize=True)

blockList1 = []
blockList2 = []

for node in cfg1.nodes():
    if (not node.is_simprocedure):
        block = node.block.vex.statements
        block = VEXOpt(block)
        blockList1.append(block)

for node in cfg2.nodes():
    if (not node.is_simprocedure):
        block = node.block.vex.statements
        block = VEXOpt(block)
        blockList2.append(block)


strands1 = GetAllStrandsNorm(blockList1)
strands2 = GetAllStrandsNorm(blockList2)

hashedSet1 = GetHashedStrands(strands1)
hashedSet2 = GetHashedStrands(strands2)

intersection = set(hashedSet1).intersection(set(hashedSet2))

print(len(intersection), len(set(hashedSet1)), len(set(hashedSet2)))
