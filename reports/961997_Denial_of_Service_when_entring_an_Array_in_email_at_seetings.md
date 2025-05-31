# Denial of Service when entring an Array in email at seetings

## Report Details
- **Report ID**: 961997
- **URL**: https://hackerone.com/reports/961997
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-08-19T02:36:43.012Z
- **Disclosed**: 2020-08-19T11:02:28.855Z

## Reporter
- **Username**: stilobit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
in settings `https://demo2.nextcloud.com/index.php/settings/users/TweLbFT93aqRnEfF/settings`
when you submit the request with email value Array the server return `500 Internal Server Error`
Poc video:
F954435

## Impact

denial a service attack on the server. This may lead to the website becoming slow or unresponsive.

## Attachments
- Screen_Recording_2020-08-19_at_3.19.11_AM.mov
