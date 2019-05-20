class Solutions:
    def isAlienSorted(self, words, order):
        order_rank = {c: i for i, c in enumerate(order)}

        for x in range(len(words) - 1):
            word1 = words[x]
            word2 = words[x + 1]

            for y in range(min(len(word1), len(word2))):
                if word1[y] != word2[y]:
                    if order_rank[word1[y]] > order_rank[word2[y]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True


def main():
    s = Solutions()
    print(s.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))


if __name__ == '__main__':
    main()
