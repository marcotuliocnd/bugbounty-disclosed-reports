# Race condition on https://judge.me/people

## Report Details
- **Report ID**: 1566017
- **URL**: https://hackerone.com/reports/1566017
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-05-11T14:32:05.836Z
- **Disclosed**: 2022-08-01T05:28:05.901Z

## Reporter
- **Username**: netboom
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: judgeme

## Vulnerability Information
##summary:An attacker can increase the followers of  the users of judge.me

Tools required : 
1.burpsuit
2.turbo intruder

##steps to reproduce:
1.visit https://judge.me/people
2.like a user and intercept the request
3.now  send it to turbo intruder and configure the script to 
     race.py

## Impact

The attacker can increase their followers in a bad way by creating fake followers

## Attachments
No attachments
