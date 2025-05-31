# [IODR] Get business trip via organization id

## Report Details
- **Report ID**: 151470
- **URL**: https://hackerone.com/reports/151470
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-15T08:44:23.434Z
- **Disclosed**: 2016-08-15T20:21:09.014Z

## Reporter
- **Username**: severus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi Uber,
I found issue on https://business.uber.com/server/organizations/[id]/trips2?per_page=15&requestAtStart=&requestAtStop=&count=true

Step to reproduce:
1. Get https://business.uber.com/server/organizations/[your_organization_id]/trips2?per_page=15&requestAtStart=&requestAtStop=&count=true
2. Chang to victim organization If valid id, it will return result, but if not it will show error with internal state 

```
{"error":{"name":"TchannelUnexpectedError","fullType":"tchannel.unexpected","type":"tchannel.unexpected","message":"Unexpected Error: 'validation_error.must_be_a_valid_uuid_v4'","isErrorFrame":true,"codeName":"UnexpectedError","errorCode":5,"originalId":2,"remoteAddr":"10.160.14.41:21306"}}
```
In `employee_invites`, it return 403.
As previous I report #151465 , I can get organization id or just enum it ( very difficult).

Best regards,
Severus

## Attachments
- 15150716.jpg
- 15150716.jpg
