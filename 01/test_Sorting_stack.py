from Sorting_stack import sort_stack


def test_sort_stack():
    assert sort_stack([2, 3, 1, 4]) == [4, 3, 2, 1]
    assert sort_stack([]) == []
    assert sort_stack([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert sort_stack([4, 3, 2, 1]) == [4, 3, 2, 1]
    assert sort_stack([1, 1, 2, 3, 4]) == [4, 3, 2, 1, 1]


test_sort_stack()
