class binarySearchTreeClem:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.data:
                if currentNode.left is None:
                    currentNode.left = binarySearchTreeClem(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = binarySearchTreeClem(value)
                    break
                else:
                    currentNode = currentNode.right
        return self

    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.data:
                currentNode = currentNode.left
            elif value > currentNode.data:
                currentNode = currentNode.right
            else:
                return True
