shekels = float(input("Enter amount in shekels→"))
rate = float(input("Enter the exchange rate (shekels to dollars)→"))
dollars = shekels / rate
print(f"The amount in dollars is {dollars:.2f}")

first_number = float(input("Enter the first number→"))
second_number = float(input("Enter the second number→"))
subtraction  = first_number - second_number
print(f"The result is {subtraction:.2f}")

hours_worked = float(input("Enter hours worked→"))
hourly_wage = float(input("Enter hourly wage→"))
tax_rate = float(input("Enter tax rate (as a percentage)→")) / 100
salary_after_tax = hours_worked * hourly_wage * (1 - tax_rate)
bonus_percentage = float(input("Enter bonus percentage (as a percentage)→")) / 100
bonus_after_tax = hours_worked * hourly_wage * bonus_percentage * (1 - tax_rate)
salary_after_tax_with_bonus = salary_after_tax + bonus_after_tax
print(f"The salary after tax is {salary_after_tax:.2f} NIS")
print(f"The salary with bonus is {salary_after_tax_with_bonus:.2f} NIS")
