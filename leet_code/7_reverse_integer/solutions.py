class Solution:
    def twoSum1(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        # O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum2(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        # Optimized Solution O(n)
        lookup_dict = {}
        if (len(nums)) <= 2:
            return [0, 1]
        for i in range(len(nums)):
            if nums[i] in lookup_dict:
                return [lookup_dict[nums[i]], i]
            lookup_dict[target - nums[i]] = i


def main():
    s = Solution()
    if [1, 3] == s.twoSum1([0, 2, 5, 7, 11], 9):
        print("Success")
    else:
        print("Failure")

    if [1, 3] == s.twoSum2([0, 2, 5, 7, 11], 9):
        print("Success")
    else:
        print("Failure")


if __name__ == '__main__':
    main()
