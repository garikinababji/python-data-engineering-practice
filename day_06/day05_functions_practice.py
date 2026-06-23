def calculate_bonus(salary):
    if salary >= 50000:
        return salary * 0.10
    else:
        return salary * 0.05

print(calculate_bonus(60000))
print(calculate_bonus(30000))
