class Node:
    def __init__(self, x: float):
        self.value = x
        self.next = None


def find_intersection_of_two_lists(head_A: Node, head_B: Node) -> Node:
    if not head_A or not head_B:
        return None

    current_node_A = head_A
    current_node_B = head_B

    while current_node_A is not current_node_B:
        if not current_node_A:
            current_node_A = head_B
        else:
            current_node_A = current_node_A.next

        if not current_node_B:
            current_node_B = head_A
        else:
            current_node_B = current_node_B.next

    return current_node_A
