# Cross Site Scripting

## Report Details
- **Report ID**: 224108
- **URL**: https://hackerone.com/reports/224108
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-26T17:06:48.936Z
- **Disclosed**: 2017-04-26T17:36:30.399Z

## Reporter
- **Username**: lulliii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Hello team,
While i was hunting (https://help.nextcloud.com), i found xss there in comment/reply box..

**Steps to reproduce**
1. go to https://help.nextcloud.com.
2. Click On Any (I'm selecting "Welcome to the Nextcloud forums")
3. Sign in or Sign up in your account.
4. Click Reply..
5. Type or paste ( <abbr title='" class="comment-link"><a href='
href="'> :-) <abbr title='" ' class="<script>alert(document.cookie)</script>">x</abbr></a> ) Without brackets..
6. You will get popup (You need to be logged in to do that.)
7. This mean xss payload is executing!

**Detail:**
I think xss payload is executing because you're using old version of akismet..
Akismet 2.5.0-3.1.4 - Is vulnerable to  Unauthenticated Stored Cross-Site Scripting (XSS).. 

Reference: https://wpvulndb.com/vulnerabilities/8215

## Attachments
No attachments
