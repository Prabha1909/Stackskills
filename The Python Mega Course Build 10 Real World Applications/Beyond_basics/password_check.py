correct_password = "qwerty"

input_password = input("Please enter the password to continue: ")

while input_password != correct_password:
    input_password = input("Wrong password! try again")

print("Logged in")