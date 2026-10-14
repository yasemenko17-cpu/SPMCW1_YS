import errno
import os

def solve(code: int) -> str:
    """Завдання 2: Код помилки errno"""
    if code not in errno.errorcode or code <= 0:
        return f"Невідомий код: {code}"
    
    name = errno.errorcode[code]
    # OSError автоматично визначає відповідний клас винятку за кодом
    exc = OSError(code, "")
    exc_class = exc.__class__.__name__
    explanation = os.strerror(code)
    
    return f"{name}: {exc_class}: {explanation}"