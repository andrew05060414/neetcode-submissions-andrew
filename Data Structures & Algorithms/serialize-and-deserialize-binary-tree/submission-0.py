# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append('null')
                return
            else:
                res.append(str(node.val))
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            # 1. 读当前 vals[self.i]
            temp = vals[self.i]
            # 2. 如果是 "null"
            #    self.i 往后走一步
            #    return None
            if temp == 'null':
                self.i += 1
                return None
            # 3. 如果不是 null
            #    创建 TreeNode
            else:
                node = TreeNode(int(temp))
            # 4. self.i 往后走一步
                self.i += 1
            # 5. node.left = dfs()
                node.left = dfs()
            # 6. node.right = dfs()
                node.right = dfs()
            # 7. return node
            return node
        return dfs()
