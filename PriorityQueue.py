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
		if len(self) == 1:
			self.queue.pop()
			return self
		self.queue[0] = self.queue.pop()
		i = 0
		height = int(math.floor(math.log(len(self), 2)))
		for x in range (0, height):
			if (i * 2) + 2 > len(self) - 1:
				if self.queue[(i * 2) + 1] < self.queue[i]:
					j = (i * 2) + 1
					storeValue = self.queue[j]
					self.queue[j] = self.queue[i]
					self.queue[i] = self.queue[j]
					i = j
			elif self.queue[i] > self.queue[(i * 2) + 1] or self.queue[i] > self.queue[(i * 2) + 2]:
				if self.queue[(i * 2) + 1] > self.queue[(i * 2) + 2]:
					j = (i * 2) + 2
					storeValue = self.queue[j]
				elif self.queue[(i * 2) + 1] <= self.queue[(i * 2) + 2]:
					j = (i * 2) + 1
					storeValue = self.queue[j]
				self.queue[j] = self.queue[i]
				self.queue[i] = storeValue
				i = j
				if ((j * 2) + 2) >= len(self):
					break
		return self.queue

	def peek(self):
		if not self.queue:
			raise LookupError
		else:
			return self.queue[0]

	def __str__(self):
		return str(self.queue)
