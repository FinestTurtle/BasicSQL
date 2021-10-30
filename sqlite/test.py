import sqlite3

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 

def insert_employee(emp):
    with conn:
        curs.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay}) 

def get_emp_by_name(lastname):
    curs.execute("SELECT * FROM employees WHERE last = :last", {'last': lastname})
    return curs.fetchall()

def update_emp_pay(emp, new_pay):
    with conn:
        curs.execute("""UPDATE employees SET pay = :pay WHERE last = :last AND first = :first""", {
            'first': emp.first, 'last': emp.last, 'pay': new_pay
        })

def remove_emp(emp):
    with conn:
        curs.execute("DELETE FROM employees WHERE first = :first AND last = :last", {
            'first': emp.first, 'last': emp.last
        })

def view_database():
    curs.execute("SELECT * FROM employees")
    print(curs.fetchall())

conn = sqlite3.connect('employees.db')

curs = conn.cursor()

# curs.execute("""CREATE TABLE employees (
#                 first text,
#                 last text,
#                 pay integer
#                 )""")

# insert_employee(emp2)
# emps = get_emp_by_name('harris')
# print(emps)

def display():
    print('1) Add employee')
    print('2) Look up employee')
    print('3) Update employee pay')
    print('4) Remove employee')
    print('5) View employees')
    print('6) Quit')

while True:
    display()
    choice = input('> ')
    if choice == '1':
        first = input('First name: ')
        last = input('Last name: ')
        pay = input('Salary: ')
        emp = Employee(first, last, pay)
        insert_employee(emp)
##conn.close()

    elif choice == '2':
        last = input('Last name: ')
        print(get_emp_by_name(last))
        
    
    elif choice == '3':
        first = input('First name: ')
        last = input('Last name: ')
        new_pay = input('New Salary: ')
        emp = Employee(first, last, pay=0)
        update_emp_pay(emp, new_pay)
        
    elif choice == '4':
        first = input('First name: ')
        last = input('Last name: ')
        emp = Employee(first, last, 0)
        remove_emp(emp)
    
    elif choice == '5':
        view_database()

    else:
        break
