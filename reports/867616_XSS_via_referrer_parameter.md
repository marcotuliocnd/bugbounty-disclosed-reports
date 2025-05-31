# XSS via referrer parameter

## Report Details
- **Report ID**: 867616
- **URL**: https://hackerone.com/reports/867616
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-05-07T06:05:49.797Z
- **Disclosed**: 2020-10-26T16:11:27.433Z

## Reporter
- **Username**: keer0k
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
# Description
Hi, i would like to report an XSS via `javascript` scheme in `https://www.twitterflightschool.com/student/award/[ID]?referer=`, the payload e need just a click of user to be triggered because the link will be placed in `a` tag.

url:`https://www.twitterflightschool.com/student/award/███?referer=javascript:alert(document.domain)`

I attached a video demonstration:
{F818801}

# Steps to reproduce
1. go to `https://www.twitterflightschool.com/student/award/████████?referer=javascript:alert(document.domain)`
2. click in "X" button in top left of the screen
3. XSS will be triggered

## Impact

it is possible to perform malicious actions on the victim's account

## Attachments
- Screen_Recording_2020-05-07_at_03.00.26.mov
