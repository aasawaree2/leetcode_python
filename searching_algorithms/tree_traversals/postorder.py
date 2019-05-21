from leet_code.helper import TreeNode


class Solutions:
    def postorder_traversal_recursive(self, root, result):
        if root:
            self.postorder_traversal_recursive(root.left, result)
            self.postorder_traversal_recursive(root.right, result)
            result.append(root.val)

    def postorder_traversal_iterative(self, root):
        stack = [root]
        output = []
        while stack:
            curr_node = stack.pop()
            if curr_node:
                output.append(curr_node.val)
                stack.append(curr_node.left)
                stack.append(curr_node.right)

        print(output[::-1])


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
    s.postorder_traversal_recursive(t, result)
    print(result)
    s.postorder_traversal_iterative(t)


if __name__ == '__main__':
    main()
