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

    """

    first_name: str
    last_name: str
    role: str

    @property
    def fullname(self):
        """Return the full name of the employee"""
        return self.first_name, self.last_name

    def __repr__(self) -> str:
        """Return a string version of an instance"""
        return f"{self.fullname}"


# noinspection PyTypeChecker
@dataclass
class HourlyEmployee(Employee):
    """Працівники у яких погодинна оплата праці"""

    amount: int = 0
    hourly_rate: float = 50.0

    def log_work(self, hours: int) -> None:
        """Log working hours"""
        self.amount += hours


# noinspection PyTypeChecker
@dataclass
class SalariedEmployee(Employee):
    """Ставка працівника на місяць"""

    salary: float
    vacation_days: int

    def take_holiday(self, requested_days: int = 1, payout: bool = False) -> None:
        """ Метод інформує, скільки днів оплачуваної відпустки можна взяти,
            а також скільки неоплачуваної.
            В параметри можна передати True або False
        """

        if payout:
            if self.vacation_days < 5:
                msg = f"{self} have not enough vacation days. " \
                      f"Remaining days: {self.vacation_days}. Requested: {requested_days}"
                return msg
                # raise ValueError(msg)
            else:
                self.vacation_days -= requested_days
                msg = f"Taking a vocation. Remaining vacation days: {self.vacation_days}"
                return msg
                # logger.info(msg)
        else:
            if self.vacation_days < 1:
                msg = f"{self} have not enough vacation days. " \
                      f"Remaining days: {self.vacation_days}. Requested: {1}"
                # raise ValueError(msg)
                return msg
            else:
                self.vacation_days -= 1
                msg = f"Taking a payout. Remaining vacation days: {self.vacation_days}"
                return msg
                # logger.info(msg)

    def __repr__(self) -> str:
        """Return a string version of an instance"""
        return f"{self.fullname}"


@dataclass
class Company:
    """A company representation"""

    title: str
    employees: list[Employee]

    def get_ceos(self) -> list[Employee]:
        """Return employees list with role of CEO"""

        result = []
        for employee in self.employees:
            if employee.role.lower() == "CEO":
                result.append(employee)
        return result

    def get_managers(self) -> list[Employee]:
        """Return employees list with role of manager"""

        result = []
        for employee in self.employees:
            if employee.role.lower() == "manager":
                result.append(employee)
        return result

    def get_developers(self) -> list[Employee]:
        """Return employees list with role of developer"""

        result = []
        for employee in self.employees:
            if employee.role.lower() == "dev":
                result.append(employee)
        return result

    @staticmethod
    def pay(employee: Employee) -> float:
        """ Рахує зарплату працівника """

        if isinstance(employee, SalariedEmployee):
            msg = (
                      "Paying monthly salary of %.2f to %s"
                  ) % (employee.salary, employee.fullname)
            logger.info(f"Paying monthly salary to {employee}")
            logger.info(msg)
            return employee.salary

        if isinstance(employee, HourlyEmployee):
            paying = employee.hourly_rate * employee.amount
            msg = (
                      "Paying %s hourly rate of %.2f for %i hours is $%.2f"
                  ) % (employee.fullname, employee.hourly_rate, employee.amount,
                       paying)
            logger.info(msg)
            return paying

    # цей метод треба доробити
    def pay_all(self) -> float:
        """Pay all the employees in this company"""
        total_pay = 0
        for employee in self.employees:
            total_pay += Company.pay(employee)
        return total_pay
