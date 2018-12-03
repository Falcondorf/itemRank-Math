import pytest
from itemrank_module import *
import numpy as np

def test_arrays1():
    a = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    assert a[1,1] == 5
    assert a[1,0] == 4

def test_csvReader():
    assert read_csv_toarray("./Personnalisation_Student12.csv") == [1,0,0,0,1,0,0,0,1,0]