import pytest


def function(x):
    return x + 1


def test_function():
    assert function(3) == 4

def test_function_1():
    assert function(4) == 2


