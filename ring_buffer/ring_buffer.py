class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    self.storage[self.current] = item
    self.current = self.current + 1 if self.current < self.capacity - 1 else 0
    pass

  def get(self):
    return [item for item in self.storage if not item == None]
    pass