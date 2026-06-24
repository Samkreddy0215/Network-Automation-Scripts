# Network Change Validation Checklist

## Purpose

Provide a standardized process for validating network changes before and after implementation.

## Pre-Change Validation

- Verify approved change ticket
- Confirm device backups completed
- Review rollback plan
- Validate maintenance window
- Notify stakeholders

## Implementation Checks

- Confirm device reachability
- Monitor CPU and memory utilization
- Verify routing adjacencies remain stable
- Check interface status
- Review system logs for errors

## Post-Change Validation

### Routing

- Verify BGP neighbors
- Verify OSPF adjacencies
- Confirm route propagation

### Switching

- Validate VLAN assignments
- Verify trunk status
- Check STP topology

### Security

- Verify firewall policies
- Test VPN connectivity
- Validate NAT functionality

### Applications

- Test critical business applications
- Verify DNS resolution
- Confirm end-user connectivity

## Rollback Criteria

- Routing instability
- Application outage
- Security policy failure
- Unexpected traffic loss

## Best Practices

- Automate validation where possible
- Document all test results
- Maintain rollback readiness
- Conduct post-change review
