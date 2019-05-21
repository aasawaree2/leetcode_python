class Solution:
    # O(N) Solution
    def romanToInt(self, s: str) -> int:
        map1 = {'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
        sum1 = 0
        for i in range(len(s) - 1):
            if map1[s[i]] < map1[s[i + 1]]:
                sum1 -= map1[s[i]]
            else:
                sum1 += map1[s[i]]
        return sum1 + map1[s[len(s) - 1]]


def main():
    s = Solution()
    print(s.romanToInt("IV"))


if __name__ == '__main__':
    main()
