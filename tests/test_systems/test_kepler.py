import pytest
import numpy as np
from src.systems import kepler


@pytest.mark.parametrize(
    "y, t, expected",
    [
        (np.array([1, 2, 3, 4]), 0, np.array([3, 4, -0.089443, -0.178885]))
    ],
)
def test_kepler(y, t, expected):
    np.testing.assert_allclose(kepler(y, t), expected, atol=1e-4, rtol=1e-4)
