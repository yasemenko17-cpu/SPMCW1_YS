import os

def solve(commands: list, data: str) -> tuple:
    """Завдання 9: Конвеєр процесів без shell"""
    n = len(commands)
    if not n:
        return (data, [])
        
    # Створюємо n + 1 каналів для зв'язку між батьком, процесами та виходом
    pipes = [os.pipe() for _ in range(n + 1)]
    
    pids = []
    for i in range(n):
        pid = os.fork()
        if pid == 0:
            # Дочірній процес
            try:
                for j in range(n + 1):
                    r, w = pipes[j]
                    if j == i:
                        os.dup2(r, 0)
                        os.close(r)
                        os.close(w)
                    elif j == i + 1:
                        os.dup2(w, 1)
                        os.close(r)
                        os.close(w)
                    else:
                        os.close(r)
                        os.close(w)
                os.execvp(commands[i][0], commands[i])
            except Exception:
                os._exit(127)
        else:
            pids.append(pid)
            
    # Батьківський процес закриває непотрібні кінці каналів
    for j in range(n + 1):
        r, w = pipes[j]
        if j == 0:
            os.close(r)
        elif j == n:
            os.close(w)
        else:
            os.close(r)
            os.close(w)
            
    # Записуємо вхідні дані у ввід першої команди
    if data:
        os.write(pipes[0][1], data.encode('utf-8'))
    os.close(pipes[0][1])
    
    # Читаємо вивід останньої команди
    output_chunks = []
    while True:
        chunk = os.read(pipes[n][0], 65536)
        if not chunk:
            break
        output_chunks.append(chunk)
    os.close(pipes[n][0])
    
    output = b"".join(output_chunks).decode('utf-8')
    
    # Очікуємо завершення всіх процесів
    codes = []
    for pid in pids:
        _, status = os.waitpid(pid, 0)
        if os.WIFEXITED(status):
            codes.append(os.WEXITSTATUS(status))
        elif os.WIFSIGNALED(status):
            codes.append(-os.WTERMSIG(status))
        else:
            codes.append(status)
            
    return (output, codes)