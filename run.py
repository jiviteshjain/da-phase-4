import subprocess as sp
import pymysql
import pymysql.cursors

tables = ["Prisoners", "Jobs", "Staff", "Offences", "Appeals", "Emergency Contacts", "Visitors", "Visits"]

def add_display():

    print("Add to the table:")
    i = 0
    
    while i < len(tables):
        i+=1       
        print(str(i) + ". " + tables[i])
    
    ch = int(input("Enter choice> "))



def update_display():
    print("Update the table:")
    i = 0
    
    while i < len(tables):
        i+=1       
        print(str(i) + ". " + tables[i])
    
    ch = int(input("Enter choice> "))

def delete_display():
    print("Delete from the table:")
    i = 0
    while i < len(tables):
        i+=1       
        print(str(i) + ". " + tables[i])
    
    ch = int(input("Enter choice> "))

def view_display():
    print("View the table:")
    i = 0
    
    while i < len(tables):
        i+=1       
        print(str(i) + ". " + tables[i])
    
    ch = int(input("Enter choice> "))

    return

def dispatch(ch):

    if(ch == 1): 
        add_display()
    elif(ch == 2):
        update_display()
    elif(ch == 3):
        delete_display()
    elif(ch == 4):
        view_display()
    else:
        print("Error: Invalid Option")

while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='Prison',
                cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear',shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")
        tmp = input("Enter any key to CONTINUE>")

        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Add")
                print("2. Update")
                print("3. Delete")
                print("4. View")
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                printf("yee")
                if ch == 5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")


    except:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
    
   
