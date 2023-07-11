import os

try:
    os.system('cmd /k "ipconfig"')
except:
    print('Incorrect command')