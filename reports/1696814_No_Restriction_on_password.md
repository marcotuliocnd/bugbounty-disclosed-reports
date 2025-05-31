# No Restriction on password

## Report Details
- **Report ID**: 1696814
- **URL**: https://hackerone.com/reports/1696814
- **State**: Closed
- **Severity**: none
- **Submitted**: 2022-09-10T07:42:49.136Z
- **Disclosed**: 2022-09-13T05:02:42.519Z

## Reporter
- **Username**: mta-sts
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Note- 1:  When I report this issue to another program, the triaged expert said ( The server is now only hashing a reasonable size password, this should not cause a Denial of Service . Since there does not appear to be evidence of DoS occurring here)

So they will take action, Only when ddos appear.

Note- 2:  (For Gitlab) while seeing (Note-1), You will also consider as same but here the interesting is happened.

My scope is not to attempt ddos to your server, because you exclude any activity related to denial of service to your assets. But without proof there is no way prove, so that I have put payloads to password field and I got internal server error from your side.


Description: 

Hey, When I tried to reset the password,  I noticed that you haven't kept any password limit.

You need to decrease password length: There are two reasons for limiting the password size. For one, hashing a large amount of data can cause significant resource consumption on behalf of the server and would be an easy target for a Denial Of Service attack.

Normally all sites have a password minimum to maximum lengths like 72 characters limit or 48 limits to prevent Denial Of Service attack.

All valid POC has been attached, So Investigate and fix the problem soon.

## Impact

The server might not be able to handle such characters coming from different machines simultaneously. The attacker can perform a DDOS attack by using this vulnerability.

## Attachments
- poc_gitlab.mov
- Screenshot_(318).png
- payload.txt
