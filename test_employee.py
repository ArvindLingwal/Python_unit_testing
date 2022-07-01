import unittest
from Employee import Employee
from unittest.mock import patch
# import requests

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('set-up\n')
        self.emp1 = Employee('arvind', 'lingwal', 50000)
        self.emp2 = Employee('vikrant', 'shukla', 60000)

    def tearDown(self):
        print('teardown\n')

    def test_email(self):
        # emp1 = Employee('arvind', 'lingwal', 50000)
        # emp2 = Employee('vikrant', 'shukla', 40000)

        self.assertEqual(self.emp1.email, 'arvind.lingwal@email.com')
        self.assertEqual(self.emp2.email, 'vikrant.shukla@email.com')

        self.emp1.first = 'dinesh'
        self.emp2.first = 'saharsh'

        self.assertEqual(self.emp1.email, 'dinesh.lingwal@email.com')
        self.assertEqual(self.emp2.email, 'saharsh.shukla@email.com')

    def test_fullname(self):
        # emp1 = Employee('arvind', 'lingwal', 50000)
        # emp2 = Employee('vikrant', 'shukla', 40000)

        self.assertEqual(self.emp1.fullname, 'arvind lingwal')
        self.assertEqual(self.emp2.fullname, 'vikrant shukla')

    def test_raise(self):
        # emp1 = Employee('arvind', 'lingwal', 50000)
        # emp2 = Employee('vikrant', 'shukla', 60000)

        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)

    def test_monthly_schdule(self):
        with patch('Employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Sucess'

            schedule = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/arvind/May')
            self.assertEqual(schedule, 'Sucess')

            mocked_get.return_value.ok = False

            schedule = self.emp1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/arvind/June')
            self.assertEqual(schedule, 'Bad Response!')



if __name__ == '__main__':
    unittest.main()
