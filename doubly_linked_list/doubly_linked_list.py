"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    self.head.insert_before(value)
    self.head = self.head.prev

  def remove_from_head(self):
    old_head = self.head.value
    new_head = self.head.next
    self.head.delete()
    return old_head

  def add_to_tail(self, value):
    self.tail.insert_after(value)
    self.tail = self.tail.next


  def remove_from_tail(self):
    new_tail = self.tail.prev 
    old_tail = self.tail.value
    self.tail.delete()
    self.tail = new_tail
    return old_tail

  def find_node(self, node):
    current_node = self.head
    while current_node:
      if current_node.value == node.value:
        return current_node
      else:
        current_node = current_node.next
    return None

  def move_to_front(self, node):
    matched_node = self.find_node(node)
    self.add_to_head(matched_node.value)
    matched_node.delete()

  def move_to_end(self, node):
    matched_node = self.find_node(node)
    self.add_to_tail(matched_node.value)
    matched_node.delete()

  def delete(self, node):
    matched_node = self.find_node(node)
    matched_node.delete()
    
  def get_max(self):
    max = float('-inf')
    current_node = self.head
    while current_node:
      if current_node.value > max:
        max = current_node.value
      current_node = current_node.next
    return max
