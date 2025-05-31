# Email Verification bypass on signup

## Report Details
- **Report ID**: 1040047
- **URL**: https://hackerone.com/reports/1040047
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-11-21T09:29:57.967Z
- **Disclosed**: 2020-12-03T08:43:26.221Z

## Reporter
- **Username**: haqsek2
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:
This bug is related to wordpress.com. There is feature in wordpress.com which allow users to invite people. We have to enter email address to invite that particular person but the invite link and invite key is also available to the person who invited. This allow attackers to create the profile without having access to the email address and they can make account on behalf of any people who  is not already signed up in wordpress.com

## Platform(s) Affected:
wordpress.com
public-api.wordpress.com

## Steps To Reproduce:
This issue can be reproduced by following these easy steps: 
* Login to your account on wordpress.com
* Setup burpsuite proxy with browser.
* Select your site and navigate to manage>people
* Enter any email address which is not already registered in wordpress.com and invite
* Open this url in browser: https://wordpress.com/people/invites/yoursite.wordpress.com   [change yoursite.wordpress.com with your site]
* See the burp suite proxy tab and find the GET request to this endpoint [https://public-api.wordpress.com/rest/v1.1/sites/siteId_here/invites?http_envelope=1&status=all&number=100]     [there will be a number instead of siteId_here]
* In response of this GET request you will see JSON which will be consisting of the details about the invitations sent and there you will find "invite_key" and "link".
* Copy the link and open this in another browser.
* You can create account on behalf of this email without having access to the email and email verification is bypassed :)

**See the attached video for POC**

## Mitigation:
This is the pure violation of secure design principles, this can be mitigated by just removing the [invite_key] and [link] from the response in [https://public-api.wordpress.com/rest/v1.1/sites/siteId_here/invites?http_envelope=1&status=all&number=100]. Because this invite key and link is the property of the person being invited, showing these creds to other people will result this type of issue.

## Impact

This issue can be used to bypass email verification on signup. Attackers can create account on behalf on any person without having access to the email account. This issue is affecting integrity of the wordpress.com

## Attachments
- wordpresscom-2020-11-21_01.21.40.mp4
