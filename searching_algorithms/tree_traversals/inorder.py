from leet_code.helper import TreeNode


class Solutions:
    def inorder_traversal_recursive(self, root, result):
        if root:
            self.inorder_traversal_recursive(root.left, result)
            result.append(root.val)
            self.inorder_traversal_recursive(root.right, result)

    def inorder_traversal_iterative(self, root):
        result = []
        stack = []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            curr_node = stack.pop()
            result.append(curr_node.val)
            if curr_node.right:
                curr_node = curr_node.right
                while curr_node:
                    stack.append(curr_node)
                    curr_node = curr_node.left
        print(result)

    def inorder_traversal_iterative2(self, root):
        result = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right

        print(result)


def main():
    t = TreeNode(9)
    t.left = TreeNode(8)
    t.left.left = TreeNode(6)
    t.left.left.left = TreeNode(2)
    t.left.left.left.right = TreeNode(5)
    t.left.left.left.right.left = TreeNode(3)
    t.left.left.left.right.left.right = TreeNode(4)
    t.right = TreeNode(12)
    t.right.left = TreeNode(10)
    t.right.left.right = TreeNode(11)
    s = Solutions()
    result = []
    s.inorder_traversal_recursive(t, result)
    print(result)
    s.inorder_traversal_iterative(t)
    s.inorder_traversal_iterative2(t)


if __name__ == '__main__':
    main()
