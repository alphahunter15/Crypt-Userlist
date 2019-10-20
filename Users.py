#!/usr/bin/python

import datetime
import reverse_isaiah
import reverse_angel
import reverse_charlie

date_object = datetime.date.today()
print(date_object)


def rev_str(s):
    return s[::-1]


password = input('Password:')

if password == 'communist':
    q = input('Future:')
    if q == 'MIT':
        print('password accepted')
        print('Welcome, Isaiah')
        command = input('read or write:')
        if command == 'write':
            i = open("isaiah_log.py", "a+")
            i.write(rev_str(input("ISAIAH'S LOG:")))
            i.write('\n')
            i.close()
        elif command == 'read':
            print(reverse_isaiah.fwd_str('reverse_isaiah'))
        else:
            print('unexpected command, try again')
    else:
        print('leave, you sit on a throne of lies.')
    print('\n')

elif password == 'charlie':
    q = input('what game do we play on Fridays (in one word):')
    if q == ['smash', 'Smash']:
        print('password accepted')
        print('Welcome, Charlie')
        command = input('read or write:')
        if command == 'write':
            c = open("charlie_log.py", "a+")
            c.write(rev_str(input("CHARLIE'S LOG:")))
            c.write('\n')
            c.close()
        elif command == 'read':
            exec(reverse_charlie)
        else:
            print('unexpected command, try again')
    else:
        print('Imposter! You sit on a trone of lies')
        print('\n')


elif password == 'love of my life':
    q = input('what movie did we watch first together:')
    if q == 'Up':
        print('password accepted')
        print('infinity - 2 = infinity')
        print('Welcome, Lilly')
        command = input('read or write:')
        if command == 'write':
            l = open("angel_log.py", "a+")
            l.write(rev_str(input("ANGEL'S LOG:")))
            l.write('\n')
            l.close()
        elif command == 'read':
            exec(reverse_angel)
        else:
            print('unexpected command, try again')
    else:
        print('imposter! you sit on a throne of lies')
    print('\n')

else:
    print('password rejected')
    print('Go away')
