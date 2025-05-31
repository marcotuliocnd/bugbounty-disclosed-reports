# Exposed Unencrypted Telnet Endpoint

## Report Details
- **Report ID**: 194454
- **URL**: https://hackerone.com/reports/194454
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-28T18:02:44.662Z
- **Disclosed**: 2017-02-08T00:51:09.048Z

## Reporter
- **Username**: zephrfish
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,

I'm not sure where to submit this as I know it is a low/medium risk issue on an asset which is out of scope. Essentially I stumbled across the endpoint whilst looking at other Starbucks domains within scope, the affected host is:
`franchisee.starbucks.com:23` it was found to be running an instance of telnet that is brute-forcible however given the host is out of scope, no attempts have been made to acquire access. When connecting to the host via telnet or netcat the following banner is presented:
`N4-DC4-STARBUCKS-RTR-01 (ttyp0)`

I'd recommend this host/endpoint be locked down ensuring that telnet is only reachable from VPN or inside the firewall. 

Thanks,

@ZephrFish

## Attachments
No attachments
