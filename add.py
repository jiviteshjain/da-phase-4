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
        print('Error: Please enter the prisoner\'s name')
        return

    attr['sex'] = input('Sex (M, F, OTHER)*: ')  # enum: checked by mysql
    attr['dob'] = empty_to_null(
        input('Date of birth as YYYY-MM-DD: '))  # date: checked by mysql

    attr['height'] = input('Height: ')  # float: handled by mysql
    attr['weight'] = input('Weight: ')  # float: handled by mysql
    attr['blood_group'] = input('Blood group: ')  # enum: handled by mysql

    attr['medical_history'] = empty_to_null(
        input('Medical History: '))  # empty string

    attr['arrival_date'] = input(
        'Arrival Date* (Press enter for today\'s date): ')
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
    if crimes == '':
        print('Please enter atleast one crime')
        return
    crimes = crimes.split(',')
    crimes = [x.strip() for x in crimes]
    crimes = set(crimes)

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

    attr['filing_date'] = input(
        'Filing Date* (Press enter for today\'s date): ')
    if attr['filing_date'] == '':
        attr['filing_date'] = datetime.now().strftime('%Y-%m-%d')

    attr['hearing_date'] = empty_to_null(
        input('Hearing Date: '))  # can be null

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
        print('Error: Please enter the prisoner\'s name')
        return

    attr['dob'] = empty_to_null(
        input('Date of birth as YYYY-MM-DD: '))  # date: checked by mysql
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

    query_str = f'INSERT INTO Prison.Prison_Staff({expand_keys(attr)}) VALUES(\
        "{attr["first_name"]}",\
        "{attr["middle_name"]}",\
        "{attr["last_name"]}",\
        {quote(attr["dob"])},\
        "{attr["sex"]}",\
        {quote(attr["address"])},\
        {quote(attr["phone"])},\
        "{attr["post"]}",\
        {attr["salary"]}\
    );'

    if attr['post'] != 'GUARD':
        try:
            cur.execute(query_str)
            con.commit()
            print('The new employee has been successfully entered into the system.')
            input('Press any key to continue.')
            return
        except Exception as e:
            print('Failed to insert into the database.')
            con.rollback()
            print(e)
            input('Press any key to continue.')
            return

    # It is a guard

    try:
        cur.execute(query_str)
        # con.commit()
        # print('The new visitor has been successfully entered into the system.')
        # input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return

    staff_id = cur.lastrowid

    attr = {}

    attr['shift'] = empty_to_null(input("Shift: "))
    attr['wing'] = empty_to_null(input('Wing: '))
    if attr['wing'] != 'NULL':
        if len(attr['wing']) != 1 or not attr['wing'].isupper():
            print('Please enter a wing from A to Z')
            return

    attr['supervisor_id'] = empty_to_null(input('Supervisor\'s ID: '))

    query_str = f'INSERT INTO Guards VALUES(\
        {staff_id},\
        {quote(attr["shift"])},\
        {quote(attr["wing"])},\
        {quote(attr["supervisor_id"])}\
    );'

    try:
        cur.execute(query_str)
        con.commit()
        print('The new employee has been successfully entered into the system.')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')


def add_job(cur, con):
    attr = {}
    print('Enter details of the new job:')

    attr['job_name'] = input('Job name*: ')
    if attr['job_name'] == '':
        print('Error: Please enter a job name')
        return

    attr['working_hours_begin'] = empty_to_null(input('Start time: '))
    attr['working_hours_end'] = empty_to_null(input('End time: '))

    attr['supervisor_id'] = empty_to_null(input('Supervisor\'s ID: '))

    guards = input('Guard ID\'s as a comma separated list: ')
    if guards != '':
        guards = guards.split(',')
        guards = [x.strip() for x in guards]
        guards = set(guards)
    else:
        guards = set()

    prisoners = input('Prisoner ID\'s as a comma separated list*: ')
    if prisoners == '':
        print('Please enter atleast one prisoner')
        return
    prisoners = prisoners.split(',')
    prisoners = [x.strip() for x in prisoners]
    prisoners = set(prisoners)

    if attr['supervisor_id'] != 'NULL':
        try:
            query_str = f'SELECT post FROM Prison.Prison_Staff WHERE id = {attr["supervisor_id"]};'
            cur.execute(query_str)
            con.commit()
            result = cur.fetchall()
        except Exception as e:
            print('Error: Please enter a valid supervisor ID.')
            con.rollback()
            print(e)
            input('Press any key to continue.')
            return

        if len(result) == 0 or result[0]['post'] == 'GUARD':
            print(
                'Error: Please enter a valid supervisor ID, which does not belong to a guard.')
            input('Press any key to continue.')
            return

    query_str = f'INSERT INTO Prison.Jobs({expand_keys(attr)}) VALUES(\
        "{attr["job_name"]}",\
        {quote(attr["working_hours_begin"])},\
        {quote(attr["working_hours_end"])},\
        {attr["supervisor_id"]}\
    );'

    try:
        cur.execute(query_str)
        # con.commit()
        # print('The new visitor has been successfully entered into the system.')
        # input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return

    job_id = cur.lastrowid

    for guard in guards:
        query_str = f'INSERT INTO Prison.Assignment_Guards VALUES(\
            {job_id},\
            {guard}\
        );'
        try:
            cur.execute(query_str)
        except Exception as e:
            print('Failed to insert into the database.')
            con.rollback()
            print(e)
            input('Press any key to continue.')
            return

    for prisoner in prisoners:
        query_str = f'INSERT INTO Prison.Assignment_Prisoners VALUES(\
            {job_id},\
            {prisoner}\
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
        print('The new job hase been successfully entered into the system.')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return


def add_offence(cur, con):
    attr = {}
    print('Enter details of the incident:')

    attr['description'] = input('Description*: ')
    if attr['description'] == '':
        print('Error: Please enter a desciption.')
        return

    attr['date_time'] = input(
        'Date and time of incident as YYYY-MM-DD HH:MM* (Press enter for the current date and time): ')
    if attr['date_time'] == '':
        attr['date_time'] = datetime.now().strftime('%Y-%m-%d %H:%M')

    attr['location'] = input('Location*: ')
    if attr['location'] == '':
        print('Error: Please enter a valid location')
        return

    # non null enum, handled by database
    attr['severity'] = input('Severity* out of LOW, MEDIUM or HIGH: ')

    print('Recognised offence types: ASSAULT, ATTEMPTED ESCAPE, FELONY, RIOTS, CONTRABAND, DESTRUCTION OF PROPERTY, INSUBORDINATION, MISCELLANEOUS')
    types = input('Offence types as a comma separated list*: ')
    if types == '':
        print('Error: Please enter atleast one offence type.')
        return
    types = types.split(',')
    types = [x.strip() for x in types]
    types = set(types)

    guards = input('Guard ID\'s as a comma separated list: ')
    if guards != '':
        guards = guards.split(',')
        guards = [x.strip() for x in guards]
        guards = set(guards)
    else:
        guards = set()

    prisoners = input('Prisoner ID\'s as a comma separated list*: ')
    if prisoners == '':
        print('Please enter atleast one prisoner')
        return
    prisoners = prisoners.split(',')
    prisoners = [x.strip() for x in prisoners]
    prisoners = set(prisoners)

    query_str = f'INSERT INTO Prison.Offences({expand_keys(attr)}) VALUES(\
        "{attr["description"]}",\
        "{attr["date_time"]}",\
        "{attr["location"]}",\
        "{attr["severity"]}"\
    );'

    try:
        cur.execute(query_str)
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return

    offence_id = cur.lastrowid
    for type in types:
        query_str = f'INSERT INTO Prison.Offence_Type VALUES(\
            {offence_id},\
            "{type}"\
        );'
        try:
            cur.execute(query_str)
        except Exception as e:
            print('Failed to insert into the database.')
            con.rollback()
            print(e)
            input('Press any key to continue.')
            return

    for prisoner in prisoners:
        query_str = f'INSERT INTO Prison.Incident_Prisoners VALUES(\
            {offence_id},\
            {prisoner}\
        ); '
        try:
            cur.execute(query_str)
        except Exception as e:
            print('Failed to insert into the database.')
            con.rollback()
            print(e)
            input('Press any key to continue.')
            return

    for guard in guards:
        query_str = f'INSERT INTO Prison.Incident_Guards VALUES(\
            {offence_id},\
            {guard}\
        );'
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
        print('The new incident hase been successfully entered into the system.')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return


def add_visit(cur, con):
    attr = {}
    print('Enter details of the visitation:')

    attr['prisoner_id'] = empty_to_null(input('Prisoner ID*: '))

    attr['date_time'] = input(
        'Date and time of incident as YYYY-MM-DD HH:MM* (Press enter for the current date and time): ')
    if attr['date_time'] == '':
        attr['date_time'] = datetime.now().strftime('%Y-%m-%d %H:%M')

    name = input('Visitor\'s Name*: ').split(' ')
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

    attr['guard_id'] = empty_to_null(input('Guard ID: '))

    query_str = f'INSERT INTO Prison.Visits VALUES(\
        {attr["prisoner_id"]},\
        "{attr["date_time"]}",\
        "{attr["first_name"]}",\
        "{attr["middle_name"]}",\
        "{attr["last_name"]}",\
        {quote(attr["guard_id"])}\
    );'
    try:
        cur.execute(query_str)
        con.commit()
        print('The visit has been successfully entered into the system.')
        input('Press any key to continue.')
    except Exception as e:
        print('Failed to insert into the database.')
        con.rollback()
        print(e)
        input('Press any key to continue.')
        return