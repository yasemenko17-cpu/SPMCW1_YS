# Завдання 13. Обробник, що блокує програму (середнє)

Програма обробляє чергу завдань і має коректно завершуватися за `SIGTERM`.

```python
import signal
import sys
import threading

lock = threading.Lock()
queue = ["a", "b", "c"]

def save_state():
    with lock:
        with open("state.txt", "w") as f:
            f.write(",".join(queue))

def on_term(signum, frame):
    save_state()
    sys.exit(0)

signal.signal(signal.SIGTERM, on_term)

while queue:
    with lock:
        item = queue.pop(0)
        handle(item)
```

Під час тестів програма іноді просто «зависає» після надсилання `SIGTERM`.

**Умова.**
- Поясніть, чому програма іноді зависає (опишіть послідовність подій).
- Назвіть ще одну проблему такого обробника, окрім зависання.
- Запропонуйте виправлення й поясніть, чому воно надійніше.

**Обсяг.** 8-12 речень.

---

Відповідь:

