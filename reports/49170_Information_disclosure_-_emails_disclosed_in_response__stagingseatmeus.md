# Information disclosure - emails disclosed in response > staging.seatme.us

## Report Details
- **Report ID**: 49170
- **URL**: https://hackerone.com/reports/49170
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-02-25T14:06:51.368Z
- **Disclosed**: 2017-05-11T11:32:43.440Z

## Reporter
- **Username**: quistertow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
Hello,
I found a  info disclosure vulnerability. We can enumerate emails via user_id parameter from Manage users.

And I found that :

>ID 1 is ██████
ID 514755 is ████████
ID 514775 is █████
ID 514764 is ███████

I attached photos from burp repeater to be more explicit.

We can easily bruteforce user_id parameter with ids to harvest user's emails.


Regards,
  Florin

## Attachments
No attachments
