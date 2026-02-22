
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

        start_clock(self.clock_var)
        start_typewriter(self.root, self.quote_var)

       self._show_tab("battles")

    def _build_header(self):
        hdr = tk.Frame(self.root, bg=RED_WAR, height=72)
        hdr.pack(fill="x", side="top")
        hdr.pack_propagate(False)

        # kiri — insignia
        tk.Label(hdr, text="✠", font=("Georgia", 36),
                 fg=KHAKI, bg=RED_WAR).pack(side="left", padx=20)

