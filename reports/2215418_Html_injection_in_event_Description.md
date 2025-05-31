# Html injection in event Description 

## Report Details
- **Report ID**: 2215418
- **URL**: https://hackerone.com/reports/2215418
- **State**: Closed
- **Severity**: low
- **Submitted**: 2023-10-19T09:20:39.906Z
- **Disclosed**: 2024-01-29T04:50:05.234Z

## Reporter
- **Username**: khaledx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: linkedin

## Vulnerability Information
#Hi team

there is Html injection   when user add   Description to event  when public user search for  published event

#Step's

* login to https://www.linkedin.com/groups/ 
* create event mark it as Public add <a href="https://malicious-site.com">Click me!</a> as  Description
{F2785963}
* save change now navigate to ==Search== enter your event name 
* when ==result== show up html code get executed in the Description

{F2785962}


POC:F2785976

## Impact

attacker able to run html code

## Attachments
- Screenshot_2023-10-19_11_11_25.png
- Screenshot_2023-10-19_11_10_59.png
- POCvokoscreenNG-2023-10-19_11-16-08.mkv
