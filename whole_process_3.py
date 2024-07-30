from Vex_opt import VexOpt
from get_strands import GetStrands
from strand_normalization import TypeNorm
from hash import GetHashedStrands

def VexOptHash3(proj):
    cfg = proj.analyses.CFGFast(normalize=True)

    statementList = []

    for node in cfg.nodes():
        if (not node.is_simprocedure):
            block = node.block.vex.statements
            statementList.extend(block)

    statementList = VexOpt(statementList)

    strands = GetStrands(statementList)

    for i in range(0, len(strands)):
        for j in range(0, len(strands[i])):
            strands[i][j] = TypeNorm(strands[i][j])

    hashedSet = GetHashedStrands(strands)

    return hashedSet