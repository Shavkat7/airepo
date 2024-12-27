class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __repr__(self):
        return f"Employee(ID: {self.employee_id}, Name: {self.name}, Position: {self.position}, Salary: {self.salary})"


class Employee_Manager:
    def __init__(self):
        self.filename = "employees_list.txt"
    
    def _read_all_employees(self):
        try:
            with open(self.filename, "r") as file:
                content = file.readlines()
            employees = []
            for line in content:
                line_parts = line.strip().split(", ")
                if len(line_parts) == 4:
                    emp_id = int(line_parts[0])
                    name = line_parts[1]
                    position = line_parts[2]
                    salary = int(line_parts[3])
                    employees.append(Employee(emp_id, name, position, salary))
            return employees
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return []

    def _write_all_employees(self, employees):
        try:
            with open(self.filename, "w") as file:
                for employee in employees:
                    file.write(f"{employee.employee_id}, {employee.name}, {employee.position}, {employee.salary}\n")
        except Exception as e:
            print(f"Error occurred while writing to file: {e}")

    def add_employee(self, emp_id, name, position, salary):
        employees = self._read_all_employees()
        
        # Check for unique employee ID
        for employee in employees:
            if employee.employee_id == emp_id:
                print(f"Error: Employee ID {emp_id} already exists!")
                return
        
        employee = Employee(emp_id, name, position, salary)
        employees.append(employee)
        self._write_all_employees(employees)
        print("Employee added successfully!")

    def view_all_employees(self, sort_by=None):
        employees = self._read_all_employees()
        
        # Sort employees by name or salary
        if sort_by == "name":
            employees.sort(key=lambda x: x.name)
        elif sort_by == "salary":
            employees.sort(key=lambda x: x.salary)

        if employees:
            print("Employee Records:")
            for employee in employees:
                print(employee)
        else:
            print("No employee records found.")

    def search_employee(self, emp_id):
        employees = self._read_all_employees()
        for employee in employees:
            if employee.employee_id == emp_id:
                print(f"Found: {employee}")
                return True
        print(f"The employee with ID {emp_id} is not found!")
        return False

    def update_employee(self, emp_id, new_name, new_position, new_salary):
        employees = self._read_all_employees()

        
        found = False
        for employee in employees:
            if employee.employee_id == emp_id:
                employee.name = new_name
                employee.position = new_position
                employee.salary = new_salary
                found = True
                break
        
        if not found:
            print(f"Cannot update: Employee with ID {emp_id} does not exist!")
            return
        
        self._write_all_employees(employees)
        print(f"Updated record: {emp_id}, {new_name}, {new_position}, {new_salary}")

    def delete_employee(self, emp_id):
        employees = self._read_all_employees()
        employees = [employee for employee in employees if employee.employee_id != emp_id]

        if len(employees) == len(self._read_all_employees()):
            print(f"The employee with ID {emp_id} is not found!")
        else:
            self._write_all_employees(employees)
            print(f"Employee with ID {emp_id} deleted successfully!")

    def exit(self):
        print("Exiting the program...")
        exit()


def main():
    manager = Employee_Manager()

    while True:
        print("\n1. Add new employee record")
        print("2. View all employee records")
        print("3. Search for an employee by Employee ID")
        print("4. Update an employee's information")
        print("5. Delete an employee record")
        print("6. Exit")
        
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                emp_id = int(input("Enter Employee ID: "))
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = int(input("Enter Salary: "))
                manager.add_employee(emp_id, name, position, salary)
            elif option == 2:
                sort_option = input("Sort by (name/salary)? (Leave empty for no sorting): ").strip().lower()
                if sort_option not in ["", "name", "salary"]:
                    print("Invalid sort option!")
                    continue
                manager.view_all_employees(sort_by=sort_option)
            elif option == 3:
                emp_id = int(input("Enter Employee ID to search: "))
                manager.search_employee(emp_id)
            elif option == 4:
                emp_id = int(input("Enter Employee ID to update: "))
                new_name = input("Enter new Name: ")
                new_position = input("Enter new Position: ")
                new_salary = int(input("Enter new Salary: "))
                manager.update_employee(emp_id, new_name, new_position, new_salary)
            elif option == 5:
                emp_id = int(input("Enter Employee ID to delete: "))
                manager.delete_employee(emp_id)
            elif option == 6:
                manager.exit()
            else:
                print("Invalid option! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input! Please enter a valid option.")

if __name__ == "__main__":
    main()
