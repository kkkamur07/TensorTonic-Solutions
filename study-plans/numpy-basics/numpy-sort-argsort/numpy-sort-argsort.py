import numpy as np

def sort_with_indices(data, axis):
    """Returns: np.ndarray of shape (2, m, n), stacked sorted values and sort indices"""

    data = np.array(data)

    sorted = np.sort(data, axis = axis)
    argsorted = np.argsort(data, axis = axis) # this gives you the indices right ?

    return np.array([sorted, argsorted])