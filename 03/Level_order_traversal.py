class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def build_tree(arr: list) -> TreeNode:
    if not arr or arr[0] is None:
        return None

    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while i < len(arr) and queue:
        node = queue.pop(0)

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root


def pass_tree_by_level_order(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_size = len(queue)
        current_level_values = []

        for _ in range(level_size):
            current_node = queue.pop(0)
            current_level_values.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        result.append(current_level_values)
    return result
