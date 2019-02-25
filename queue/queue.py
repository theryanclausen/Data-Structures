class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def enqueue(self, item):
    self.size += 1
    self.storage.append(item)
  
  def dequeue(self):
    dequeued = None
    if len(self.storage):
      dequeued=self.storage[0]
      self.storage =self.storage[1:]
      self.size -= 1
    return dequeued

  def len(self):
    return self.size
