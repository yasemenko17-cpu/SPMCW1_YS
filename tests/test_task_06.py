"""Відкриті приклади завдання 06: Сигнали: обробники й блокування."""
import pytest
from conftest import load

M = load(6)
solve = M.solve

PUBLIC = [((['SIGUSR1', 'SIGUSR2'], False), ([], ['SIGUSR1', 'SIGUSR2'])),
 ((['SIGUSR1', 'SIGUSR1', 'SIGUSR1'], True), (['SIGUSR1'], ['SIGUSR1']))]

HIDDEN = []


@pytest.mark.parametrize("args,expected", PUBLIC + HIDDEN)
def test_solve(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
