
def GetPeepholes(cfg):
    L = len(cfg.nodes())
    k = L/6 # Maximum length of a peephole
    c = 2 # Minimum number of visits per basic block
    visitIndex = {}
    pSet = set()
