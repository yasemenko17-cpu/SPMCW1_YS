"""Відкриті приклади завдання 04: Метадані файла (lstat)."""
import os
import pytest
from conftest import load

M = load(4)
solve = M.solve

PUBLIC = [('file640', 'Тип: звичайний файл\nПрава: rw-r----- (0640)\nЖорстких посилань: 1'),
 ('missing', 'Помилка: ENOENT')]

HIDDEN = []

def make(tmp_path, kind):
    """Створює об'єкт файлової системи для сценарію kind і повертає шлях до нього."""
    path = tmp_path / "obj"
    if kind in ("file640", "file755", "file000", "setuid", "setuid_noexec", "hardlink", "symlink", "broken_symlink"):
        mode = {"file640": 0o640, "file755": 0o755, "file000": 0o000, "setuid": 0o4755, "setuid_noexec": 0o4644,
                "hardlink": 0o644, "symlink": 0o644, "broken_symlink": 0o644}[kind]
        if kind != "broken_symlink":
            path.write_text("дані", encoding="utf-8")
            path.chmod(mode)
        if kind == "hardlink":
            os.link(path, tmp_path / "other")
        if kind == "symlink":
            link = tmp_path / "link"
            link.symlink_to(path)
            return str(link)
        if kind == "broken_symlink":
            link = tmp_path / "link"
            link.symlink_to(tmp_path / "немає_такого")
            return str(link)
    elif kind == "fifo":
        os.mkfifo(path, 0o600)
    elif kind == "socket":
        import socket
        sock = socket.socket(socket.AF_UNIX)
        sock.bind(str(path))
        sock.close()
        path.chmod(0o600)
    elif kind == "notdir":
        (tmp_path / "plain").write_text("x", encoding="utf-8")
        return str(tmp_path / "plain" / "child")
    elif kind == "missing":
        return str(tmp_path / "немає")
    return str(path)


@pytest.mark.parametrize("kind,expected", PUBLIC + HIDDEN)
def test_solve(tmp_path, kind, expected):
    assert solve(make(tmp_path, kind)) == expected


def test_functions_exist():
    assert callable(getattr(M, "solve", None)), "немає функції solve"
