# No rate limiting in changing room subject.

## Report Details
- **Report ID**: 418145
- **URL**: https://hackerone.com/reports/418145
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-10-03T12:23:54.508Z
- **Disclosed**: 2018-10-09T03:59:44.566Z

## Reporter
- **Username**: cunn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
Before i shed more light on this: I noticed i can create over 200 apps but i don't really know how valid that was.
I want to report that there is no rate limiting  in changing room subject.
Attacker scenrio:
1. Navigate to https://chaturbate.com/b/your username
2. Try to create a room subject and capture the request.
3. Send to intruder and repeater it numerous times.
4. I tried this 144 times and it was succesful
Thanks
Below is a video as a poc

## Impact

bruteforcing.

## Attachments
- ScreenCapture_2018-10-3_05.20.00.mp4
