"""Відкриті приклади завдання 01: Розбір рядка strace."""
import pytest
from conftest import load

M = load(1)
solve = M.solve

PUBLIC = [(('openat(AT_FDCWD, "/etc/hostname", O_RDONLY|O_CLOEXEC) = 3',), 'openat: успіх, результат 3'),
 (('openat(AT_FDCWD, "/no/such", O_RDONLY) = -1 ENOENT (No such file or directory)',),
  'openat: помилка ENOENT (No such file or directory)')]

HIDDEN = []


@pytest.mark.parametrize("args,expected", PUBLIC + HIDDEN)
def test_solve(args, expected):
    assert solve(*args) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
