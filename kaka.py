import pytest
import math


def test0():
    assert len(set([1,2,3,1])) == 3

    for i in range(-2,2):
        assert i*0 == 0


def test1():
    s0 = set([1,2,3])
    s1 = set([2,3,4])
    assert s0.difference(s1) == set([1])
    assert s1.difference(s0) == set([4])

    for i in range(-2,2):
        assert 1**i == 1


def test2():
    try:
        assert set([1])[0] == 1
    except TypeError:
        pass
    try:
        assert math.acos(2) == 0
    except ValueError:
        pass



test0()
test1()
test2()
