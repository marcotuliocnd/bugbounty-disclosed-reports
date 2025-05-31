# Send email asynchronously

## Report Details
- **Report ID**: 128856
- **URL**: https://hackerone.com/reports/128856
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-04-07T02:15:36.529Z
- **Disclosed**: 2017-03-17T17:58:17.878Z

## Reporter
- **Username**: hharry
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
It seems like the https://gratipay.com/~USER/emails/modify.json endpoint has some protection to prevent email flooding as seen here https://github.com/gratipay/gratipay.com/blob/master/gratipay/models/participant.py#L407 plus CSRF validation.

However, it is possible to flood the server with multiple email requests as long as you send different email addresses. This might be a door to a DoS attack considering emails are sent synchronous on the request (this means each email sending request will hold that thread and connection for quite a good time). Finally, depending on what email server you are using, if this can be abused you might end up paying for a lot of sent emails.

Note that I'm not 100% sure there's no other kind of throttling on this endpoint and I was too afraid to test.

Below is the screenshot of a few sent emails showing how all of them were sent correctly and high time it took on the server and another one of me receiving all of them.

## Attachments
- emails.PNG
- emails2.png
