# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def insertAfter(self, prev_node, new_data):
    
        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return
    
        # 2. Create new node &
        # 3. Put in the data
        new_node = ListNode(new_data)
    
        # 4. Make next of new Node as next of prev_node
        # new_node.next = prev_node.next
    
        # 5. make next of prev_node as new_node
        prev_node.next = new_node

def addTwoNumbers(l1, l2):
    addNext = 0
    newVal = 0
    ansL = ListNode(l1.val+l2.val%10)
    l2OutOfIndex = False
    l1OutOfIndex = False
    while l1 != None or l2 != None:
        if (l1 == None):
            x = 0
            l1OutOfIndex = True
        elif (l2 == None):
            y = 0
            l2OutOfIndex = True
        else:
            x= l1.val
            y=l2.val
        temp = x + y + addNext
        addNext = int(temp/10)
        # print(addNext)
        temp = temp%10
        new = ListNode(temp)
        print(temp)
        print(new.val)
        #
        while ansL.next != None:
            ansL = ansL.next
        ansL.next = new
        if(l1OutOfIndex == False):
            l1 = l1.next
        if(l2OutOfIndex == False):
            l2 = l2.next
    print(ansL.val)
# create ListNode
c = ListNode(3)
b = ListNode(4,c)
a = ListNode(2,b)

g = ListNode(9)
f = ListNode(4,g)
e = ListNode(6,f)
d = ListNode(5,e)


addTwoNumbers(a,d)
