# Case Study 2

# You are developing a simple playlist manager for a music app. 
# Use a singly linked list to represent the playlist where each node stores a song name. 
# Implement operations to add a song at the end, delete a song by name, and display the 
# full playlist. Demonstrate how a circular linked list could help in continuous song playback.
class node:
    def __init__(self,data=None,next=None):
        self.data = data 
        self.next = next
        
class music:
    def __init__(self,head=None):
        self.head=head
    
    def isempty(self):
        return self.head == None
    def insert(self,s):
        nn = node(s)
        if self.isempty():
            self.head=nn
        else:
            temp=self.head
            while temp.next != None:
                temp = temp.next
            temp.next=nn
    def delete(self,s):
        if self.isempty():
            print("underflow")
            return
        if self.head==s:
            self.head=self.head.next
            return
        temp =self.head
        while temp.next.data != s:
            temp=temp.next
        temp.next=temp.next.next 
    def display(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

m = music()
m.insert("shivabhishek geet")
m.insert("aale marathe")
m.insert("aala raja")
m.insert("chakar shivba ch honar r")
m.display()
m.delete("aala raja")
print("after delete")
m.display()