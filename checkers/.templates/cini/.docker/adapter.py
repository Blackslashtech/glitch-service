import os
import sys

# Because the checklib expects to send flagids back to a server, we have to run that server locally to avoid needing to modify the checklib
os.environ['FLAGID_SERVICE'] = 'http://127.0.0.1'
os.environ['ACTION'] = 'check'
os.environ['TEAM_ID'] = '0'
os.environ['VULNBOX_ID'] = '0'
os.environ['ROUND'] = '0'
os.environ['FLAGID_TOKEN'] = ''

import checker



def check(params: list):
    host = params[0]
    checker.team_ip = host
    checker.base_url = f'http://{host}:{checker.PORT}'
    checker.check_sla()

def put(params: list):
    host = params[0]
    flag = params[1]
    flag_id = params[2]
    callback_url = params[3]
    checker.team_ip = host
    checker.base_url = f'http://{host}:{checker.PORT}'
    checker.flag = flag
    os.environ['FLAGID_SERVICE'] = callback_url
    checker.put_flag()

def get(params: list):
    host = params[0]
    flag = params[1]
    checker.team_ip = host
    checker.base_url = f'http://{host}:{checker.PORT}'
    checker.flag = flag
    checker.get_flag()


actions = {
    'check': check,
    'put': put,
    'get': get
}

if __name__ == '__main__':
    action = sys.argv[1]
    params = sys.argv[2:]
    actions[action](params)

