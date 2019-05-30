import collections


class Solutions:
    def firstUniqChar(self, s: str) -> int:
        unique_chars = {}
        seen_values = set()
        for index, char in enumerate(s):
            if char not in seen_values:
                seen_values.add(char)
                unique_chars[char] = index
            elif char in unique_chars:
                del unique_chars[char]
        return min(unique_chars.values()) if unique_chars else -1

    def firstUniqChar1(self, s: str) -> int:

        chars = [0] * 26
        for ch in s:
            chars[ord(ch) - ord('a')] += 1
        for i, ch in enumerate(s):
            if chars[ord(ch) - ord('a')] == 1:
                return i
        return -1

    def firstUniqChar2(self, s: str) -> int:

        count = collections.Counter(s)
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1


def main():
    s = Solutions()
    a = s.firstUniqChar("leetcode")
    print(a)
    a = s.firstUniqChar1("leetcode")
    print(a)
    a = s.firstUniqChar1("leetcode")
    print(a)


if __name__ == '__main__':
    main()
