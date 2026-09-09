import numpy as np

def filter_and_extract(data, row_start, row_stop, threshold):
    """
    Returns: 1D ndarray of float64
    """
    data = np.array(data, dtype = np.float64)
    sliced_data = data[row_start:row_stop].flatten()

    return sliced_data[sliced_data > threshold]

    