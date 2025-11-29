employee = {}

def add_employee(emp_id, name, age, department, salary):
    if emp_id in employee :
        print("This Employee_ID is already exist")

    else :
        employee[emp_id] = {"Name":name, "Age":age, "Department":department, "Salary":salary}
        print("The Employee Information added successfully")

def display():
    for emp_id, data in employee.items():
        print(f"Employee ID :{emp_id}, Name :{data['Name']}, Age :{data['Age']}. Department :{data['Department']}, Salary :{data['Salary']}")
    print()



def search(emp_id):
    if emp_id in employee :
        print(f"Employee ID :{emp_id}")
        print(f"Name :{employee[emp_id]['Name']}")
        print(f"Age :{employee[emp_id]['Age']}")
        print(f"Department :{employee[emp_id]['Department']}")
        print(f"Salary :{employee[emp_id]['Salary']}")

    else :
        print("Employee Not Found")

print("Menu")
print("1. Add Employee")
print("2. View All Employee")
print("3. Search For Employee")
print("4. Exit")
print("Enter the number between 1-4")

while True:
    choice = int(input("Enter the number between 1-4 :"))

    if choice == 1:
        emp_id = int(input("Enter The ID of Employee :"))
        name = input("Enter the Name of Employee :")
        age = int(input("Enter the Age of Employee :"))
        department = input("Enter the Department of the Employee :")
        salary = int(input("Enter the Salary of Employee :"))
        add_employee(emp_id, name, age, department,salary)

    elif choice == 2:
        display()

    elif choice == 3:
        search_id = int(input("Enter the ID which you want to search :"))
        if search_id in employee:
            search(search_id)

        else :
            print("ID Not Found")

    elif choice == 4:
        print("bye,System is going to close")
        break

    else :
        print("Invalid No")
