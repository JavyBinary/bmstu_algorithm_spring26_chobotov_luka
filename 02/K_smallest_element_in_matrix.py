def find_K_smallest_element_in_matrix(matrix: list[list[int]], k: int) -> int:
    if not matrix or not matrix[0]:
        return -1

    left = matrix[0][0]
    right = matrix[len(matrix) - 1][len(matrix) - 1]

    while left < right:
        mid = (left + right) // 2

        if count_elements_less_mid(matrix, mid) < k:
            left = mid + 1
        else:
            right = mid

    return left


def count_elements_less_mid(matrix: list[list[int]], value: int) -> int:
    if not matrix or not matrix[0]:
        return 0

    count = 0
    row = len(matrix) - 1
    column = 0

    while row >= 0 and column < len(matrix):
        if matrix[row][column] <= value:
            count += row + 1
            column += 1
        else:
            row -= 1
    return count
