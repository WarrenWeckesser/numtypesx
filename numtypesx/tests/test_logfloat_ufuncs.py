
import pytest
import numpy as np
from numpy.testing import assert_allclose
import numtypesx as nt


# Really basic tests.
#
# These tests can be simplified when more casting operations
# and more ufuncs (e.g. unary, comparisons, etc) are added.

@pytest.mark.parametrize('dtype, rtol', [(nt.LogFloat32(), 8e-6),
                                         (nt.LogFloat64(), 1e-14)])
@pytest.mark.parametrize('ufunc', [np.add,
                                   np.subtract,
                                   np.multiply,
                                   np.true_divide,
                                   np.power])
def test_ufuncs(dtype, rtol, ufunc):
    adata = [1.0, 1.5, 75.0]
    bdata = [0.5, 1.5, 15.0]
    a = np.array(adata, dtype=dtype)
    b = np.array(bdata, dtype=dtype)
    c = ufunc(a, b)

    for ai, bi, ci in zip(adata, bdata, c):
        v = ufunc(ai, bi)
        if not (v == 0.0 and ci.log == -np.inf):
            assert_allclose(np.exp(ci.log), v, rtol=rtol, atol=0)
