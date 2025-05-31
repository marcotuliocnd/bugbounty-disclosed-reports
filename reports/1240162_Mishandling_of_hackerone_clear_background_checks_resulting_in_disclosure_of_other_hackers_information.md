# Mishandling of hackerone clear background checks resulting in disclosure of other hacker's information

## Report Details
- **Report ID**: 1240162
- **URL**: https://hackerone.com/reports/1240162
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-21T16:02:59.278Z
- **Disclosed**: 2021-08-05T15:24:09.996Z

## Reporter
- **Username**: frozensolid
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**
Mishandling of hackerone clear background checks resulting in disclosure of other hacker's information .

**Description:**
I received a hackerone clear invite for "█████" I am not █████. There appears to be some kind of off by one error or similar problem with the hackerone clear invites!

first email was from "h1-clear@hackerone.com subject" "Action Required to maintain your HackerOne Clear Status" dated Jun 18, 2021, 3:06 PM Mountain Time. Alerting to an upcoming change the hackerone clear background checks. 

After that the "First Advantage" email subject "You have been invited to kick off your new background check" dated Jun 18, 3:16 PM Mountain Time included someone else's name. This email from first advantage included someone else's name. 
████

Clicking the link I was given a background check and asked to sign as "████"
██████████
████████

I also notified h1-clear@hackerone.com as requested in the invite but didn't get any kind of tracking number back and thought this was worth reporting here. 

### Steps To Reproduce

1. I'm not sure how to reproduce, but it appears there was an issue processing or mishandling the list of hackerone clear applicants in a way that I received the background check for someone else with the same first name.
2. Some kind of issue with escaping or safely processing the hacker names (CWE-20) on the list resulting in an off by one error (CWE-193)? 

### Optional: Supporting Material/References (Screenshots)
██████
███████

## Impact

It is hard to know the exact impact without knowing the exact nature of how this was messed up but a few guesses: 
1. Integrity/assurance of the hackerone clear program:  Hacker A could be "cleared" using the results of Hacker B's credentials?
2. disclosure of the name of Hacker A to Hacker B?
3. Some kind of issue with escaping or safely processing the names on the list resulting in an off by one error?

## Attachments
No attachments
