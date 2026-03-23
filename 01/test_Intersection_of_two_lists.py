from Intersection_of_two_lists import find_intersection_of_two_lists, Node


def test_find_intersection_of_two_lists():
    intersection_node = Node(8)
    intersection_node.next = Node(4)
    intersection_node.next.next = Node(5)

    list_A = Node(4)
    list_A.next = Node(1)
    list_A.next.next = intersection_node

    list_B = Node(5)
    list_B.next = Node(6)
    list_B.next.next = Node(1)
    list_B.next.next.next = intersection_node

    assert find_intersection_of_two_lists(list_A, list_B) is intersection_node


test_find_intersection_of_two_lists()
