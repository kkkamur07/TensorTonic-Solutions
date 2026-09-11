import numpy as np

def angle_features(angles):

    # Considering the angles are in radians. 

    angles = np.array(angles) 

    return np.array([np.sin(angles), np.cos(angles), np.tan(angles)])
    