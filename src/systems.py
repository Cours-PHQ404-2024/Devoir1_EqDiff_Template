import numbers

import numpy as np


def kepler(y: np.ndarray, t: numbers.Number) -> np.ndarray:
    r"""
    The Kepler problem.

    :param y: The state of the system. The state is in the form `[x, z, vx, vz]` where `x` and `z` are the position
                components and `vx` and `vz` are the velocity components.
    :type y: np.ndarray
    :param t: The time.
    :type t: float

    :return: The derivative of the state.
    :rtype: np.ndarray
    """
    raise NotImplementedError("This function is not implemented yet.")
