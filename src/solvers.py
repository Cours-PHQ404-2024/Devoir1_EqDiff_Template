from typing import Callable, Any, Union
import numbers

import numpy as np


def euler(
        func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float],
        y0: Union[numbers.Number, np.ndarray],
        time_steps: Union[numbers.Number, np.ndarray],
        *args,
        **kwargs
) -> np.ndarray:
    r"""
    Solve differential equation using Euler's method.

    :param func: The differential equation to solve. The function is in the form `y' = func(y, t, *args, **kwargs)`.
    :type func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float]
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
    raise NotImplementedError("This function is not implemented yet.")


def pred_corr(
        func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float],
        y0: Union[numbers.Number, np.ndarray],
        time_steps: Union[numbers.Number, np.ndarray],
        *args,
        **kwargs
) -> np.ndarray:
    r"""
    Solve differential equation using the predictor-corrector method.

    :param func: The differential equation to solve. The function is in the form `y' = func(y, t, *args, **kwargs)`.
    :type func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float]
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
    raise NotImplementedError("This function is not implemented yet.")


def rk2(
        func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float],
        y0: Union[numbers.Number, np.ndarray],
        time_steps: Union[numbers.Number, np.ndarray],
        *args,
        **kwargs
) -> np.ndarray:
    r"""
    Solve differential equation using the Runge-Kutta 2 method.

    :param func: The differential equation to solve. The function is in the form `y' = func(y, t, *args, **kwargs)`.
    :type func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float]
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
    raise NotImplementedError("This function is not implemented yet.")


def rk4(
        func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float],
        y0: Union[numbers.Number, np.ndarray],
        time_steps: Union[numbers.Number, np.ndarray],
        *args,
        **kwargs
) -> np.ndarray:
    r"""
    Solve differential equation using the Runge-Kutta 4 method.

    :param func: The differential equation to solve. The function is in the form `y' = func(y, t, *args, **kwargs)`.
    :type func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float]
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
    raise NotImplementedError("This function is not implemented yet.")


def scipy_int(
        func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float],
        y0: Union[numbers.Number, np.ndarray],
        time_steps: Union[numbers.Number, np.ndarray],
        *args,
        **kwargs
) -> np.ndarray:
    r"""
    Solve differential equation using the SciPy integration method.

    :param func: The differential equation to solve. The function is in the form `y' = func(y, t, *args, **kwargs)`.
    :type func: Callable[[Union[numbers.Number, np.ndarray], numbers.Number, Any], float]
    :param y0: The initial value for the differential equation.
    :type y0: Union[numbers.Number, np.ndarray]
    :param time_steps: The time steps to use.
    :type time_steps: Union[numbers.Number, np.ndarray]
    :param args: The arguments to pass to the differential equation.
    :param kwargs: The keyword arguments to pass to the differential equation and/or
        to the scipy.integrate.odeint function.

    :keyword float dt: The time step to use if time_steps is not given or is a scalar. Default to 0.01.

    :Note: The other keyword arguments are passed to the scipy.integrate.odeint function.

    :return: The solution of the differential equation for each time step.
    :rtype: np.ndarray
    """
    raise NotImplementedError("This function is not implemented yet.")

