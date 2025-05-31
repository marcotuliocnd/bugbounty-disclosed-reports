# On Singing up with a Phone number , The 4 digit OTP does not expires for a long time leading to an easy attack and make a verified account easilty

## Report Details
- **Report ID**: 792295
- **URL**: https://hackerone.com/reports/792295
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-02-10T18:35:08.910Z
- **Disclosed**: 2020-11-25T18:11:12.110Z

## Reporter
- **Username**: theuniversaldude
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
Hello there how are you doing ?
Go to sign up page and enter a new phone number and you will be redirected to https://bumble.com/registration/confirm-phone .
You will receive a easy breakable 4 digit OTP Code .
I waited for about 4 hours and the OTP did not expired , This shows that the OTP can be easily bruteforced even having the rate limiting , assuming rate limiting is implemented as this is an old program .
The OTP can be bruteforced , by changing IP via VPN and as the OTP does not expires for a long time it gives sufficient time , to get the actual OTP Code also the OTP is only of 4 digits , So it only requires 10,000 requests .


For Solving of this issue , Captcha Implementation is recommended .
POC - Please check screenshots

## Impact

Impact
Registering with a different person mobile number without actual verification .
Impersonating other's identity .

## Attachments
No attachments
