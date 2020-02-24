'''Main python process that accesses and processes stream data '''
from json import loads

from connect import connect, check_stream
from timepoint import get_timepoint
from store import start_pid_log


if __name__ == '__main__':
    TIMEPOINT = get_timepoint()
    start_pid_log()
    STREAM = check_stream(connect(timepoint=TIMEPOINT))
    for line in STREAM.iter_lines():
        if line:
            data = loads(line).pop('data')
            company_id = data.get('company_number')
            with open(f'data/{company_id}', 'wb') as record:
                record.write(line)
