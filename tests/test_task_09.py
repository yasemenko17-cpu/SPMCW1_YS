"""Відкриті приклади завдання 09: Конвеєр процесів без shell."""
import pytest
from conftest import load

M = load(9)
solve = M.solve

PUBLIC = [(([['tr', 'a-z', 'A-Z']], 'hello\n'), ('HELLO\n', [0])),
 (([['sort'], ['uniq', '-c']], 'b\na\nb\n'), ('      1 a\n      2 b\n', [0, 0]))]

HIDDEN = []


@pytest.mark.parametrize("args,expected", PUBLIC + HIDDEN)
def test_solve(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
