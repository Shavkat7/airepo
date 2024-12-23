
    # USE ONCE TO CREATE A FILE    
# with open("employees.txt", "w") as file:
#     file.write("")



print("1. Add new employee record\n\
2. View all employee records\n\
3. Search for an employee by Employee ID\n\
4. Update an employee's information\n\
5. Delete an employee record\n\
6. Exit")

a = int(input("Choose number between 1 to 6: "))

match a:
    case 1:

        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter full name: ")
        position = input("Enter position: ")
        salary = int(input("Enter salary: "))

        try:
            with open("lesson-6/homework/employees.txt", "a") as file:
                file.write(f"{emp_id}, {name}, {position}, {salary}")
                file.write("\n")
                print("Employee record added successfully!")
        except:
            print("Error occured")

        
    case 2:
        try:
            with open("lesson-6/homework/employees.txt") as file:
                print(file.read())
        except FileNotFoundError as e:
            print(e)
    case 3:
        to_search_emp_id = int(input("Enter employee's ID you want to find: "))
        found = False
        with open("lesson-6/homework/employees.txt") as file:
            for line in file:
                line1 = line.split(",")
                if int(line1[0]) == to_search_emp_id:
                    print(line)
                    found = True
                    break
            if not found:
                print(f"The employee with {to_search_emp_id} ID is not found!")

    case 4:
        to_update_emp_id = int(input("Enter employee's ID you want to update: "))
        found = False

        # store all lines
        with open("lesson-6/homework/employees.txt", "r") as filecha:
            content = filecha.readlines()

        
        for i, line in enumerate(content):
            line1 = line.strip().split(",")
            if int(line1[0]) == to_update_emp_id:
                found = True

                new_name = input("Enter new name: ")
                new_position = input("Enter new position: ")
                new_salary = int(input("Enter new salary: "))

                content[i] = f"{to_update_emp_id}, {new_name}, {new_position}, {new_salary}\n"
                break

        if found:
            with open("lesson-6/homework/employees.txt", "w") as file:
                file.writelines(content)
            print(f"Updated record is: {content[i].strip()}")
        else:
            print(f"The employee with ID {to_update_emp_id} is not found!")

    case 5:
        to_delete_emp_id = int(input("Enter employee's ID you want to delete: "))
        with open("lesson-6/homework/employees.txt") as file:
            content = file.readlines()
        
        with open("lesson-6/homework/employees.txt", "w") as file:
            for line in content:
                if not line:
                    continue
                line1 = line.split(",")
                if int(line1[0]) != to_delete_emp_id:
                    file.write(f"{line}\n")                               
    case 6:
        exit()