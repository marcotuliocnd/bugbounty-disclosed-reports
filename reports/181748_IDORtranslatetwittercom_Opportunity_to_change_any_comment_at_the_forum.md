# [IDOR][translate.twitter.com] Opportunity to change any comment at the forum

## Report Details
- **Report ID**: 181748
- **URL**: https://hackerone.com/reports/181748
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-11-12T13:24:04.119Z
- **Disclosed**: 2017-05-12T20:35:58.486Z

## Reporter
- **Username**: kedrischh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
POC: https://translate.twitter.com/forum/getting-started/topics/7037/posts/43287/edit
Steps to reproduce:
1) Go to any forums topic for example: https://translate.twitter.com/forum/getting-started/topics/7037
2) View source code of the page and take post id (screenshot "idor edit.jpg")
3) Append "/posts/*post_id*/edit" to url at the first step (screenshot "idor edit 2.jpg")
4) Make some change at the comment and save it

## Attachments
- idor_edit_2.jpg
- idor_edit.jpg
