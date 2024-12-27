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
    
    def add_employee(self, emp_id, name, position, salary):
        employee = Employee(emp_id, name, position, salary)
        try:
            with open(self.filename, "a") as file:
                file.write(f"{employee.employee_id}, {employee.name}, {employee.position}, {employee.salary}\n")
                print("Employee added successfully!")
        except Exception as e:
            print(f"Error occurred: {e}")

    def view_all_employees(self):
        try:
            with open(self.filename) as file:
                print("Employee Records:")
                print(file.read())
        except FileNotFoundError as e:
            print(f"File not found: {e}")

    def search_employee(self, emp_id):
        try:
            with open(self.filename) as file:
                for line in file:
                    line_parts = line.strip().split(", ")
                    if int(line_parts[0]) == emp_id:
                        print(f"Found: {line.strip()}")
                        return True
            print(f"The employee with ID {emp_id} is not found!")
            return False
        except FileNotFoundError as e:
            print(f"File not found: {e}")
            return False

    def update_employee(self, emp_id, new_name, new_position, new_salary):
        if not self.search_employee(emp_id):
            print(f"Cannot update: Employee with ID {emp_id} does not exist!")
            return

        try:
            with open(self.filename, "r") as file:
                content = file.readlines()

            updated = False
            with open(self.filename, "w") as file:
                for line in content:
                    line_parts = line.strip().split(", ")
                    if int(line_parts[0]) == emp_id:
                        file.write(f"{emp_id}, {new_name}, {new_position}, {new_salary}\n")
                        updated = True
                        print(f"Updated record: {emp_id}, {new_name}, {new_position}, {new_salary}")
                    else:
                        file.write(line)

            if not updated:
                print(f"Error: Employee with ID {emp_id} was not updated.")
        except FileNotFoundError as e:
            print(f"File not found: {e}")

    def delete_employee(self, emp_id):
        try:
            with open(self.filename, "r") as file:
                content = file.readlines()

            with open(self.filename, "w") as file:
                deleted = False
                for line in content:
                    line_parts = line.strip().split(", ")
                    if int(line_parts[0]) != emp_id:
                        file.write(line)
                    else:
                        deleted = True
                if deleted:
                    print(f"Employee with ID {emp_id} deleted successfully!")
                else:
                    print(f"The employee with ID {emp_id} is not found!")
        except FileNotFoundError as e:
            print(f"File not found: {e}")

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
                manager.view_all_employees()
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
