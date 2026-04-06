def find_longest_unique_substring(string: str) -> int:
    if not string:
        return 0

    last_seen_symbol_indices = {}
    length = 0
    left = 0
    for right in range(len(string)):
        current_symbol = string[right]

        if (
            current_symbol in last_seen_symbol_indices
            and last_seen_symbol_indices[current_symbol] >= left
        ):
            left = last_seen_symbol_indices[current_symbol] + 1
        last_seen_symbol_indices[current_symbol] = right

        length = max(length, right - left + 1)

    return length
