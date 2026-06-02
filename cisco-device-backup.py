from netmiko import ConnectHandler

device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "admin",
    "password": "password"
}

connection = ConnectHandler(**device)

config = connection.send_command("show running-config")

with open("backup.txt", "w") as file:
    file.write(config)

connection.disconnect()

print("Configuration backup completed.")
