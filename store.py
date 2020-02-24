''' Process stores PID for is_up.sh to search for
'''
import os

def start_pid_log():
    ''' leaves a note of scripts process id for
        cronjob
    '''
    pid = os.getpid()
    name = '/tmp/company_house.pid'
    with open(name, 'w') as file:
        file.write(f'{pid}')
