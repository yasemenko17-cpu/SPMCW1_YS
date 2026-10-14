"""Відкриті приклади завдання 08: Канал між батьком і дитиною."""
import pytest
from conftest import load

M = load(8)
solve = M.solve

PUBLIC = [((['раз', 'два', 'три'],), (['раз', 'два', 'три'], 3)), (([],), ([], 0))]

HIDDEN = []


@pytest.mark.parametrize("args,expected", PUBLIC + HIDDEN)
def test_solve(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
