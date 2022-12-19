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
    """Basic employee representation"""

    first_name: str
    last_name: str
    role: str


    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"



# noinspection PyTypeChecker
@dataclass
class HourlyEmployee(Employee):
    """Represents employees who are paid on worked hours base"""

    hours_worked: int = 0
    hourly_rate: float = 50.0


    def log_work(self, hours: int) -> None:
        """Log working hours"""

        self.hours_worked += hours


# noinspection PyTypeChecker
@dataclass
class SalariedEmployee(Employee):
    """Represents employees who are paid on a monthly salary base"""

    salary: float
    vacation_days: int = 0

    def _check_vacation_days(self, requested_days: int) -> None:
        if self.vacation_days < requested_days:
            msg = f"{self.fullname} have not enough vacation days. Remaining days: {self.vacation_days}. Requested: {requested_days}"
            raise ValueError(msg)

    def take_holiday(self, requested_days: int = 1, payout: bool = False) -> None:
        self._check_vacation_days(requested_days)
        self.vacation_days -= requested_days
        if payout:
            msg = f"Taking a payout vacation, {requested_days} days. Remaining vacation days: {self.vacation_days}"
        else:
            msg = f"Taking a single holiday. Remaining vacation days: {self.vacation_days}"
        logger.info(msg)


# noinspection PyTypeChecker
@dataclass
class Company:
    """A company representation"""

    title: str
    employees: list[Employee]

    def get_employees_by_role(self, role: str) -> list[Employee]:
        """Return employees list with specific role"""

        result = []
        for employee in self.employees:
            if employee.role.lower() == role.lower():
                result.append(employee.fullname)
        return result

    @staticmethod
    def pay(employee: Employee) -> float:
        """Pay to employee"""

        if isinstance(employee, SalariedEmployee):
            msg = (
                "Paying monthly salary of $%.2f to %s."
            ) % (employee.salary, employee.fullname)
            logger.info(msg)
            return employee.salary

        if isinstance(employee, HourlyEmployee):
            paying = employee.hourly_rate * employee.hours_worked
            msg = (
                "Paying %s hourly rate of %.2f for %i hours is $%.2f."
            ) % (employee.fullname, employee.hourly_rate, employee.hours_worked, paying)
            logger.info(msg)
            return paying

    def pay_all(self) -> None:
        """Pay all the employees in this company"""

        total_pay = 0
        for employee in self.employees:
            total_pay += self.pay(employee)
        msg = (
                  "The total payment to all employees is: $%.2f"
              ) % total_pay
        logger.info(msg)
        return total_pay


if __name__ == "__main__":
    ...
