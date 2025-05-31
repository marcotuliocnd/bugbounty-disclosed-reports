# Authentication bypass and potential RCE on the https://████ due to exposed Cisco TelePresence SX80 with default credentials

## Report Details
- **Report ID**: 684758
- **URL**: https://hackerone.com/reports/684758
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-08-29T22:32:24.468Z
- **Disclosed**: 2024-07-19T14:30:38.509Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
##Description
Hello. I was able to identify another one Cisco TelePresence SX80 device located on the https://████████ right near the previous device `████` (after #684070 report I decided to check ████* range)
According to the IP Info: https://ipinfo.io/AS257/████0/24 it belongs to ASN with ID 
```
AS257 ███
```

The mentioned instance has same credentials `admin:admin`.
This instance is different and less used, the logs reveals that last time device was used in 2017 year.

##POC
https://████████
Login with `admin:admin`
███████
Since we are logged in as admin, we can completely control the device and all connections, and add our startup scripts via https://███████/web/scripts thus achiecing code execution.

##Suggested fix
Change the credentials and likely you will need to reset the device to factory settings

## Impact

Potential device compromise and code execution. This devices are used mainly for trainings, briefings, and demonstration rooms, as well as auditoriums, so attacker with full control of the device potentially can intercept the data (RCE potential is interesting, but ability to silently compromise the device and use it as backdoor can be much more harmful).

## Attachments
No attachments
