"""Відкриті приклади завдання 10: Наглядач за процесами з тайм-аутом."""
import pytest
from conftest import load

M = load(10)
solve = M.solve

PUBLIC = [(([['sh', '-c', 'exit 3'], ['sleep', '30']], 0.3, 0.5), ['exit 3', 'signal SIGTERM']), (([], 0.1, 0.1), [])]

HIDDEN = []


@pytest.mark.parametrize("args,expected", PUBLIC + HIDDEN)
def test_solve(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
