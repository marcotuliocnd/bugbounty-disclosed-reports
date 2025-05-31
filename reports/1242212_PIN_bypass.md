# PIN bypass

## Report Details
- **Report ID**: 1242212
- **URL**: https://hackerone.com/reports/1242212
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2021-06-23T14:36:05.900Z
- **Disclosed**: 2021-06-29T20:19:24.430Z

## Reporter
- **Username**: tushar_rec0n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: myetherwallet

## Vulnerability Information
## Summary:

MEW apk has improper rate limit.


When we try to brute force the PIN, we are rate limited for 5 minutes after 5 or 6 attempt.


In my testing I found that it was checking the device's local time so by changing it we can brute force the PIN.


## Steps To Reproduce:

1.Install MEW app from play store.

2.Create your PIN.

3.Now open again your MEW apk.

4.You will be asked to enter the PIN.

5.Try to brute force the code. You will see a message to try again after 5 min.

6.Now change the time of your device.

7.Observe there is no rate limit now.

## Supporting Material/References:


{F1350023}

## Impact

An attacker can brute force the PIN of an user

## Attachments
- bandicam_2021-06-23_19-57-14-572.mp4
