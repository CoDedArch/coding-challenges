class NewNode(object):
    def __init__(self) -> None:
        self.value = None
        self.ref = None

class FixedArray(list):
    def __init__(self, size=5):
        self.arr = []
        self.size = size
    def append(self, value):
        if not self.OutOfBoundsError():
            self.arr.append(value)

    def OutOfBoundsError(self):
        if len(self.arr) > self.size:
            raise IndexError


class LinkedList(object):
    def __init__(self):
        self.list_of_elements = FixedArray()
        self._head = None
        self._tail = None

    def returnNodes(self):
        return self.list_of_elements.arr
    
    def insertAtAnyIndex(self, index):
        pass
    
    def addElement(self, element):
        if len(self.list_of_elements) == 0:
            head = NewNode()
            head.value = element
            self._head = head
            self.list_of_elements.append(head)
        elif len(self.list_of_elements) == 1:
            tail = NewNode()
            tail.value = element
            self._tail = tail
            self._head.ref = id(self._tail)
            self.list_of_elements.append(tail)
        else:
            pass




    def getRefToNextNode(self):
        pass

newElement = LinkedList()
newElement.addElement(1)
newElement.addElement(2)
for node in newElement.returnNodes():
    print(node.value)
