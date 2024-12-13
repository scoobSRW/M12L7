class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def delete(self, key):
        if self.root is None:
            print("Error: Tree is empty. Cannot delete.")
        else:
            self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            print(f"Error: Key {key} not found in the tree.")
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp = self._find_min_key(root.right)
            root.key = temp.key
            root.right = self._delete_recursive(root.right, temp.key)
        return root

    def _find_min_key(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, key):
        if self.root is None:
            print("Error: Tree is empty. Cannot search.")
            return False
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def in_order_traversal(self):
        if self.root is None:
            print("Error: Tree is empty. No traversal possible.")
        else:
            self._in_order_traversal_recursive(self.root)
            print()

    def _in_order_traversal_recursive(self, node):
        if node:
            self._in_order_traversal_recursive(node.left)
            print(node.key, end=" ")
            self._in_order_traversal_recursive(node.right)

    def in_order_traversal_iterative(self):
        if self.root is None:
            print("Error: Tree is empty. No traversal possible.")
            return
        stack = []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.key, end=" ")
            current = current.right
        print()

    def pre_order_traversal(self):
        if self.root is None:
            print("Error: Tree is empty. No traversal possible.")
        else:
            self._pre_order_traversal_recursive(self.root)
            print()

    def _pre_order_traversal_recursive(self, node):
        if node:
            print(node.key, end=" ")
            self._pre_order_traversal_recursive(node.left)
            self._pre_order_traversal_recursive(node.right)

    def pre_order_traversal_iterative(self):
        if self.root is None:
            print("Error: Tree is empty. No traversal possible.")
            return
        stack = [self.root]
        while stack:
            node = stack.pop()
            print(node.key, end=" ")
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        print()

    def post_order_traversal(self):
        if self.root is None:
            print("Error: Tree is empty. No traversal possible.")
        else:
            self._post_order_traversal_recursive(self.root)
            print()

    def _post_order_traversal_recursive(self, node):
        if node:
            self._post_order_traversal_recursive(node.left)
            self._post_order_traversal_recursive(node.right)
            print(node.key, end=" ")

    def post_order_traversal_iterative(self):
        if self.root is None:
            print("Error: Tree is empty. No traversal possible.")
            return
        stack1 = [self.root]
        stack2 = []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            print(stack2.pop().key, end=" ")
        print()

    def print_tree(self):
        self._print_tree_recursive(self.root, 0)

    def _print_tree_recursive(self, node, depth):
        if node is None:
            return
        self._print_tree_recursive(node.right, depth + 1)
        print("    " * depth + str(node.key))
        self._print_tree_recursive(node.left, depth + 1)

if __name__ == "__main__":
    tree = BinaryTree()

    # Insert keys
    keys = [50, 30, 70, 20, 40, 60, 80]
    for key in keys:
        tree.insert(key)

    # Traversals
    print("In-order traversal (recursive):")
    tree.in_order_traversal()

    print("In-order traversal (iterative):")
    tree.in_order_traversal_iterative()

    print("Pre-order traversal (recursive):")
    tree.pre_order_traversal()

    print("Pre-order traversal (iterative):")
    tree.pre_order_traversal_iterative()

    print("Post-order traversal (recursive):")
    tree.post_order_traversal()

    print("Post-order traversal (iterative):")
    tree.post_order_traversal_iterative()

    print("Binary tree structure:")
    tree.print_tree()

    # Search for a key
    search_key = 40
    if tree.search(search_key):
        print(f"Key {search_key} found in the tree.")
    else:
        print(f"Key {search_key} not found in the tree.")

    # Delete a key
    delete_key = 30
    tree.delete(delete_key)
    print(f"Deleted key: {delete_key}")

    # In-order traversal after deletion
    print("In-order traversal after deletion:")
    tree.in_order_traversal()
