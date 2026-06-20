# Ansible BGP Neighbor Validation

## Objective

Use Ansible to verify BGP neighbor status across multiple Cisco routers and generate a validation report.

## Prerequisites

- Ansible installed
- SSH access to network devices
- Cisco IOS XE routers
- Inventory file configured

## Workflow

1. Connect to routers
2. Run BGP neighbor commands
3. Collect neighbor state information
4. Identify non-established sessions
5. Generate validation report

## Sample Command

show ip bgp summary

## Data to Capture

- Router hostname
- Neighbor IP
- Remote AS
- Session state
- Prefix count
- Uptime

## Expected Outcome

- All BGP sessions verified
- Failed adjacencies identified
- Consistent reporting across devices

## Benefits

- Faster operational validation
- Reduced manual effort
- Improved network visibility
- Repeatable audit process
