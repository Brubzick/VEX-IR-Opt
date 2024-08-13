# Find the longest path in a CFG
import networkx as nx
# dfsNode that can store its previous node in the current path
class dfsNode:
    node = None
    pre = None
    cStep = 0
    def __init__(self, node, pre, cStep):
        self.node = node
        self.pre = pre
        self.cStep = cStep

def InPath(node, pathNode):
    while (pathNode):
        if (node.node == pathNode.node):
            return True
        pathNode = pathNode.pre
    return False

def FindLongest(cfg, entry):
    # Preprocess
    Digraph = cfg.graph
    components = nx.connected_components(Digraph.to_undirected())
    for component in components:
        if entry in component:
            subGraph = nx.subgraph(Digraph, component)
            break
    # Find cycles (not always correct)
    cycles = list(nx.simple_cycles(subGraph))
    delIndex = []
    for i in range(len(cycles)):
        cycle = cycles[i]
        if (cycle[0] not in cycle[-1].successors):
            delIndex.append(i)
        else:
            for j in range(len(cycle)-1):
                if (cycle[j+1] not in cycle[j].successors):
                    delIndex.append(i)
                    break
    delIndex.sort(reverse=True)
    for index in delIndex:
        del cycles[index]

    # Find the longest path without cycle
    head = entry
    stack = [] #work stack
    lNode = None # the leaf dfsNode of the longest path
    cPathLeaf = None # the leaf of current path
    maxStep = 0
    stack.append(dfsNode(head, None, 0))
    count = 0

    while (stack):
        cNode = stack.pop()
        if (InPath(cNode, cPathLeaf)):
            continue
        else:
            tNode = cNode.node
            cPathLeaf = cNode
            if (tNode.successors):
                for node in tNode.successors:
                    stack.append(dfsNode(node, cNode, cNode.cStep+1))
            else:
                count += 1
                if (cNode.cStep > maxStep):
                    maxStep = cNode.cStep
                    lNode = cNode
                if (count >= 1000000):
                    print('too many pathes, use the current longest path.')
                    break

    # get longest path without cycle
    lPath = []
    while (lNode):
        lPath.append(lNode.node)
        lNode = lNode.pre
    lPath.reverse()

    # insert cycles into the path
    for cycle in cycles:
        for i in range(len(lPath)):
            if cycle[0] == lPath[i]:
                lPath[i:i] = cycle
                break

    return lPath