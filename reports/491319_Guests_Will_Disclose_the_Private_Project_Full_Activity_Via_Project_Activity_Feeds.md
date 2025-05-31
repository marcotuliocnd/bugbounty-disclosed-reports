# Guests Will Disclose the Private Project Full Activity Via Project Activity Feeds

## Report Details
- **Report ID**: 491319
- **URL**: https://hackerone.com/reports/491319
- **State**: Closed
- **Severity**: none
- **Submitted**: 2019-02-05T11:30:59.833Z
- **Disclosed**: 2019-02-08T11:45:12.654Z

## Reporter
- **Username**: uzkova
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gitlab

## Vulnerability Information
Hello!

Here guests will disclose the complete activity of the project via feeds

##Reproduction Steps:

Create Private Project.

Invite Attacker as Guest.

Next attacker will go to https://gitlab.com/victimyoursz/helloproject/activity

and he access the feeds link

https://gitlab.com/victimyoursz/helloproject.atom?feed_token=FeRKF1AafTSJiLzJ5EyX


It Contains sensitive data i.e activity of the private project it can be disclosed by Guests.

###Here main thing is If guests distribute this links any unauthorized users can access this private project activity.


{F418246}

## Impact

Guests will disclose the private project activity via feeds.

## Attachments
- complete_activity_of_private_project.png
