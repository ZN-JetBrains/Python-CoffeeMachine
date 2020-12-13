class Stack:
    def __init__(self):
        self.list = []

    def push(self, el):
        self.list.append(el)

    def pop(self):
        return self.list.pop()

    def peek(self):
        if not self.is_empty():
            return self.list[-1]
        return None

    def is_empty(self):
        return self.list == []
