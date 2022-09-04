import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')

import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from RANDOM import Main

        Main()

if bit == "32bit":

        from RANDOM_32 import Main

        Main()

