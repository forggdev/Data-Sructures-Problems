# Problem 2: Altura de un Arbol
class Node:
    def __init__(self, key, height):
        self.key = key
        self.left = None
        self.right = None
        self.height = height


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insertRecursively(self.root, key, 1)

    def _insertRecursively(self, root, key, height):
        if root is None:
            return Node(key, height)
        if key < root.key:
            root.left = self._insertRecursively(root.left, key, height+1)
        elif key > root.key:
            root.right = self._insertRecursively(root.right, key, height+1)
        return root

    def search(self, key):
        if self._searchRecursively(self.root, key) != None:
            return True
        else:
            return False

    def _searchRecursively(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self._searchRecursively(root.left, key)
        return self._searchRecursively(root.right, key)

    def delete(self, key):
        self.root = self._deleteRecursively(self.root, key)

    def _deleteRecursively(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self._deleteRecursively(root.left, key)
        elif key > root.key:
            root.right = self._deleteRecursively(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._minValueNode(root.right).key
            root.right = self._deleteRecursively(root.right, root.key)
        return root

    def _minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def preOrder(self):
        elements = []
        self._preOrderRecursively(self.root, elements)
        return elements

    def _preOrderRecursively(self, root, elements):
        if root:
            elements.append(root.height)
            self._preOrderRecursively(root.left, elements)
            self._preOrderRecursively(root.right, elements)


N = int(input())
for i in range(N):
    A = tuple(map(int, input().split()))
    bst = BinarySearchTree()
    for elem in A:
        if elem == -1:
            break
        bst.insert(elem)
    print(max(bst.preOrder()))