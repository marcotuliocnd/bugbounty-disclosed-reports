# Stored XSS templates -> 'call for action' feature

## Report Details
- **Report ID**: 237927
- **URL**: https://hackerone.com/reports/237927
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-06-08T08:04:58.056Z
- **Disclosed**: 2017-06-09T17:41:09.049Z

## Reporter
- **Username**: r0h17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mixmax

## Vulnerability Information
Hi Jeff,

Reporting the Stored XSS in template section on 'call for action' button. (Already discussed in mail)
1] Login to Mixmax and navigate to template section
2] Click on enhance and select call for action button
3] Enter anything in button text and in URL enter XSS payload (javascript:alert(document.cookie))
4] Insert the button and click it to execute XSS.

Impact : XSS can be stored in template and when Team manager/admin uses that template and clicks the button , our XSS executes 

Thank you

## Attachments
No attachments
