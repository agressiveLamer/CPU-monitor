import psutil as pt


class CPU:
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()

    def CPUpercentReturn(self):
        return pt.cpu_percent(percpu=True)

    def ramUsage(self):
        return pt.virtual_memory()