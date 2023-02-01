def calculate_salary(salary, bonus):
    if bonus == "да":
        bonus = salary/2
    else:
        bonus = 0
    tax = (salary+bonus)*13/100
    res = salary+bonus-tax
    return res