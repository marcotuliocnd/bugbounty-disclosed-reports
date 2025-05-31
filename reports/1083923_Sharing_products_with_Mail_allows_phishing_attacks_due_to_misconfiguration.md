#  Sharing products with Mail allows phishing attacks due to misconfiguration.

## Report Details
- **Report ID**: 1083923
- **URL**: https://hackerone.com/reports/1083923
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-22T02:34:09.026Z
- **Disclosed**: 2021-04-25T00:13:31.730Z

## Reporter
- **Username**: grmx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: openmage

## Vulnerability Information
Hello Team. I found a part that could cause a phishing attack. Incorrect configuration in the part of sharing products with mail causes this.

1. Go to https://demo.openmage.org/sendfriend/product/send/id/430/cat_id/20/
2. The Sender email address should normally be an email address provided by you. Here, our own e-mail address allows us to send an e-mail to a user with an e-mail address that does not belong to us.
3. Then write the e-mail address of the person you will send the e-mail to and send it.
4. Check your mailbox and spam box. You can send mail from accounts that do not belong to you.


Correction: We can only choose the e-mail address to send. You can get yourself an e-mail address and use that e-mail address to share products.
Example: An e-mail address in the form of sharefriend@demo.openmage.org. This will likely prevent this event.

## Impact

It enables phishing attacks.

## Attachments
No attachments
