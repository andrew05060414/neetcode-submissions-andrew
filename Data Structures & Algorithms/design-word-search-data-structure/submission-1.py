class TrieNode:
    def __init__(self):
        self.children = {}   # 字母 → 子节点
        self.isEnd = False   # 标记是否为完整单词的结尾


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        # 递归回溯
        def dfs(node: TrieNode, index: int) -> bool:
            # 已经走完整个 pattern，检查是否是一个完整单词
            if index == len(word):
                return node.isEnd

            ch = word[index]
            if ch == '.':
                # 通配符：尝试所有子节点，只要有一条路走通就返回 True
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                # 普通字母：必须找到对应子节点，否则失败
                if ch not in node.children:
                    return False
                return dfs(node.children[ch], index + 1)

        return dfs(self.root, 0)