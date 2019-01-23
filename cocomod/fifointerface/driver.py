from cocotb import SimLog, coroutine
from cocotb.drivers import Driver
from cocotb.result import TestError
from cocotb.triggers import RisingEdge, FallingEdge


class FIFODriver(Driver):
    def __init__(self, signals, clk):
        self.log = SimLog("cocomod.fifointerface.%s" % (self.__class__.__name__))
        self.valid = signals.valid
        self.ready = signals.ready
        self.data = signals.data
        self.clk = clk.signal

        self.valid <= 0

        Driver.__init__(self)

    @coroutine
    def _driver_send(self, transaction, sync=True, **kwargs):
        if sync:
            yield RisingEdge(self.clk)

        while True:
            yield FallingEdge(self.clk)

            self.valid <= 1

            if isinstance(self.data, dict):
                if not isinstance(transaction, dict):
                    yield TestError("transaction is no dict")
                for name, signal in self.data.items():
                    if name not in transaction:
                        signal <= transaction[name]
            else:
                self.data <= transaction

            yield RisingEdge(self.clk)

            if self.ready == 1:
                break

        self.valid <= 0
