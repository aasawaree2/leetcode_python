class Solutions:
    def missingNumber(self, nums):

        for i, num in enumerate(sorted(nums)):
            if i != num:
                return i

    def missingNumber2(self, nums):
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def missingNumber3(self, nums):

        num_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in num_set:
                return number


def main():
    s = Solutions()


if __name__ == '__main__':
    main()
