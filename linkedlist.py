class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self, value):
    new_node = Node(value)

    self.head = new_node
    self.tail = new_node
    self.length = 1
  
  def print_val(self):
    temp = self.head
    while temp is not None:
      print(temp.value)
      temp = temp.next

linkedlist1 = LinkedList(1)

linkedlist1.print_val()