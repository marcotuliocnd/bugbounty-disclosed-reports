# No Rate Limit On Forgot Password Page Of affiliates.nordvpn.com

## Report Details
- **Report ID**: 791498
- **URL**: https://hackerone.com/reports/791498
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-09T08:34:32.742Z
- **Disclosed**: 2020-02-24T11:00:31.355Z

## Reporter
- **Username**: alishah
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
###Introduction:-
A little bit about Rate Limit:
A rate limiting algorithm is used to check if the user session (or IP-address) has to be limited based on the information in the session cache.
In case a client made too many requests within a given time frame, HTTP-Servers can respond with status code 429: Too Many Requests.

###Description:-
I have identified that when Forgetting Password for account , the request has no rate limit which then can be used to loop through one request. Which can be annoying to the root users sending mass password to one email.

###Steps To Reproduce The Issue
Step 1-  Go To This Link https://affiliates.nordvpn.com/users/forgot_password
Enter Email Click On Forget Password

Step 2- Intercept This Request In Burp And Forward It In To Intruder

Step 3- Now Send  Request To Intruder And Repeat It 100 Time By Fixing Any Arbitrary Payload Which Doesn't No Effect Request I Choose Accept-Language: en-US,en;q=0.$5$

Step 4 - See You Will Get 200 ok Status Code & 100 + Email In Your INBOX

See It Is Resulting In Mass Mailing Or Email Bombing To Your Users Which Is Bad For Business Impact.

###Solution -
I Will Recommend You To Add A Re-Captcha & Sort Of Something Which Requires Manual Human Interaction To Proceed Like You Can Add Captcha Like 2+2=___ so that it cannot be brute forced.

###Find Video Attached Below

Regards: 
Ali Shah Mughal

## Impact

If You Are Using Any Email Service Software API Or Some Tool Which Costs You For Your Email This Type Of Attack Can Result You In Financial Lose And It Can Also Slow Down Your Services It Can Take Bulk Of Storage In Sent Mail Although If Users Are Affected By This Vulnerability They Can Stop Using Your Services Which Can Lead To Business Risk.

## Attachments
- Aff.Nordvpn.mp4
