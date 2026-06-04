from netmiko import ConnectHandler

required_configs = [
    "service password-encryption",
    "logging buffered",
    "ntp server"
]

device = {
    "device_type": "cisco_ios",
    "host": "10.1.1.1",
    "username": "admin",
    "password": "password"
}

connection = ConnectHandler(**device)

running_config = connection.send_command("show running-config")

print("\nConfiguration Compliance Report\n")

for item in required_configs:
    if item in running_config:
        print(f"[PASS] {item}")
    else:
        print(f"[FAIL] {item}")

connection.disconnect()
