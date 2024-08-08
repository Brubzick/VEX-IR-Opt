from Vex_opt import VexOpt
from get_strands import GetAllStrandsNorm
from hash import GetHashedStrands

def VexOptHash2(proj):
    cfg = proj.analyses.CFGFast(normalize=True)

    blockList = []

    for node in cfg.nodes():
        if (not node.is_simprocedure):
            block = node.block.vex.statements
            block = VexOpt(block)
            blockList.append(block)
            
    strands = GetAllStrandsNorm(blockList)

    hashedSet = GetHashedStrands(strands)

    return hashedSet