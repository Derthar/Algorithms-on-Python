

class Node:
    def __init__(self, value=None, sled=None):
        self.value = value
        self.next = sled


class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.lenght = 0

    def add(self, n):
        self.lenght += 1
        if self.head is None:
            self.head = self.tail = Node(value=n, sled=None)
            return
        self.tail.next = self.tail = Node(value=n, sled=None)

    def __get_values(self, node):
        if node.next is not None:
            print(f'{node.value} -> {node.next.value}')
            self.__get_values(node.next)
        else:
            print(node.value)

    def print(self):
        if self.head is not None:
            print(f'{self.head.value} -> {self.head.next.value}')
            self.__get_values(node=self.head.next)
        else:
            print('Empty list')

    def reverse(self):
        # Суть в том, чтобы пробежаться по списку, отсечь у первой вершины ссылку на следующую
        #  у каждой следующей вместо ссылки на следующую поставить ссылку на предыдущую
        # затем меняем первую вершину на последнюю
        current_node = self.head
        prev_node = None
        next_node = current_node.next

        while next_node is not None:
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            next_node = current_node.next

        current_node.next = prev_node
        self.head = current_node


if __name__ == '__main__':

    L = LinkedList()
    L.add(1)
    L.add(4)
    L.add(9)
    L.add(7)
    L.add(3)

    L.print()

    L.reverse()
    print('********')

    L.print()
