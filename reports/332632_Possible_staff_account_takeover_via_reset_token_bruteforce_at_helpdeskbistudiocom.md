# (Possible) staff account takeover via reset token bruteforce at helpdesk.bistudio.com

## Report Details
- **Report ID**: 332632
- **URL**: https://hackerone.com/reports/332632
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2018-04-03T15:53:55.674Z
- **Disclosed**: 2018-09-19T14:42:15.945Z

## Reporter
- **Username**: europa
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bohemia

## Vulnerability Information
As stated in a brief exchange with @rvn in my other report ##312433, I might have found a logic flaw in the way https://helpdesk.bistudio.com handles the reset flow and tokens.
I've asked if it was possible to obtain a test account, but I fully understand that it's something that cannot be done; as such I'll submit a "blind" report based on my black-box analysis and wait for your team to verify it. Also note that this flaw seems to also be present in the "Set out of office email response" flow, albeit less critical.

### Flow
The **SYSTEM PASSWORD RESET** flow is a 3-steps process:

1. the staff member requests a SMS TOKEN using the first form
2. the 6-digits SMS TOKEN is used in the second form
3. the staff member can now set a new SYSTEM PASSWORD in the third form

### Analysis and logic
I was able to go through the process even after providing non-existing usernames and tokens by intercepting the **response** in BurpSuite and changing the status code from **400 Bad Request** to **200 OK** and the body from `"status":"error"` to `"status":"ok"`, allowing the AngularJS applet to follow through.
I then noticed that the API endpoint for verifying the SMS TOKEN and changing the password where open and free of rate-limiting measures, allowing for a quick bruteforce of the 000000-999999 space. 
It should be therefore possible to perform an account takeover on any staff member, provided the SMS TOKEN really is a 6-digits code

### Theoretical POC
1. adversary starts the SYSTEM PASSWORD RESET process for the target victim using a POST request to `/api/system/verification-codes` (ie: `{"username":"admin"}`). The backend generates a SMS TOKEN and sends it to the victim's phone. Meanwhile,
2. adversary obtains the **securityCode** value for the victim by bruteforcing `/api/system/verification-codes/[0-9]{6}` before the victim can cancel the flow (threat scenario places the attack durin night time)
3. adversary can now reset the SYSTEM PASSWORD by sending the complete POST request to `/api/system/email-account/password` (ie: `{"password":"<NEW PASSWORD>","code":"<BRUTEFORCED SMS TOKEN>","securityCode":"<RETRIEVED SECURITY CODE>"}`)

Step #1 offers a ReCAPTCHA anti-CSRF token but it's not used anywhere in the flow, making the attack possible

Step #2 is really a matter of resources. Being free of rate-limiting, the API endpoint will be quickly queried for all the possible token combinations in a matter of minutes using a multithreaded approach (ie: using BurpSuite's Intruder).

Albeit theoretical, the logic behind the threat scenario seems plausible. It might be worth investigating.

### Recommended actions
Properly implement the ReCAPTCHA and a strict ratelimiting on the API endpoints

## Impact

An adversary might be able to takeover staff accounts, or set their "out of office" email replies.

## Attachments
No attachments
