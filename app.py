import hashlib

user_database = {}

def register_user():
    username = input("Enter your username: ")

    if username in user_database:
        print("Username already exists. Please choose a different one.")
        return

    password = input("Enter your password: ")

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user_database[username] = hashed_password

    print("Registration successful!")

def login_user():
    username = input("Enter your username: ")

    # Check if the username exists
    if username not in user_database:
        print("Username not found. Please register first.")
        return

    password = input("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Compare the entered password with the stored hashed password
    if hashed_password == user_database[username]:
        print("Login successful! Welcome, " + username)
        access_secured_page()
    else:
        print("Incorrect password. Login failed.")

def access_secured_page():
    print("This is the secured page. Only logged-in users can access this content.")

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
