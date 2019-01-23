from cocotb import SimLog, coroutine
from cocotb.monitors import Monitor
from cocotb.triggers import FallingEdge, RisingEdge


class FIFOMonitor(Monitor):
    def __init__(self, signals, clk, callback=None, event=None):
        self.name = "cocomod.fifointerface.%s" % (self.__class__.__name__)
        self.log = SimLog(self.name)
        self.valid = signals.valid
        self.ready = signals.ready
        self.data = signals.data
        self.clk = clk.signal
        Monitor.__init__(self, callback, event)

    @coroutine
    def _monitor_recv(self):
        while True:
            yield FallingEdge(self.clk)

            self.ready <= 1

            while True:
                yield RisingEdge(self.clk)
                try:
                    if self.valid == 1:
                        if isinstance(self.data, dict):
                            transaction = []
                            for name, signal in self.data:
                                transaction[name] = signal
                        else:
                            transaction = self.data
                        self._recv(transaction)
                        break
                except ValueError:
                    pass
