# Private IP addresses Disclosure

## Report Details
- **Report ID**: 908880
- **URL**: https://hackerone.com/reports/908880
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-06-26T12:31:32.945Z
- **Disclosed**: 2020-07-23T17:59:10.593Z

## Reporter
- **Username**: iwiwwooqo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
The following URL leaks the Private IP Addresses:- kubernetes.io/feed.xml

The following Server’s Cluster RFC 1918 IP addresses were disclosed in the response: 
•	10.1.2.3 
•	10.104.207.136 
•	10.224.0.0 
•	10.250.0.0 
•	10.250.112.0 
•	10.250.96.0 
•	10.55.252.216 
•	10.96.0.0 
•	10.96.0.1 
•	10.96.15.180 
•	10.97.125.254 
•	10.97.62.68 
•	172.17.0.4 
•	192.168.1.4 
•	192.168.1.7 
•	192.168.99.100


Steps to reproduce:- Simply by opening the above mentioned link we can extract the server's Cluster IP Addresses.

References:- Attached Snaps  
CWE-200: Information Exposure

## Impact

Attackers can use this information to exploit the ip addresses.

## Attachments
- 2.JPG
