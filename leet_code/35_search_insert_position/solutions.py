"""
Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:
Input: [1, 3, 5, 6], 5
Output: 2

Example 2:
Input: [1, 3, 5, 6], 2
Output: 1

Example 3:
Input: [1, 3, 5, 6], 7
Output: 4

Example 4:
Input: [1, 3, 5, 6], 0
Output: 0
"""


class Solutions:
    def searchInsert_solution1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums) - 1):
            if target <= nums[i]:
                return i
        return len(nums)

    def searchInsert_solution2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        pass

def main():
    s = Solutions()

    output = s.searchInsert_solution1([1, 3, 5, 6], 1)
    print('Solution 1 - ', output)
    output = s.searchInsert_solution2([1, 3, 5, 6], 5)
    print('Solution 2 - ', output)

    output = s.searchInsert_solution1([1, 3, 5, 6], 2)
    print('Solution 1 - ', output)
    output = s.searchInsert_solution2([1, 3, 5, 6], 2)
    print('Solution 2 - ', output)

    output = s.searchInsert_solution1([1, 3, 5, 6], 7)
    print('Solution 1 - ', output)
    output = s.searchInsert_solution2([1, 3, 5, 6], 7)
    print('Solution 2 - ', output)

    output = s.searchInsert_solution1([1, 3, 5, 6], 0)
    print('Solution 1 - ', output)
    output = s.searchInsert_solution2([1, 3, 5, 6], 0)
    print('Solution 2 - ', output)


if __name__ == '__main__':
    main()