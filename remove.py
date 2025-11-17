# remove Nth node from the end of the list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n) :
        count=0
        temp=head
        temp2=head
        while temp != None:
            count+=1
            temp=temp.next

        n_count=count-n-1
        if count==1:
            head=None
            return head
        for i in range(n_count):
            temp2=temp2.next
        temp2.next=temp2.next.next
        return head
        