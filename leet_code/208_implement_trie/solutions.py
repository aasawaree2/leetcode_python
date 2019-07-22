import collections


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        for letter in word:
            current = current.children.get(letter)
            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return False
        return True

    def prefix(self, prefix):
        result = []
        current = self.root
        for letter in prefix:
            current = current.children.get(letter)
            if current is None:
                return []

        stack = [(current, prefix)]

        while stack:
            temp, path = stack.pop()
            if temp.is_word:
                result.append(path)
            for ch in temp.children:
                stack.append((temp.children.get(ch), path+ch))
        return result


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("cat")
obj.insert("cater")
obj.insert("catering")
obj.insert("cats")

obj.insert("dog")
a = obj.prefix("ca")
print(a)
param_2 = obj.search("cat")
param_3 = obj.startsWith("cat")
