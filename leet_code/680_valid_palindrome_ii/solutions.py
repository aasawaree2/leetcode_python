class Solutions:
    def validPalindrome(self, s):
        last_index = len(s) - 1
        first_index = 0
        while last_index > first_index:
            if s[first_index] == s[last_index]:
                first_index += 1
                last_index -= 1
                continue
            else:
                if s[first_index + 1] == s[last_index]:
                    first_index += 1
                elif s[first_index] == s[last_index - 1]:
                    last_index -= 1
                else:
                    return False
        return True

    def isPalindrome1(s, i, j, deleted):
        while i < j:
            if s[i] != s[j]:
                return not deleted and (isPalindrome(s, i + 1, j, True) or isPalindrome(s, i, j - 1, True))
            i, j = i + 1, j - 1
            return True

    # return isPalindrome1(s, 0, len(s) - 1, False)

def main():
    s = Solutions()
    print(s.validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))


if __name__ == '__main__':
    main()
