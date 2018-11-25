import json
import os
import time

def read_data_from_file(filename):
    try:
        with open(filename,'r') as f:
            output = json.load(f)
    except Exception as e:
        return e, None
    
    return  None, output

def write_data_to_file(data, filename):
    try:
        with open(filename,'w') as f:
            json.dump(data, f)
    except Exception as e:
        print 'err write --' + e

def wait_file_open(filename):
    while True:
        if os.path.isfile(filename):
            time.sleep(2)
            break

def remove_file(filename):
        try:
            os.remove(filename)
        except Exception as e:
            print 'err remove --', e

