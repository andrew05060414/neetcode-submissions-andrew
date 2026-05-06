"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        if not node:
            return None
        from collections import deque

        # Create an empty queue
        worklist = deque()
        old_to_new[node] = Node(node.val)
        worklist.append(node)
        while worklist:
            curr = worklist.popleft()
            # go over neighbors of this node
            for nei in curr.neighbors: 
                # found new node (not in dict)
                if nei not in old_to_new:
                    # copy and add to dict
                    worklist.append(nei)
                    old_to_new[nei] = Node(nei.val)
                #update the neighbors of the curr node
                old_to_new[curr].neighbors.append(old_to_new[nei])

        return old_to_new[node]
