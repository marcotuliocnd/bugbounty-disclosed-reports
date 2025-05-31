# HTML Injection in E-mail Not Resolved ()

## Report Details
- **Report ID**: 1600720
- **URL**: https://hackerone.com/reports/1600720
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-06-14T17:22:20.520Z
- **Disclosed**: 2022-07-19T09:11:30.236Z

## Reporter
- **Username**: thewikiii
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary
On this report  " https://hackerone.com/reports/1536899  "  You closed the report and changed the status to Resolved.
But it's Not Resolved The Bug  It's Still there 

## Steps To Reproduce

    1.Please register at https://www.acronis.com/en-us/products/cyber-protect/trial/#registration with the victim's email.
    2. Inject "First Name" field with HTML tags, for example:    "/><img src="x"><a href="https://evil.com">login</a>.
    3.Check the email inbox, HTML tags will be executed. "Your Acronis Cyber Protect trial starts today!" 

Proof of Concept: 
                                         F1774045

## Impact

HTML injection into emails is dangerous!

* Your users are at risk when a hacker is able to take control of the emails that your applications send, but what's especially dangerous is that the emails       will be coming from your company email address.

*  When a malicious email comes from your company email, it looks a lot more legitimate.

## Attachments
- screen-recording(4).webm
