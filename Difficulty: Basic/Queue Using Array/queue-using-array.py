class myQueue:
    def __init__(self, n):
        self.q = []
        self.n = n

    
    def isEmpty(self):
        if len(self.q) == 0:
            return True
        else:
            return False

    
    def isFull(self):
        if len(self.q) == self.n:
            return True
        else:
            return False

    
    def enqueue(self, x):
        if not self.isFull():
            self.q.append(x)

    
    def dequeue(self):
        if not self.isEmpty():
            self.q = self.q[1:]

    
    def getFront(self):
        if self.isEmpty():
            return -1
        return self.q[0]
       
    
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.q[-1]
        
        