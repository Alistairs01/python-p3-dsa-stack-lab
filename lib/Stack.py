class Stack:

    def __init__(self, items = [], limit = 100):
        if items is None :
            self.items = []
        else:
            self.items = items
        self.limit = limit
        

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

        else :
            return None

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for index, value in enumerate(self.items):
            if value ==  target:
                return len(self.items) - (index +1)
        else:
            return -1