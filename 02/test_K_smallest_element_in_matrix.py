from K_smallest_element_in_matrix import find_K_smallest_element_in_matrix


def test_find_K_smallest_element_in_matrix() -> None:
    matrix = [[1, 5, 9, 11], [2, 6, 10, 12], [3, 7, 13, 14], [4, 8, 15, 16]]
    assert find_K_smallest_element_in_matrix(matrix, 1) == 1
    assert find_K_smallest_element_in_matrix(matrix, 7) == 7
    assert find_K_smallest_element_in_matrix(matrix, 12) == 12
    assert find_K_smallest_element_in_matrix(matrix, 16) == 16
    assert find_K_smallest_element_in_matrix([[-5]], 1) == -5

    matrix = [[1, 10, 22, 34], [3, 13, 25, 37], [5, 16, 28, 40], [7, 19, 31, 43]]
    assert find_K_smallest_element_in_matrix(matrix, 5) == 10
    assert find_K_smallest_element_in_matrix(matrix, 16) == 43
    assert find_K_smallest_element_in_matrix([[]], 5) == -1
    assert find_K_smallest_element_in_matrix([], 5) == -1
