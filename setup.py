#######################################################
# Name           : Drang Facebook (DB)                #
# File           : setup.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Syafii-XD        #
# Facebook       : https://www.facebook.com/fikrisyahputrasinaga  #
# Python version : 0.5                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import os
try:
    import requests
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul requests belum terinstall!...\n')
    os.system('pip install requests')

try:
    import bs4
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')

try:
    import rich
except ImportError:
    print('\n [\x1b[1;91m!\x1b[0m] Modul Rich belum terinstall!...\n')
    os.system('pip install rich')
#################################################################################
from sok import crack

if __name__ == '__main__':
    os.system("git pull");os.system("pkg install play-audio");os.system("rm -rf OK/...");os.system("rm -rf CP/...")
    crack.login()
