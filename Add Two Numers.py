# Definition for singly-linked list.
from re import T


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):

    while l1.next != None:
        print(l1.val)
        l1=l1.next
c = ListNode(33)
b = ListNode(22,c)
a = ListNode(11,b)
addTwoNumbers(a,b)
