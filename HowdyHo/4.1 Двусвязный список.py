

class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self, head=None, tail=None, lenght=0):
        self.head = head
        self.tail = tail
        self.lenght = lenght

    def add_tail(self, value):
        if self.head is None:
            self.head = self.tail = Node(value=value)
            self.lenght += 1
        elif self.head is not None and self.head == self.tail:
            self.tail.next = Node(value=value)
            self.head.next = self.tail = Node(value=value)
            self.tail.prev = self.head
            self.lenght += 1
        else:
            node = self.tail
            self.tail = Node(value=value)
            self.tail.prev = node
            node.next = self.tail

    def add_head(self, value):
        self.head, self.head.next = Node(value=value), self.head

    def __get_values(self, node):
        if node.next is not None:
            print(f'{node.value} <--> {node.next.value}')
            self.__get_values(node.next)
        else:
            print(node.value)

    def print_values(self):
        if self.head is None:
            print('Empty list')
        else:
            print(f'{self.head.value} <--> {self.head.next.value}')
            self.__get_values(self.head.next)

    def delete_head(self):
        self.head, self.head.next.prev = self.head.next, None

    def delete_tail(self):
        self.tail, self.tail.next = self.tail.prev, None

    def reverse(self):
        if self.head is None:
            print('Empt list')
            return
        cur_node = self.head
        next_node = cur_node.next
        while next_node is not None:
            cur_node.next, cur_node.prev = cur_node.prev, cur_node.next
            cur_node = next_node
            next_node = cur_node.next
        else:
            cur_node.next, cur_node.prev = cur_node.prev, cur_node.next
        self.head, self.tail = self.tail, self.head


if __name__ == '__main__':
    Ll = LinkedList()

    Ll.add_tail(1)
    Ll.add_tail(2)
    Ll.add_tail(3)
    Ll.add_tail(4)

    Ll.print_values()

    print('********')
    Ll.reverse()
    Ll.print_values()
