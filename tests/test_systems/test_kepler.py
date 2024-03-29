import pytest
import numpy as np
import pickle
import os
from src.systems import kepler

kepler_data = pickle.load(open(os.path.join(os.path.dirname(__file__), "..", "test_data", "kepler.pkl"), "rb"))


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (inputs_expected_dict["inputs"], inputs_expected_dict["output"])
        for inputs_expected_dict in kepler_data
    ],
)
def test_kepler(inputs, expected):
    np.testing.assert_allclose(kepler(*inputs), expected, atol=1e-4, rtol=1e-4)
