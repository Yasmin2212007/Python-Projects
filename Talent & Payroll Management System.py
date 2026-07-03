
def calculate_bonus(base_salary, performance_rating):
    if performance_rating == 5:
        return base_salary * 0.20

    elif performance_rating in [3, 4]:
        return base_salary * 0.10

    else:
        return 0


def calculate_tax(gross_salary):
    if gross_salary > 7000:
        return gross_salary * 0.15

    elif 3000 <= gross_salary <= 7000:
        return gross_salary * 0.10

    else:
        return 0


def main_hr_app():
    print("=" * 50)
    print(" Corporate Talent & Payroll Management System ")
    print("=" * 50)

    employee_name = input("Enter Employee Name: ").strip().title()
    department = input("Enter Department: ").strip().title()

    base_salary = float(input("Enter Base Salary: "))
    while base_salary < 0:
        print("Salary cannot be negative.")
        base_salary = float(input("Enter Base Salary Again: "))

    performance_rating = int(input("Enter Performance Rating (1-5): "))
    while performance_rating not in range(1, 6):
        print("Rating must be between 1 and 5.")
        performance_rating = int(input("Enter Performance Rating Again: "))

    bonus = calculate_bonus(base_salary, performance_rating)

    gross_salary = base_salary + bonus

    tax = calculate_tax(gross_salary)

    net_salary = gross_salary - tax

    print("=" * 50)
    print("Employee Payroll Summary")
    print("=" * 50)
    print(f"Employee Name      : {employee_name}")
    print(f"Department         : {department}")
    print(f"Base Salary        : {base_salary:.2f}")
    print(f"Performance Rating : {performance_rating}")
    print(f"Bonus              : {bonus:.2f}")
    print(f"Gross Salary       : {gross_salary:.2f}")
    print(f"Tax Deduction      : {tax:.2f}")
    print(f"Net Salary         : {net_salary:.2f}")
    print("=" * 50)


main_hr_app()

