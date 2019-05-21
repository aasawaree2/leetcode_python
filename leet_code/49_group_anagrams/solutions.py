import collections


class Solutions:
    def groupAnagrams(self, strs):
        # O(NK log K) where,
        # N is length of strs
        # K is length of max string in strs
        # Space Complexity - O(NK)
        dic = collections.defaultdict(list)
        for c in strs:
            dic["".join(sorted(c))].append(c)
        return list(dic.values())

        # O(NK) where,
        # N is length of strs
        # K is length of max string in strs
        # Space Complexity - O(NK)
        dic = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            dic[tuple(count)].append(s)
        return dic.values()


def main():
    s = Solutions()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    main()
