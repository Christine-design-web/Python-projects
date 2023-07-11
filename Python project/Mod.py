import os

try:
    os.system('cmd /k "systeminfo"')
except:
    print('Incorrect command')