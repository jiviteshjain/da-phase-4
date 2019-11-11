import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate

def print_query(query, con, cur):
    try:
        cur.execute(query)
        con.commit()
        result = cur.fetchall()
        
        if len(result) != 0:
            header = result[0].keys()
            rows =  [x.values() for x in result]
            print(tabulate(rows, header, tablefmt = 'grid'))

    except Exception as e:
        print("Error!")
        con.rollback()
        input("Press any key to continue")


def view_appeal(cur, con):

    print("1. View all appeals")
    print("2. View appeals by a prisoner")
    print("3. Go back")

    while(1):
        ch = input("Enter choice> ")
        if (ch == '1'):
            query = "select * from Appeals;"
            print_query(query, con, cur)
            break

        elif (ch == '2'):
            p_id = input("Enter Prisoner ID: ")
            query = "select * from Appeals where prisoner_id = " + p_id +";"
            print_query(query, con, cur)
            break

        elif(ch != '3'):
            print("Enter valid command")


def view_offence(cur, con):

    print("1. View Offences in a certain time frame")
    print("2. View Offences involving a particular prisoner")
    print("3. Go back")

    while(1):
        ch = input("Enter choice> ")
        if (ch == '1'):
            print("Format for DateTime: YYYY-MM-DD hh:mm:ss")
            d1 = input("Enter DateTime_begin: ")
            d2 = input("Enter DateTime_end: ")
            query = "select A.id, A.description, A.date_time, A.location, A.severity, B.guard_id, C.prisoner_id from Offences A, Incident_Guards B, Incident_Prisoners C where A.id = B.offence_id and A.id = C.offence_id and A.date_time between " + d1 " and "+ d2 + ";"
            print_query(query, con, cur)
            break

        elif (ch == '2'):
            p_id = input("Enter Prisoner ID: ")
            query = "select A.id, A.description, A.date_time, A.location, A.severity, B.guard_id, C.prisoner_id from Offences A, Incident_Guards B, Incident_Prisoners C where A.id = B.offence_id and A.id = C.offence_id and C.prisoner_id = %s;" %(p_id)
            print_query(query, con, cur)
            break

        elif(ch != '3'):
            print("Enter valid command")
   


def view_visits(cur, con):
    
    print("1. View Visits in a certain time frame")
    print("2. View Visits for a particular prisoner")
    print("3. Go back")

    while(1):
        ch = int(input("Enter choice> "))
        if (ch == 1):
            print("Format for DateTime: YYYY-MM-DD hh:mm:ss")
            d1 = input("Enter DateTime_begin\n")
            d2 = input("Enter DateTime_end\n")
            query = "select * from Visits where date_time BETWEEN %s and %s" %(d1, d2)
            print_query(query, con, cur)
            break

        elif (ch == 2):
            p_id = int(input("Enter Prisoner ID\n"))
            query = "select * from Visits where prisoner_id = %s" %(p_id)
            print_query(query, con, cur)
            break

        elif(ch != 3):
            print("Enter valid command")

def view_prisoner(cur, con):

    query = "select id as 'Prisoner ID', concat(first_name, middle_name, last_name) as 'Name' from Prisoners;"
    print_query(query, con, cur)

    print("1. View Prisoner report")
    print("2. Go back")

    while(1):
        ch = input("Enter choice> ")
        if (ch == '1'):
            p_id = input("Enter Prisoner ID: ")
            queries = ["select * from Prisoners where id = ", "select * from Visitors where prisoner_id = ", "select * from Emergency_Contacts where prisoner_id = ", "select * from Visits where prisoner_id = ", "select * from Appeals where prisoner_id = ", "select A.job_name from Jobs A, Assignment_Prisoners B where B.job_id = A.id and B.prisoner_id = ", "select crime from Crimes where prisoner_id = ", "select * from Offences A, Incident_Prisoners B where A.id = B.offence_id and B.prisoner_id = "]
            for i in queries:
                query = i + p_id + ";"    
                print_query(query, con, cur)
            
            #input()
            break

        elif(ch != '2'):
            print("Enter valid command")

        else:
            break

def view_job(cur, con):
    query = "select * from Jobs;"
    print_query(query, con, cur)

    print("1. View Job report")
    print("2. Go back")

    while(1):
        ch = input("Enter choice> ")
        if (ch == '1'):
            j_id = input("Enter Job ID\n")
            queries = ["select * from Jobs where id = ", "select prisoner_id from Jobs where job_id = ", "select guard_id from Jobs where job_id = "]
            
            for i in queries:
                query = i + j_id + ";"
                print_query(query, con, cur)
            
            break

        elif(ch != 2):
            print("Enter valid command")



def view_staff(cur, con):
    query = "select id as 'Staff_ID', concat(first_name, middle_name, last_name), sex, post as 'Name' from Jobs;"
    print_query(query, con, cur)

    print("1. View Staff report")
    print("2. Go back")

    while(1):
        ch = input("Enter choice> ")
        if (ch == '1'):
            s_id = input("Enter Staff ID: ")
            f =
            query = "select * from Prison_Staff where id = " + s_id + ";"
            print_query(query, con, cur)
            query = "select shift, wing, supervisor_id from Guards where id = " + s_id + ";"
            print_query(query, con, cur)
            break

        elif(ch != '2'):
            print("Enter valid command")





