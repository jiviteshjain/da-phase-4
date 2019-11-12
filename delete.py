def delete_prisoner(cur, con):
    try:
        print("Enter ID of prisoner you want to delete")
        id = int(input())
        query = "delete from Prisoners where id = %d ;" % (id)
        cur.execute(query)
        con.commit()
        print("Deleted prisoner")
        input("Press any key to continue")


    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")
    return


def delete_job(cur, con):
    try:
        print("Enter ID of job you want to delete")
        id = int(input())
        query = "delete from Jobs where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted job")
        input("Press any key to continue")


    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")

    return


def delete_staff(cur, con):
    try:
        print("Enter ID of the staff member you want to delete")
        id = int(input())
        query = "delete from Prison_Staff where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted staff member")
        input("Press any key to continue")


    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")

    return


def delete_offence(cur, con):
    try:
        print("Enter ID of the offence you want to delete")
        id = int(input())
        query = "delete from Offences where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted offence")
        input("Press any key to continue")


    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")

    return

def delete_appeal(cur, con):
    try:
        print("Enter ID of the appeal you want to delete")
        id = int(input())
        query = "delete from Appeals where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted appeal")
        input("Press any key to continue")


    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")

    return

def delete_visit(cur, con):
    try:
        print("Enter ID of the visit you want to delete")
        id = int(input())
        query = "delete from Visits where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted visit")
        input("Press any key to continue")


    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
        input("Press any key to continue")

    return

