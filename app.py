
import tkinter as tk
from datetime import datetime

from config import *
from utils.clock      import start_clock
from utils.typewriter import start_typewriter
from tabs import BattlesTab, FiguresTab, TimelineTab, QuotesTab, IntelTab

class WW2App:
    """
    Assembler utama aplikasi. Bertanggung jawab atas:
      - header & navigation bar
      - menginstansiasi setiap tab
      - status bar bawah
      - clock & typewriter effect
      - etc.
    """

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(APP_SIZE)
        self.root.configure(bg=BG_DARK)
        self.root.minsize(*APP_MINSIZE)

        self._build_header()
        self._build_nav()
        self._build_statusbar()
        self._build_body()


