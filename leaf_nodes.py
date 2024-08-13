def GetLeafNodes(cfg):
    leafNodes = []
    for node in cfg.nodes():
        if node.successors == []:
            leafNodes.append(node)
    
    return leafNodes