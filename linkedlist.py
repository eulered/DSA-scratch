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

  def append(self, value):
    new_node = Node(value)
        
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next = new_node
        self.tail = new_node
        
    self.length += 1
        
  def print_val(self):
    temp = self.head
    while temp is not None:
        print(temp.value)
        temp = temp.next
            
  def get_middle(self):
    values = []
    temp = self.head
        
    while temp is not None:
        values.append(temp.value)
        temp = temp.next
            
    middle = len(values) // 2
    return values[middle]
