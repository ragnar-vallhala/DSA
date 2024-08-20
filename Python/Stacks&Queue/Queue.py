class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self,item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def __len__(self):
        return len(self.items)
    


if __name__=='__main__':
    q = Queue()
    q.enqueue(1)
    q.enqueue(9)
    q.enqueue(6)
    q.enqueue(31)
    
    
    for i in range(len(q)):
        print(q.dequeue())