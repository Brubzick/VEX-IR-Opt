from vex_opt import VexOpt
from get_strands import GetStrands
from strand_normalization import TypeNorm

def VexOptStrands(proj):
    cfg = proj.analyses.CFGFast(normalize=True)

    blockList = []

    for node in cfg.nodes():
        if (not node.is_simprocedure):
            block = node.block.vex.statements
            optBlock = VexOpt(block)
            if optBlock != []:
                for i in range(len(optBlock)):
                    optBlock[i] = TypeNorm(optBlock[i])
                blockList.append(optBlock)

    return blockList