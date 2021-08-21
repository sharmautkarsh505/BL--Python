import re

def first_name(fname):
    if fname.isalpha()==True and len(fname)>=3 and fname[0]==fname[0].upper() and fname[1:len(fname)-1]==fname[1:len(fname)-1].lower():
        return fname
    else:
        pass 

def last_name(lname):
    if lname.isalpha()==True and len(lname)>=3 and lname[0]==lname[0].upper() and lname[1:len(lname)-1]==lname[1:len(lname)-1].lower():
        return lname
    else:
        pass


def email_id(eid):
    pattern_of_email_1=re.compile(r"[a-z]{3}[a-z]*\@[a-z]{2}[a-z]*\.co")
    pattern_of_email_2=re.compile(r"[a-z]{3}[a-z]+\.[a-z]{3}[a-z]+\@[a-z]{2}[a-z]+\.co\.in")

    if pattern_of_email_1.fullmatch(eid)!=None or pattern_of_email_2.fullmatch(eid)!=None:
        return eid
    else:
        print('Invalid input')

def mobile_number(mno):
    pattern_of_mobile_no=re.compile(r"\+?\d{2}\s\d{10}")
    #match=pattern_of_mobile_no.fullmatch(mno)
    valid_input=bool
    if pattern_of_mobile_no.fullmatch(mno)!=None:
        valid_input==True
    else:
        valid_input==False
    return valid_input

def user_password(password):
    pattern_of_password=re.compile(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$")

    if pattern_of_password.fullmatch(password):
        return password
    else:
        pass

print(mobile_number('91 9923645994'))