import pytest

from solutions import (
    AverageOfLevelsOrderTraversalSolution,
    TreeNode,
)


@pytest.fixture
def solution():
    return AverageOfLevelsOrderTraversalSolution()


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
    values = [1] * 105

    def build_binary_tree(i):
        if i < len(values):
            return TreeNode(
                values[i],
                left=build_binary_tree((i + 1) * 2 - 1),
                right=build_binary_tree((i + 1) * 2),
            )

    return build_binary_tree(0)


def test_average_of_levels_tree_one(solution, tree_one):
    ref = [3.00000, 14.50000, 11.00000]
    assert ref == solution.average_of_levels(tree_one)


def test_constraints(solution, tree_two):
    with pytest.raises(AssertionError):
        root = TreeNode(2**31)
        solution.average_of_levels(root)

    with pytest.raises(AssertionError):
        solution.average_of_levels(tree_two)
