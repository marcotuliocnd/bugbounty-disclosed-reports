# No rate limit in otp code sending

## Report Details
- **Report ID**: 1060518
- **URL**: https://hackerone.com/reports/1060518
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-12-16T22:44:15.765Z
- **Disclosed**: 2021-08-16T19:57:32.255Z

## Reporter
- **Username**: aliyugombe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:

There is no rate limit in sendind otp code. Thus, attacker can use this vulnerability to bomb out the mobile inbox of the victim.

## Steps To Reproduce:

##Step 1.
Open burp suite, and click on "Intercept is on " button from Proxy tab.

##Step 2.
Launch browser and visit https://mtnonline.com/nim, and fill all the required fields, then submit.

##Step 3.
Open burp suite window, and click on "HTTP history" under "Proxy" Tab, scroll on the history list and navigate on the history with https://mtnonline.com host and /nim/otp URL, and right click to "Send to Intruder".

##Step 4.
Click on "Intruder" tab -> click "Position" -> click "Clear" button,
and click on "Payloads", under payload type -> Select "Null payloads", In generate input, enter 10 .

##Step 5.
Click on "Attack" button, and click ok on the pop-up screen.


##NOTE : I only limit the sms as 10 for testing, but attacker can send unlimited sms in short time.



## Supporting Material/References:

  * [attachment / reference]

## Impact

Attacker can bomb victim mobile inbox and cause MTN to loose the charges of sms in vein.

## Attachments
- Screenshot_20201216-234013.png
- Screenshot_at_2020-12-16_22-56-21.png
