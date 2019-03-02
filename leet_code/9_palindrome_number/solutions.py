class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        if (x % 10 == 0 and x != 0) or x < 0:
            return False
        while x > result:
            result = result * 10 + x % 10
            x = x // 10
        return x == result or x == result // 10


def main():
    s = Solution()
    print(s.isPalindrome(12321))
    print(s.isPalindrome(1231))


if __name__ == '__main__':
    main()
