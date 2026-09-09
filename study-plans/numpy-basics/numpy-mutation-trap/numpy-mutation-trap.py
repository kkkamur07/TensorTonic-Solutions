import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    data = np.array(data, dtype = np.float64)
    row_data = data[row_idx, :]
    clipped = np.clip(row_data, lo, hi)

    return row_data, clipped