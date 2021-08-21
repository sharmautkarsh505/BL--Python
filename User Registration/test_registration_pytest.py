import pytest
import re

def first_name(fname):
    if fname.isalpha()==True and len(fname)>=3 and fname[0]==fname[0].upper() and fname[1:len(fname)-1]==fname[1:len(fname)-1].lower():
        return fname
    else:
        return None

def test_fname():
    pattern_fname=re.compile(r'[A-Z][a-z]{2,}')
    assert re.fullmatch(pattern_fname,first_name('Utkarsh'))
    assert re.fullmatch(pattern_fname,first_name('utkarsh'))
    assert re.fullmatch(pattern_fname,first_name('L1james'))
    
    

def last_name(lname):
    if lname.isalpha()==True and len(lname)>=3 and lname[0]==lname[0].upper() and lname[1:len(lname)-1]==lname[1:len(lname)-1].lower():
        return lname
    else:
        pass
