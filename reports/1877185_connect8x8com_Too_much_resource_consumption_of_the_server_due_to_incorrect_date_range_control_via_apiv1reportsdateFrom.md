# connect.8x8.com: Too much resource consumption of the server due to incorrect date range control via /api/v1/reports?dateFrom=

## Report Details
- **Report ID**: 1877185
- **URL**: https://hackerone.com/reports/1877185
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-02-16T23:11:54.608Z
- **Disclosed**: 2023-06-26T20:27:28.838Z

## Reporter
- **Username**: exhandler
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: 8x8-bounty

## Vulnerability Information
## Summary:
Hi Team, When we enter the date range in the reporting endpoint, we see this in the response. When we increase the date range, the byte returned by the server increases. By repeating this over and over, we can cause the server to consume too many resources. As a result, the server may crash.

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. First we must be logged in and go to https://connect.8x8.com/messaging/reports
  2. We can see this request when we look at burp requests 
https://connect.8x8.com/api/v1/reports?dateFrom=2023-02-10&dateTo=2023-02-17&tzName=Europe%2FIstanbul&tz=(UTC%2B03%3A00)&tzOffset=180&timeInterval=1440
  3.  the server will respond late as you increase the date range and the response size will increase a lot {F2178902} {F2178901}

## Remediation
Date range control can be added.

## Impact

Potential Dos...

## Attachments
- Screen_Shot_2023-02-17_at_02.07.29.png
- Screen_Shot_2023-02-17_at_02.07.12.png
