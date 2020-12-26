"""
linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def deletenode(self, key):
        temp = self.head

        if temp is not None:
            if temp.next is None:
                self.head = None
            else:
                self.head = temp.next
            return
        while temp is not None:
            print(temp)
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None


    def getcount(self):
        temp = self.head
        count = 0
        print(temp)
        while temp is not None:
            print('in while')
            count += 1
            print('count:',count)
            temp = temp.next
        return count

    def search(self,li, key):
        if not li:
            return False
        if li.data == key:
            return True
        return self.search(li.next, key)
    def getNthNode(self,li,position):

        count = 0
        while(li):
            if count == position:
                print("in if loop")
                return li.data
            count = count + 1
            li = li.next

        return 0






llist = LinkedList()
llist.push(10)
llist.push(20)
llist.printlist()
#llist.deletenode(2)
print('2ndpostion',llist.getNthNode(llist.head, 1))
print('count is :', llist.getcount())
if llist.search(llist.head,2):
    print("yes")
else:
    print("false")
