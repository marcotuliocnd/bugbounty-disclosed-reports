# Store XSS on Informatica University via transcript (informatica.csod.com)

## Report Details
- **Report ID**: 219509
- **URL**: https://hackerone.com/reports/219509
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-04-08T13:09:13.224Z
- **Disclosed**: 2017-09-09T18:15:06.379Z

## Reporter
- **Username**: alfredsaonoy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hi,

Vulnerable field: Training Description

Steps to reproduce:
1. Login to your account and go Informatica University.
2. You can either click on "My Training" or "Universal Profile" at the upper right hand corner of the page.
3. You will then be redirected to the Universal profile bio page, click on the "Transcript tab"
4. Select options on the upper right side then select "Add external training: on the drop down option.
5. Fill out the needed information but for the Training Description use the following payload:
'"><img src=x onerror=alert(document.cookie);>
6. Complete the rest of the form and click on Submit.
7. You will then be redirected to your training transcript.
8. On the right side of the transcript which has a label withdraw, select from the drop down "View training details"
9. The page will be redirected and you will then get the xss pop-up.

Would be best to sanitize all input on this form to avoid xss. 

Works on latest versions of chrome, and firefox.


Please let me know if you need further information. Thanks!

Cheers,

@ninjakatz__


## Attachments
No attachments
