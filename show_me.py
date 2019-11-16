from netmiko import ConnectHandler
cisco_3560 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.0.30',
    'username':"admin",
    'password': "Password01",
    'port' : 22,          # optional, defaults to 22
    'secret': "cisco",     # optional, defaults to ''
}
net_connect = ConnectHandler(**cisco_3560)

output = net_connect.send_command('show ip int brief')
output2 = net_connect.send_command('show cdp neighbors')
print(output + "\n" + output2)
