import unittest

from system import *


class TestSystem(unittest.TestCase):
    def setUp(self):
        self.employee_1 = HourlyEmployee("Serhii", "Mazur", "developer", 100)
        self.employee_2 = HourlyEmployee("Andrii", "Merkulov", "CEO", 12)
        self.employee_3 = SalariedEmployee("Gramatton", "Clerick", "manager", 22500.0, 4)

        firma = Company("ETA", [self.employee_1, self.employee_2, self.employee_3])

    def test_fullname(self):
        self.assertEqual(self.employee_2.fullname, ('Andrii', 'Merkulov'))

    def test_hourly_rate(self):
        self.assertEqual(self.employee_2.hourly_rate, 50.0)

    def test_take_holiday(self):
        self.assertEqual(self.employee_3.take_holiday(), 'Taking a payout. Remaining vacation days: 3')


if __name__ == "__main__":
    unittest.main()
