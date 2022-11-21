import pytest

def test_foo():
    assert 1 == 1

class TestFoo:
    def test_foo(self):
        assert 1 == 1