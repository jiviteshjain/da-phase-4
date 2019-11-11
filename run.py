import subprocess as sp
import pymysql
import pymysql.cursors

from add import add_prisoner

tables = ["Prisoners", "Jobs", "Staff", "Offences", "Appeals", "Visits", "Go back"]

def add_display():

    print("Add to the table:")
    i = 0
    
    while i < len(tables):
        i+=1       
        print(str(i) + ". " + tables[i-1])
    
    ch = int(input("Enter choice> "))
    if(ch == 1):
        add_prisoner(cur, con)
    
    # elif(ch == 2):
    #     add_job(cur, con)
    
    # elif(ch==3):
    #     add_staff(cur, con)
    
    # elif(ch==4):
    #     add_offence(cur, con)
    
    # elif(ch == 5):
    #     add_appeal(cur, con)

    # elif(ch == 6):
    #     add_visit(cur, con)

    elif(ch!=7):
        print("Enter valid value!")
        

def update_display():
    print("Update the table:")
    i = 0
    
    while i < len(tables):
        i+=1       
        print(str(i) + ". " + tables[i])
    
    ch = int(input("Enter choice> "))
    if(ch == 1):
        update_prisoner(cur, con)
    
    elif(ch == 2):
        update_job(cur, con)
    
    elif(ch==3):
        update_prisoner(cur, con)
    
    elif(ch == 2):
        update_job(cur, con)
    
    elif(ch==3):
        update_staff(cur, con)
    
    elif(ch==4):
        update_offence(cur, con)
    
    elif(ch == 5):
        update_appeal(cur, con)
        update_staff(cur, con)
    
    elif(ch==4):
        update_offence(cur, con)
    
    elif(ch == 5):
        update_appeal(cur, con)
    
    elif(ch == 6):
        update_visit(cur, con)

    elif(ch!=7):
        print("Enter valid value!")
        

def delete_display():
    print("Delete from the table:")
    i = 0
    while i < len(tables):
        i+=1       
        print(str(i) + ". " + tables[i])
    
    ch = int(input("Enter choice> "))

    if(ch == 1):
        delete_prisoner(cur, con)
    
    elif(ch == 2):
        delete_job(cur, con)
    
    elif(ch==3):
        delete_staff(cur, con)
    
    elif(ch==4):
        delete_offence(cur, con)
    
    elif(ch == 5):
        delete_appeal(cur, con)
    
    elif(ch == 6):
        delete_visit(cur, con)

    elif(ch!=7):
        print("Enter valid value!")

def view_display():
    print("View the table:")
    i = 0
    
    while i < len(tables):
        i+=1       
        print(str(i) + ". " + tables[i])
    
    ch = int(input("Enter choice> "))

    if(ch == 1):
        view_prisoner(cur, con)
    
    elif(ch == 2):
        view_job(cur, con)
    
    elif(ch==3):
        view_staff(cur, con)
    
    elif(ch==4):
        view_offence(cur, con)
    
    elif(ch == 5):
        view_appeal(cur, con)
    
    elif(ch == 6):
        view_visits(cur, con)
    
    elif(ch!=7):
        print("Enter valid value!")
        
    return

def dispatch(ch):

    if(ch == 1): 
        add_display()
    # elif(ch == 2):
    #     update_display()
    # elif(ch == 3):
    #     delete_display()
    # elif(ch == 4):
    #     view_display()
    else:
        print("Error: Invalid Option")

while True:
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
            input("Press any key to continue.")
        else:
            print("Failed to connect")
            input("Press any key to continue.")
            continue;
        
        with con:
            cur = con.cursor()
            while True:
                tmp = sp.call('clear',shell=True)
                print("1. Add")
                print("2. Update")
                print("3. Delete")
                print("4. View")
                print("5. Logout")
                print("6. Exit")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear',shell=True)
                
                if ch == 5:
                    break
                elif ch == 6:
                    raise SystemExit;
                else:
                    dispatch(ch)
                    input("Press any key to continue.")


    except Exception as e:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        print(e)
        input("Press any key to continue.")
    
   
