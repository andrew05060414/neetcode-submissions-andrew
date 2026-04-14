class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            # for each str 生成 key
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            # 如果 key 不在 groups 里，先建一个空列表
            if key not in groups:
                groups[key] = []
            # 把 s 放进去
            groups[key].append(s)
            
        return list(groups.values())