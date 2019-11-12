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
        
        else:
            print("Empty!")

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

        else:
            break


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
            query = "select A.id, A.description, A.date_time, A.location, A.severity, B.guard_id, C.prisoner_id from Offences A, Incident_Guards B, Incident_Prisoners C where A.id = B.offence_id and A.id = C.offence_id and A.date_time between " + d1 +" and "+ d2 + ";"
            print_query(query, con, cur)
            break

        elif (ch == '2'):
            p_id = input("Enter Prisoner ID: ")
            print("\nOffences by the prisoner: ")
            query = "select A.id, A.description, A.date_time, A.location, A.severity from Offences A, Incident_Prisoners C where A.id = C.offence_id and C.prisoner_id = %s;" %(p_id)
            print_query(query, con, cur)
            break

        elif(ch != '3'):
            print("Enter valid command")

        else:
            break
   


def view_visits(cur, con):
    
    print("1. View Visits in a certain time frame")
    print("2. View Visits for a particular prisoner")
    print("3. Go back")

    while(1):
        ch = int(input("Enter choice> "))
        if (ch == 1):
            print("Format for DateTime: YYYY-MM-DD hh:mm:ss")
            d1 = input("Enter DateTime_begin: ")
            d2 = input("Enter DateTime_end: ")
            print(d1)
            query = "select * from Visits where date_time BETWEEN '" + d1 + "' and '"+ d2 +"';"
            print_query(query, con, cur)
            break

        elif (ch == 2):
            p_id = int(input("Enter Prisoner ID: "))
            query = "select * from Visits where prisoner_id = %s" %(p_id)
            print_query(query, con, cur)
            break

        elif(ch != 3):
            print("Enter valid command")

        else:
            break

def view_prisoner(cur, con):

    query = "select id as 'Prisoner ID', concat(first_name, middle_name, last_name) as 'Name' from Prisoners;"
    print_query(query, con, cur)

    print("1. View Prisoner report")
    print("2. Go back")

    while(1):
        ch = input("Enter choice> ")
        if (ch == '1'):
            p_id = input("Enter Prisoner ID: ")
            titles = ["Prisoner Details", "Visitors", "Emergency Contacts", "Visits involving the prisoner", "Appeals made by the prisoner", "Jobs the prisoner works","Crimes committed", "Offences prisoner committed", "Volatility Level"]
            queries = ["select * from Prisoners where id = ", "select * from Visitors where prisoner_id = ", "select * from Emergency_Contacts where prisoner_id = ", "select * from Visits where prisoner_id = ", "select * from Appeals where prisoner_id = ", "select A.job_name from Jobs A, Assignment_Prisoners B where B.job_id = A.id and B.prisoner_id = ", "select crime from Crimes where prisoner_id = ", "select * from Offences A, Incident_Prisoners B where A.id = B.offence_id and B.prisoner_id = ", "select count(*) as 'Volatility Level' from Incident_Prisoners where prisoner_id = "]
            i = 0
            while i < len(queries):
                print("\n"+titles[i])
                query = queries[i] + p_id + ";"    
                print_query(query, con, cur)
                i += 1
            
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
            j_id = input("Enter Job ID: ")
            titles = ["Job details", "Prisoners", "Guards"]
            queries = ["select * from Jobs where id = ", "select A.prisoner_id, concat(B.first_name, ' ', B.middle_name,' ', B.last_name) as 'Name' from Assignment_Prisoners A, Prisoners B where A.prisoner_id = B.id and job_id = ", "select A.guard_id, concat(B.first_name, ' ',B.middle_name,' ',  B.last_name) as 'Name'  from Assignment_Guards A, Prison_Staff B where B.id = A.guard_id and job_id = "]
            
            i = 0
            while i < len(queries):
                print("\n"+titles[i])
                query = queries[i] + j_id + ";"    
                print_query(query, con, cur)
                i += 1
            
            break

        elif(ch != 2):
            print("Enter valid command")
        
        else:
            break



def view_staff(cur, con):
    query = "select id as 'Staff_ID', concat(first_name, ' ', middle_name, ' ', last_name) as 'Name' , sex, post from Prison_Staff;"
    print_query(query, con, cur)

    print("1. View Staff report")
    print("2. Go back")

    while(1):
        ch = input("Enter choice> ")
        if (ch == '1'):
            s_id = input("Enter Staff ID: ")
            query = "select * from Prison_Staff where id = " + s_id + ";"
            print_query(query, con, cur)
            query = "select shift, wing, supervisor_id from Guards where id = " + s_id + ";"
            cur.execute(query)
            con.commit()
            result = cur.fetchall()

            if len(result)!=0:
                print("\nGuard Details: ")
                header = result[0].keys()
                rows =  [x.values() for x in result]
                print(tabulate(rows, header, tablefmt = 'grid'))
                print("\nWork Assignment duties: ")
                query = "select A.job_id, B.job_name from Assignment_Guards A, Jobs B where A.job_id = B.id and A.guard_id = " + s_id + ";"
                print_query(query, con, cur)
                print("\nOffences that occured during the guard's presence: ")
                query = "select A.offence_id, B.description from Incident_Guards A, Offences B where A.offence_id = B.id and A.guard_id = " + s_id + ";"
                print_query(query, con, cur)
            
            else:
                print("\nJobs the staff oversees: ")
                query = "select id as 'job_id', job_name from Jobs where supervisor_id = " + s_id + ";"
                print_query(query, con, cur)
            break

        elif(ch != '2'):
            print("Enter valid command")

        else:
            break





