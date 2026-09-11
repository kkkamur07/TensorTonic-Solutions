import numpy as np

def winsorize(data, lo_q, hi_q):
    """Returns: np.ndarray of shape (3, m, n), stacked clipped values, lo_mask, hi_mask"""

    data = np.array(data, dtype = np.float64)

    lo = np.percentile(data, lo_q, axis = 0) # act on the columns
    hi = np.percentile(data, hi_q, axis = 0) # act on the columsn

    # okay clip works on the vectors as well :)
    clipped = np.clip(data, lo, hi)

    lo = lo.reshape(1, -1)
    hi = hi.reshape(1, -1)

    # hoping that broadcasting works
    boolean_low = (data < lo).astype(np.float64)
    boolean_high = (data > hi).astype(np.float64)

    return np.array([clipped, boolean_low, boolean_high])