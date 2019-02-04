#Implementing linked list 
class node:
    def __init__(self, data, priority=None):
        self.data=data
        self.next=None
        self.priority=priority

class linkedlist:
    def __init__(self):
        self.head=None

    def prepend(self,element,priority=None):
        new_node=node(element,priority)
        new_node.next=self.head
        self.head=new_node
    
    def append(self,element,priority=None):
        new_node=node(element,priority)
        if self.head==None:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node

    def remove(self,element):
        prev=None
        current=self.head
        if current==None:
            return("The list is empty ; cannot remove anything")
        if current.data==element:
            self.head=current.next
            return
        while current.next:
            if current.data!=element:
                prev=current
                current=current.next
            else:
                prev.next=current.next
        if current.data==element:
            prev.next=None
            return
        return("Did not find given value in list ; nothing deleted")

    def insert(self,element,position,priority=None):
        new_node=node(element,priority)
        prev=None
        current=self.head
        pos=0
        if position==0:
            self.prepend(element)
        if current==None:
            self.head=node(element)
        else:
            while current.next:
                prev=current
                current=current.next
                pos+=1
                if pos==position:
                    prev.next=new_node
                    new_node.next=current
            if pos<position:
                print("Position given is larger than size of list")
                return
        
    def find(self,element):
        current=self.head
        while current:
            if current.data==element:
                return True
            current=current.next
        return False

    def size(self):
        s=0
        current=self.head
        while current.next:
            s+=1
            current=current.next
        return s+1
    
    def show(self):
        nodes=[]
        current=self.head
        while current:
            nodes.append(current.data)
            current=current.next
        print(nodes)

    def peek(self):
        if self.head==None:
            print("List is empty")
            return
        print(self.head.data)

class p_queue:
    def __init__(self):
        self.queue=linkedlist()

    def peek(self):
        self.queue.peek()

    def push(self,value,priority):
        current=self.queue.head
        pos=0
        if current==None:
            self.queue.append(value,priority)    
            return
        while current.next:
            if current.priority>priority:
                self.queue.insert(value, pos, priority)
                return
            pos+=1
            current=current.next
        if current.next==None:
            if current.priority<=priority:
                self.queue.append(value,priority)
            else:
                self.queue.insert(value,pos,priority)

    def pop(self):
        if self.queue.head==None:
            print("List is empty")
        else:
            current=self.queue.head
            self.queue.head=current.next
            return(current.data,current.priority)
            
    def show(self):
        self.queue.show()
            
a=p_queue()
a.push('Adam',2)
a.push('Tim',5)

                
                
            
