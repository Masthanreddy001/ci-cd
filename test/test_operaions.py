from src.math_operations import add,sub
def test_add():
    assert add(3,2)==5
    assert add(4,5)==9

def test_sub():
    assert sub(3,2)==1
    assert sub(2,3)==-1
        