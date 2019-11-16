from netmiko import ConnectHandler
from past.builtins import raw_input
# enables support for python syntax e.g. raw_input
user = raw_input("Enter username:")
password = raw_input("Enter you password: ")
secret_password = raw_input("Enter enable password: ")
host_ip = raw_input("Enter IP address of host: ")
cisco_3560_1 = {
    'device_type': 'cisco_ios',
    'host': host_ip,
    'username': user,
    'password': password,
    'secret': secret_password,
    'port': 22
}
net_connect = ConnectHandler(**cisco_3560_1)
output_vlan_summary = net_connect.send_command('show vlan summary')
output_vlan_mtu = net_connect.send_command("show vlan mtu")
output_vlan_brief = net_connect.send_command("show vlan brief")
print(output_vlan_summary)
print(output_vlan_mtu)
print(output_vlan_brief)

net_connect.disconnect()
