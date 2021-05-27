


def findClosestValueInBst(tree, target):
    closest = None
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode):
            closest = currentNode.value
        if currentNode.value > target:
            closest = currentNode.left
        elif currentNode.value < target:
            closest = currentNode.right
        else:
            break
    return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




