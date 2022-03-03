from icecream_parlor import icecreamParlor



def test_icecreamParlor1():
    m = 4
    arr = [1, 4, 5, 3, 2]

    result = icecreamParlor(m, arr)
    expected = [1, 4]
    assert result == expected

def test_icecreamParlor2():
    m = 4
    arr = [2, 2, 4, 3]

    result = icecreamParlor(m, arr)
    expected = [1, 2]
    assert result == expected

def test_icecreamParlor3():
    m = 9
    arr = [1, 3, 4, 6, 7, 9]

    result = icecreamParlor(m, arr)
    expected = [2, 4]
    assert result == expected

def test_icecreamParlor4():
    m = 8
    arr = [1, 3, 4, 4, 6, 8]

    result = icecreamParlor(m, arr)
    expected = [3, 4]
    assert result == expected

def test_icecreamParlor5():
    m = 3
    arr = [1, 2]

    result = icecreamParlor(m, arr)
    expected = [1, 2]
    assert result == expected