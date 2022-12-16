class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.output_stack.append(x)

    def pop(self) -> int:
        return self.output_stack.pop(0)

    def peek(self) -> int:
        return self.output_stack[-1]

    def empty(self) -> bool:
        if len(self.output_stack) != 0:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
