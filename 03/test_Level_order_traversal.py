from Level_order_traversal import pass_tree_by_level_order, build_tree


def test_pass_tree_by_level_order() -> None:
    tree = build_tree([9, 16, 8, None, None, 6, 11])
    assert pass_tree_by_level_order(tree) == [[9], [16, 8], [6, 11]]

    tree = build_tree([9, None, None, None, None])
    assert pass_tree_by_level_order(tree) == [[9]]

    tree = build_tree([])
    assert pass_tree_by_level_order(tree) == []
