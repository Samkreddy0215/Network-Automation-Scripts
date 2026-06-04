from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "admin",
    "password": "password"
}

connection = ConnectHandler(**device)

output = connection.send_command("show vlan brief")

with open("vlan_report.txt", "w") as file:
    file.write(output)

print(output)

connection.disconnect()
