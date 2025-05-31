# Authentication bypass and RCE on the https://████ due to exposed Cisco TelePresence SX80 with default credentials

## Report Details
- **Report ID**: 684070
- **URL**: https://hackerone.com/reports/684070
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-08-29T01:13:11.963Z
- **Disclosed**: 2021-01-12T21:55:36.855Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
Hello. I was able to identify Cisco TelePresence SX80 device located on the https://█████
According to the IP Info: https://ipinfo.io/████████it belongs to ASN with ID 
```
███████
```
so it's likely in scope of the program.
The mentioned instance has default credentials `████`

##POC
https://███████
Login with `█████████`
████
Since we are logged in as ███, we can completely control the device and all connections, and add our startup scripts via https://██████████/web/scripts

##Suggested fix
Change the credentials and likely you will need to reset the device

## Impact

Potential device compromise and code execution. This devices are used mainly for trainings, briefings, and demonstration rooms, as well as auditoriums, so attacker with full control of the device potentially can intercept the data (RCE potential is interesting, but ability to silently compromise the device and use it as backdoor can be much more harmful).

## Attachments
No attachments
