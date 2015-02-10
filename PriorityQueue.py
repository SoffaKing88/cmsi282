"""PriorityQueue.py
Nicholas Soffa
2/9/15
Worked together with Joel Hoeman"""

import math
class PriorityQueue:

	def __init__(self):
		self.queue = []

	def __len__(self):
		return len(self.queue)

	def add(self, input):
		self.queue.append(input)
		i = len(self) - 1
		while self.queue[i] < (self.queue[int(math.floor(i / 2))]):
			storeValue = self.queue[int(math.floor(i / 2))]
			self.queue[int(math.floor(i / 2))] = self.queue[i]
			self.queue[i] = storeValue
			i = int(math.floor(i / 2))
		return self

	def remove(self):
		if not self.queue:
			raise LookupError
		self.queue[0] = self.queue.pop()
		i = 0
		for x in range (0, int(math.log(len(self), 2)) + 1):
			if self.queue[i] > self.queue[i * 2] or self.queue[i] > self.queue[i * 2 + 1]:
				if self.queue[i * 2] >= self.queue[i * 2 + 1]:
					storeValue = self.queue[i * 2 + 1]
					j = i * 2 + 1
				elif self.queue[i * 2] < self.queue[i * 2 + 1]:
					storeValue = self.queue[i * 2]
					j = i * 2
				self.queue[j] = self.queue[i]
				self.queue[i] = storeValue
				i = j
		return self.queue

	def peek(self):
		if not self.queue:
			raise LookupError
		else:
			return self.queue[0]

	def __str__(self):
		return str(self.queue)

q = PriorityQueue()
q.add(8)
q.add(5)
q.add(4)
q.add(48)
q.add(2)
q.add(17)
q.add(28)
q.remove()
print(q.__str__())
