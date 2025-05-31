# Division by zero if terminal width is 2

## Report Details
- **Report ID**: 774883
- **URL**: https://hackerone.com/reports/774883
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-01-14T17:44:31.429Z
- **Disclosed**: 2021-02-08T07:53:40.195Z

## Reporter
- **Username**: danielmarjamaki
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
In fly() there will be a division by zero if progress bar width is 2.

That can happen if terminal width is 2.

## Steps To Reproduce:
This script crash:
stty rows 10 cols 2 ; curl --progress-bar somefile > temp

## Impact

I believe that if it's possible to set terminal width for a service, then that service will not be able to curl.

## Attachments
No attachments
