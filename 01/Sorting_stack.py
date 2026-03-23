def sort_stack(stack: list) -> list:
    if not stack:
        return []
    temp_stack = []

    while stack:
        temp_value = stack.pop()

        while temp_stack and temp_stack[-1] > temp_value:
            stack.append(temp_stack.pop())

        temp_stack.append(temp_value)

    while temp_stack:
        stack.append(temp_stack.pop())

    return stack
