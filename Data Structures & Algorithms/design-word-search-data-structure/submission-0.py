class WordDictionary:
    def __init__(self):
        self.words = []          # 存所有单词

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        for w in self.words:
            if self._match(w, word):
                return True
        return False
    
    # 辅助函数：判断一个单词是否匹配带 '.' 的模式
    def _match(self, w: str, pattern: str) -> bool:
        if len(w) != len(pattern):
            return False
        for i in range(len(w)):
            if pattern[i] != '.' and w[i] != pattern[i]:
                return False
        return True