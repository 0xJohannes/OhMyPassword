import getpass
from Crypto.Cipher import AES
import math
banner='''\n\n

$$$$$$\  $$\       $$\      $$\           $$$$$$$\                                                                       $$\ 
$$  __$$\ $$ |      $$$\    $$$ |          $$  __$$\                                                                      $$ |
$$ /  $$ |$$$$$$$\  $$$$\  $$$$ |$$\   $$\ $$ |  $$ |$$$$$$\   $$$$$$$\  $$$$$$$\ $$\  $$\  $$\  $$$$$$\   $$$$$$\   $$$$$$$ |
$$ |  $$ |$$  __$$\ $$\$$\$$ $$ |$$ |  $$ |$$$$$$$  |\____$$\ $$  _____|$$  _____|$$ | $$ | $$ |$$  __$$\ $$  __$$\ $$  __$$ |
$$ |  $$ |$$ |  $$ |$$ \$$$  $$ |$$ |  $$ |$$  ____/ $$$$$$$ |\$$$$$$\  \$$$$$$\  $$ | $$ | $$ |$$ /  $$ |$$ |  \__|$$ /  $$ |
$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |  $$ |$$ |     $$  __$$ | \____$$\  \____$$\ $$ | $$ | $$ |$$ |  $$ |$$ |      $$ |  $$ |
 $$$$$$  |$$ |  $$ |$$ | \_/ $$ |\$$$$$$$ |$$ |     \$$$$$$$ |$$$$$$$  |$$$$$$$  |\$$$$$\$$$$  |\$$$$$$  |$$ |      \$$$$$$$ |
 \______/ \__|  \__|\__|     \__| \____$$ |\__|      \_______|\_______/ \_______/  \_____\____/  \______/ \__|       \_______|
                                 $$\   $$ |                                                                                   
                                 \$$$$$$  |                                                                                   
                                  \______/                                                                                   \n\n
                                   
                                  Oh my password is a tool written to simplify and secure your password choice. 
                                  Just by remembering serveral simple values you can generate your password again and again.
                                  For further simplification you can encorporate those values in pass, for example -- mypass5050
                                                                     '''


print(banner)
IV="S6U7vNK03OZpuYM7"
KEY="VL4G7O6fee0vBUbCMWmm7QYrqLpPVbgM"
aes = AES.new(KEY, AES.MODE_CBC, IV)
p = getpass.getpass(prompt='Submit the base string for password generation: ')
pcheck = getpass.getpass(prompt='Please repeat the password: ')
rounds=60000
if p!=pcheck:
    exit("\n Error: Passwords do not match\n")
l=int(input("Submit length of string you want to get(default 20): ") or "20")
r=int(input("Submit additional rounds of encryption (setting too much might freeze your screen)(default 0): ") or "0")

rounds+=r+l
padval=math.ceil(rounds/16)*16
finpass=""
print("Notice: This might take a while due to supplied values.\n Just remember the slow compitation is a measure against bruteforce attacks\n")
for i in range(0,rounds):
    p+='A'*(padval-len(p))
    finpass+=((aes.encrypt(p)).hex())[13:14]
    p=finpass
print('Your password is -- '+finpass[-l:])