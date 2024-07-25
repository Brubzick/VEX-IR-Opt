from IR_opt import VEXOpt
from get_strands import GetAllStrandsNorm
from hash import GetHashedStrands

def VexOptHash(proj):
    cfg = proj.analyses.CFGFast(normalize=True)

    blockList = []

    for node in cfg.nodes():
        if (not node.is_simprocedure):
            block = node.block.vex.statements
            block = VEXOpt(block)
            blockList.append(block)

    strands = GetAllStrandsNorm(blockList)

    hashedSet = GetHashedStrands(strands)

    return hashedSet