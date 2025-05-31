# Attacker could setup reminder remotely using brute force

## Report Details
- **Report ID**: 158393
- **URL**: https://hackerone.com/reports/158393
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-11T07:50:23.422Z
- **Disclosed**: 2016-09-19T00:04:46.344Z

## Reporter
- **Username**: cymtrick
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: uber

## Vulnerability Information
Hi,

Attacker could setup the reminder for bulk  no of amount of accounts using there phone no's. He could setup infinite no of reminders. Tried brute force for 100 times worked perfectly
here is the link : https://widgets.uber.com/american-airlines-reminders/
Here any phone-no is accepted. Actually logged in user phone-no should be cross checked.

TCP DUMP while setting up reminder:

```
POST /american-airlines-reminders/api/v1/reminders HTTP/1.1
Host: widgets.uber.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-CSRF-Token: 
x-uber-origin: web-reminders
Content-Type: application/json
Referer: https://widgets.uber.com/american-airlines-reminders/
Content-Length: 87
Cookie: 
Connection: keep-alive

{"event":{"time":1470940200},"phone_number":"+919949111969","reminder_time":1470937500}
```

Send that request to intruder in burp and try to brute force. Setting up reminder is always shown with response code 200 .
my reminder was setup on Thu, 11 Aug 2016 17:45:00 GMT multiple times. Attacker could perform this on multiple phone-no.
This could issue for user's because their phone gets constantly notifications.
Regards
prashanth varma



## Attachments
- Screen_Shot_2016-08-11_at_1.14.42_PM.png
- Screen_Shot_2016-08-11_at_1.14.52_PM.png
