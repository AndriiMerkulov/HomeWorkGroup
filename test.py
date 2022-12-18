import unittest

from system import *


class TestSystem(unittest.TestCase):
    def setUp(self):
        self.employee_1 = HourlyEmployee("Serhii", "Mazur", "developer", 100, 60.0)
        self.employee_2 = HourlyEmployee("Andrii", "Merkulov", "CEO")
        self.employee_3 = SalariedEmployee("Gramatton", "Clerick", "manager", 22500.0)
        self.employee_4 = SalariedEmployee("Otto", "Fancent", "CEO", 20000.0, 25)

        self.firma = Company("ETA", [self.employee_1, self.employee_2, self.employee_3, self.employee_4])

    def test_fullname(self):
        self.assertEqual(self.employee_2.fullname, ('Andrii Merkulov'))
        self.assertEqual(self.employee_3.fullname, ('Gramatton Clerick'))

    def test_hourly_rate(self):
        self.assertEqual(self.employee_2.hours_worked, 0)
        self.assertEqual(self.employee_2.hourly_rate, 50.0)
        self.assertEqual(self.employee_1.hours_worked, 100)
        self.assertEqual(self.employee_1.hourly_rate, 60.0)

    def test_log_work(self):
        self.employee_1.log_work(10)
        self.assertEqual(self.employee_1.hours_worked, 110)
        self.employee_2.log_work(10)
        self.assertEqual(self.employee_2.hours_worked, 10)

    def test_take_holiday(self):
        msg = "Gramatton Clerick have not enough vacation days. Remaining days: 0. Requested: 1"
        self.employee_3.take_holiday()
        self.assertLogs(msg)
        msg = "Gramatton Clerick have not enough vacation days. Remaining days: 0. Requested: 5"
        self.employee_3.take_holiday(5, True)
        self.assertLogs(msg)
        msg = "Taking a single holiday. Remaining vacation days: 24"
        self.employee_4.take_holiday()
        self.assertLogs(msg)
        msg = "Taking a payout vacation, 5 days. Remaining vacation days: 20"
        self.employee_4.take_holiday(5, True)
        self.assertLogs(msg)

    def test_get_ceos(self):
        self.assertEqual(self.firma.get_ceos(), ['Andrii Merkulov', 'Otto Fancent'])

    def test_get_managers(self):
        self.assertEqual(self.firma.get_managers(), ['Gramatton Clerick'])

    def test_get_developers(self):
        self.assertEqual(self.firma.get_developers(), ['Serhii Mazur'])

    def test_pay(self):
        self.assertEqual(self.firma.pay(self.employee_1), 6000.0)
        self.assertEqual(self.firma.pay(self.employee_3), 22500.0)

    def test_pay_all(self):
        self.assertEqual(self.firma.pay_all(), 48500.0)



if __name__ == "__main__":
    unittest.main()