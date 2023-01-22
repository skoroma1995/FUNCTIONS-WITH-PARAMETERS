employee_count = 0
total_hours = 0
total_gross_pay = 0
total_tax = 0
total_net_pay = 0

def get_employee_name():
    name = input("Enter the employee's name: ")
    return name

def get_total_hours():
    total_hours = input("Enter the employee's total hours: ")
    return total_hours

def get_hourly_rate():
    hourly_rate = input("Enter the employee's hourly rate: ")
    return hourly_rate

def get_tax_rate():
    tax_rate = input("Enter the employee's income tax rate: ")
    return tax_rate

def calculate_pay(total_hours, hourly_rate, tax_rate):
    gross_pay = float(total_hours) * float(hourly_rate)
    income_tax = gross_pay * float(tax_rate)
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_pay_info(employee_name, total_hours, hourly_rate, gross_pay, tax_rate, income_tax, net_pay):
    print("Employee name: ", employee_name)
    print("Total hours: ", total_hours)
    print("Hourly rate: ", hourly_rate)
    print("Gross pay: ", gross_pay)
    print("Income tax rate: ", tax_rate)
    print("Income tax: ", income_tax)
    print("Net pay: ", net_pay)

def display_summary():