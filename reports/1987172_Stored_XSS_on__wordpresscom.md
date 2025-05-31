# Stored XSS on  wordpress.com

## Report Details
- **Report ID**: 1987172
- **URL**: https://hackerone.com/reports/1987172
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-05-14T00:48:58.383Z
- **Disclosed**: 2023-05-19T14:08:50.342Z

## Reporter
- **Username**: riadalrashed
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
## Summary:

Hi team

I found Stored XSS in wordpress.com via  app.crowdsignal.com


## Platform(s) Affected:
 wordpress.com

## Steps To Reproduce:
1 . Go to https://app.crowdsignal.com/dashboard and create a poll
2 . Put the payload as answer <img src=x onerror=alert(document.cookie)>
3.  Go to Share Your Poll and Copy  the Website Popup
4.Go to https://wordpress.com/posts add new post
5. App Website Popup 
6. Save it
7.Open the page and the XSS will fired

█████████

## Impact

The attacker can use this issue to execute malicious script code in the victim user browser also redirect the victim user to malicious sites

## Attachments
No attachments
