
import pytest
import numtypesx as nt


@pytest.mark.parametrize('typ', [nt.LogFloat32Scalar, nt.LogFloat64Scalar])
def test_logfloat(typ):
    log = 1.5
    x = typ(log=log)
    assert x.log == log
