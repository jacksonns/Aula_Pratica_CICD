import pytest
from app.bubblesort import Bubblesort

@pytest.fixture
def bubblesort():
    bubblesort = Bubblesort()
    return bubblesort

class TestBubblesort:

    def test_sort(self, bubblesort):
        list = [4, 5, 1, 2, 7, 3, 6]
        ordered = bubblesort.sort(list)
        assert ordered == [1, 2, 3, 4, 5, 6, 7]
