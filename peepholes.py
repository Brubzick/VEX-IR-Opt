import random

def RandomPath(v):
    path = [v]

    while (v.successors != []):
        v = random.choice(v.successors)
        path.append(v)
    
    return path
    

def GetPeepholes(cfg):
    # c: minimum number of visits per node
    c = 2
    worklist = list(cfg.nodes())
    count = {}
    for node in worklist:
        count[node] = 0
    peepholes = [] # set of peepholes

    while (worklist != []):
        v = random.choice(worklist)
        path = RandomPath(v)
        delList = []
        
        for node in path:
            count[node] += 1
            if count[node] >= c:
                delList.append(node)
        
        for node in delList:
            del count[node]
        
        peepholes.append(path)

    return peepholes