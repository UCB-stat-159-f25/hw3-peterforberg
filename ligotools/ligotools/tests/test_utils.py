import ligotools.utils as ltu
import pytest

# This test provides too few arguments to `whiten()`, which raises a TypeError
def test_whiten():
    fakestrain = []
    fakeinterp = []
    with pytest.raises(TypeError):
        ltu.whiten(fakestrain, fakeinterp)

# This test provides an incompatible data type to `reqshift`, which raises an IndexError
def test_reqshift():
    with pytest.raises(IndexError):
        ltu.reqshift(100)
    