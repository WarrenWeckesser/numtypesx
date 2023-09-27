import pytest
import math
import numtypesx as nt


@pytest.mark.parametrize('nint', [nt.nint8, nt.nint16, nt.nint32, nt.nint64])
def test_neg(nint):
    x = nint(54)
    assert -x == nint(-54)


@pytest.mark.parametrize('nint', [nt.nint8, nt.nint16, nt.nint32, nt.nint64])
def test_pos(nint):
    x = nint(54)
    assert +x == x


@pytest.mark.parametrize('nint', [nt.nint8, nt.nint16, nt.nint32, nt.nint64])
def test_add(nint):
    x = nint(30)
    y = nint(-3)
    assert x + y == nint(27)


@pytest.mark.parametrize('nint', [nt.nint8, nt.nint16, nt.nint32, nt.nint64])
def test_multiply(nint):
    x = nint(30)
    y = nint(-3)
    assert x * y == nint(-90)


@pytest.mark.parametrize('nint', [nt.nint8, nt.nint16, nt.nint32, nt.nint64])
def test_subtract(nint):
    x = nint(30)
    y = nint(-3)
    assert x - y == nint(33)


@pytest.mark.parametrize('nint', [nt.nint8, nt.nint16, nt.nint32, nt.nint64])
def test_floor_div(nint):
    x = nint(30)
    y = nint(-3)
    assert x // y == nint(-10)


@pytest.mark.parametrize('nint', [nt.nint8, nt.nint16, nt.nint32, nt.nint64])
def test_true_div(nint):
    x = nint(30)
    y = nint(-3)
    assert x / y == -10.0


@pytest.mark.parametrize('nint', [nt.nint8, nt.nint16, nt.nint32, nt.nint64])
def test_nan(nint):
    x = nint(math.nan)
    y = nint(-23)
    assert math.isnan(x)
    assert math.isnan(x + y)
