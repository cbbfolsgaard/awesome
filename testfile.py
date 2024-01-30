import numpy as np

def lag(a, n):
    lagged = np.empty_like(a)
    lagged[:n] = np.nan
    lagged[n:] = a[:-n]
    return lagged

