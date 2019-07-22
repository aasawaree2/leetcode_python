class Solutions:
    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                right_idx = i
                break
        return [left_idx, right_idx]

    def searchRange2(self, nums, target):
        start, end = 0, len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        left = end

        if not nums or nums[left] != target:
            return [-1, -1]

        start, end = 0, len(nums) - 1
        while start < end:
            mid = (start + end + 1) // 2
            if nums[mid] > target:
                end = mid - 1
            else:
                start = mid
        right = start
        return [left, right]


def main():
    s = Solutions()
    a = s.searchRange2([5,7,7,8,8,10], 8)
    print(a)
    a = s.searchRange2([1,1], 1)
    print(a)

    a = s.searchRange2([1,1,1], 1)
    print(a)
    a = s.searchRange2([5,7,7,8,8,10], 9)
    print(a)
    a = s.searchRange2([1, 1], 3)
    print(a)


if __name__ == '__main__':
    main()