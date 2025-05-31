# csp bypass + xss

## Report Details
- **Report ID**: 153666
- **URL**: https://hackerone.com/reports/153666
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-07-25T11:37:10.338Z
- **Disclosed**: 2017-07-05T23:53:00.642Z

## Reporter
- **Username**: b6117130df17feef13481e3
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,

On my previous report (number 126464) I've mentioned that 
analytics.twitter.com has a CSP bypass which I couldn't exploit that time.

Now, I've found a reflected XSS on careers.twitter.com which again I couldn't exploit by itself. Because you have CSP, and I've combined two of them to successfully trigger XSS.

If you visit the url:
https://careers.twitter.com/en/jobs-search.html?location=1%22%3E%3Cscript%20src=//analytics.twitter.com/tpm?tpm_cb=alert%28document.domain%29%3E//

you will see xss triggered. 

Regards.

## Attachments
- ct1.jpg
