import pytest

from solutions import (
    MirrorReflection,
)


@pytest.fixture
def solution():
    return MirrorReflection()


def test_mirror_reflection_case1(solution):
    p, q = 2, 1
    ref = 2
    result = solution.mirror_reflection(p, q)
    assert ref == result


def test_mirror_reflection_case2(solution):
    p, q = 3, 1
    ref = 1
    result = solution.mirror_reflection(p, q)
    assert ref == result


def test_constraints(solution):
    with pytest.raises(AssertionError):
        p, q = 1001, 1
        solution.mirror_reflection(p, q)

    with pytest.raises(AssertionError):
        p, q = 1, 1001
        solution.mirror_reflection(p, q)
