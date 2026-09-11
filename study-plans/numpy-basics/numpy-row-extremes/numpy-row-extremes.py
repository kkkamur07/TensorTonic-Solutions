import numpy as np

def row_extremes(data):
    """Returns: np.ndarray of shape (4, m), rows are max_val, max_col, min_val, min_col"""

    data = np.array(data, dtype = np.float64)

    # this gives us the indices
    argmax = np.argmax(data, axis=1)
    argmin = np.argmin(data, axis =1)

    # to get the values either we index ? or we just call np.max and np.min

    max = np.max(data, axis = 1)
    min = np.min(data, axis = 1)

    return np.array([max, argmax, min, argmin])