class myStack:
    def __init__(self, n):
        self.st = []
        self.n = n
    
    def isEmpty(self):
        if len(self.st) == 0:
            return True
        else:
            return False

    
    def isFull(self):
        if len(self.st) == self.n:
            return True
        else:
            return False

    
    def push(self, x):
        self.st.append(x)

    
    def pop(self):
        if self.isEmpty():
            return -1
        self.st.pop()

    
    def peek(self):
        if self.isEmpty():
            return -1
        return self.st[-1]