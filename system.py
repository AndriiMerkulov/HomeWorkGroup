"""
A very advanced employee management system

"""

import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# noinspection PyTypeChecker
@dataclass
class Employee:
    """ Це клас Працівники, тут ми створюємо об'єкти які будуть нашими працівниками.

    :first_name: Ім'я працівника
    :last_name: Прізвище працівника
    :role: посада працівника
    :vacation_days: кількість не використаної відпустки

    """

    first_name: str
    last_name: str
    role: str
    vacation_days: int = 25

    @property
    def fullname(self):
        """Return the full name of the employee"""
        return self.first_name, self.last_name

    def __repr__(self) -> str:
        """Return a string version of an instance"""
        return f"{self.fullname}"

    def take_holiday(self, payout: bool = False) -> None:
        """ Метод інформує, скільки днів оплачуваної відпустки можна взяти,
            а також скільки неоплачуваної.
            В параметри можна передати True або False
        """

        remaining = self.vacation_days
        if payout:
            if self.vacation_days < 5:
                msg = f"{self} have not enough vacation days. " \
                      f"Remaining days: {remaining}. Requested: {5}"
                return msg
                # raise ValueError(msg)
            else:
                self.vacation_days -= 5
                msg = f"Taking a holiday. Remaining vacation days: {remaining}"
                return msg
                # logger.info(msg)
        else:
            if self.vacation_days < 1:
                remaining = self.vacation_days
                msg = f"{self} have not enough vacation days. " \
                      f"Remaining days: {remaining}. Requested: {1}"
                # raise ValueError(msg)
                return msg
            else:
                self.vacation_days -= 1
                msg = f"Taking a payout. Remaining vacation days: {remaining}"
                return msg
                # logger.info(msg)


# noinspection PyTypeChecker
@dataclass
class HourlyEmployee(Employee):
    """Працівники у яких погодинна оплата праці"""

    amount: int = 0
    hourly_rate: int = 50

    def log_work(self, hours: int) -> None:
        """Log working hours"""

        self.amount += hours


# noinspection PyTypeChecker
@dataclass
class SalariedEmployee(Employee):
    """Ставка працівника на місяць, значення стале"""

    salary: int = 5000


@dataclass
class Company:
    """A company representation"""

    title: str
    employees: list[Employee]

    def get_ceos(self) -> list[Employee]:
        """Return employees list with role of CEO"""

        result = []
        for employee in self.employees:
            if employee.role == "CEO":
                result.append(employee)
        return result

    def get_managers(self) -> list[Employee]:
        """Return employees list with role of manager"""

        result = []
        for employee in self.employees:
            if employee.role == "manager":
                result.append(employee)
        return result

    def get_developers(self) -> list[Employee]:
        """Return employees list with role of developer"""

        result = []
        for employee in self.employees:
            if employee.role == "dev":
                result.append(employee)
        return result

    @staticmethod
    def pay(employee: Employee) -> None:
        """ Рахує зарплату працівника """

        if isinstance(employee, SalariedEmployee):
            msg = (
                      "Paying monthly salary of %.2f to %s"
                  ) % (employee.salary, employee)
            logger.info(f"Paying monthly salary to {employee}")
            logger.info(msg)

        if isinstance(employee, HourlyEmployee):
            msg = (
                      "Paying %s hourly rate of %.2f for %d hours"
                  ) % (employee, employee.hourly_rate, employee.amount)
            logger.info(msg)

    # цей метод треба доробити
    def pay_all(self) -> None:
        """Pay all the employees in this company"""
