class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def add_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def print_backward(self):
        print("[", sep=",", end="")
        if self.head is not None:
            self.head.print_backward()
        print("]", end="")


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

    def print_backward(self):
        if self.next is not None:

            tail = self.next
            tail.print_backward()
            print(", ", end="")
        print(self.value, end="")


def print_list(node):
    print("[", end="")
    while node != None:
        print(node, end=",")
        node = node.next
    print("]")


def print_backwards(node):
    if node == None:
        return
    head_node = node
    next_node = head_node.next
    print_backwards(next_node)
    print(head_node, end=" ")


def print_backward_nicely(list):
    print("[", end=" ")
    print_backwards(list)
    print("]")


def remove_second(node):
    head = node
    node2 = head.next
    head.next = node2.next
    node2.next = None
    return node2
