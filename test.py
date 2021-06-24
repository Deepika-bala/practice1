import pytest


from main import Student

obj1 = Student('Cricket.txt', 'unique_filename')
crk = obj1.read_file()
@pytest.mark.test1
def test_to_ing():
    assert obj1.to_ing(crk)!= -1
def test_cou():
    assert obj1.cou(crk) != '2008'
def test_pali():
    assert obj1.pali(crk) == 0
def test_uin():
    assert obj1.uin(crk) != 0
def test_swapblank():
    assert obj1.swapblank(crk) == 'null'








