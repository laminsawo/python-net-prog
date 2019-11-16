from netmiko import ConnectHandler
from getpass import getpass

user = str(input("Enter username: "))
password = str(input("Enter password: "))
secret_pass = str(input("Enter enable password: "))
cisco_3560 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.30',
    'username': user,
    'password': passsword,
    'port' : 22,          # optional, defaults to 22
    'secret': secret_pass,     # optional, defaults to ''
}
net_connect = ConnectHandler(**cisco_3560)
# established a connection to the object i.e cisco device

output = net_connect.send_command('show ip int brief')
# sends command to show ip interface brief of interfaces

output2 = net_connect.send_command('show cdp neighbors')
# displays CDP neighbors

print(output + "\n" + output2)
# prints the show command outputs and seperates them by a line


net_connect.disconnect()
# disconnects the connections