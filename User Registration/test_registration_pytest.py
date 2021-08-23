import pytest
from registration import first_name,last_name,email_id,mobile_number,user_password

def test_fname():
    assert first_name('Utkarsh')==True
    assert first_name('UTkarsh')==False
    assert first_name('utkarsh')==False

def test_lname():
    assert last_name('Sharma')==True
    assert last_name('SHarma')==False
    assert last_name('SHARMA')==False 

def test_email():
    assert email_id('utkarsh@bl.co')==True
    assert email_id('utkarsh.sharma@bl.co.in')==True
    assert email_id('UTKARSH@bl.co')==False 

def test_mobile_number():
    assert mobile_number('00 0000000000')==False
    assert mobile_number('81 7989886451')==True
    assert mobile_number('80 1234567092')==True

def test_password():
    assert user_password('U@1karsh')==True 
    assert user_password('UTKARS1$')==True
    assert user_password('&$Utkars')==False
