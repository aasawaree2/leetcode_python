class Solution:
    # O(N) Solution
    def myAtoi(self, s):
        sign = 1
        sign_check = False
        res = ''
        for ch in s:
            if ch == ' ' and sign_check is False:
                continue
            if ch == '-' and sign_check is False:
                sign = -1
                sign_check = True
                continue
            if ch == '+' and sign_check is False:
                sign_check = True
                continue
            if ch.isnumeric():
                res += ch
                sign_check = True
            else:
                break

        res = sign * int(res) if res else 0
        if res < -2 ** 31:
            return -2 ** 31
        elif res >= 2 ** 31:
            return 2 ** 31 - 1
        else:
            return res


def main():
    s = Solution()
    print(s.myAtoi("-33 83 ud "))


if __name__ == '__main__':
    main()
