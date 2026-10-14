"""Відкриті приклади завдання 07: Перенаправлення виводу через dup2."""
import pytest
from conftest import load

M = load(7)
solve = M.solve

PUBLIC = [(['перший', 'другий'], 'перший\nдругий\n'), ([], '')]

HIDDEN = []


@pytest.mark.parametrize("lines,expected", PUBLIC + HIDDEN)
def test_solve(tmp_path, lines, expected):
    path = tmp_path / "out.txt"
    assert solve(str(path), lines) == expected
    assert path.read_text(encoding="utf-8") == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
