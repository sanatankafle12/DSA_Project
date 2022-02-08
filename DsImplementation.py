class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self,data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def show(self):
        return [x for x in self.items]


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self,data):
        self.items.append(data)
    
    def dequeue(self):
        return self.items.pop()