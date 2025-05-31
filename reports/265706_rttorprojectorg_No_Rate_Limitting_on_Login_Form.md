# [rt.torproject.org] No Rate Limitting on Login Form

## Report Details
- **Report ID**: 265706
- **URL**: https://hackerone.com/reports/265706
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-09-04T03:22:39.943Z
- **Disclosed**: 2023-11-28T09:01:38.643Z

## Reporter
- **Username**: 0xspade
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
Hello Team,

**Description**
I just Notice that you didn't implement a captcha or Rate Limiting on one of your sub-domain which is vulnerable to brute force.

**Proof Of Concept**
Download {F218177} 
You can use your own wordlist to test my python script
Usage:
```
~$ python tor.py -t username -p passwordlist.txt
```
it should be just like this if the script runs 
{F218178}

Results on burpsuite when i try to login 500 times
{F218179}

**Fix / Mitigation**
You can implement a Rate Limit or Captcha in Login Form :)

Let me know if you needs more info and i will look forward to your reply.
Kind Regards,


## Attachments
- wordlist.txt
- tor.py
- Screenshot_at_2017-09-04_11-09-47.png
- Screenshot_at_2017-09-04_10-37-42.png
