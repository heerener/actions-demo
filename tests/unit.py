import os


SUM_LEFT = int(os.environ["SUM_LEFT"])
SUM_RIGHT = int(os.environ["SUM_RIGHT"])
SUM_TOTAL = int(os.environ["SUM_TOTAL"])


def test_sum():
    assert SUM_LEFT + SUM_RIGHT == SUM_TOTAL


def test_product():
    assert 2 * 2 == 4
