
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

        tk.Label(hdr, text="✠", font=("Georgia", 36),
                 fg=KHAKI, bg=RED_WAR).pack(side="left", padx=20)

        mid = tk.Frame(hdr, bg=RED_WAR)
        mid.pack(side="left", expand=True)
        tk.Label(mid, text="W O R L D   W A R   I I",
                 font=("Georgia", 26, "bold"),
                 fg=CREAM, bg=RED_WAR).pack()
        tk.Label(mid, text="HISTORICAL COMMAND CENTER  •  1939 – 1945",
                 font=("Courier New", 9), fg=KHAKI, bg=RED_WAR).pack()

        self.clock_var = tk.StringVar()
        tk.Label(hdr, textvariable=self.clock_var,
                 font=("Courier New", 10), fg=KHAKI, bg=RED_WAR).pack(side="right", padx=20)

        tk.Frame(self.root, bg=GOLD, height=2).pack(fill="x")


    def _build_nav(self):
        nav = tk.Frame(self.root, bg=BG_MID, height=38)
        nav.pack(fill="x")
        nav.pack_propagate(False)

        self._nav_btns: dict[str, tk.Button] = {}

        for label, key in NAV_TABS:
            btn = tk.Button(
                nav, text=label,
                font=("Courier New", 10, "bold"),
                bg=BG_MID, fg=GRAY_LT,
                activebackground=OLIVE, activeforeground=CREAM,
                relief="flat", bd=0, padx=16, pady=8,
                cursor="hand2",
                command=lambda k=key: self._show_tab(k)
            )
            btn.pack(side="left")
            self._nav_btns[key] = btn

            def _build_body(self):
                self._body = tk.Frame(self.root, bg=BG_DARK)
                self._body.pack(fill="both", expand=True)
        
                self._tabs: dict[str, tk.Frame] = {
                    "battles":  BattlesTab(self._body,  self._set_status),
                    "figures":  FiguresTab(self._body,  self._set_status),
                    "timeline": TimelineTab(self._body, self._set_status),
                    "quotes":   QuotesTab(self._body,   self._set_status),
                    "intel":    IntelTab(self._body,    self._set_status),
                }


            build_date = datetime.now().strftime("%d %b %Y")
            tk.Label(nav, text=f"  ARCHIVE BUILD: {build_date}  ",
                     font=("Courier New", 8), fg=GRAY_DK, bg=BG_MID).pack(side="right", padx=8)
    
            tk.Frame(self.root, bg=OLIVE, height=1).pack(fill="x")

            def _show_tab(self, key: str):
                for k, frame in self._tabs.items():
                    frame.pack_forget()
                self._tabs[key].pack(fill="both", expand=True)
        
                for k, btn in self._nav_btns.items():
                    btn.config(bg=OLIVE if k == key else BG_MID,
                               fg=CREAM if k == key else GRAY_LT)

            def _build_statusbar(self):
                bar = tk.Frame(self.root, bg=BG_MID, height=24)
                bar.pack(fill="x", side="bottom")
                bar.pack_propagate(False)
                tk.Frame(bar, bg=OLIVE, height=1).pack(fill="x")
        
                self._status_var = tk.StringVar(value="Ready.")
                self.quote_var   = tk.StringVar()

