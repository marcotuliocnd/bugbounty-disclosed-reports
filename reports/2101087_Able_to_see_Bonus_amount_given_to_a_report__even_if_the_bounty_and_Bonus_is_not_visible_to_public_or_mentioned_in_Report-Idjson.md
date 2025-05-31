# Able to see Bonus amount given to a report  even if the bounty and Bonus is not visible to public or mentioned in {Report-Id}.json

## Report Details
- **Report ID**: 2101087
- **URL**: https://hackerone.com/reports/2101087
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-08-08T12:28:50.787Z
- **Disclosed**: 2023-09-14T07:45:39.073Z

## Reporter
- **Username**: harshdranjan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:** 
Hey team,
while looking at your Disclosed reports I noticed that on report #2082680 you awarded the user with a Bonus and no bounty at all it was hidden as well because the Activity shows that "HackerOne rewarded someone with a bounty. " which also included the **Bonus**, upon checking the #2082680.json  I did not found the "bonus_amount" parameter at all or any number representing ████ which was the bonus given to the user thus it was supposed to be a Confidential but it's now exposed to the public.

As a PoC look at this report showing the Bonus amount in JSON 
A bonus of ███████ was given to the user of this report as well  https://hackerone.com/reports/1952124.json but upon checking the JSON format of this you can clearly see it's mentioned in the "bonus_amount"  parameter.

**Description:**

### Steps To Reproduce

1. Go to https://hackerone.com/reports/2082680 and see the right column of the screen and see the activity column's Bounty amount  
 ████

## Impact

Confidential  Information Disclosure

## Attachments
No attachments
