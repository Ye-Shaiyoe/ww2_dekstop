
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
