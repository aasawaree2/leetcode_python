class Solutions:

    def addBinary2(self, a, b):
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a, b):
        a = int(a)
        b = int(b)
        c = ""
        carry_forward = 0

        if not a and not b:
            return "0"
        while a or b:
            if a:
                carry_forward += a % 10
                a = a // 10
            if b:
                carry_forward += b % 10
                b = b // 10
            c = str(carry_forward % 2) + c
            carry_forward = carry_forward // 2

        if carry_forward:
            c = "1" + c

        return c


def main():
    s = Solutions()
    print(s.addBinary("111", "111"))
    print(s.addBinary2("111", "111"))


if __name__ == '__main__':
    main()
