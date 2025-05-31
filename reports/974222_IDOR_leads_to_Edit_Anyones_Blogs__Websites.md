# IDOR leads to Edit Anyone's Blogs / Websites

## Report Details
- **Report ID**: 974222
- **URL**: https://hackerone.com/reports/974222
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-09-03T17:41:58.243Z
- **Disclosed**: 2020-11-18T14:20:47.759Z

## Reporter
- **Username**: ali
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello there,
I hope all is well!

Steps:
1. Go to `https://intensedebate.com/signup` and create 2 accounts.
2. Login as victim and go to `https://www.intensedebate.com/edit-user-profile`
3. Click `Add Blog / Website` text and fill the form > click `Save Settings` button
4. Go to `https://www.intensedebate.com/edit-user-profile`, again and search `radMainSite` text in page source and copy value.   
{F975085}
5. Then login as attacker.
6. Go to `https://www.intensedebate.com/edit-user-profile` > click `Add Blog / Website` text and fill the form > click `Save Settings` button
7. Go to `https://www.intensedebate.com/edit-user-profile`, again and click `Save Settings` button > open burp suite and change `hidBlogID` parameter with victim's `hidBlogID`.
8. Forward the request and go to victim's account. Check your website informations. You will see it's changed.

PoC:   
{F975096}

## Impact

Changing victim's website/blog informations.

Best Regards,
@mygf

## Attachments
- 1.png
- 3.png
- bandicam_2020-09-03_20-39-49-941.mp4
