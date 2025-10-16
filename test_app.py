from app import suma, resta, division

def test_suma () :
    assert suma(2,3) == 5

def test_resta():
    assert resta(3,2) == 1

def test_division():
    assert division(5,2)==2.5