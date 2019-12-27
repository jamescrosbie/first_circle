import sys
import os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')


def test_connect():
    import basic
    assert True


def test_add():
    from basic import add as add
    assert add(1, 2) == 3


def test_sub():
    from basic import sub as sub
    assert sub(2, 1) == 1


def test_mult():
    import basic
    assert basic.mult(2, 2) == 4


def test_div():
    import basic
    assert basic.div(4, 2) == 2
