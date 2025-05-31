# Open SMTP port can let anyone send email from mail.chihar.com

## Report Details
- **Report ID**: 223435
- **URL**: https://hackerone.com/reports/223435
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-04-24T13:07:36.985Z
- **Disclosed**: 2017-05-20T12:34:24.535Z

## Reporter
- **Username**: str33
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
An open SMTP port 587 can let anyone connect and send emails impersonating someone in your the company if he could enumerate the email addresses.

POC - 
1.  I performed an nmap scan and was able to find an open port 587 for SMTP
2. I did a netcat connection to it and was able to run commands such as HELO and EHLO(which is harmless)
3. I could even use commands STARTTLS and MAIL TO.
4. I can impersonate the support team of weblate and send an email to one of the employees asking them to visit a link and even though they know about phishing they might do it and hence stealing their sessionID.

The image shows few commands which I was able to run on the server.

Pretty much all the companies have strong email security policies and hence you should implement it and deny end user access to the SMTP server.




## Attachments
- Capture2.PNG
