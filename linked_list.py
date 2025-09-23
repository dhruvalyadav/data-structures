class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def traversal(head):
    while head is not None:
        print(head.data, end=" ") #printing current data of node on which head is pointing
        head=head.next #move to next node
    print()
def travel(head): #recursive approach
    if head is None:
        print()
        return
    print(head.data,end=" ")
    travel(head.next)

# def search(head,k):#recursive approach
#     if head is None:
#         return False
#     if(head.data==k):
#         return True
#     return search(head.next,k)

def search(head,k):
    curr=head
    while curr is not None:
        if(curr.data==k):
            return True
        curr=curr.next
    return False

def length(head):#length of linked list
    count=0
    curr=head
    while curr is not None:
        curr=curr.next
        count+=1
    print(count)
head=Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next=Node(200)
travel(head)
k=200
if search(head,k):
    print("Yes")
else:
    print("No")
length(head)



#insertionṇ at start
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def insert(head,new):
    new =Node(new)
    new.next=head
    curr=new
    while curr is not None:
        print(curr.data,end=" ")
        curr=curr.next
    print()
    return new
def end(head,new):
    new=Node(new)
    if head is None:#if empty
        head=new
    else:
        curr=head
        while curr.next:
            curr=curr.next
        curr.next=new
    while curr: #print
        print(curr.data,end=" ")
        curr= curr.next
    print()
    return head

def reverse(head):
    prev=None
    curr=head
    while curr is not None:
        next_Node=curr.next #stores the node
        curr.next=prev  #reverse the pointer to prev node
        prev=curr #moves prev forward
        curr=next_Node #move to next node
    head=prev
    return head 
def display(head):
    curr=head
    while curr:
        print(curr.data,end=" ")
        curr=curr.next
    print()
head=None
head=insert(head,1)
head=insert(head,3)
head=insert(head,5)
head=end(head,10)
display(head)
head=reverse(head)
display(head)


#doubly linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly:
    def __init__(self):
        self.head=None
    def insert(self,data): #at beginning
        new=Node(data)
        if(self.head):
            new.next=self.head
            self.head.prev=new
        self.head=new
    def inend(self,data):
        new=Node(data)
        if not self.head:
            self.head=new
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new
        new.prev=curr
    def position(self,pos,data):
        if pos==1:
            self.insert(data)
        new=Node(data)
        curr=self.head
        for _ in range(pos-2):
            if not curr:
                print("out of range")
                return
            curr=curr.next
        new.next=curr.next
        new.prev=curr
        if curr.next:
            curr.next.prev=new
        curr.next=new
    def delete(self,key):
        curr=self.head
        while curr is not None:
            if(curr.data==key):
                if curr.prev:
                    curr.prev.next=curr.next
                else:
                    self.head=curr.next
                if curr.next:
                    curr.next.prev=curr.prev
                return
            curr=curr.next
        print('value not found')            
        
    def reverse(self):
        curr=self.head
        temp=None
        while curr:
            temp=curr.next
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        if temp:
            self.head=temp.prev
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end=" ")
            curr=curr.next
        print("None")
dll=Doubly()
dll.insert(10)
dll.insert(20)
dll.inend(40)
dll.position(2,30)
dll.display()
dll.delete(2)
dll.reverse()
dll.display()