"""
Дуже продвинута система управління співробітниками

"""

import logging
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


@dataclass
class Employee:
    """Основна репрезентація працівника

    :first_name: Ім'я працівника
    :last_name: Прізвище працівника
    :role: посада працівника

    """

    first_name: str
    last_name: str
    role: str

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"


@dataclass
class HourlyEmployee(Employee):
    """Клас представляє працівників, які отримують погодинну оплату

    hours_worked: Загальна кількість відпрацьованих години
    hourly_rate: Оплата за годину

    """

    hours_worked: int = 0
    hourly_rate: float = 50.0

    def log_work(self, hours: int) -> None:
        """Журнал робочих годин

        hours: кількість відпрацьованих годин

        """

        self.hours_worked += hours


@dataclass
class SalariedEmployee(Employee):
    """Клас представляє працівників, які отримують щомісячний оклад

    salary: Оплата за місяць
    vacation_days: Кількість днів відпустки

    """

    salary: float
    vacation_days: int = 0

    def take_holiday(self, requested_days: int = 1, payout: bool = False) -> None:
        """Метод для надання працівникові відпустки

        requested_days: Кількість днів відпустки які  хоче взяти співробітник
        payout: Оплачувана відпустка чи ні

        """
        if self.vacation_days < requested_days:
            msg = f"{self.fullname} have not enough vacation days. Remaining days: {self.vacation_days}. Requested: {requested_days}"
            logger.error(msg)
            return
        self.vacation_days -= requested_days
        if payout:
            msg = f"Taking a payout vacation, {requested_days} days. Remaining vacation days: {self.vacation_days}"
        else:
            msg = f"Taking a single holiday. Remaining vacation days: {self.vacation_days}"
        logger.info(msg)


# noinspection PyTypeChecker
@dataclass
class Company:
    """Репрезентація компанії

    title: Назва компанії
    employees: Список працівників компанії

    """

    title: str
    employees: list[Employee]

    def get_employees_by_role(self, role: str) -> list[Employee]:
        """Список співробітників із певною посадою

        role: Посда співробітника

        """

        result = []
        for employee in self.employees:
            if employee.role.lower() == role.lower():
                result.append(employee.fullname)
        return result

    @staticmethod
    def pay(employee: Employee) -> float:
        """Оплата працівнику

        employee: Працівник

        """

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
        """Заробітна плата всім працівникам цієї компанії"""

        total_pay = 0
        for employee in self.employees:
            total_pay += self.pay(employee)
        msg = (
                  "The total payment to all employees is: $%.2f"
              ) % total_pay
        logger.info(msg)
        return total_pay


if __name__ == '__main__':
    ...

