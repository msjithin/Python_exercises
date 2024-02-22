from collections import deque

class Node:
    def __init__(self, data) -> None:
        self.data = data 
        self.next = None 
        
    def __repr__(self) -> str:
        return self.data
    
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None 
            
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next 
            
        nodes.append('None')
        return " -> ".join(nodes)
    
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr 
            curr = curr.next 
            
    def append_left(self, node):
        node.next = self.head
        self.head = node 
    
    def append_right(self, node):
        if self.head is None:
            self.head = node 
            return 

        for curr in self:
            pass 
        
        curr.next = node 
        
    def append_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        for curr in self:
            if curr.data == target_node_data:
                new_node.next = curr.next 
                curr.next = new_node
                return 
        
        raise Exception(f"Node with data {target_node_data} not found")
        
        
    def append_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List if empty")
        
        if self.head.data == target_node_data:
            return self.append_left(new_node)
        
        prev = self.head 
        for curr in self:
            if curr.data == target_node_data:
                prev.next = new_node
                new_node.next = curr 
                return 
            prev = curr 
            
        raise Exception(f"Node with data {target_node_data} not found")
    
    def insert_at_index(self, data, index):
        new_node = Node(data)
        curr = self.head 
        
        position = 0
        if position == index:
            self.append_left(new_node)
            return 
    
        while curr != None and position +1 != index:
            position += 1
            curr = curr.next
            
        if curr != None :
            new_node.next = curr.next
            curr.next = new_node
        else:
            raise Exception(f'Index {index} not present')
        
    def update_node(self, data, index):
        curr = self.head 
        position = 0
        if position == index :
            curr.data = data 
            return 
        
        while curr != None and position != index:
            position += 1
            curr = curr.next 
            
        if curr != None:
            curr.data = data 
        else:
            raise Exception(f'Index {index} not found')
            
        
        
    def remove(self, target_node_data):
        if self.head is None:
            raise Exception("List if empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next 
            return 
        
        prev = self.head 
        for curr in self:
            if curr.data ==target_node_data:
                prev.next = curr.next
                return 
            prev = curr 
            
        raise Exception(f"Node with data {target_node_data} not found")
        
    def remove_first(self):
        if self.head is None:
            return 
        
        self.head = self.head.next
        
    def remove_last(self):
        if self.head is None:
            return 
        
        curr = self.head 
        while curr.next.next:
            curr = curr.next
            
        curr.next = None
        
    def remove_at_index(self, index):
        if self.head is None:
            return 
        
        curr = self.head 
        positon = 0
        if positon == index:
            self.remove_first()
            return 
        
        while curr != None and positon + 1 != index:
            positon += 1
            curr = curr.next 
            
        if curr != None:
            curr.next = curr.next.next
        else:
            raise Exception(f'Index {index} not found')
            
        
    def __len__(self) -> int:
        size = 0
        if self.head is None:
            return size 
        
        for curr in self:
            size += 1
        return size
        

def mergeLists(head1, head2):
    result = LinkedList()
    max_ll = LinkedList()
    max_ll.append_left(Node(float('inf')))
    heads = [head1, head2, max_ll]
    while len(heads) > 1:
        which = heads[0].data > heads[1].data
        result.insert_node(heads[which].data)
        if not heads[which].next: heads.pop(which)
        else: heads[which] = heads[which].next
    return result.head


def deque_example():
    queue  = deque()
    print(queue)
    
    queue.append('Mary')
    queue.append('John')
    queue.append('Susan')
    print(queue)
    
    queue.popleft()
    print(queue)
    queue.pop()
    print(queue)
    queue.appendleft('David')
    print(queue)
    
    
def ll_example():
    llist = LinkedList()
    print(llist)
    
    Node1 = Node("a")
    Node2 = Node("b")
    Node3 = Node("c")
    Node1.next = Node2
    Node2.next = Node3 
    
    llist.head = Node1 
    print(llist)
    
    llist.append_left(Node("z"))
    print(llist)
    
    llist.append_right(Node("d"))
    print(llist)
    
    for node in llist:
        print(node)
    
    
    llist.append_after('c', Node('AFc'))
    print(llist)
    
    llist.append_before('d', Node('BFd'))
    print(llist)
    
    llist.remove('b')
    print(llist)
    
    llist.remove_last()
    print(llist)
    
    llist.insert_at_index('in3', 3)
    print(llist)
    
    llist.remove_first()
    print(llist)
    
    llist.remove_at_index(2)
    print(llist)
    
    print(len(llist))
    
    
if __name__ == "__main__":
    print("Deque :")
    deque_example()
    print("\nLinked list:")
    ll_example()