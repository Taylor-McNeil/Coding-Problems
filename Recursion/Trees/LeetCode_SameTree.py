from dataclasses import dataclass
from typing import Optional

@dataclass
class Node():
    val:int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

@dataclass
class Tree():
    root: Node  


def isSameTree_Stack(treeOne,treeTwo):

#Base Case One: Both trees are empty therefore the same :)
    if treeOne is None and treeTwo is None:
        return True

# Base Case Two:  One tree is empty but the other tree is not
    if treeTwo is None or treeTwo is None:
        return False

    stack = [(treeOne,treeTwo)]

    while stack:
        treeOneNode, treeTwoNode = stack.pop()

        if treeOneNode is None and treeTwoNode is None:
            continue
        if treeOneNode is None or treeTwoNode is None:
            return False
        if treeOneNode.val != treeTwoNode.val:
            return False

        stack.append((treeOneNode.right,treeTwoNode.right))
        stack.append((treeOneNode.left,treeTwoNode.left))
    return True


def isSameTree_Recursive(treeOneNode,treeTwoNode):
    if not treeOneNode and not treeTwoNode:
        return True
    if not treeOneNode or not treeTwoNode:
        return False
    if treeOneNode.val != treeTwoNode.val:
        return False
    return isSameTree_Recursive(treeOneNode.left,treeTwoNode.left) and isSameTree_Recursive(treeOneNode.right,treeTwoNode.right)


one = Node(1)
two = Node(2)
three= Node(3)

oneA = Node(1)
twoA= Node(2)
threeA = Node(32)

one.left = two
one.right = three

oneA.left = twoA
oneA.right = threeA

treeOne = one
treeTwo = oneA

print(isSameTree_Stack(treeOne,treeTwo))
print(isSameTree_Recursive(treeOne,treeTwo))