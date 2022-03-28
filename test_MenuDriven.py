import MenuDriven
def test_Area_rectangle():
    x = 10
    y = 20
    result = MenuDriven.Area_rectangle(x, y)
    assert x * y == result
def test_Peri_rectangle():
    x = 10
    y = 20
    result = MenuDriven.Peri_rectangle(x, y)
    assert 2 * (x + y) == result
def test_Area_Square():
    x = 10
    y = 20
    result = MenuDriven.Area_Square(x)
    assert x*x == result
