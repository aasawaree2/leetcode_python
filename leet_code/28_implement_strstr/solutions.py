class Solutions:
    # def strStr(self, haystack: str, needle: str) -> int:
    #     if needle in haystack:
    #         return haystack.index(needle)
    #     return -1

    # KMP algorithm
    def strStr(self, haystack, needle):
        len_haystack = len(haystack)
        len_needle = len(needle)

        if haystack == needle or not needle:
            return 0

        if not haystack:
            return -1

        # create prefix_lst[] that will hold the longest prefix suffix
        # values for pattern
        i = 0  # index for haystack[]
        j = 0  # index for needle[]
        prefix_lst = [0] * len_needle

        # Preprocess the pattern (calculate lps[] array)
        self.computeLPSArray(needle, len_needle, prefix_lst)

        while i < len_haystack:
            if needle[j] == haystack[i]:
                i += 1
                j += 1

            if j == len_needle:
                return i - j
                # For multiple indexes uncomment this
                # print("Found pattern at index " + str(i - j))
                # j = prefix_lst[j - 1]

                # mismatch after j matches
            elif i < len_haystack and needle[j] != haystack[i]:
                # Do not match lps[0..lps[j-1]] characters,
                # they will match anyway
                if j != 0:
                    j = prefix_lst[j - 1]
                else:
                    i += 1
        return -1

    def computeLPSArray(self, needle, len_needle, prefix_lst):
        i = 1
        len_prefix_suffix = 0  # length of the previous longest prefix suffix

        prefix_lst[0] = 0  # lps[0] is always 0

        # the loop calculates lps[i] for i = 1 to M-1
        while i < len_needle:
            if needle[i] == needle[len_prefix_suffix]:
                len_prefix_suffix += 1
                prefix_lst[i] = len_prefix_suffix
                i += 1
            else:
                # This is tricky. Consider the example.
                # AAACAAAA and i = 7. The idea is similar
                # to search step.
                if len_prefix_suffix != 0:
                    len_prefix_suffix = prefix_lst[len_prefix_suffix - 1]

                    # Also, note that we do not increment i here
                else:
                    prefix_lst[i] = 0
                    i += 1


def main():
    s = Solutions()
    txt = "hello"
    pat = "ll"
    print(s.strStr(txt, pat))


if __name__ == '__main__':
    main()