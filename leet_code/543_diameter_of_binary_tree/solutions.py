class TreeNode:
    def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


class Solutions:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root):
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        depth(root)

        return self.diameter


def main():
    s = Solutions()
    s.diameterOfBinaryTree()


if __name__ == '__main__':
    main()