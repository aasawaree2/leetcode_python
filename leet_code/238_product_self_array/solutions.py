class Solutions:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

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

def main():
    s = Solutions()


if __name__ == '__main__':
    main()