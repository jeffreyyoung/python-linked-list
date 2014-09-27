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

	def printList(self):
		node = self.head
		str = ""
		while node:
			str += '{},'.format(node.data)
			node = node.next
		print str

ll = LinkedList()
ll.push_back(99)
ll.push_front(1)
ll.push_front("asdf")
ll.push_front(3)
ll.push_front(4)
ll.push_back(5)

ll.printList()
