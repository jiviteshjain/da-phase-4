def delete_prisoner(con, cur):
    try:
        print("Enter ID of prisoner you want to delete")
        id = int(input())
        query = "delete from Prisoners where id = %d ; delete from Crimes where prisoner_id = %d" % (
            id, id)
        cur.execute(query)
        con.commit()
        print("Deleted prisoner")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return


def delete_job(con, cur):
    try:
        print("Enter ID of job you want to delete")
        id = int(input())
        query = "delete from Jobs where id = %d ; delete from Assignment_Guards where job_id = %d ; delete from Assignment_Prisoners where job_id = %d" % (
            id, id, id)
        cur.execute(query)
        con.commit()
        print("Deleted job")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return

def delete_staff(con, cur):
    try:
        print("Enter ID of job you want to delete")
        id = int(input())
        query = "delete from Jobs where id = %d ; delete from Assignment_Guards where job_id = %d ; delete from Assignment_Prisoners where job_id = %d" % (
            id, id, id)
        cur.execute(query)
        con.commit()
        print("Deleted job")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)
    return
