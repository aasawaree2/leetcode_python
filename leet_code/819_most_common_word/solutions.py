import collections
import re


class Solutions:
    def mostCommonWord(self, paragraph: str, banned):
        banset = set(banned)
        words = re.split(r'[!?\',;. ]', paragraph.lower())
        count = collections.Counter(words)
        ans, best = '', 0
        for word in count:
            if word and count[word] > best and word not in banset:
                ans, best = word, count[word]

        return ans

    def mostCommonWord1(self, paragraph: str, banned):
        words = re.split(r'[!?\',;. ]', paragraph.lower())
        c = collections.Counter(words)
        banned = set(banned)
        for word, count in c.most_common():
            if word and word not in banned:
                return word
        return ''


def main():
    s = Solutions()
    a = s.mostCommonWord("Bob, ball g  g ball g ", "g")
    print(a)


if __name__ == '__main__':
    main()
