from collections import namedtuple


FIFOSignals = namedtuple("FIFOSignals", ['valid', 'ready', 'data'])
