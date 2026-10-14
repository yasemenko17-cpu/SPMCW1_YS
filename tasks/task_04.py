import errno
import os
import stat

def solve(path: str) -> str:
    """Завдання 4: Метадані файла (lstat)"""
    try:
        st = os.lstat(path)
    except OSError as e:
        err_name = errno.errorcode.get(e.errno, str(e.errno))
        return f"Помилка: {err_name}"
    
    mode = st.st_mode
    
    # Визначення типу файлу
    if stat.S_ISREG(mode):
        file_type = "звичайний файл"
    elif stat.S_ISDIR(mode):
        file_type = "каталог"
    elif stat.S_ISLNK(mode):
        file_type = "символьне посилання"
    elif stat.S_ISFIFO(mode):
        file_type = "канал FIFO"
    elif stat.S_ISSOCK(mode):
        file_type = "сокет"
    elif stat.S_ISCHR(mode):
        file_type = "символьний пристрій"
    elif stat.S_ISBLK(mode):
        file_type = "блоковий пристрій"
    else:
        file_type = "невідомо"
        
    # Формування прав у стилі ls -l
    perms = []
    # Owner
    perms.append('r' if mode & stat.S_IRUSR else '-')
    perms.append('w' if mode & stat.S_IWUSR else '-')
    if mode & stat.S_ISUID:
        perms.append('s' if mode & stat.S_IXUSR else 'S')
    else:
        perms.append('x' if mode & stat.S_IXUSR else '-')
        
    # Group
    perms.append('r' if mode & stat.S_IRGRP else '-')
    perms.append('w' if mode & stat.S_IWGRP else '-')
    if mode & stat.S_ISGID:
        perms.append('s' if mode & stat.S_IXGRP else 'S')
    else:
        perms.append('x' if mode & stat.S_IXGRP else '-')
        
    # Others
    perms.append('r' if mode & stat.S_IROTH else '-')
    perms.append('w' if mode & stat.S_IWOTH else '-')
    if mode & stat.S_ISVTX:
        perms.append('t' if mode & stat.S_IXOTH else 'T')
    else:
        perms.append('x' if mode & stat.S_IXOTH else '-')
        
    perms_str = "".join(perms)
    octal_mode = f"{stat.S_IMODE(mode):04o}"
    rights_line = f"{perms_str} ({octal_mode})"
    
    nlink = st.st_nlink
    
    return f"Тип: {file_type}\nПрава: {rights_line}\nЖорстких посилань: {nlink}"