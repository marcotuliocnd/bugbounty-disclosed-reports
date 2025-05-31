# two aws access key and secret key and database username and password exposed 

## Report Details
- **Report ID**: 2401648
- **URL**: https://hackerone.com/reports/2401648
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-03-04T19:25:36.853Z
- **Disclosed**: 2024-10-18T08:01:06.029Z

## Reporter
- **Username**: ghaazy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
## Summary:
hello mozilla security team i found two aws access key and secret key and database username and password exposed  in dockerhub image 

## Steps To Reproduce:
go to https://hub.docker.com/r/mozilla/commonvoice
and do pull for this image
you will find them in 
/code/scripts/test/config.json
███████
poc of  the asw keys 
████
and also 
████
reference 
{F3097699}
and the enum for it 
████████
## Supporting Material/References
  *https://hackerone.com/reports/1720278
  * https://hackerone.com/reports/1580567

## Impact

## Summary:
exposure of sensitive data lead to many serious attacks and access

## Attachments
- image.png
