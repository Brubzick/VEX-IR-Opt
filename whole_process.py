from vex_opt import VexOpt
from longest_path import FindLongest
from get_strands import GetStrands
from strand_normalization import TypeNorm

def VexOptStrands(proj):
    cfg = proj.analyses.CFGFast(normalize=True)
    entry = cfg.get_any_node(proj.entry)

    lP = FindLongest(cfg,entry)

    statements = []

    for node in lP:
        if (not node.is_simprocedure):
            statements.extend(node.block.vex.statements)

    optVex = VexOpt(statements)

    strands = GetStrands(optVex)
    for i in range(0, len(strands)):
        for j in range(0, len(strands[i])):
            strands[i][j] = TypeNorm(strands[i][j])
    
    return strands