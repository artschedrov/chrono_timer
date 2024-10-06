import os
import tkinter as tk
from ttkbootstrap import ttk, Style
from datetime import timedelta
from datetime import datetime

WORK_TIME = 0
ACTIVITY = ''
START_TIME = None
END_TIME = None
key = 'HOME'
HOME_PATH = os.getenv(key)

class ChronoTimer():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("200x300")
        self.root.title("Chrono Timer")
        self.style = Style(theme="simplex")
        self.style.theme_use()

        self.timer_label = tk.Label(self.root, text="", font=("TkDefaultFont", 40))
        self.timer_label.pack(pady=20)

        self.inputtxt = tk.Text(self.root, height = 5, width = 20, bg = "light yellow")
        self.inputtxt.pack()

        self.start_button = ttk.Button(self.root, text="Start", command=self.start_timer)
        self.start_button.pack(pady=5)

        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_timer,
                                      state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.work_time = WORK_TIME
        self.start_time = START_TIME
        self.end_time = END_TIME
        self.is_work_time, self.is_running = True, False
        self.activity = ACTIVITY
        self.home_path = HOME_PATH

        self.root.mainloop()

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.is_running = True
        self.start_time = datetime.now().strftime('%H:%M:%S')
        self.update_timer()

    def stop_timer(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.is_running = False
        self.end_time = datetime.now().strftime('%H:%M:%S')
        self.activity = self.inputtxt.get("1.0", "end-1c")
        self.inputtxt.delete("1.0", "end-1c")
        self.make_note(self.activity, self.start_time, self.end_time)
        self.is_work_time, self.work_time = True, WORK_TIME

    def update_timer(self):
        if self.is_running:
            if self.is_work_time:
                self.work_time += 1
            minutes, seconds = divmod(self.work_time, 60)
            self.timer_label.config(text="{:02d}:{:02d}".format(minutes, seconds))
            self.root.after(1000, self.update_timer)

    def make_note(self, act, start, end):
        m_s = timedelta(seconds=self.work_time)
        os.system(f"cd {self.home_path} && echo {start} {end} {m_s} {act} >> today")

ChronoTimer()
