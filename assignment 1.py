class Employees:
    file = {}
    def __init__(self, enumber, ename, eaddress, esalary, emarried, count):
        self.emp_number = enumber
        self.emp_name = ename
        self.emp_address = eaddress
        self.emp_salary = esalary
        self.emp_married = emarried
        self.file[count] = {'Employee_name': emp_name, 'Emoloyee_number': emp_number, 'Employee_address': emp_address, 'Employee_salary': emp_salary, 'Employee_married': emp_married }

    
    def show_data(self):
        for i in self.file:
            print(self.file[i])

choice = 0
count = 1
while choice == 0:
        ##### Read employee data from keyboard  #####
    emp_number = input("Enter employee number: ")
    emp_name = input("Enter employee name : ")
    emp_address = input("Enter employee address : ")
    emp_salary =  int(input("Enter employee salary : "))
    emp_married = int(input('Enter 0 if unmarried and any other number if married: '))
    if emp_married == 0:
        emp_married = False
    else:
        emp_married = True
    count += 1
    choice = int(input('Enter 0 to continue and any other number to exit: '))

    a = Employees(emp_number, emp_name, emp_address, emp_salary, emp_married, count)

a.show_data()