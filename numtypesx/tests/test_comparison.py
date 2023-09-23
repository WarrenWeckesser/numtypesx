
import pytest
import numpy as np
from numpy.testing import assert_array_equal
from numtypesx import LogFloat32, LogFloat64


@pytest.mark.parametrize('dt', [LogFloat32(), LogFloat64()])
def test_copy_method(dt):
    x = np.array([0.0, 1.0, np.e, 100.0], dtype=dt)
    y = np.array([1.0, 1.0, 1.0, 99.0], dtype=dt)
    assert_array_equal(x == y, [False, True, False, False])
    assert_array_equal(x != y, [True, False, True, True])
    assert_array_equal(x < y, [True, False, False, False])
    assert_array_equal(x <= y, [True, True, False, False])
    assert_array_equal(x > y, [False, False, True, True])
    assert_array_equal(x >= y, [False, True, True, True])
