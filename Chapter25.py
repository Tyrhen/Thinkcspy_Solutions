class Stack:
    def __init__(self):
        self.size = 0
        self.items = []

    def __str__(self):
        return str(self.items)

    def pop(self):
        self.size -= 1
        return self.items.pop()

    def push(self, item):
        self.items.append(item)
        self.size += 1

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


def postfix(expr):
    import re

    token_list = re.split("([^0-9])", expr)
    stack = Stack()

    for token in token_list:
        if token == " " or token == "":
            continue

        elif token == "+":
            sum = stack.pop() + stack.pop()
            stack.push(sum)

        elif token == "*":
            product = stack.pop() * stack.pop()
            stack.push(product)

        else:
            stack.push(int(token))

    return stack.pop()


# postfix("2 3 * 1 +")
