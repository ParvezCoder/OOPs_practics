class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def show_details(self):
        print(f"Employee ID: {self.emp_id}, Name: {self.name}")

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []  # Aggregation: list of Employee objects

    def add_employee(self, employee):
        self.employees.append(employee)  # Referencing existing Employee object

    def show_department(self):
        print(f"\nDepartment: {self.dept_name}")
        print("Employees:")
        for emp in self.employees:
            emp.show_details()

# Creating Employee objects independently
e1 = Employee(101, "Alice")
e2 = Employee(102, "Bob")

# Creating a Department and adding existing Employee objects
hr_dept = Department("Human Resources")
hr_dept.add_employee(e1)
hr_dept.add_employee(e2)

# Showing department details
hr_dept.show_department()

# Employees still exist independently
print(f"\nAccessing employee directly: {e1.name}")  # Alice
