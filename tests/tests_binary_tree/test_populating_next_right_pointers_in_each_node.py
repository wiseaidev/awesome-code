import pytest

from solutions import (
    Node,
    PopulatingNextRightPointersSolution,
)


@pytest.fixture
def solution():
    return PopulatingNextRightPointersSolution()


@pytest.fixture
def tree_one():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    return root


def test_populating_next_right_pointers_tree_one(solution, tree_one):
    ref = Node(
        val=1,
        left=Node(
            val=2,
            left=Node(
                val=4,
                left=None,
                right=None,
                next=Node(
                    val=5,
                    left=None,
                    right=None,
                    next=Node(
                        val=6,
                        left=None,
                        right=None,
                        next=Node(val=7, left=None, right=None, next=None),
                    ),
                ),
            ),
            right=Node(
                val=5,
                left=None,
                right=None,
                next=Node(
                    val=6,
                    left=None,
                    right=None,
                    next=Node(val=7, left=None, right=None, next=None),
                ),
            ),
            next=Node(
                val=3,
                left=Node(
                    val=6,
                    left=None,
                    right=None,
                    next=Node(val=7, left=None, right=None, next=None),
                ),
                right=Node(val=7, left=None, right=None, next=None),
                next=None,
            ),
        ),
        right=Node(
            val=3,
            left=Node(
                val=6,
                left=None,
                right=None,
                next=Node(val=7, left=None, right=None, next=None),
            ),
            right=Node(val=7, left=None, right=None, next=None),
            next=None,
        ),
        next=None,
    )
    assert ref == solution.connect(tree_one)
