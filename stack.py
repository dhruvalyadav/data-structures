class Stack:
    def __init__(self):
        self.data = []
    def push(self,values):
        self.data.append(values)
    def pop(self):
        if len(self.data)==0:
            return 
        else:
            self.data.pop()
    def peek(self):
        if len(self.data)==0:
            return
        else:
            return self.data[-1]
    def size(self):
        return len(self.data)
    def show(self):
        return str(self.data)
s=Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.size())
s.pop()
print(s.show())

#reverse a string
s='hello'
ans=''
stack=[]
for i in s:
    stack.append(i)
while stack:
    ans+=stack.pop()
print(ans)

#reverse a list
ls=[10,200,30]
rev=[]
stack=[]
for i in range(len(ls)):
    stack.append(ls[i])
while stack:
    rev.append(stack.pop())
print(rev)

#paraenthesis matching
def matching(s):
    stack=[]
    for i in s:
        if(i=='(' or i=='{' or i=='['):
            stack.append(i)
        else:
            if not stack:
                return False
            p=stack.pop()
            if(i==')'and p!='(') or (i=='}'and p!='{') or (i==']' and p!='['):
                return False
    return len(stack)==0
print(matching("()"))

#stack using linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def is_empty(self):
        return self.head is None
    def push(head,data):
        new=Node(new)
