# Деревья

from hypothesis import given, strategies as st


class TreeNode:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.v:
            if node.l is not None:
                self._add(val, node.l)
            else:
                node.l = TreeNode(val)
        else:
            if node.r is not None:
                self._add(val, node.r)
            else:
                node.r = TreeNode(val)

    def find(self, val):
        if self.root is not None:
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if val == node.v:
            return node
        elif (val < node.v and node.l is not None):
            return self._find(val, node.l)
        elif (val > node.v and node.r is not None):
            return self._find(val, node.r)

    def deleteTree(self):
        self.root = None
        return 0

    def printTree(self):
        if self.root is not None:
            self._printTree(self.root)

    def _printTree(self, node):
        if node is not None:
            self._printTree(node.l)
            print(str(node.v) + ' ')
            self._printTree(node.r)


@given(q=st.integers(), w=st.integers(), e=st.integers(), r=st.integers(), t=st.integers(), y=st.integers())
def testing_tree(q, w, e, r, t, y):
    tree = Tree()
    assert tree is not None
    tree.add(q)
    tree.add(w)
    tree.add(e)
    tree.add(r)
    tree.add(t)
    tree.add(y)
    tree.printTree()
    assert tree.deleteTree() == 0  # Трудно доказать, легко проверить


testing_tree()