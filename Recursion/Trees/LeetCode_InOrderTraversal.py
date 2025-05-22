from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    val: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

five = Node(5)
three = Node (3)
two = Node(2)
four = Node(4)
seven = Node(7)
six = Node(6)
eight= Node(8)

five.left = three
five.right = seven
three.left = two
three.right = four
seven.left = six
seven.right = eight

def iterativeInOrderTraverse(node):
    list = []

    stack = [(node)]

    while stack:
        val = stack.pop()
        while val.left != None:
            stack.append(val.left)
            val.left = val.left.left
        list.append(stack.pop())
        while val.right != None:
            stack.append(val.right)
            val.right = val.right.right
    print(list)        


iterativeInOrderTraverse(five)