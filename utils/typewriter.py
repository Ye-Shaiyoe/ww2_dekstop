import random
from assets.data import QUOTES


def start_typewriter(root, string_var, delay_ms=500, speed_ms=35):
    """
    Ambil quote acak, lalu tampilkan karakter per karakter.
    """
    q, _ = random.choice(QUOTES)
    short = q[:72].replace("\n", " ")
    idx = [0]

    def _type():
        if idx[0] <= len(short):
            string_var.set(short[: idx[0]])
            idx[0] += 1
            root.after(speed_ms, _type)

    root.after(delay_ms, _type)
