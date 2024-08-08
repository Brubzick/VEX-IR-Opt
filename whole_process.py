from vex_opt import VexOpt
from find_longest_path import FindLongest
from get_strands import GetStrands
from strand_normalization import TypeNorm

def VexOptStrands(proj):
    cfg = proj.analyses.CFGFast(normalize=True)

    lP = FindLongest(cfg)

    statements = []

    for node in lP:
        if (not node.is_simprocedure):
            statements.extend(node.block.vex.statements)

    optVex = VexOpt(statements)

    strands = GetStrands(optVex)
    for i in range(0, len(strands)):
        for j in range(0, len(strands[i])):
            strands[i][j] = TypeNorm(strands[i][j])

    for i in range(0, len(strands)):
        strands[i] = ''.join(strands[i])
    
    return strands