# Accessing unauthorized administration pages and seeing admin password - speakerkit.state.gov

## Report Details
- **Report ID**: 1806387
- **URL**: https://hackerone.com/reports/1806387
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-12-15T13:18:55.408Z
- **Disclosed**: 2023-03-25T13:44:22.594Z

## Reporter
- **Username**: qualw1n
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: us-department-of-state

## Vulnerability Information
## Summary:
- I discovered an issue referred to as no-redirect in a subdomain on state.gov.
When you enter the page, it directs you directly to the entrance. When I examined it via burp suite, it gave 302 found, but the homepage data was showing below.
When I tried it as admin, it still gave 302 found, but this time we could see the content of the admin page.
this way i was able to see admin user and normal user's info.
I was also able to perform many transactions.
uploading files, adding categories and many more.

## Steps To Reproduce:
1- Login to https://speakerkit.state.gov/
- and it will throw you to the page named "spklogin". Using the find and replace feature on burpsuite, I told it to change all requests that gave 302 found to 200 Ok, and I easily performed my operations.
You will be able to do it when you watch the video.

## Supporting Material/References:
https://hackerone.com/reports/1026146
https://hackerone.com/reports/95441

  * [attachment / reference]

{F2078131}
{F2078132}
{F2078133}

* [ poc / video]
████████

## Impact

access the admin page. unauthorized.

## Attachments
- image.png
- image.png
- image.png
