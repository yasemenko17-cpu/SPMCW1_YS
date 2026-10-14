"""Відкриті приклади завдання 03: Статус завершення дитини."""
import pytest
from conftest import load

M = load(3)
solve = M.solve

PUBLIC = [((768,), 'Завершився з кодом 3'), ((9,), 'Завершено сигналом SIGKILL (9)')]

HIDDEN = []


@pytest.mark.parametrize("args,expected", PUBLIC + HIDDEN)
def test_solve(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
