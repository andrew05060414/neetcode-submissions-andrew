class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            length = len(s)
            code += f"{length}#{s}"
        # print(code)
        return code
            

    def decode(self, s: str) -> List[str]:
        strs = []
        index = 0

        while index < len(s):
            # 1. 读长度
            num_s = ""
            while s[index] != '#': # find the entire number
                num_s = num_s + s[index] # add current number char to the num string
                index += 1
            count = int(num_s)
            # 2. 跳过 '#'
            index += 1
            # 3. 读字符串
            strs.append(s[index:index+count])
            index+=count
            # 4. 放进 result

        return strs

