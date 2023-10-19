import os

if(not(os.path.exists("User.Txt"))):
    myfile = open("User.txt","a")
    myfile.close()

    
def addUser():
    username = input("Enter username: ")
    password = input("Enter pasword: ")
    value = (username + "," + password + ",")
    myfile = open("User.txt","a")
    myfile.write(value)
    myfile.close()

def viewUser():
    myfile = open("User.txt", "r")
    contents = myfile.read()
    user = contents.split("-")
    for x in range(len(user)-1):
        mysplit = x.split(",")
        uname = mysplit[0]
        password = mysplit[1]
        print(uname + "/" + password)
def Contactnamenum():
    Cnumber = input("Input contact number: ")
    Cname = input("Input contact name: ")
    value = (Cnumber + "/" + Cname)
    myfile = open("User.txt", "c")
    myfile.write(Cname)
    myfile.close()
    
    

def main():
    print("[1] Add user")
    print("[2] View user")
    print("[3] Add contact number and name: ")
    print("[x] Exit")

    choice = input("Please select an option: ").lower()
    if choice == '1':
        addUser()
    
    elif choice == '2':
        viewUser()
    
    elif choice == '3':
        Cname()
        
    
    elif choice == 'x':
        print("The program has ended")
        exit()

    
    else:
        print("You input an invalid option!")
main()

    


