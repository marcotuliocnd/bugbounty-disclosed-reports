# Email spoofing at weblate.org

## Report Details
- **Report ID**: 224186
- **URL**: https://hackerone.com/reports/224186
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-26T23:53:23.210Z
- **Disclosed**: 2017-06-16T14:13:09.528Z

## Reporter
- **Username**: pyrk2142
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Good day.

I found security bug at weblate.org. Now anybody may send email from weblate.org domain.

Now you have SPF policy and DMARC policy, that does not protect anything (because exists insecure domain policy: "p=none" and "sp=none"). Anybody may send email from weblate.org (or subdomain), that are not protected (because SPF does not mean, that email service will do something with spoofed email (for example, Yahoo will add it to inbox)). 

You may use https://emkei.cz/ to test this bug. For example, I sent email from admin@weblate.org (or test@mail.weblate.org) to my email and got this message.

Why it is dangerous?

Attacker may send fake email from your domain and ask user to do somethig. For example, go to site and insert password. User may trust, because email send from normal domain.

If you try send email from Facebook main site, Google domain, you will not get message. You may use DMARC Policy (with "p=reject") to prevent sending emails form your domain.



## Attachments
No attachments
