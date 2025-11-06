from ligotools import readligo as rl

def test_ligo():
    try:
        data = rl.loaddata("data/H-H1_LOSC_4_V2-1126259446-32.hdf5")
        assert data != None
    except:
        raise 