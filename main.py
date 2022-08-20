import tkinter as tk
from tkinter import ttk
import sys
from process import CPU
from widgetUpdate import widgetsConfigure


class Applicaiton(tk.Tk, CPU, widgetsConfigure):

    def __init__(self):
        super().__init__()
        self.baseSettings()
        self.CPU = CPU()
        self.setUI()
        self.makeBarCPUUsage()
        self.confCPUbar()

    def baseSettings(self):
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.title('CPU-RAM usage monitor bar')
        pass

    def setUI(self):
        self.exitBut = ttk.Button(self, text='Выйти', command=self.appExit).pack(fill=tk.X)

        self.bar2 = ttk.LabelFrame(self, text='Manual')
        self.bar2.pack(fill=tk.X)

        self.comboWin = ttk.Combobox(self.bar2,
                                     values=[
                                         "Спрятать",
                                         "Отобразить",
                                         "Мини"],
                                     state='readonly',
                                     width=12)
        self.comboWin.current(1)
        self.comboWin.pack(side=tk.LEFT)

        self.windowMoveButton = ttk.Button(self.bar2, text='move', command=self.configureWin).pack(side=tk.LEFT)
        self.trippleRightButton = ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bind_class('Tk', '<Enter>', self.enterMouse)
        self.bind_class('Tk', '<Leave>', self)

    def makeBarCPUUsage(self):
        self.CPUFrameBar = ttk.LabelFrame(self, text='Power')
        self.CPUFrameBar.pack(fill=tk.BOTH)

        self.labelCores = ttk.Label(self.CPUFrameBar, text=f'physical cores: {self.CPU.cpu_count},'
                                                           f'logical cores: {self.CPU.cpu_count_logical}',
                                    anchor=tk.CENTER).pack(fill=tk.X)

        self.listLabel = []
        self.listPBar = []

        for i in range(self.CPU.cpu_count_logical):
            self.listLabel.append(ttk.Label(self.CPUFrameBar, anchor=tk.CENTER))
            self.listPBar.append(ttk.Progressbar(self.CPUFrameBar, length=100))
        for i in range(self.CPU.cpu_count_logical):
            self.listLabel[i].pack(fill=tk.X)
            self.listPBar[i].pack(fill=tk.X)

        self.ramLab = ttk.Label(self.CPUFrameBar, text='', anchor=tk.CENTER)
        self.ramLab.pack(fill=tk.X)
        self.ramBar = ttk.Progressbar(self.CPUFrameBar, length=100)
        self.ramBar.pack(fill=tk.X)

    def enterMouse(self, event):
        if self.comboWin.current() == 0 or 1:
            self.geometry('')

    def leeaveMouse(self, event):
        if self.comboWin.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')

    def appExit(self):
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = Applicaiton()
    root.mainloop()
