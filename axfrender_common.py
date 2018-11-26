import json
import os
import time

try:
    from PySide2 import QtCore, QtGui, QtWidgets
    from PySide2 import __version__
except ImportError:
    from PySide import QtCore, QtGui
    from PySide import __version__
    #QtWidgets = QtGui

def message_out(mess):
    if '2.0.0' in __version__:
        msg = QtWidgets.QMessageBox()    
    else:
        msg = QtGui.QMessageBox()
    msg.setText(mess)
    msg.exec_()

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

