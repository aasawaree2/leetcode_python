class Solution:
    # O(N^2) Solution
    def lengthOfLongestSubstring(self, s):
        max_len = 0
        for i in range(len(s)):
            temp = []
            for j in range(i, len(s)):
                if s[j] not in temp:
                    temp.append(s[j])
                    max_len = max(max_len, len(temp))
                else:
                    break
        return max_len

    # O(N) Solution
    def lengthOfLongestSubstring1(self, s):
        cache = {}
        max_len = 0
        next_start_index = 0
        for i in range(len(s)):
            if s[i] in cache:
                next_start_index = max(next_start_index, cache[s[i]])
            max_len = max(max_len, i - next_start_index + 1)
            cache[s[i]] = i + 1
        return max_len


def main():
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabac"))
    print(s.lengthOfLongestSubstring1("abcabac"))


if __name__ == '__main__':
    main()
