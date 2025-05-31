# svcardproxydevus.starbucks.com Subdomain take over

## Report Details
- **Report ID**: 380158
- **URL**: https://hackerone.com/reports/380158
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-07-10T13:14:17.255Z
- **Disclosed**: 2018-07-23T17:47:15.343Z

## Reporter
- **Username**: txt3rob
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
You have left a dns record pointing to a dead cloudapp vm.

```
svcardproxydevus.starbucks.com -> s00307ntmp0svcardproxydev0.trafficmanager.net -> s00307dpipsvcardproxy00.eastus.cloudapp.azure.com = Dead
```

## Impact

```
1) Attacker takes over subdomain and then puts something like porn or something that shouldn't be on the domain.
2) hacker then contacts support pretending to be a concerned user.
3) support click on it to check what is going on
4) attacker has put responder on the page via a image file using a UNC path (https://github.com/SpiderLabs/Responder)
5) attacker is then sent supports hash for their windows login.
6) attacker then cracks hash and uses the VPN to pivot 
```

They can also use it to phish and other bad activitys

## Attachments
- Capture.PNG
