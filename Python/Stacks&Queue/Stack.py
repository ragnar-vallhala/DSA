class Stack:
    
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)
    
    def peek(self):
        return self.items[-1]
    
    def pop(self):
        return self.items.pop()

    def __len__(self):
        return len(self.items)


if __name__=="__main__":
    s = Stack()
    s.push(5)
    s.push(15)
    s.push(55)
    s.push(53)
    
    for i in range(len(s)):
        print(s.pop())