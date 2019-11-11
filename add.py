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
    attr['dob'] = input('Date as YYYY-MM-DD: ')  # date: checked by mysql
    
    attr['height'] = input('Height: ') # float: handled by mysql
    attr['weight'] = input('Weight: ') # float: handled by mysql
    attr['blood_group'] = input('Blood group: ') # enum: handled by mysql
    attr['medical_history'] = input('Medical History: ') # empty string
    
    attr['arrival_date'] = input('Arrival Date* (Press enter for today\'s date): ')
    if attr['arrival_date'] == '':
        attr['arrival_date'] = datetime.now().strftime('%Y-%m-%d')
    
    attr['sentence'] = input('Sentence*: ')
    if attr['sentence'] == '':
        print('Please enter the sentence details')
        return

    attr['cell'] = input('Cell*: ')
    try:
        int(attr['cell'])
    except NameError:
        print('Please enter a cell number between 1 and 999')
        return
    if int(attr['cell']) < 1 or int(attr['cell']) > 100:
        print('Please enter a cell number between 1 and 999')
        return

    attr['wing'] = input('Wing*: ')
    if len(attr['wing']) != 1 or not attr['wing'].isupper():
        print('Please enter a wing from A to Z')
        return

    attr['security_level'] = input('Security level*: ')
    if attr['security_level'] not in ('LOW', 'MEDIUM', 'HIGH'):
        print('Please choose a security level out of LOW, MEDIUM or HIGH')
        return

    query_str = f'INSERT INTO Prison.Prisoners({expand_keys(attr)}) VALUES(\
        "{attr["first_name"]}",\
        "{attr["middle_name"]}",\
        "{attr["last_name"]}",\
        "{attr["sex"]}",\
        "{attr["dob"]}",\
        {attr["height"]},\
        {attr["weight"]},\
        "{attr["blood_group"]}",\
        "{attr["medical_history"]}",\
        "{attr["arrival_date"]}",\
        "{attr["sentence"]}",\
        "{attr["cell"]}",\
        "{attr["wing"]}",\
        "{attr["security_level"]}"\
    ); '
    
    try:
        cur.execute(query_str)
        con.commit()
        print('The new inmate hase been successfully entered into the system.')
    except MySQLError as e:
        con.rollback()
        print('Failed to insert into the database')
        print(e)
    



    
