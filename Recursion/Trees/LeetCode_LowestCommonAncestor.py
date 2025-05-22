


def lca(node,nodeQ,nodeP):

    if node is None:
        return None
    if node.val == nodeQ.val or node.val == nodeP.val
        return node
    
    left = lca(node.left,nodeQ,nodeP)
    right = lca(node.right,nodeQ,nodeP)

    if left and right:
        return node
    
    return left if left else right