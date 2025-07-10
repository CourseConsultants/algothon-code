import numpy as np

### TO RUN, RUN 'eval.py' ##########################

nInst = 50
currentPos = np.zeros(nInst)

import numpy as np

nInst = 50
currentPos = np.zeros(nInst)

def getMyPosition(prcSoFar):
    global currentPos
    n, t = prcSoFar.shape

    if t < 20:
        return np.zeros(n)

    short_window = 5
    long_window = 20

    short_ma = np.mean(prcSoFar[:, -short_window:], axis=1)
    long_ma = np.mean(prcSoFar[:, -long_window:], axis=1)

    signals = np.sign(short_ma - long_ma)  # +1 = long, -1 = short

    position_scale = 5000
    prices = prcSoFar[:, -1]
    max_units = 10000 // prices  # instrument limit

    raw_pos = (signals * position_scale) // prices
    clipped_pos = np.clip(raw_pos, -max_units, max_units)

    currentPos = clipped_pos.astype(int)
    return currentPos
