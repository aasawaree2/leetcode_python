class Solutions:
    def productExceptSelf(self, nums):

        res = [1] * len(nums)

        product = 1
        for i in range(len(nums)):
            res[i] *= product
            product *= nums[i]

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= product
            product *= nums[i]

        return res

    def productExceptSelf2(self, nums):
        product = 1
        count_zero = 0
        for i in nums:
            if i == 0:
                count_zero += 1
            else:
                product = product * i

        for i in range(len(nums)):
            if count_zero > 1:
                nums[i] = 0
            elif count_zero == 1:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            else:
                nums[i] = product // nums[i]

        return nums


def main():
    s = Solutions()
    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf2([1,2,3,4]))


if __name__ == '__main__':
    main()
