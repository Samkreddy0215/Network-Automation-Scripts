from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "admin",
    "password": "password"
}

connection = ConnectHandler(**device)

output = connection.send_command("show ip interface brief")

print(output)

connection.disconnect()
