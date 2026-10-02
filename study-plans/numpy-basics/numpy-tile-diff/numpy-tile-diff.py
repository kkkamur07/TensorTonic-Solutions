import numpy as np

def tile_diff(data: list, reps: int) -> np.ndarray:
    """
    Returns float64 slices of tiled values and next-row differences with a final zero row.
    """
    data = np.array(data, dtype = np.float64)
    tiled = np.tile(data, (reps,1))
    difff = np.diff(tiled, axis = 0)
    padded_diff = np.pad(difff, ((0,1),(0,0)))

    return np.stack([tiled, padded_diff])
