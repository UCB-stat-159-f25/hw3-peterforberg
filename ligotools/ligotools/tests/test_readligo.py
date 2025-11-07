from ligotools import readligo as rl
import pytest
import os

# This test provides an empty .hdf5 file, which should output `None` if loaded using loaddata
def test_loaddata_length():
    fakefile = "test.hdf5"
    fakecontent = ""
    with open(fakefile, 'w') as file_object:
        file_object.write(fakecontent)

    value1, value2, value3 = rl.loaddata("test.hdf5")
    assert value1 == None

    os.remove(fakefile)

# This test provides a list instead of a dict to `dq_channel_to_seglist()`, which raises a TypeError
def test_dq_channel_to_seglist():
    fakedict = []
    with pytest.raises(TypeError):
        rl.dq_channel_to_seglist(fakedict)