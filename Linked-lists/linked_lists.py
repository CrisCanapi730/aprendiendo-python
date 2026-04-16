
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    
    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_at_end(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
            
    def print(self):
        current = self.head
        while current.next is not None:
            print(current.val, end="->")
            current = current.next
        print(f'{current.val}->None')
        
    def delete_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def delete_last(self):
        if self.head is None:
            return
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
    
    def delete_value(self, value):
        if self.head is None:
            return
        
        if self.head.val == value:
            self.head = self.head.next
            return
        
        current = self.head
        while current.next is not None:
            if current.next.val == value:
                current.next = current.next.next
                return
            current = current.next
    def get_length(self):
        count = 0
        current = self.head
        while current is not None:
            count+=1
            current = current.next
        return count
    # ---- REVISAR ----
    def reverse(self): # revisar
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
    
        
my_list = LinkedList()
my_list.add_at_beginning(3)
my_list.add_at_beginning(2)
my_list.add_at_beginning(1)
my_list.add_at_beginning(0)
my_list.add_at_end(4)
my_list.add_at_end(8)
my_list.print()