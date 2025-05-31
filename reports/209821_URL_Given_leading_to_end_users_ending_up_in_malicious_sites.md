# URL Given leading to end users ending up in malicious sites

## Report Details
- **Report ID**: 209821
- **URL**: https://hackerone.com/reports/209821
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-03-01T10:10:32.598Z
- **Disclosed**: 2017-03-01T22:15:49.827Z

## Reporter
- **Username**: ant_pyne
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Hi,

I found a design issue in the profile statement for the registered user. This is dependant on the end user however.

In the profile statement, one can write something as well giving links is allowed. This, I think is by design. However, let us suppose the authenticated user creates a website of his own which is basically a phishing page. Or he gives links to malicious websites.

Next he sends the link of his page to the victim. Try out this page.
https://gratipay.com/~www.google.com/.

Here the first link is to www.google.com. However, the next link is unknown and can be malicious.

Yes, this depends on the end user completely but I still think this is an issue.

Mitigation: Allow only alphabets or display the entire thing as text. The end user can copy paste the link in the browser if it is that relevant.

Thanks & Regards,
Dipmalya Pyne

## Attachments
- URLRedirection_Gratipay.jpg
