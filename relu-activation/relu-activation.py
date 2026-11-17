import numpy as np
import math
def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    x = np.array(x)
    result = np.where(x > 0,x,0)
    return result