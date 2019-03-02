class Solution:
    def reverse(self, x):
        max_int = 2 ** 31 - 1
        result = 0
        if x < 0:
            sign = -1
            x = x * -1
        else:
            sign = 1
        while x >= 10:
            result = result * 10 + x % 10
            x = x // 10
        if result > max_int // 10 or (result > max_int // 10 and x % 10 > 7):
            return 0
        else:
            result = result * 10 + x % 10
        return result * sign

def main():
    s = Solution()
    print(s.reverse(-2147483648))


if __name__ == '__main__':
    main()
