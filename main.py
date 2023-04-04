import smtplib
import random
import os
from pathlib import Path

number = random.randint(100000,999999)

with open("codes.txt", "a") as g:
        g.write(str(number))
        g.write("\n")

def checking():
    global number
    with open('codes.txt') as myfile:
         if str(number) in myfile.read():
             number = random.randint(100000,999999)
             checking()
checking()
def login():
    global yes
    global username
    global the_email_man
    global password

    yes = 0
    try:
        username = input("Whats your username: ")
        if not username:
            login()
        with open('username.txt', 'r') as myfile:
            if str(username) in myfile.read():
                yes+=1
            else:
                checkForLogOrReg()
        the_email_man = input("Whats your email: ")
        if not the_email_man:
            login()
        with open('email.txt', 'r') as myfile:
            if str(the_email_man) in myfile.read():
                yes+=1
            else:
                checkForLogOrReg()
        password = input("Whats you pasword: ")
        if not password:
            login()
        with open('password.txt', 'r') as myfile:
            if str(password) in myfile.read():
                yes+=1
            else:
                checkForLogOrReg()
    except:
        checkForLogOrReg()
            
    if yes == 3:
        print("yey u got in")
    else:
        print("what")
        checkForLogOrReg()
    
def finishregister():
    check = input("Please enter the passcode: ")
    if check == str(number):
        with open('username.txt', "w") as myfile:
            myfile.write(username)
        with open('email.txt', "w") as myfile:
            myfile.write(the_email_man)
        with open('password.txt', "w") as myfile:
            myfile.write(str(password))
        login()
    else:
        print("That is incorrect")
        input()
        checkForLogOrReg()


def checkemail():
    global username
    global the_email_man
    global password
    input()
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(open(Path('passwords/email.txt')).read(), open(Path('passwords/password.txt')).read())

        subject = "Verify yout email"
        body = "Your passcode is: "+str(number)+"\nPlease use this number to verify your email."

        msg = f"Subject: {subject}\n\n{body}"

        #try:
        smtp.sendmail(open(Path('passwords/email.txt')).read(), the_email_man, msg)
        finishregister()
        #except:
        #    print("That is not a valid email")
        #    checkForLogOrReg()
    

def register():
    global username
    global the_email_man
    global g
    global password
    if os.path.isfile("username.txt") == True:
        os.remove("username.txt")
        os.remove("email.txt")
        os.remove("password.txt")
    username = input("What would you like your username to be: ")
    the_email_man = input("What would you like your email to be: ")
    password = input("What would you like your password to be: ")
    checkemail()

def checkForLogOrReg():
    global l_or_r
    global g
    l_or_r = input("Are you login in or registering (login or register)")

    if l_or_r == "login":
        login()
    elif l_or_r == "register":
        register()
    else:
        print("You did not input a valid response.")
        checkForLogOrReg()

checkForLogOrReg()

