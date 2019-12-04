#
# Script that will perform API calls based on the user's input
#
import api_functions as functions, getpass as gp, sys, time

print("\n***********************************************")
print("*************** Check Point API ***************")
print("***********************************************\n")

sid = None
login_attempts = 0
# Presents login screen until the login is successful or fails 3 times
while(sid is None):
    if(login_attempts >= 0 and login_attempts < 3):
        login_attempts += 1
    else:
        print("You have exceeded your login attempts")
        print("Goodbye")
        time.sleep(5)
        sys.exit()

    mgmt_ip = raw_input("Please enter the Management IP Address: ")
    user = raw_input("Username: ")
    password = gp.getpass()
    print("\n")
    sid = functions.login(user, password, mgmt_ip)
    if(sid is None):
        print("The information you have entered is incorrect.\n")

exit = 0
first_iteration = 1

while(exit == 0):
    if(first_iteration == 1):
        print("Welcome " + user)
    
    print("Configuration Options:")
    print("----------------------")
    print("(1)\tAdd Host")
    print("(2)\tDelete Host")
    print("(3)\tAdd Network")
    print("(4)\tDelete Network")
    print("(5)\tPublish")
    print("(6)\tLogout\n")
    response = raw_input("Enter your choice number: ")

    if(response == '1'):
        name = raw_input("Enter Host Name: ")
        host_addr = raw_input("\nEnter Host IP Address: ")
        response = functions.add_host(name, host_addr, mgmt_ip, sid)

    if(response == '5'):
        functions.publish(mgmt_ip, sid)

    if(response == '6'):
        exit = 1

    first_iteration += 1
