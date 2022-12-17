from system import *

user_1 = Employee('Andrii', 'Godevening', 'CEO', 2)
user_2 = Employee('Ivan', 'Reacher', 'dev', 10)
user_3 = Employee('Viva', 'Muhailova', 'manager', 1)
user_4 = Employee('Esmeralda', 'Kuchma', 'CEO', 22)
user_5 = Employee('Xena', 'Warrior', 'manager', 0)
user_7 = Employee('Hercules', 'Weak', 'dev', 4)

# print(user_1.role)
# user_1.take_holiday(True)

print(f"{user_2.fullname} >>> {user_2.take_holiday(True)}")
print(f"{user_3.fullname} >>> {user_3.take_holiday()}")
print(f"{user_7.fullname} >>> {user_7.take_holiday()}")
print(f"{user_5.fullname} >>> {user_5.take_holiday()}")

firma = Company("ETA", [user_1, user_2, user_3, user_4, user_5, user_7])

# print(firma.employees)
# print(firma.get_ceos())
# print(firma.get_managers())
# print(firma.get_developers())
# print(firma.pay(user_1))
# print(user_1.fullname)
