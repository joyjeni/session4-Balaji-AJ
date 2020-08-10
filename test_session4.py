import pytest
import random
import string
import session4
import os
import inspect
import re
import math
from decimal import Decimal

README_CONTENT_CHECK_FOR = ['and',
'or',
'repr',
'str',
'add',
'eq',
'float',
'ge',
'gt',
'invertsign',
'le',
'lt',
'mul',
'sqrt',
'bool']


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_bankers_rounding():
    q1 = session4.Qualean(1)
    assert len(str(q1).split(".")[-1]) == 10

def test_qualean_initializations():
    q1, q2, q3 = session4.Qualean(1), session4.Qualean(-1), session4.Qualean(0)
    q1, q2, q3 = session4.Qualean(1), session4.Qualean(-1), session4.Qualean(0)
    if q1 in range(-1,1):
        assert "Not in range"
    if q2 in range(-1,1):
        assert "Not in range"
    assert q3 == 0

    
def test_readme_contents():
    readme = open("README.md", "r",encoding = 'utf-8')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding = 'utf-8')
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_intentation():
    """ Returns pass if used four spaces for each level of syntactically \
    significant indenting."""
    lines = inspect.getsource(session4)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert re.search(
            '[a-zA-Z#@""]', space
        ), "Your code intentation does not follow PEP8 guidelines"
        assert (
            len(re.sub(r"[a-zA-Z#@\n\"\"]", "", space)) % 4 == 0
        ), "Your code intentation does not follow PEP8 guidelines"
 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_class_repr():
    s = session4.Qualean(0)
    assert 'object at' not in s.__repr__() 
 
def perfect_input():    
    with pytest.raises(ValueError) as e_info:
        r = session4.Qualean(-5)


def test_sum_till_100_equality():
    final_q=0
    a = session4.Qualean(1)
    q =a.qualean()
    for i in range(0,100):
        final_q = q + final_q
    last_q = Decimal(100*q)
    assert final_q == last_q, "Use of decimal was not wisely"

def test_or_functionality():
    
    a1 = session4.Qualean(1)
    assert a1 or b1 == True, "session4.Qualean OR not implemented properly"

def test_and_functionality():
    
    a1 = session4.Qualean(0)
    print(a1 and b1)
    assert (bool(a1) and b1) == False, "session4.Qualean AND not implemented properly"

def test_sqrt():
    q = session4.Qualean(1)
    if q < 0:
        ~q

    assert q.__sqrt__() == Decimal(str(q)).sqrt()


def test_add():
    q1, q2 = session4.Qualean(1), session4.Qualean(1)
    assert q1 + q2 == q1.num + q2.num


def test_mul():
    q1, q2 = session4.Qualean(1), session4.Qualean(1)
    assert q1 * q2 == q1.num * q2.num,'Error in Multiplication function'

def test_and():
    q1, q2, q3 = session4.Qualean(-1), session4.Qualean(1), session4.Qualean(0)

    assert bool(q1) and bool(q2) == True
    assert bool(q1) and bool(q3) == False
    assert bool(q2) and bool(q3) == False


def test_or():
    q1, q2, q3 = session4.Qualean(-1), session4.Qualean(1), session4.Qualean(0)

    assert bool(q1) or bool(q2) == True
    assert bool(q1) or bool(q3) == True
    assert bool(q2) or bool(q3) == True
    assert bool(q3) or bool(q3) == False

def test_inverse():
    q = session4.Qualean(1)
    y = q.qualean()
    ~q
    assert q + y == 0,'Inverse Function is not working !!'

def test_gt():
    q1, q2 = session4.Qualean(1), session4.Qualean(0)
    if q1 < 0:
        ~q1
    assert q1 > q2,'Greater then to functions is not working !!'


def test_ge():
    q1, q2 = session4.Qualean(1), session4.Qualean(0)
    if q1 < 0:
        ~q1
    assert q1 >= q2,'Greater then and equals to functions is not working !!'


def test_lt():
    q1, q2 = session4.Qualean(0), session4.Qualean(1)
    if q2 < 0:
        ~q2
    assert q1 < q2,'less then and equals to functions is not working !!'


def test_le():
    q1, q2 = session4.Qualean(0), session4.Qualean(1)
    if q2 < 0:
        ~q2
    assert q1 <= q2,'less then and equals to functions is not working !!'


def test_eq():
    q1, q2 = session4.Qualean(0), session4.Qualean(0)
    assert q1 == q2,'Equal functions is not working !!'
    
def test_qualean_type():
    q = session4.Qualean(1)
    assert isinstance(q, session4.Qualean)

def test_million_qsum():
    finalsum = 0
    for i in range(1000000):
        x = session4.Qualean(random.choice([-1, 0, 1]))
        finalsum = finalsum + x.qualean()
    assert math.isclose(x, 0), "not nearing to 0"


