# [parc.informatica.com] Reflected Cross Site Scripting and Open Redirect

## Report Details
- **Report ID**: 178278
- **URL**: https://hackerone.com/reports/178278
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-26T19:40:50.097Z
- **Disclosed**: 2017-04-29T15:08:23.233Z

## Reporter
- **Username**: bogdantcaciuc
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hi !
I just want to report you a vulnerability in your subdomain ,,parc''

**Description**

In this link *https://parc.informatica.com/partners/apex/Cloud_chat?endpoint=* the vulnerable parameter is ,,endpoint''. Once the parameter takes the value of a XSS vector or a website link the code is executed after we complete the form.

**Steps to reproduce**

Go to *https://parc.informatica.com/partners/apex/Cloud_chat?endpoint=javascript:alert(document.domain)*

After you complete the form, alert executed document.domain .

and Open redirect: *https://parc.informatica.com/partners/apex/Cloud_chat?endpoint=http://evil.com* after you complete the form, you are redirected to evil.com

I think it's valid because in your scope is *.informatica.com
Thanks for attention !

## Attachments
No attachments
