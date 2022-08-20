class widgetsConfigure:

    def confCPUbar(self):
        r = self.CPU.CPUpercentReturn()
        for i in range(self.CPU.cpu_count_logical):
            self.listLabel[i].configure(text=f'core {i + 1} usage {r[i]}%')
            self.listPBar[i].configure(value=r[i])

        r2 = self.CPU.ramUsage()
        self.ramLab.configure(text=f'RAM usage:{r2[2]}%, used{round(r2[3] / 1048576)} Mb,'
                                   f'\n available: {round(r2[1] / 1048576)} Mb')
        self.ramBar.configure(value=r2[2])

        self.wheel = self.after(1000, self.confCPUbar)

    def configureWin(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()