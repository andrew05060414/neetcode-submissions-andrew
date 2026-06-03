class TrieNode:
    def __init__(self):
        self.children = {}          # 字符 → 子节点
        self.isEnd = False          # 标记这个节点是否是某个单词的结尾

class PrefixTree:  # 题目里类名是 PrefixTree
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True           # 最后一个字符标记为单词结尾

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.isEnd           # 不仅路径存在，还必须是一个完整单词

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True                 # 路径走通即可，不要求是完整单词