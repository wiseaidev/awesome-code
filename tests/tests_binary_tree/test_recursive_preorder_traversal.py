import pytest

from solutions import (
    RecursiveBinaryTreeSolution,
    TreeNode,
)


@pytest.fixture
def solution():
    return RecursiveBinaryTreeSolution()


@pytest.fixture
def tree_one():
    root = TreeNode(1)
    root.right = TreeNode(2)

    root.right.left = TreeNode(3)

    return root


@pytest.fixture
def tree_two():
    return TreeNode(None)


@pytest.fixture
def tree_three():
    return TreeNode(1)


@pytest.fixture
def tree_four():
    values = [1] * 101

    def build_binary_tree(i):
        if i < len(values):
            return TreeNode(
                values[i],
                left=build_binary_tree((i + 1) * 2 - 1),
                right=build_binary_tree((i + 1) * 2),
            )

    return build_binary_tree(0)


def test_preorder_traversal_tree_one(solution, tree_one):
    ref = [1, 2, 3]
    assert ref == solution.preorder_traversal(tree_one)


def test_preorder_traversal_tree_two(solution, tree_two):
    ref = [None]
    assert ref == solution.preorder_traversal(tree_two)


def test_preorder_traversal_tree_three(solution, tree_three):
    ref = [1]
    assert ref == solution.preorder_traversal(tree_three)


def test_constraints(solution, tree_four):
    with pytest.raises(AssertionError):
        root = TreeNode(101)
        solution.preorder_traversal(root)

    with pytest.raises(AssertionError):
        solution.preorder_traversal(tree_four)
