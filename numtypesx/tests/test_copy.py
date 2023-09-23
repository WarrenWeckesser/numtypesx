
import pytest
import numpy as np
from numpy.testing import assert_array_equal
from numtypesx import LogFloat32, LogFloat64


@pytest.mark.parametrize('dt', [LogFloat32(), LogFloat64()])
def test_copy_method(dt):
    x = np.array([0.0,  1e-24, 1.0, np.e, 100.0], dtype=dt)
    y = x.copy()
    assert_array_equal(x, y, strict=True)
