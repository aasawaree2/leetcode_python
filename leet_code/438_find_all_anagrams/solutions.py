from collections import Counter


class Solutions:
    def findAnagrams(self, s, p):
        s_len = len(s)
        p_len = len(p)

        res = []

        if s_len < p_len:
            return res

        counter_p = Counter(p)

        for i in range(0, s_len - p_len+1):
            current_set = s[i:i + p_len]
            if counter_p == Counter(current_set):
                res.append(i)
        return res

    def findAnagram2(self, s,p):
        len_p = len(p)
        if not s or len(s) < len_p:
            return []
        ans = []
        hs, hp = 0, 0
        for i in range(len_p):
            hs += hash(s[i])
            hp += hash(p[i])
        if hs == hp:
            ans.append(0)
        for right in range(len_p, len(s)):
            left = right - len_p
            hs += hash(s[right]) - hash(s[left])
            if hs == hp:
                ans.append(left + 1)
        return ans

def main():
    s = Solutions()
    # print(s.findAnagrams("abab", "ab"))
    print(s.findAnagram2("abab", "ab"))


if __name__ == '__main__':
    main()
