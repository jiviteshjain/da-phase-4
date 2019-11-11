import subprocess as sp
import pymysql
import pymysql.cursors

from datetime import datetime


def update_prisoner(cur, con):
    attr = {}
    print("Enter the id of the prisoner whose details you want to update")
    id = int(input())
    prisoner_details = ["Name", "Sex", "DOB", "Height", "Weight", "Blood Group",
                        "Medical History", "Arrival date", "Sentence", "Cell", "Wing", "Security level"]
    print("Enter the number beside the attribute you want to update")
    i = 0
    while i < len(prisoner_details):
        i += 1
        print(str(i) + ". " + prisoner_details[i-1])
    ch = int(input("Enter choice> "))
    if(ch == 1):
        name = input('Name*: ').split(' ')
        if len(name) >= 3:
            attr['first_name'] = name[0];
            attr['middle_name'] = ' '.join(name[1:-1])
            attr['last_name'] = name[-1]
        elif len(name) == 2:
            attr['first_name'] = name[0]
            attr['middle_name'] = ''
            attr['last_name'] = name[1]
        elif len(name) == 1:
            attr['first_name'] = name[0]
            attr['middle_name'] = ''
            attr['last_name'] = ''
        else:
            print('Error: Please enter the prisoner\'s name')
            return
        query = "update Prisoners set first_name = '%s', middle_name = '%s', last_name = '%s' where id = %d;" % (attr["first_name"],attr["middle_name"],attr["last_name"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return

    if(ch == 2):
        attr['sex'] = input('Sex (M, F, OTHER)*: ') 
        query = "update Prisoners set sex = '%s' where id = %d;" % (attr["sex"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    
    if(ch == 3):
        attr['dob'] = input('Date as YYYY-MM-DD: ')  # date: checked by mysql
        query = "update Prisoners set dob = '%s' where id = %d;" % (attr["dob"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    if(ch == 4):
        attr['height'] = input('Height: ') # float: handled by mysql
        query = "update Prisoners set height = '%s' where id = %d;" % (attr["height"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    if(ch == 5):
        attr['weight'] = input('Weight: ') # float: handled by mysql
        query = "update Prisoners set weight = '%s' where id = %d;" % (attr["weight"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    if(ch == 6):
        attr['blood_group'] = input('Blood group: ') # enum: handled by mysql
        query = "update Prisoners set blood_group = '%s' where id = %d;" % (attr["blood_group"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    if(ch == 7):
        attr['medical_history'] = input('Medical History: ') # empty string
        query = "update Prisoners set medical_history = '%s' where id = %d;" % (attr["medical_history"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return    
    if(ch == 8):
        attr['arrival_date'] = input('Arrival Date* (Press enter for today\'s date): ')
        if attr['arrival_date'] == '':
            attr['arrival_date'] = datetime.now().strftime('%Y-%m-%d')
        query = "update Prisoners set arrival_date = '%s' where id = %d;" % (attr["arrival_date"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    if(ch == 9):
        attr['sentence'] = input('Sentence*: ')
        if attr['sentence'] == '':
            print('Please enter the sentence details')
            return
        query = "update Prisoners set sentence = '%s' where id = %d;" % (attr["sentence"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    if(ch == 10):
        attr['cell'] = input('Cell*: ')
        try:
            int(attr['cell'])
        except NameError:
            print('Please enter a cell number between 1 and 999')
            return
        if int(attr['cell']) < 1 or int(attr['cell']) > 999:
            print('Please enter a cell number between 1 and 999')
            return
        query = "update Prisoners set cell = %d where id = %d;" % (attr["cell"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    if(ch == 11):
        attr['wing'] = input('Wing*: ')
        if len(attr['wing']) != 1 or not attr['wing'].isupper():
            print('Please enter a wing from A to Z')
            return
        query = "update Prisoners set wing = '%s' where id = %d;" % (attr["wing"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    if(ch == 12):
        attr['security_level'] = input('Security level*: ')
        if attr['security_level'] not in ('LOW', 'MEDIUM', 'HIGH'):
            print('Please choose a security level out of LOW, MEDIUM or HIGH')
            return
        query = "update Prisoners set security_level = '%s' where id = %d;" % (attr["security_level"],id)
        try:
            cur.execute(query)
            print("Updated details")
        except Exception as e:
            print("Failed to update")
            con.rollback()
            print(e)
            input('Press any key to continue. ')
            return
    else:
        print("Enter a choice from the given ones")
        input("Press any key to continue. ")
        return
    
    try:
        con.commit()
        print('Success')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return
