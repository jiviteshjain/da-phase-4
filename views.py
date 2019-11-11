import subprocess as sp
import pymysql
import pymysql.cursors

def print_table(results, cur):
    widths = []
    columns = []
    tavnit = '|'
    separator = '+' 

    for cd in cur.description:
        widths.append(max(cd[2], len(cd[0])))
        columns.append(cd[0])

    for w in widths:
        tavnit += " %-"+"%ss |" % (w,)
        separator += '-'*w + '--+'

    print(separator)
    print(tavnit % tuple(columns))
    print(separator)
    for row in results:
        print(tavnit % row)
    print(separator)


def view_appeal(cur, con):
    print("1. View all appeals")
    print("2. View appeals by a prisoner")
    print("3. Go back")

    while(1):
        ch = int(input("Enter choice> "))
        if (ch == 1):
            query = "select * from Appeals;"
            cur.execute(query)
            con.commit()
            results = cur.fetchall()
            print_table(results, cur)
            break

        elif (ch == 2):
            p_id = int(input("Enter Prisoner ID\n"))
            query = "select * from Appeals where prisoner_id = %d" %(p_id)
            cur.execute(query)
            con.commit()
            results = cur.fetchall()
            print_table(results, cur)
            break

        elif(ch != 3):
            print("Enter valid command")
    

def view_offence(cur, con):

    print("1. View Offences in a certain time frame")
    print("2. View Offences involving a particular prisoner")
    print("3. Go back")

    while(1):
        ch = int(input("Enter choice> "))
        if (ch == 1):
            print("Format for DateTime: YYYY-MM-DD hh:mm:ss")
            d1 = input("Enter DateTime_begin\n")
            d2 = input("Enter DateTime_end\n")
            query = "select A.id, A.description, A.date_time, A.location, A.severity, B.guard_id, C.prisoner_id from Offences A, Incident_Guards B, Incident_Prisoners C where A.id = B.offence_id and A.id = C.offence_id and A.date_time between d1 and d2;"
            cur.execute(query)
            con.commit()
            break

        elif (ch == 2):
            p_id = int(input("Enter Prisoner ID\n"))
            query = "select A.id, A.description, A.date_time, A.location, A.severity, B.guard_id, C.prisoner_id from Offences A, Incident_Guards B, Incident_Prisoners C where A.id = B.offence_id and A.id = C.offence_id and C.prisoner_id = %d;" %(p_id)
            cur.execute(query)
            con.commit()
            break

        elif(ch != 3):
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
            cur.execute(query)
            con.commit()
            break

        elif (ch == 2):
            p_id = int(input("Enter Prisoner ID\n"))
            query = "select * from Visits where prisoner_id = %d" %(p_id)
            cur.execute(query)
            con.commit()
            break

        elif(ch != 3):
            print("Enter valid command")

def view_prisoner(cur, con):

    query = "select id as 'Prisoner ID', concat(first_name, middle_name, last_name) as 'Name' from Prisoners;"
    cur.execute(query)
    con.commit()

    print("1. View Prisoner report")
    print("2. Go back")

    while(1):
        ch = int(input("Enter choice> "))
        if (ch == 1):
            p_id = int(input("Enter Prisoner ID\n"))
            query = "select * from Prisoners; select * from Visitors where prisoner_id = %d; select * from Emergency_Contacts where prisoner_id = %d; select * from Visits where prisoner_id = %d; select * from Appeals where prionser_id = %d; select A.job_name from Jobs A, Assignment_Prisoners B where B.job_id = A.id and B.prisoner_id = %d; select crimes from Crimes where prisoner_id = %d; select * from Offences A, Incident_Prisoners B where A.id = B.offence_id and B.prisoner_id = %d;" %(p_id, p_id, p_id, p_id, p_id, p_id, p_id)
            cur.execute(query)
            con.commit()
            break

        elif(ch != 2):
            print("Enter valid command")



def view_job(cur, con):
    query = "select * from Jobs;"
    cur.execute(query)
    con.commit()

    print("1. View Job report")
    print("2. Go back")

    while(1):
        ch = int(input("Enter choice> "))
        if (ch == 1):
            j_id = int(input("Enter Job ID\n"))
            query = "select * from Jobs where id = %d; select prisoner_id from Jobs where job_id = %d; select guard_id from Jobs where job_id = %d;" %(j_id, j_id, j_id)
            cur.execute(query)
            con.commit()
            break

        elif(ch != 2):
            print("Enter valid command")



def view_staff(cur, con):
    query = "select id as 'Staff_ID', concat(first_name, middle_name, last_name), sex, post as 'Name' from Jobs;"
    cur.execute(query)
    con.commit()

    print("1. View Staff report")
    print("2. Go back")

    while(1):
        ch = int(input("Enter choice> "))
        if (ch == 1):
            s_id = int(input("Enter Staff ID\n"))
            query = "select * from Jobs where id = %d; select prisoner_id from Jobs where job_id = %d; select guard_id from Jobs where job_id = %d;" %(j_id, j_id, j_id)
            cur.execute(query)
            con.commit()
            break

        elif(ch != 2):
            print("Enter valid command")





