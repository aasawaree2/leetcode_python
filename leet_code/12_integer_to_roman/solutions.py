class Solutions:
    # O(N) Solution
    def intToRoman(self, num: int) -> str:
        dividend, key = 0, 0
        dic = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC",
               100: "C", 400: "CD", 500: "D",
               900: "CM", 1000: "M"}

        res = ""
        keys = sorted(dic.keys(), reverse=True)
        while num != 0:
            for key in keys:
                if num // key >= 1:
                    dividend = num // key
                    num = num % key
                    break
            res += dividend * dic[key]
        return res


def main():
    s = Solutions()
    print(s.intToRoman(1))


if __name__ == '__main__':
    main()