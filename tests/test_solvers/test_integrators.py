import pytest
import numpy as np
import pickle
import os
from src.solvers import euler, pred_corr, rk2, rk4


test_data = {}
for function in ["euler", "pred_corr", "rk2", "rk4"]:
    test_data[function] = pickle.load(
        open(os.path.join(os.path.dirname(__file__), "..", "test_data", f"{function}.pkl"), "rb")
    )


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (inputs_expected_dict["inputs"], inputs_expected_dict["output"])
        for inputs_expected_dict in test_data["euler"]
    ],
)
def test_euler(inputs, expected):
    np.testing.assert_allclose(euler(*inputs), expected, atol=1e-4, rtol=1e-4)


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (inputs_expected_dict["inputs"], inputs_expected_dict["output"])
        for inputs_expected_dict in test_data["pred_corr"]
    ],
)
def test_pred_corr(inputs, expected):
    np.testing.assert_allclose(pred_corr(*inputs), expected, atol=1e-4, rtol=1e-4)


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (inputs_expected_dict["inputs"], inputs_expected_dict["output"])
        for inputs_expected_dict in test_data["rk2"]
    ],
)
def test_rk2(inputs, expected):
    np.testing.assert_allclose(rk2(*inputs), expected, atol=1e-4, rtol=1e-4)


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (inputs_expected_dict["inputs"], inputs_expected_dict["output"])
        for inputs_expected_dict in test_data["rk4"]
    ],
)
def test_rk4(inputs, expected):
    np.testing.assert_allclose(rk4(*inputs), expected, atol=1e-4, rtol=1e-4)
