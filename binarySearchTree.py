class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


def minimum_element(self):
    if self.left is None:
        return self.data
    return self.left.minimum_element()


def maximum_element(self):
    if self.right is None:
        return self.data
    return self.right.maximum_element()


def calculate_sum(self):
    left_side = self.left.calcualte_sum() if self.left else 0
    right_side = self.right.calcualte_sum() if self.right else 0
    root = self.data
    return left_side + right_side + root


def post_order_traversal(self):
    elements = []
    if self.left:
        elements += self.left.post_order_traversal()

    if self.right:
        elements += self.right.post_order_traversal()

    elements.append(self.data)

    return elements


def pre_order_traversal(self):
    elements = []

    elements.append(self.data)

    if self.left:
        elements += self.left.pre_order_traversal()

    if self.right:
        elements += self.right.pre_order_traversal()

    return elements


def delete(self, val):
    if val < self.data:
        if self.left:
            self.left = self.left.delete(val)
    elif val > self.data:
        if self.right:
            self.right = self.right.delete(val)
    else:
        if self.left is None and self.right is None:
            return None
        elif self.left is None:
            return self.right
        elif self.right is None:
            return self.right

        max_val = self.left.maximum_element()
        self.data = max_val
        self.left = self.left.delete(max_val)

    return self


if __name__ == '__main__':
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
    print(minimum_element)
