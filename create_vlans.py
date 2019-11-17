from netmiko import ConnectHandler
from past.builtins import raw_input

user = raw_input("Enter username: ")
password = raw_input("Enter password: ")
secret_password = raw_input("Enter enable password: ")
host_ip = raw_input("Enter IP address of device: ")
vlan_number = raw_input("Type in vlan and number e.g. vlan 100: ")
cisco_3560_x = {
    'device_type': 'cisco_ios',
    'host': host_ip,
    'port': 22,
    'username': user,
    'password': password,
    'secret': secret_password
}
net_connect = ConnectHandler(**cisco_3560_x)

create_vlan = net_connect.send_config_set(vlan_number)
show_vlan_db = net_connect.send_command("show vlan brief")
print(create_vlan)
print(show_vlan_db)

net_connect.disconnect()
