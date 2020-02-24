''' finds correct timepoint id to send to stream.
Ensures no data loss for restarts
'''
import glob
import os
from json import loads


def get_timepoint():
    ''' retrieves timepoint id from most recent data '''
    files = glob.glob('data/*')
    latest = max(files, key=os.path.getctime) if files else None
    if latest:
        with open(latest, 'rb') as file:
            data = loads(file.readline())
            event = data.get('event')
            timepoint = event.get('timepoint')
            return timepoint
    return None
