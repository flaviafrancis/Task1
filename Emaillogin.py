import re
import os.path
def check_email(email):
    if re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Za-z]{2,}\b', email):
        print("Valid Email")
        return 1
    else:
        print("Invalid Email")

def check_passd(pswd):
    reg = re.compile(r'^[A-Za-z0-9@#$]{5,9}$')

    mat = re.match(reg, pswd)

    if mat:
        print(f"{pswd} is a valid password.")
        return 1
    else:
        print("Please check password requirements")

def output_file(email):
    login_info = {}
    for line in open("C:\Lincoln\myfile.txt", "r").readlines():
        login_info = line.split()
        if email == login_info[0]:
                print("inside output_file function"+login_info[1])
def login():
    email = input("Enter email: ")
    pswd = input('Please enter your password: ')
    flag=4
    for line in open("C:\Lincoln\myfile.txt", "r").readlines():
        login_info = line.split()
        if email == login_info[0] and pswd==login_info[1]:
                print("logged in successfully")
                flag=5
    if flag==4:
        print("User doesnot exits Please register")
        register()

def register():
    print("Register")
    flag1 = 0
    flag2 = 0
    email = input("Enter email: ")
  #  regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Za-z]{2,}\b'
    flag1 = check_email(email)
    pswd = input('Please enter your password: ')
    flag2 = check_passd(pswd)

    if flag1 == 1 and flag2 == 1:
        file_exists = os.path.exists('C:\Lincoln\myfile.txt')
        if (file_exists == False):
            file1 = open("C:\Lincoln\myfile.txt", "x")
        else:
            file1 = open("C:\Lincoln\myfile.txt", "a")
            for line in open("C:\Lincoln\myfile.txt", "r").readlines():
                login_info = line.split()
                if email == login_info[0]:
                    print("Existing username")
                    if pswd==login_info[1]:
                        print("user already exists please login ")
                        login()
                        return
                    else:
                        print("password forgotten")
                        forgotpassd()
                        return

            file1.write(email + " " + pswd + "\n")
        file1.close()

def forgotpassd():
    email= input("Enter the existing email")
    flag=1
    for line in open("C:\Lincoln\myfile.txt", "r").readlines():
        login_info = line.split()
        if(email == login_info[0]):
                print("your password is "+login_info[1])
                flag=2
    if(flag==1):
        print("User doesnot exits  Please register")
        register()


def switch(n):
    if n==1:
        register()
    if n==2:
        login()
    if n==3:
        forgotpassd()

print("press 1 to register or 2 to login or 3 for forgot password")
n=0
n= int(input())
switch(n)
#if(login_flag==0):
 #   register()
#else:
 #   if(login_flag==2):
  #      print("password forgotten")
   #     email= input("Enter the existing email")
    #    output_file(email)

