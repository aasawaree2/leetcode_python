class Solution:
    def removeDuplicates(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) <= 1:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1


def main():
    s = Solution()
    print(s.removeDuplicates([1, 1, 2]))


if __name__ == '__main__':
    main()
