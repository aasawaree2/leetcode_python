class Solutions:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        if len(nums) <= 1:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


def main():
    s = Solutions()
    nums = [1, 1, 2]
    a = s.removeDuplicates(nums)
    print(nums[:a])


if __name__ == '__main__':
    main()
