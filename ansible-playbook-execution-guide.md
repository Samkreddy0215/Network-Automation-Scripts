# Ansible Playbook Execution Guide

## Purpose

Ansible playbooks automate configuration, deployment, and operational tasks across network devices.

## Running a Playbook

ansible-playbook -i inventory/hosts backup-config.yml

## Common Options

--check      # Dry run mode
--diff       # Show configuration differences
--limit      # Run against specific hosts
--tags       # Execute specific tasks

## Example Workflow

1. Verify inventory connectivity
2. Run playbook in check mode
3. Review output
4. Execute production run
5. Validate changes

## Troubleshooting

- Verify SSH connectivity
- Check inventory definitions
- Validate credentials
- Review task output logs
- Confirm device reachability

## Best Practices

- Test in lab environments first
- Use version control for playbooks
- Store secrets in Ansible Vault
- Document all automation workflows
- Use meaningful task names
