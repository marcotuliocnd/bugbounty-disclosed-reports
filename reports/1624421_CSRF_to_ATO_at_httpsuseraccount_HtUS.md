# CSRF to ATO at https://█████/user/account [HtUS]

## Report Details
- **Report ID**: 1624421
- **URL**: https://hackerone.com/reports/1624421
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-07-04T14:14:29.195Z
- **Disclosed**: 2023-01-06T18:50:07.543Z

## Reporter
- **Username**: pwn33d
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
hello dod security team today while i was doing pentest on your scope
i came across
https://████████/user/account
so i register and after that tried to edit my data and the data was in json request
so i simple change content-type to
content-type application/x-www-form-urlencoded
and the data was change
and in the next step i create html file 
to edit users data with 
0 click 
which allow me to change victim email and leads to account takeover
check my html poc file and video

## Impact

account takeover

## Attachments
No attachments
