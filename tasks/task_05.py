import os

def solve(plan: list) -> list:
    """Завдання 5: Діти: fork і waitpid"""
    pids = []
    for n in plan:
        pid = os.fork()
        if pid == 0:
            # Дитячий процес
            try:
                if n >= 0:
                    os._exit(n)
                else:
                    os.kill(os.getpid(), -n)
            finally:
                os._exit(0)
        else:
            pids.append(pid)
            
    results = []
    for pid in pids:
        _, status = os.waitpid(pid, 0)
        if os.WIFEXITED(status):
            results.append(('exit', os.WEXITSTATUS(status)))
        elif os.WIFSIGNALED(status):
            results.append(('signal', os.WTERMSIG(status)))
            
    return results