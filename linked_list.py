#linked list

class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        if self.head:
            while current.next:
                current = current.next
                current.next = new_element
        else:
            self.head = new_element
        







