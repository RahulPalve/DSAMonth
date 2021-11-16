class Queue:
   def __init__(self):
       self.queue = []
       self.front = 0
       self.back = 0
   def enqueue(self, no):
       self.back =+1
       self.queue[self.back] = no
   def dequeue(self):
       del self.queue[self.front]
       self.front =+1
