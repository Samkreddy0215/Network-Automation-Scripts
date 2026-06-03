from netmiko import ConnectHandler

devices = [
    {
        "device_type": "cisco_ios",
        "host": "10.1.1.1",
        "username": "admin",
        "password": "password"
    }
]

for device in devices:
    connection = ConnectHandler(**device)

    hostname = connection.send_command("show run | include hostname")
    version = connection.send_command("show version | include Version")

    print("=" * 50)
    print(hostname)
    print(version)

    connection.disconnect()
