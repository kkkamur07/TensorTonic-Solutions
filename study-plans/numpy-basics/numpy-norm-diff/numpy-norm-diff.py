import numpy as np

def norm_diff(a, b, lo, hi):
    """Returns: np.ndarray of absolute differences after clipping and rescaling to [0, 1]"""

    a = np.array(a, dtype = np.float64)
    b = np.array(b, dtype = np.float64)

    a_clipped = np.clip(a, lo, hi)
    b_clipped = np.clip(b, lo, hi)

    # Broadcasting is going to help here. 
    a_rescaled = (a_clipped - lo)/(hi-lo)
    b_rescaled = (b_clipped - lo)/(hi-lo)

    # hope they are of the same size. 
    return np.abs(a_rescaled - b_rescaled)
    