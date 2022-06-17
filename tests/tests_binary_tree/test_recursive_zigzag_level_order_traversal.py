import pytest

from solutions import (
    RecursiveZigzagLevelOrderTraversal,
    TreeNode,
)


@pytest.fixture
def solution():
    return RecursiveZigzagLevelOrderTraversal()


@pytest.fixture
def tree_one():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root


@pytest.fixture
def tree_two():
    return TreeNode(None)


@pytest.fixture
def tree_three():
    return TreeNode(1)


@pytest.fixture
def tree_four():
    values = [1] * 2001

    def build_binary_tree(i):
        if i < len(values):
            return TreeNode(
                values[i],
                left=build_binary_tree((i + 1) * 2 - 1),
                right=build_binary_tree((i + 1) * 2),
            )

    return build_binary_tree(0)


def test_zigzag_level_order_traversal_tree_one(solution, tree_one):
    ref = [[3], [20, 9], [15, 7]]
    assert ref == solution.zigzag_level_order(tree_one)


def test_zigzag_level_order_traversal_tree_two(solution, tree_two):
    ref = [[None]]
    assert ref == solution.zigzag_level_order(tree_two)


def test_zigzag_level_order_traversal_tree_three(solution, tree_three):
    ref = [[1]]
    assert ref == solution.zigzag_level_order(tree_three)


def test_constraints(solution, tree_four):
    with pytest.raises(AssertionError):
        root = TreeNode(101)
        solution.zigzag_level_order(root)

    with pytest.raises(AssertionError):
        solution.zigzag_level_order(tree_four)
