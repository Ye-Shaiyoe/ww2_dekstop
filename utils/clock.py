import threading
import time
from datetime import datetime


def start_clock(string_var):
    """
    Mulai thread background yang mengupdate `string_var` setiap detik
    dengan format jam ZULU militer.
    """
    def _tick():
        while True:
            now = datetime.now().strftime("ZULU %H:%M:%S  |  %d %b %Y")
            try:
                string_var.set(now)
            except Exception:
                break  
            time.sleep(1)

    t = threading.Thread(target=_tick, daemon=True)
    t.start()
    return t
