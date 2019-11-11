def delete_prisoner(con, cur):
    try:
        print("Enter ID of prisoner you want to delete")
        id = int(input())
        query = "delete from Prisoners where id = %d ;" % (id)
        cur.execute(query)
        con.commit()
        print("Deleted prisoner")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return


def delete_job(con, cur):
    try:
        print("Enter ID of job you want to delete")
        id = int(input())
        query = "delete from Jobs where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted job")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return


def delete_staff(con, cur):
    try:
        print("Enter ID of the staff member you want to delete")
        id = int(input())
        query = "delete from Prison_Staff where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted staff member")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return


def delete_offence(con, cur):
    try:
        print("Enter ID of the offence you want to delete")
        id = int(input())
        query = "delete from Offences where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted offence")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return

def delete_appeal(con, cur):
    try:
        print("Enter ID of the appeal you want to delete")
        id = int(input())
        query = "delete from Appeals where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted appeal")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return

def delete_visit(con, cur):
    try:
        print("Enter ID of the visit you want to delete")
        id = int(input())
        query = "delete from Visits where id = %d ; " % (id)
        cur.execute(query)
        con.commit()
        print("Deleted visit")

    except Exception as e:
        con.rollback()
        print("Failed to delete from database")
        print(">>>>>>>>>>>>>", e)
    return

