uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
weak = True

while weak:
    password = input("Enter password: ")

  
    if len(password) < 8:
        print("Password is too short")
        continue


    req = any(char in uppercase for char in password)

    if req:
        print("Password is strong.")
        weak = False
    else:
        print("Password must contain at least one uppercase letter.")
