# Internal IP addresses range and AWS cluster region leaked in a Github repository 

## Report Details
- **Report ID**: 877303
- **URL**: https://hackerone.com/reports/877303
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-05-18T17:25:09.627Z
- **Disclosed**: 2020-07-24T00:43:28.230Z

## Reporter
- **Username**: njaysec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kubernetes

## Vulnerability Information
Report Submission Form

## Summary:
I was exploring the GitHub repository and found some internal IP address and its cluster region related to AWS cluster. So i decided to report it to you. Please have a look and let me know.

## Steps To Reproduce:
VISIT THIS LINK : 
Repository - kubernetes / kubernetes 
File Link - https://github.com/kubernetes/kubernetes/blob/d4d02a9028337e41b4f7a76e4e7de50067e8529e/cluster/aws/config-default.sh


## Supporting Material/References:
Reference:
https://hackerone.com/reports/329791
https://hackerone.com/reports/271700
https://hackerone.com/reports/310036

## Impact

1. These IPs are related to AWS cloud, if someone get enter in the Vnet can also exploit machine on the machines already known.
2. Gives the idea of the organization of internal network. 
3. Revealing the AWS cluster region can also narrow down the search of any hacker and make their work easy
4. This will allow attackers to gain access to an internal IP of a DOD website along with other sensitive information that may be leaked with the request

## Attachments
- kub-aws1.png
- kub-aws2.png
- kub-aws3.png
