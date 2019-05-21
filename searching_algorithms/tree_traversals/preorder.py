from leet_code.helper import TreeNode


class Solutions:
    def preorder_traversal_recursive(self, root, result):
        if root:
            result.append(root.val)
            self.preorder_traversal_recursive(root.left, result)
            self.preorder_traversal_recursive(root.right, result)

    def preorder_traversal_iterative(self, root):
        stack = [root]
        result = []
        while stack:
            curr_node = stack.pop()
            if curr_node:
                result.append(curr_node.val)
                stack.append(curr_node.right)
                stack.append(curr_node.left)
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
    s.preorder_traversal_recursive(t, result)
    print(result)
    s.preorder_traversal_iterative(t)


if __name__ == '__main__':
    main()
