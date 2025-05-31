# demo.nextcloud.com: Content spoofing due to default Apache Error Page

## Report Details
- **Report ID**: 155189
- **URL**: https://hackerone.com/reports/155189
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-29T21:45:14.614Z
- **Disclosed**: 2016-09-29T19:03:00.012Z

## Reporter
- **Username**: sysecure
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hi ,I would like to report report a text injection and a miss-configuration of the 403 page which can be used in phishing.

POC:

https://demo.nextcloud.com//this%20website%20-----------------------------------------------------------------------------------------------------------------------------------------------------------------------%20thanks%20for%20visiting%20our%20website,becase%20we%27re%20having%20some%20problems%20we%20have%20been%20moved%20to%20this%20site%20http:/www.malicious.com%20please%20note%20that%20our%20website%20is%20no%20longer%20exist%20Fix%20:

Just use a 403 page that don't include attacker text just as hackerone do 
or just as you do in your in other not found pages.

Thanks !


## Attachments
- Screenshot_(175).png
