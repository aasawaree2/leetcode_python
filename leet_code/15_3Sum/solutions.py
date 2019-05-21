class Solution:

    # O(N) Solution
    def threeSum(self, nums):
        result = []
        n = len(nums)
        nums.sort()
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            adjacent = i + 1
            right = n - 1

            while adjacent < right:
                total = nums[i] + nums[adjacent] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    adjacent += 1
                else:
                    result.append([nums[i], nums[adjacent], nums[right]])
                    while adjacent < right and nums[adjacent] == nums[adjacent + 1]:
                        adjacent += 1
                    while adjacent < right and nums[right] == nums[right - 1]:
                        right -= 1
                    adjacent += 1
                    right -= 1
        return result


def main():
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))


if __name__ == '__main__':
    main()
