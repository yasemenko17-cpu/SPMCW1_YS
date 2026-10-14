"""Відкриті приклади завдання 05: Діти: fork і waitpid."""
import pytest
from conftest import load

M = load(5)
solve = M.solve

PUBLIC = [(([3, -9],), [('exit', 3), ('signal', 9)]), (([0],), [('exit', 0)])]

HIDDEN = []


@pytest.mark.parametrize("args,expected", PUBLIC + HIDDEN)
def test_solve(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
