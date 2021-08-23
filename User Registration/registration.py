import re

def first_name(fname):
    pattern_of_fname=re.compile(r"^[A-Z][a-z]{2,}$")
    if pattern_of_fname.fullmatch(fname):
        return True 
    else:
        return False

def last_name(lname):
    pattern_of_lname=re.compile(r"^[A-Z][a-z]{2,}$")
    if pattern_of_lname.fullmatch(lname):
        return True
    else:
        return False


def email_id(eid):
    pattern_of_email_1=re.compile(r"^[a-z]{3,}\@bl\.co$")
    pattern_of_email_2=re.compile(r"^[a-z]{3,}\.[a-z]{3,}\@bl\.co\.in$")

    if pattern_of_email_1.fullmatch(eid) or pattern_of_email_2.fullmatch(eid):
        return True
    else:
        return False

def mobile_number(mno):
    pattern_of_mobile_no=re.compile(r"^\+?[1-9][0-9]\s[0-9]{10}$")
    if pattern_of_mobile_no.fullmatch(mno):
        return True
    else:
        return False
    
def user_password(password):
    pattern_of_password=re.compile(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8}$")

    if pattern_of_password.fullmatch(password):
        return True
    else:
        return False