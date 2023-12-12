from typing import Callable, Any, Union
import numbers

import numpy as np


def euler(
        func: Callable[[float, float, Any], float],
        y0: Union[numbers.Number, np.ndarray],
        time_steps: Union[numbers.Number, np.ndarray],
        *args,
        **kwargs
) -> np.ndarray:
    r"""
    Solve differential equation using Euler's method.

    :param func: The differential equation to solve.
    :type func: Callable[[float, float, Any], float]
    :param y0: The initial value for the differential equation.
    :type y0: Union[numbers.Number, np.ndarray]
    :param time_steps: The time steps to use.
    :type time_steps: Union[numbers.Number, np.ndarray]
    :param args: The arguments to pass to the differential equation.
    :param kwargs: The keyword arguments to pass to the differential equation.

    :keyword float dt: The time step to use if time_steps is not given or is a scalar. Default to 0.01.

    :Note: The other keyword arguments are passed to the differential equation.

    :return: The solution of the differential equation for each time step.
    :rtype: np.ndarray
    """
    raise NotImplementedError("euler is not implemented yet.")

