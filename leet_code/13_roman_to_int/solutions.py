class Solution:
    def romanToInt(self, s: str) -> int:
        map1 = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        sum1 = 0
        prev = 'I'
        for c in s[::-1]:
            if map1[c] < map1[prev]:
                sum1 -= map1[c]
            else:
                sum1 += map1[c]
            prev = c
        return sum1


def main():
    s = Solution()
    print(s.romanToInt("IV"))


if __name__ == '__main__':
    main()
