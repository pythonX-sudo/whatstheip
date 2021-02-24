import socket

print('''
 __          ___           _         _______ _            _____ _____  
 \ \        / / |         | |       |__   __| |          |_   _|  __ \ 
  \ \  /\  / /| |__   __ _| |_ ___     | |  | |__   ___    | | | |__) |
   \ \/  \/ / | '_ \ / _` | __/ __|    | |  | '_ \ / _ \   | | |  ___/ 
    \  /\  /  | | | | (_| | |_\__ \    | |  | | | |  __/  _| |_| |     
     \/  \/   |_| |_|\__,_|\__|___/    |_|  |_| |_|\___| |_____|_|     

Created by PythonX ~ ShahadathAkash                                                                       
''')

web_address = input('[*] Give the Web Address here to get the IP Address. \nEx: www.google.com \n>>> ')
ip_address = socket.gethostbyname(web_address)
print('[+] The IP for ' + web_address + ' is ' + str(ip_address))
