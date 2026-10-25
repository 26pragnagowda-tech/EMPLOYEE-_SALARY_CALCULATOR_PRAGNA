# Employee Salary Calculator

# Configurable salary rules
SALARY_RULES = {
    "hra_rate": 0.20,       # 20% of basic salary
    "da_rate": 0.10,        # 10% of basic salary
    "pf_rate": 0.12,        # 12% of basic salary
    "tax_rate": 0.05        # 5% of gross salary
}


def calculate_salary(basic_salary):
    hra = basic_salary * SALARY_RULES["hra_rate"]
    da = basic_salary * SALARY_RULES["da_rate"]

    gross_salary = basic_salary + hra + da

    pf = basic_salary * SALARY_RULES["pf_rate"]
    tax = gross_salary * SALARY_RULES["tax_rate"]

    total_deductions = pf + tax
    net_salary = gross_salary - total_deductions

    return {
        "Basic Salary": basic_salary,
        "HRA": hra,
        "DA": da,
        "Gross Salary": gross_salary,
        "PF": pf,
        "Tax": tax,
        "Total Deductions": total_deductions,
        "Net Salary": net_salary
    }


def display_salary(employee):
    salary = calculate_salary(employee["basic_salary"])

    print("\n========== SALARY SLIP ==========")
    print("Employee ID:", employee["employee_id"])
    print("Employee Name:", employee["name"])

    for item, amount in salary.items():
        print(f"{item}: Rs. {amount:,.2f}")

    print("=================================")


# Sample employee records
employees = [
    {
        "employee_id": 101,
        "name": "Rahul",
        "basic_salary": 30000
    },
    {
        "employee_id": 102,
        "name": "Priya",
        "basic_salary": 40000
    },
    {
        "employee_id": 103,
        "name": "Kiran",
        "basic_salary": 25000
    }
]


def main():
    print("EMPLOYEE SALARY CALCULATOR")
    print("1. View sample employee salaries")
    print("2. Calculate salary for a new employee")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        for employee in employees:
            display_salary(employee)

    elif choice == "2":
        name = input("Enter employee name: ").strip()
        employee_id = input("Enter employee ID: ").strip()

        if not name or not employee_id:
            print("Error: Name and employee ID cannot be empty.")
            return

        try:
            basic_salary = float(input("Enter basic salary: "))

            if basic_salary <= 0:
                print("Error: Salary must be greater than zero.")
                return

        except ValueError:
            print("Error: Please enter a valid numeric salary.")
            return

        employee = {
            "employee_id": employee_id,
            "name": name,
            "basic_salary": basic_salary
        }

        display_salary(employee)

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
