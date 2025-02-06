from example import add, subtract

def test_add():
    assert add(1,1) == 2
    assert add(1,-1) == 0
    assert add(5.5,4.5) == 10

def test_subtract():
    assert subtract(1,1) == 0
    assert subtract(1,-1) == 2
    assert subtract(5.5,4.5) == 1.0