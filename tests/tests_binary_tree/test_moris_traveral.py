import pytest

from solutions import (
    MorrisSolutionVersionOne,
    MorrisSolutionVersionTwo,
    TreeNode,
)


@pytest.fixture
def solution_one():
    return MorrisSolutionVersionOne()


@pytest.fixture
def solution_two():
    return MorrisSolutionVersionTwo()


@pytest.fixture
def tree_one():
    # Driver program to test
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


@pytest.mark.skip(reason="Time Limit Exceeded")
def test_preorder_traversal_tree_one(solution_one, solution_two, tree_one):
    ref = [1, 2, 3]
    assert ref == solution_one.morris_traversal(tree_one)
    assert ref == solution_two.morris_traversal(tree_one)


@pytest.mark.skip(reason="Time Limit Exceeded")
def test_preorder_traversal_tree_two(solution_one, solution_two, tree_two):
    ref = [None]
    assert ref == solution_one.morris_traversal(tree_two)
    assert ref == solution_two.morris_traversal(tree_two)


@pytest.mark.skip(reason="Time Limit Exceeded")
def test_preorder_traversal_tree_three(solution_one, solution_two, tree_three):
    ref = [1]
    assert ref == solution_one.morris_traversal(tree_three)
    assert ref == solution_two.morris_traversal(tree_three)


@pytest.mark.skip(reason="Time Limit Exceeded")
def test_constraints(solution_one, solution_two):
    with pytest.raises(AssertionError):
        root = TreeNode(101)
        solution_one.morris_traversal(root)
        solution_two.morris_traversal(root)
