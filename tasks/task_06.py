import os
import signal

def solve(sequence: list, block: bool) -> tuple:
    """Завдання 6: Сигнали: обробники й блокування"""
    allowed = {'SIGHUP', 'SIGUSR1', 'SIGUSR2', 'SIGTERM'}
    for name in sequence:
        if name not in allowed:
            raise ValueError(f"Невідомий сигнал: {name}")
            
    sig_nums = [getattr(signal, name) for name in sequence]
    unique_sigs = set(sig_nums)
    
    handled = []
    def make_handler(sig_name):
        def handler(signum, frame):
            handled.append(sig_name)
        return handler
        
    old_handlers = {}
    for sig in unique_sigs:
        sig_name = signal.Signals(sig).name
        old_handlers[sig] = signal.signal(sig, make_handler(sig_name))
        
    old_mask = None
    try:
        sigset = set(unique_sigs)
        if block:
            old_mask = signal.pthread_sigmask(signal.SIG_BLOCK, sigset)
            
        for sig in sig_nums:
            os.kill(os.getpid(), sig)
            
        pending = []
        if block:
            pending_nums = signal.sigpending()
            pending = sorted(
                [signal.Signals(s).name for s in pending_nums],
                key=lambda x: getattr(signal, x)
            )
    finally:
        if block and old_mask is not None:
            signal.pthread_sigmask(signal.SIG_SETMASK, old_mask)
        for sig, old_h in old_handlers.items():
            signal.signal(sig, old_h)
            
    return (pending, handled)