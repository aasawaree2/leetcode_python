class Solution:
    # O(N) Solution
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area = 0

        for i in range(len(height) - 1, 0, -1):
            if height[left] < height[right]:
                area = max(area, height[left] * i)
                left += 1
            else:
                area = max(area, height[right] * i)
                right -= 1
        return area


def main():
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))


if __name__ == '__main__':
    main()
