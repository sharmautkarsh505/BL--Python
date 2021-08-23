import unittest 
from registration import first_name,last_name,email_id,mobile_number,user_password

class UserValidation(unittest.TestCase):

    def test_fname(self):
        self.assertEqual(first_name('Utkarsh'),True)
        self.assertEqual(first_name('UTkarsh'),False)
        self.assertEqual(first_name('utkarsh'),False)
        self.assertEqual(first_name('Ka'),False)
        self.assertEqual(first_name('K1aran'),False)
        self.assertEqual(first_name('Utkarsh   '),False)

    def test_lname(self):
        self.assertEqual(last_name('Sharma'),True)
        self.assertEqual(last_name('SHarma'),False)
        self.assertEqual(last_name('Sh'),False)
        self.assertEqual(last_name('S1har'),False)
        self.assertEqual(last_name('SHARMA'),False)
    
    def test_emailid(self):
        self.assertEqual(email_id('utkarsh@bl.co'),True)
        self.assertEqual(email_id('utkarsh.sharma@bl.co.in'),True)
        self.assertEqual(email_id('UTKARSH@bl.Co'),False)
        self.assertEqual(email_id('uk.lm@bl.co.in'),False)
        self.assertEqual(email_id('uke@bl.co'),True,)

    def test_mobile_number(self):
        self.assertEqual(mobile_number('00 0000000000'),False)
        self.assertEqual(mobile_number('81 7989886451'),True)
        self.assertEqual(mobile_number('80 1234567092'),True)
        
    
    def test_password(self):
        self.assertEqual(user_password('U@1karsh'),True)
        self.assertEqual(user_password('UTKARS1$'),True)
        self.assertEqual(user_password('&$Utkars'),False)
        self.assertEqual(user_password('Ut@k1arsh'),False)
        self.assertEqual(user_password('UK123@kl'),True)

if __name__ == '__main__':
    unittest.main()


