class Solutions:
    def factorial_rec(self, number):
        if number == 0:
            return 0
        if number == 1:
            return 1
        else:
            return number * self.factorial_rec(number - 1)

    def factorial(self, number):
        if number == 0:
            return 0
        fact = 1
        while number - 1 > 0:
            fact = fact * number
            number = number - 1
        return fact


def main():
    s = Solutions()
    print(s.factorial_rec(4))
    print(s.factorial(4))


if __name__ == '__main__':
    main()
