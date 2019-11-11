import subprocess as sp
import pymysql
import pymysql.cursors

from datetime import datetime

def expand_keys(d):
    s = ''
    for key in d.keys():
        s = s + key + ', '

    if s[-2:] == ', ':
        return s[:-2]
    return s

def quote(s):
    if s == 'NULL':
        return s
    else:
        return '"' + s + '"'

def empty_to_null(s):
    if s == '':
        return 'NULL'
    else:
        return s

def add_prisoner(cur, con):
    attr = {}
    print('Enter details of the new inmate:')
    
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

    attr['sex'] = input('Sex (M, F, OTHER)*: ') # enum: checked by mysql
    attr['dob'] = empty_to_null(input('Date of birth as YYYY-MM-DD: '))  # date: checked by mysql
    
    attr['height'] = input('Height: ') # float: handled by mysql
    attr['weight'] = input('Weight: ') # float: handled by mysql
    attr['blood_group'] = input('Blood group: ') # enum: handled by mysql
    
    attr['medical_history'] = empty_to_null(input('Medical History: '))  # empty string
    
    attr['arrival_date'] = input('Arrival Date* (Press enter for today\'s date): ')
    if attr['arrival_date'] == '':
        attr['arrival_date'] = datetime.now().strftime('%Y-%m-%d')
    
    attr['sentence'] = input('Sentence*: ')
    if attr['sentence'] == '':
        print('Please enter the sentence details')
        return

    attr['cell'] = input('Cell*: ')
    if not attr['cell'].isnumeric() or not len(attr['cell']) == 3:
        print('Please enter a cell number between 001 and 999')
        return

    attr['wing'] = input('Wing*: ')
    if len(attr['wing']) != 1 or not attr['wing'].isupper():
        print('Please enter a wing from A to Z')
        return

    attr['security_level'] = input('Security level*: ')
    if attr['security_level'] not in ('LOW', 'MEDIUM', 'HIGH'):
        print('Please choose a security level out of LOW, MEDIUM or HIGH')
        return

    crimes = input('Crimes as a comma separated list*: ')
    crimes = crimes.split(',')
    crimes = [x.strip() for x in crimes]
    crimes = set(crimes)
    if len(crimes) == 0:
        print('Please enter atleast one crime')
        return

    query_str = f'INSERT INTO Prison.Prisoners({expand_keys(attr)}) VALUES(\
        "{attr["first_name"]}",\
        "{attr["middle_name"]}",\
        "{attr["last_name"]}",\
        "{attr["sex"]}",\
        {quote(attr["dob"])},\
        {attr["height"]},\
        {attr["weight"]},\
        "{attr["blood_group"]}",\
        {quote(attr["medical_history"])},\
        "{attr["arrival_date"]}",\
        "{attr["sentence"]}",\
        "{attr["cell"]}",\
        "{attr["wing"]}",\
        "{attr["security_level"]}"\
    ); '
    # print(query_str)
    try:
        cur.execute(query_str)
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return

    prisoner_id = cur.lastrowid
    for crime in crimes:
        query_str = f'INSERT INTO Prison.Crimes VALUES(\
            {prisoner_id},\
            "{crime}"\
        ); '
        try:
            cur.execute(query_str)
        except Exception as e:
            print('Failed to insert into the database.')
            con.rollback()
            print(e)
            input('Press any key to continue.')
            return

    try:
        con.commit()
        print('The new inmate hase been successfully entered into the system.')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return

def add_visitor(cur, con):
    prisoner_id = input('Enter the prisoner\'s ID: ')
    attr = {}
    print('Enter details of the visitor:')

    name = input('Name*: ').split(' ')
    if len(name) >= 3:
        attr['first_name'] = name[0]
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
        print('Error: Please enter the visitor\'s name')
        return

    attr['relationship'] = empty_to_null(input('Relationship: '))

    attr['address'] = empty_to_null(input('Address: '))

    attr['phone'] = input('Phone: ')
    if attr['phone'] == '':
        attr['phone'] = 'NULL'
    elif not len(attr['phone']) == 10 or not attr['phone'].isnumeric():
        print('Please enter a valid 10 digit phone number')
        return

    query_str = f'INSERT INTO Prison.Visitors VALUES(\
        {prisoner_id}, \
        "{attr["first_name"]}",\
        "{attr["middle_name"]}",\
        "{attr["last_name"]}",\
        {quote(attr["relationship"])},\
        {quote(attr["address"])},\
        {quote(attr["phone"])}\
    );'
    
    try:
        cur.execute(query_str)
        con.commit()
        print('The new visitor has been successfully entered into the system.')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')

def add_emergency_contact(cur, con):
    prisoner_id = input('Enter the prisoner\'s ID: ')
    attr = {}
    print('Enter details of the contact:')

    name = input('Name*: ').split(' ')
    if len(name) >= 3:
        attr['first_name'] = name[0]
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
        print('Error: Please enter the contact\'s name')
        return

    attr['relationship'] = empty_to_null(input('Relationship: '))

    attr['address'] = input('Address: ')
    if attr['address'] == '':
        print('Error: Please enter a valid adress')
        return

    attr['phone'] = input('Phone: ')
    if not len(attr['phone']) == 10 or not attr['phone'].isnumeric():
        print('Please enter a valid 10 digit phone number')
        return

    query_str = f'INSERT INTO Prison.Emergency_Contacts VALUES(\
        {prisoner_id}, \
        "{attr["first_name"]}",\
        "{attr["middle_name"]}",\
        "{attr["last_name"]}",\
        {quote(attr["relationship"])},\
        "{attr["address"]}",\
        "{attr["phone"]}"\
    );'

    try:
        cur.execute(query_str)
        con.commit()
        print('The new contact has been successfully entered into the system.')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')

def add_appeal(cur, con):
    prisoner_id = input('Enter the prisoner\'s ID: ')
    attr = {}

    attr['filing_date'] = input('Filing Date* (Press enter for today\'s date): ')
    if attr['filing_date'] == '':
        attr['filing_date'] = datetime.now().strftime('%Y-%m-%d')

    attr['hearing_date'] = empty_to_null(input('Hearing Date: ')) # can be null

    attr['status'] = input('Status:* ')  # enum and not null: checked by mysql
    
    query_str = f'INSERT INTO Prison.Appeals({expand_keys(attr)}, prisoner_id) VALUES(\
        "{attr["filing_date"]}",\
        {quote(attr["hearing_date"])},\
        "{attr["status"]}",\
        {prisoner_id}\
    ); '
    
    try:
        cur.execute(query_str)
        con.commit()
        print('The appeal has been successfully entered into the system.')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')

def add_prison_staff(cur, con):
    attr = {}
    print('Enter details of the new employee:')

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

    attr['dob'] = empty_to_null(input('Date of birth as YYYY-MM-DD: '))  # date: checked by mysql
    attr['sex'] = input('Sex (M, F, OTHER)*: ')  # enum: checked by mysql
    attr['address'] = empty_to_null(input('Address: '))

    attr['phone'] = input('Phone: ')
    if attr['phone'] == '':
        attr['phone'] = 'NULL'
    elif not len(attr['phone']) == 10 or not attr['phone'].isnumeric():
        print('Please enter a valid 10 digit phone number')
        return

    attr['post'] = input('Post*: ')  # non nullable enum: handled by mysql
    attr['salary'] = input('Salary*: ')  # non nullable float: handled by mysql

    query_str = f'INSERT INTO Prison.Staff({expand_keys(attr)}) VALUES(\
        "{attr["first_name"]}",\
        "{attr["middle_name"]}",\
        "{attr["last_name"]}",\
        {quote(attr["dob"])},\
        "{attr["sex"]}",\
            
    );'
    
