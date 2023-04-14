class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

    def __str__(self):
        return self.data


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if not fl_find and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    def show_tree(self, node):
        if node is None:
            return
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    @staticmethod
    def show_wide_tree(node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn

    @staticmethod
    def __del_leaf(s, p):
        if p.left == s:
            p.left = None
        else:
            p.right = None

    @staticmethod
    def __del_one_child(s, p):
        if s.left is None:
            if p.left == s:
                p.left = s.right
            else:
                p.right = s.right
        elif s.right is None:
            if p.left == s:
                p.left = s.right
            else:
                p.right = s.right

    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        elif s.left is not None and s.right is not None:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)


if __name__ == '__main__':
    # vi = [10, 5, 7, 16, 14, 2, 20]
    vi = [20, 5, 24, 2, 16, 11, 18]
    t = Tree()
    for item in vi:
        t.append(obj=Node(item))

    t.show_wide_tree(node=t.root)
    print('--------------')
    t.del_node(5)
    t.show_wide_tree(node=t.root)
