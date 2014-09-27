class Node:
	def __init__(self):
		self.data = None
		self.next = None


class LinkedList:
	def __init__(self):
		self.size = 0
		self.head = None
		self.tail = None

	def addFront(self, data):
		n = Node()
		n.data = data
		if self.head is None:
			self.head = n
			self.tail = n
		else:
			n.next = self.head
			self.head = n
		print "head:", self.head, ",tail: ", self.tail


	def addToTail(self, data):
		n = Node()
		n.data = data
		if self.tail is None:
			self.head = n
			self.tail = n
		else:
			self.tail.next = n
			self.tail = n


	def printList(self):
		node = self.head
		str = ""
		while node:
			str += '{},'.format(node.data)
			node = node.next
		print str

ll = LinkedList()
ll.addFront(1)
ll.addFront("asdf")
ll.addFront(3)
ll.addFront(4)
ll.addToTail(5)

ll.printList()
