class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value > self.value:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)
    if value <= self.value:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.value > target:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    if self.value < target:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if self.right:
      return self.right.get_max()
    else:
      return self.value
