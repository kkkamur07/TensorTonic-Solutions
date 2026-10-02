import numpy as np

def quantize_and_frame(data: list, decimals: int, pad_width: int) -> np.ndarray:
    """
    Returns float64 slices of rounded, floored, and ceiling-rounded values with zero borders.
    """
    data = np.array(data, dtype = np.float64)
    layers = [np.round(data, decimals), np.floor(data), np.ceil(data)]

    noi = [np.pad(layer, pad_width, mode = "constant", constant_values = 0.0 ) for layer in layers]
    return np.stack(noi)    
