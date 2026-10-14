"""Відкриті приклади завдання 02: Код помилки errno."""
import pytest
from conftest import load

M = load(2)
solve = M.solve

PUBLIC = [((2,), 'ENOENT: FileNotFoundError: No such file or directory'), ((999,), 'Невідомий код: 999')]

HIDDEN = []


@pytest.mark.parametrize("args,expected", PUBLIC + HIDDEN)
def test_solve(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
