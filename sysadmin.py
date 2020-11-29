import os
def new_user():
    confirm = "N"
    while confirm != "Y":
        username = str(input("Please enter the name of the user to add: "))
        print("Use the username '" + username + "'? (Y/N)")
        confirm = str(input("")).upper()
        #os.system("sudo adduser " + username)
        print("a new user " + username + " have been added to the system")


new_user()