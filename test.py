from system import *

#
# user_1 = Employee('Andrii', 'Godevening', 'CEO')
# user_2 = Employee('Ivan', 'Reacher', 'dev', 10)
# user_3 = Employee('Viva', 'Muhailova', 'manager', 1)
# user_4 = Employee('Esmeralda', 'Kuchma', 'CEO', 4)
# user_5 = Employee('Xena', 'Warrior', 'manager', 0)
# user_7 = Employee('Hercules', 'Weak', 'dev', 4)

# print(user_1.role)
# user_1.take_holiday(True)

# print(f"{user_2.fullname} >>> {user_2.take_holiday(True)}")
# print(f"{user_4.fullname} >>> {user_4.take_holiday(True)}")
# print(f"{user_3.fullname} >>> {user_3.take_holiday()}")
# print(f"{user_7.fullname} >>> {user_7.take_holiday()}")
# print(f"{user_5.fullname} >>> {user_5.take_holiday()}")

employee_1 = HourlyEmployee("Serhii", "Mazur", "developer", 100)
employee_2 = HourlyEmployee("Andrii", "Merkulov", "CEO", 12)
employee_3 = SalariedEmployee("Gramatton", "Clerick", "manager", 22500.0, 4)

firma = Company("ETA", [employee_1, employee_2, employee_3])

# print(firma.employees)
# print(firma.get_ceos())
# print(firma.get_managers())
# print(firma.get_developers())
# print(firma.pay(user_1))
# print(user_1.fullname)
print(firma.pay(employee_1))
print(firma.pay(employee_2))
print(firma.pay(employee_3))