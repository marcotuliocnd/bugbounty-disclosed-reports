# Stored XSS via Discussion Title and Send as Email attribute in [marketplace.informatica.com]

## Report Details
- **Report ID**: 203912
- **URL**: https://hackerone.com/reports/203912
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-02-06T18:05:31.580Z
- **Disclosed**: 2017-04-08T12:39:29.782Z

## Reporter
- **Username**: fillawful
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
POC
===
1.  Under "Your Stuff" choose to "Create a Discussion/Ask a question"
2. Choose a space to submit your discussion/question. Any space will do.
3. Title your discussion with the payload `"><img src=x onerror=alert(1)>`
4. Choose "Post message" to publish.
5. View the message as any user. Under "Actions" choose to "Send as Email"
6. Observe XSS poc alert box"

Please let me know if you have any questions.

## Attachments
- Email_XSS.PNG
- Message_title.PNG
