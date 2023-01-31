from main import *

def test_1():
    assert binconv(15) == 1111
def test_2():
    assert binconv(126) == 1111110
def test_3():
    assert binconv(52) == 110100
def test_4():
    assert binconv(5884) == 1011011111100
def test_5():
    assert binconv(444) == 110111100
def test_6():
    assert binconv(97) == 1100001
def test_7():
    assert binconv(552) == 1000101000
def test_8():
    assert binconv(39) == 100111
def test_9():
    assert binconv(75) == 1001011
def test_10():
    assert binconv(447774) == 1101101010100011110
def test_11():
    assert binconv(10) == 1010
def test_12():
    assert binconv(1) == 1
def test_13():
    assert binconv(2) == 10
def test_14():
    assert binconv(388) == 110000100
def test_15():
    assert binconv(7625) == 1110111001001
def test_16():
    assert binconv(-45) == -101101

