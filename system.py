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

    amount: int = 0
    hourly_rate: float = 50.0


    def log_work(self, hours: int) -> None:
        """Log working hours"""

        self.amount += hours


# noinspection PyTypeChecker
@dataclass
class SalariedEmployee(Employee):
    """Represents employees who are paid on a monthly salary base"""

    salary: float
    vacation_days: int

    def take_holiday(self, requested_days: int = 1, payout: bool = False) -> None:
        """Take a single holiday or a payout vacation"""

        if payout:
            if self.vacation_days < requested_days:
                msg = f"{self} have not enough vacation days. " \
                      f"Remaining days: %d. Requested: %d" % (self.vacation_days, requested_days)
                raise ValueError(msg)
            self.vacation_days -= requested_days
            msg = "Taking a payout vacation, %d days. Remaining vacation days: %d" % (requested_days, self.vacation_days)
            logger.info(msg)
        else:
            if self.vacation_days < 1:
                msg = f"{self} have not enough vacation days. " \
                      f"Remaining days: %d. Requested: %d" % (self.vacation_days, 1)
                raise ValueError(msg)
            self.vacation_days -= 1
            msg = "Taking a single holiday. Remaining vacation days: %d" % self.vacation_days
            logger.info(msg)


# noinspection PyTypeChecker
@dataclass
class Company:
    """A company representation"""

    title: str
    employees: list[Employee]

    def get_ceos(self) -> list[Employee]:
        """Return employees list with role of CEO"""

        result = []
        for employee in self.employees:
            if employee.role.lower() == "ceo":
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
            if employee.role.lower() == "developer":
                result.append(employee)
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
            paying = employee.hourly_rate * employee.amount
            msg = (
                "Paying %s hourly rate of %.2f for %i hours is $%.2f."
            ) % (employee.fullname, employee.hourly_rate, employee.amount, paying)
            logger.info(msg)
            return paying

    def pay_all(self) -> None:
        """Pay all the employees in this company"""

        # TODO: implement this method

if __name__ == "__main__":
    worker = HourlyEmployee("Serhii", "Mazur", "developer", 10)
    worker2 = HourlyEmployee("Jon", "Snow", "CEO", 15, 100.0)
    worker3 = HourlyEmployee("Boba", "Fett", "manager", 6, 35.0)
    worker4 = SalariedEmployee("Jib", "Ridl", "manager", 5000.0, 35)
    worker5 = SalariedEmployee("Rahim", "Azir", "ceo", 2500.0, 4)
    worker6 = SalariedEmployee("Raja", "Safyr", "Developer", 3500.0, 22)

    worker_list = [worker, worker2, worker3, worker4, worker5, worker6]

    com = Company("PapaZi", worker_list)
    print(com.pay(worker4))