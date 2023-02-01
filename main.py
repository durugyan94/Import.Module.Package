from application.salary import calculate_salary
import application.db.people as p
from datetime import datetime as dt


# оклад
salary = 69000
# будет премия: да/любой символ
bonus = "да"
res = 0


if __name__ == '__main__':

    now = dt.now()

    print(f"""
        Зарплата сотрудника {p.get_employees()}, составляет {calculate_salary(salary,bonus)} руб.
        Дата отчета: {now.day}.{now.month}.{now.year}г.
        """)