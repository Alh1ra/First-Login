# Python program to make first steps

'''     Targets:
            - Ask for user name:
                - check in login.py (module) if name is correct
                - if user name is not Alhira, increment counter in login.py
                  and give proper output.
                - if user name is Alhira, ask for a random number and a random
                  food type. Save both variables in login.py.
'''
##        Message from future self: "Oh, you fool."


import sqlite3

con = sqlite3.connect('example.db')
cursor = con.cursor()

print("")
print("Database successfully loaded!")

print("")
print(" - - - ")
print("")

# a warm welcome
print("Hello, user.")

# asking for your user name
login_attempt = input("Please enter your name: ")

print("")
print("Hello,", login_attempt)

# fetch data and provide for future use; note that 'RandonNumber' simply got lazily reused
cursor.execute("SELECT FailedLogins, RandomNumber FROM UserData WHERE Username=?", [login_attempt])
for row in cursor:
    failed_logins = row[0]
    random_number = row[1]

login_user = login_attempt

# asking for RandomNumber; substitute for password
login_number = int(input("Please enter your randomly chosen number for ID verification: "))
print("")

# if-else; on fail a counter in the database get incremented by 1
if random_number == login_number:
    print("Credentials correct. There were a total of", failed_logins, "failed logins since your last visit.")
    print("")
    input("What can I do for you?")
else:
    print("Credentials incorrect. Please wait patiently for your incarceration.")
    cursor.execute("UPDATE UserData SET FailedLogins = FailedLogins + 1 WHERE Username=?", [login_user])
    con.commit()
    input()
    exit()

'''     AAR
HOLY SHIT! 15 hours for this piece of code. But i learned a lot along the way. (One time i stared
an hour onto the screen trying to figure out why one of my lines was always printed twice. It was
a duplicate db entry.

Targets shifted as i realized that using a simple database would be the best way to go forward.
Thus the login with (basically) a password was created in the process. Yes i obviously cut it a bit
short but i already had the next thing in my mind. Which this project was a stepping stone into.
'''
