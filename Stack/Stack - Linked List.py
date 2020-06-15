#Stack Implemented via a Linked List

class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node
    
    def get_value(self):
        return self.data
    
    def set_next_node(self, next_node):
        self.next_node = next_node
    
    def get_next_node(self):
        return self.next_node

class Stack:
    def __init__(self, limit = 1000):
        self.head = None
        self.limit = limit
        self.size = 0
    
    def is_empty(self):
        if self.size == 0:
            return True
    
    def has_space(self):
        return self.limit > self.size
    
    def push(self, data):
        if self.has_space():
            temp = Node(data)
            temp.set_next_node(self.head)
            self.head = temp
            self.size += 1
        else:
            print("Sorry, stack is full!")
    
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        else:
            temp = self.head
            self.head = self.head.get_next_node()
            self.size -= 1
            return temp.get_value()
            
    def peek(self):
        if not self.is_empty():
            return self.head.get_value()
    

#driver program
values = Stack(5)
values.push(10)
values.push(2)
values.push(12)
values.push(13)
values.push(-1)

print(values.pop())
print(values.peek())
    
        
        
        
        
        
        
        
            
            
            
            
            
            
            