class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    deleted = self.storage[0]
    end = self.storage.pop()
    if len(self.storage):
      self.storage[0] = end
      self._sift_down(0)
    return deleted

  def get_max(self):
    if not len(self.storage):
      return 
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def get_left_child(self,index):
    left_child = (index * 2) + 1
    if left_child > len(self.storage) - 1:
      return None
    else:
      return left_child

  def get_right_child(self,index):
    right_child = (index * 2) + 2
    if right_child > len(self.storage) - 1:
      return None
    else:
      return right_child

  def _bubble_up(self, index):
    parent_index = (index - 1) // 2
    heap = self.storage
    while parent_index >= 0:
      if heap[index] > heap[parent_index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
      index, parent_index = parent_index,(parent_index - 1) // 2

  def _sift_down(self, index):
    heap = self.storage
    while self.get_left_child(index):
      bigger_child = self.get_left_child(index)
      right_child = self.get_right_child(index)
      if right_child and heap[right_child] > heap[bigger_child]:
        bigger_child = right_child
      if heap[bigger_child] > heap[index]:
        heap[index], heap[bigger_child] = heap[bigger_child], heap[index]
      index = bigger_child

        
    

