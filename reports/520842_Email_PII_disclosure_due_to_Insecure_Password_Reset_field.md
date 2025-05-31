# Email PII disclosure due to Insecure Password Reset field

## Report Details
- **Report ID**: 520842
- **URL**: https://hackerone.com/reports/520842
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-04-02T12:09:34.499Z
- **Disclosed**: 2019-12-02T19:13:18.422Z

## Reporter
- **Username**: alyssa_herrera
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
I revisited report #235041 and discovered the vulnerability isn't patched properly as I was able to discover more emails I could gleam. It appears the core mechanism allows anyone who knows specific names or user names to leak sensitive emails 
**Description:**
This password reset field allows an attacker to guess at user accounts such as admin and it will then expose the account user's email, this coupled with the lack of rate limiting allows me to easily bruteforce through a list of names to grab various sensitive emails.  Normally password reset fields keep the account emails hidden to prevent any attempt to directly attack the user, for example phishing emails. 
## Impact
medium-high
## Step-by-step Reproduction Instructions

 First we visit, https://██████████/griduc/accounts/request_reactivation/
Then we type in Alex, and click reset. Observe the email █████ is leaked 

I was able to discover few other emails as well,  
Bryan =█████████
knowles = █████ bein

## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
As per my previous report, I'd say the same solution is needed. I would recommend changing the account reset field to log any attempts for password resets to check for any malicious or abusive attempts to harvest account names, set a limit for amount of requests for the field, and additionally make a general message such as "We have sent the reset request to the email you used on registration"

My current theories either point to a possible code reversion or simply just removing the accounts  i used to previously test

## Impact

Attackers will be able to grab sensitive emails which can be targeted directly for phishing attacks or simple hijacked if the user in question reused their password and it has been previously leaked

## Attachments
No attachments
