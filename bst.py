# Binary Search Tree — Python Implementation
# Operations: insert, search, delete, inorder, preorder, postorder, level-order

from collections import deque
from typing import Optional, List


class Node:
    def __init__(self, value: int):
        self.value: int = value
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None


class BST:
    def __init__(self):
        self.root: Optional[Node] = None

    # ── Insert ────────────────────────────────────────────────────────────
    def insert(self, value: int) -> None:
        self.root = self._insert(self.root, value)

    def _insert(self, node: Optional[Node], value: int) -> Node:
        if node is None:
            return Node(value)
        if value < node.value:
            node.left = self._insert(node.left, value)
        elif value > node.value:
            node.right = self._insert(node.right, value)
        # duplicate values are silently ignored
        return node

    # ── Search ────────────────────────────────────────────────────────────
    def search(self, value: int) -> bool:
        return self._search(self.root, value)

    def _search(self, node: Optional[Node], value: int) -> bool:
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

    # ── Delete ────────────────────────────────────────────────────────────
    def delete(self, value: int) -> None:
        self.root = self._delete(self.root, value)

    def _delete(self, node: Optional[Node], value: int) -> Optional[Node]:
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Node found — handle three cases
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Two children: replace with inorder successor (min of right subtree)
            successor = self._min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def _min_node(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ── Height ────────────────────────────────────────────────────────────
    def height(self) -> int:
        return self._height(self.root)

    def _height(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    # ── Count ─────────────────────────────────────────────────────────────
    def count(self) -> int:
        return self._count(self.root)

    def _count(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return 1 + self._count(node.left) + self._count(node.right)

    # ── Traversals ────────────────────────────────────────────────────────
    def inorder(self) -> List[int]:
        result: List[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Optional[Node], result: List[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)

    def preorder(self) -> List[int]:
        result: List[int] = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: Optional[Node], result: List[int]) -> None:
        if node is None:
            return
        result.append(node.value)
        self._preorder(node.left, result)
        self._preorder(node.right, result)

    def postorder(self) -> List[int]:
        result: List[int] = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: Optional[Node], result: List[int]) -> None:
        if node is None:
            return
        self._postorder(node.left, result)
        self._postorder(node.right, result)
        result.append(node.value)

    def level_order(self) -> List[List[int]]:
        if self.root is None:
            return []
        result: List[List[int]] = []
        queue: deque = deque([self.root])
        while queue:
            level_size = len(queue)
            level: List[int] = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


# ── Demo ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    tree = BST()
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

    print("=== Binary Search Tree — Python ===\n")
    print(f"Inserting: {values}")
    for v in values:
        tree.insert(v)

    print(f"\nInorder    (sorted): {tree.inorder()}")
    print(f"Preorder   (root first): {tree.preorder()}")
    print(f"Postorder  (root last): {tree.postorder()}")
    print(f"Level-order (BFS): {tree.level_order()}")

    print(f"\nHeight:     {tree.height()}")
    print(f"Node count: {tree.count()}")

    print(f"\nSearch 40:  {tree.search(40)}")
    print(f"Search 99:  {tree.search(99)}")

    print("\nDeleting 30 (two children)...")
    tree.delete(30)
    print(f"Inorder: {tree.inorder()}")

    print("Deleting 80 (leaf)...")
    tree.delete(80)
    print(f"Inorder: {tree.inorder()}")

    print(f"\nFinal node count: {tree.count()}")
