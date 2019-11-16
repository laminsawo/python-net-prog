from netmiko import ConnectHandler
from getpass import getpass

user = raw_input("Enter username: ")
password = raw_input("Enter password: ")
secret_pass = raw_input("Enter enable password: ")
cisco_3560_30 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.30',
    'username': user,
    'password': password,
    'port' : 22,          # optional, defaults to 22
    'secret': secret_pass,     # optional, defaults to ''
}

cisco_3560_31 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.31',
    'username': user,
    'password': password,
    'port' : 22,          # optional, defaults to 22
    'secret': secret_pass,     # optional, defaults to ''
}

cisco_3560_32 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.32',
    'username': user,
    'password': password,
    'port' : 22,          # optional, defaults to 22
    'secret': secret_pass,     # optional, defaults to ''
}
net_connect_1 = ConnectHandler(**cisco_3560_30)
net_connect_2 = ConnectHandler(**cisco_3560_31)
net_connect_3 = ConnectHandler(**cisco_3560_32)
# established a connection to the object i.e cisco device

output_int_1 = net_connect.send_command('show ip int brief')
# sends command to show ip interface brief of interfaces
output_cdp_1 = net_connect.send_command('show cdp neighbors')
# displays CDP neighbors

output_int_2 = net_connect.send_command('show ip int brief')
# sends command to show ip interface brief of interfaces
output_cdp_2 = net_connect.send_command('show cdp neighbors')
# displays CDP neighbors

output_int_3 = net_connect.send_command('show ip int brief')
# sends command to show ip interface brief of interfaces
output_cdp_3 = net_connect.send_command('show cdp neighbors')
# displays CDP neighbors

print(output_int_1 + "\n" + output_int_2 + "\n" + output_int_3 )
# prints the interface brief of interfaces
print(output_cdp_1 + "\n" + output_cdp_2 + "\n" + output_cdp_3 )
# prints the cdp neighbor relationship for each switch 

net_connections =  net_connect_1, net_connect_1, net_connect_1
net_connections.disconnect()
# disconnects the connections