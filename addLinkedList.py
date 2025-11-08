# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single 
# digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self,start=None):
        self.start=start
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode])-> Optional[ListNode]:
        num1=""
        num2=""
        temp1=l1
        temp2=l2
        while temp1!=None:
            num1+=str(temp1.val)
            temp1=temp1.next
        while temp2!=None:
            num2+=str(temp2.val)
            temp2=temp2.next 
        
        num3=int(num1)+int(num2)
        num3=str(num3)
        num3=num3[::-1]
        if self.start==None:
            nn=ListNode(int(num3[0]))
            self.start=nn
        for i in range(1,len(num3)):
            temp=self.start
            while temp.next != None:
                temp=temp.next
            nn=ListNode(int(num3[i]))
            temp.next=nn
            temp=temp.next
        return self.start