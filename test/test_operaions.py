from src.math_operations import add,sub,multiply,divison
def test_add():
    assert add(3,2)==5
    assert add(4,5)==9

def test_sub():
    assert sub(3,2)==1
    assert sub(2,3)==-1
def test_multiply():
    assert multiply(2, 3) == 6

def test_multiply_zero():
    assert multiply(10, 0) == 0        

def test_division():
    assert divison(10,2)==5   