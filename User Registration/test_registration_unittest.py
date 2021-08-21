import unittest 

class UserValidation(unittest.TestCase):

    def test_fname(self):
        self.assertRegex('Utkarsh',r'^[A-Z][a-z]{2,}$')
        self.assertNotRegex('SAYMA',r'^[A-Z][a-z]{2,}$')
        self.assertNotRegex('A1ana',r'^[A-Z][a-z]{2,}$')
        self.assertRegex('Karan',r'^[A-Z][a-z]{2,}$')
        self.assertNotRegex('Ka',r'^[A-Z][a-z]{2,}$')
    def test_lname(self):
        self.assertRegex('Sharma',r'^[A-Z][a-z]{2,}$')
    def test_emailid(self):
        self.assertRegex('utkarsh@bl.co',r"[a-z]{3,}\@bl\.co" or r"[a-z]{3,}+\.[a-z]{3,}\@bl\.co\.in")
        self.assertRegex('utkarsh.sharma@bl.co.in',r"[a-z]{3,}\@bl\.co" or r"[a-z]{3,}+\.[a-z]{3,}\@bl\.co\.in")
        self.assertRegex('utkarsh@gmail.co',r"[a-z]{3,}\@bl\.co" or r"[a-z]{3,}+\.[a-z]{3,}\@bl\.co\.in")
    def test_mobileno(self):
        self.assertRegex('91 9923645994',r"\+?\d{2}\s\d{10}")  
        self.assertRegex('+94 8823467891',r"\+?\d{2}\s\d{10}")

if __name__ == '__main__':
    unittest.main()


