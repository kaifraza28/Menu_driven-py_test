
def test_add():
    x = 10
    y = 20
    result = Calculator_New.add(x,y)
    assert x+y==result
def test_sub():
    x = 10
    y = 20
    result = Calculator_New.sub(x,y)
    assert x-y==result
def test_mult():
    x = 10
    y = 20
    result = Calculator_New.mult(x,y)
    assert x*y==result
def test_div():
    x = 10
    y = 20
    result = Calculator_New.div(x,y)
    assert x/y==result
