# HAProxy stats panel exposed externally

## Report Details
- **Report ID**: 1884372
- **URL**: https://hackerone.com/reports/1884372
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-02-23T12:30:51.552Z
- **Disclosed**: 2023-03-24T17:25:49.058Z

## Reporter
- **Username**: kalkii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Team

I was able to find exposed web panel for HAProxy running on ████at port 1024

## Impact

By visiting http://██████:1024/haproxy-status, the statistics page for HAProxy is shown. I have attached a screenshot to confirm that the endpoint is accessible externally
███

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
To Reproduce this simply visit 
http://███:1024/haproxy-status?stats
http://███:1024/haproxy-status

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
