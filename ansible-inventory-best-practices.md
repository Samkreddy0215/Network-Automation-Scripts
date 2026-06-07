# Ansible Inventory Best Practices

## What is an Inventory?

An Ansible inventory defines the hosts and groups of devices that Ansible manages.

## Example Inventory

[routers]
router1
router2

[switches]
switch1
switch2

## Best Practices

- Group devices by function
- Use meaningful hostnames
- Separate production and lab devices
- Store sensitive credentials in Ansible Vault
- Use group variables for common settings

## Directory Structure

inventory/
├── hosts
├── group_vars/
├── host_vars/

## Benefits

- Easier management of large environments
- Consistent configuration deployment
- Improved scalability
- Reduced operational errors

## Security Recommendations

- Never store plaintext passwords
- Use SSH key authentication
- Restrict inventory file access
- Implement role-based access controls
