from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    val:int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

@dataclass
class BST:
    root: Node


def isValidBST(root):

    def isValidNode(node,minValue,maxValue):
        if node is None:
            return True
        if not minValue <node.val < maxValue:
            return False
        
        return(
            isValidNode(node.left,minValue,node.val) and
            isValidNode(node.right, node.val,maxValue)
        )

        
    return isValidNode(root,float('-inf'),float('inf'))

tree = BST(Node(10))
tree.root.right = Node(15)
tree.root.left = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(20)

print(isValidBST(tree.root))