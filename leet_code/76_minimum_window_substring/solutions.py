import collections


class Solutions:
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = 0
        start_index = 0
        end_index = 0
        for j, c in enumerate(s,1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not end_index or j - i <= end_index - start_index:
                    start_index, end_index = i, j
        return s[start_index:end_index]


def main():
    s = Solutions()
    print(s.minWindow("ADOBECODEBANC", "ABC"))


if __name__ == '__main__':
    main()



