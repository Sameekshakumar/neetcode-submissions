# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        if root is None:
            return "N"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + "," + left + "," + right

    def deserialize(self, data):
        vals = iter(data.split(","))  # iterator remembers position automatically
    
        def helper():
            val = next(vals)  # get next value, automatically advances
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
    
        return helper()