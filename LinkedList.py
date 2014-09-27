class Node:
	def __init__(self):
		self.data = None
		self.next = None


class LinkedList:
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None

	def push_front(self, data):
		n = Node()
		n.data = data
		if self.size is 0:
			self.head = n
			self.tail = n
		else:
			n.next = self.head
			self.head = n
		self.size += 1


	def push_back(self, data):
		n = Node()
		n.data = data
		if self.size is 0:
			self.head = n
			self.tail = n
		else:
			self.tail.next = n
			self.tail = n
		self.size += 1 

	def insert(self, data, index): #first list element is at index 0
		if self.size == 0:
			n = Node()
			n.data = data
			self.head = n
			self.tail = n
			self.size += 1
		elif index <= self.size:
			n = Node()
			n.data = data
			node = self.head
			for i in range(0, index):
				node = node.next
			a = node
			c = node.next
			a.next = n
			n.next = c
			self.size += 1
		else:
			print "index too large, index ={}, size={}".format(index, self.size)

	def printList(self):
		node = self.head
		str = ""
		counter = 0
		while node:
			str += '{},'.format(node.data)
			node = node.next
			print counter, node.data
			counter += 1

		#print str

ll = LinkedList()
for i in range(0,40):
	ll.push_back(i)
for i in range(0, 99):
	d = i * 4
	ll.insert("inserted at {} position".format(d),d)




ll.printList()
