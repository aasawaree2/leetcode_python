class Solutions:
    def isPalindrome(self, s):
        last_index = len(s) - 1
        first_index = 0
        while last_index > first_index:
            while not s[last_index].isalpha():
                last_index -= 1
            while not s[first_index].isalpha():
                first_index += 1
            if not (s[last_index].upper() == s[first_index].upper()):
                return False
            last_index -= 1
            first_index += 1

        return True


def main():
    s = Solutions()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))


if __name__ == '__main__':
    main()
