import time
from random import shuffle


class Node:
    def __init__(self, value=None, next=None):
        self.next = next
        self.value = value

    def __str__(self):
        return str(self.value)


class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        self.items.append(value)
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            First = self.items.pop(0)
            self.size -= 1
            return First
        raise ValueError("Queue is Empty")


class ImprovedQueue:
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None

    def is_empty(self):
        return self.length == 0

    def insert(self, cargo):
        node = Node(cargo)
        if self.length == 0:
            # If list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # Find the last node
            last = self.last
            # Append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        cargo = self.head.value
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return cargo


class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item


class NodePriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        return str(Node.value)

    def is_empty(self):
        return self.size == 0

    def enqueue(self, cargo):
        NewNode = Node(cargo)
        if self.size == 0:
            self.head = self.tail = NewNode
        else:
            last = self.tail
            last.next = NewNode
            self.tail = NewNode
        self.size += 1

    def print_queue(self):
        last = self.head
        print("[", end="")
        while last.next:
            print(last, end=",")
            last = last.next
        print("]")

    def dequeue(self):
        maxval = 0
        last = self.head
        while last != None:
            if last.value > maxval:
                maxval = last.value

            last = last.next
        self.size -= 1

        return maxval

    def OrderedDequeue(self):
        maxval = self.head.value
        self.head = self.head.next
        self.size -= 1
        return maxval


def TimeComplexityTesting():
    # Node PQ
    DO1 = NodePriorityQueue()
    t1 = time.process_time()
    for i in range(3):
        x = [x for x in range(0, 3000, 1)]
        shuffle(x)
        for val in x:
            DO1.enqueue(val)

        for i in range(len(x)):
            DO1.dequeue()
    t2 = time.process_time()

    # List PQ
    DO2 = PriorityQueue()
    t3 = time.process_time()
    for i in range(3):
        x = [x for x in range(3000)]
        shuffle(x)
        for val in x:
            DO2.insert(val)

        for i in range(len(x)):
            DO2.remove()
    t4 = time.process_time()

    # NodeQ
    DO3 = ImprovedQueue()
    t5 = time.process_time()
    for i in range(3):
        x = [x for x in range(3000)]
        for val in x:
            DO3.insert(val)

        for i in range(len(x)):
            DO3.remove()
    t6 = time.process_time()

    # ListQ
    DO4 = ListQueue()
    t7 = time.process_time()
    for i in range(3):
        x = [x for x in range(3000)]
        for val in x:
            DO4.enqueue(val)

        for i in range(len(x)):
            DO4.dequeue()
    t8 = time.process_time()

    print(
        "The node implemented PQ took {0:.3f}\nThe list implemented PQ took {1:.3f}".format(
            t2 - t1, t4 - t3
        )
    )

    print(
        "The node implemented Queue took {0:.3f}\nThe list implemented Queue took {1:.3f}".format(
            t6 - t5, t8 - t7
        )
    )


TimeComplexityTesting()