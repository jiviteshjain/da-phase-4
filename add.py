import subprocess as sp
import pymysql
import pymysql.cursors

def add_prisoner(cursor, conn):
    attr = {}
    name = input('Enter the prisoner\'s name: ').split(' ')
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

    