# Stored XSS on 1.4.0

## Report Details
- **Report ID**: 1331281
- **URL**: https://hackerone.com/reports/1331281
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-09-06T14:25:40.146Z
- **Disclosed**: 2021-12-18T14:32:32.826Z

## Reporter
- **Username**: tehwinsam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: impresscms

## Vulnerability Information
## Summary:
The hacker (AppleBois) on Jun 19, 2020 has raise this Stored Stored Cross Site Scripting on GitHub and it has fixed on Jul 7, 2020. The hacker now raise the issue to Hackerone. Furthermore, this issue can now tracked under CVE-2020-17551.

## ImpressCMS branch :
[1.4.0 ]

## Steps To Reproduce:
  1. Navigate to modules/system/admin.php?fct=adsense&op=mod&adsenseid=4
  2. Look for the Textbar `"ID of the [adsense tag to display this ad]"`
  3. Input XSS PAYLOAD `<script>alert('AppleBois');</script>`

  1. Navigate to /modules/system/admin.php?fct=customtag&op=mod
  2. Look for the Textbar `"Name"`
  3. Input XSS PAYLOAD `<script>alert('AppleBois');</script>`

## Suggestions to mitigate or resolve the issue:
1 . Filter input on arrival. At the point where user input is received, filter as strictly as possible based on what is expected or valid input.
2 . Encode data on output. At the point where user-controllable data is output in HTTP responses, encode the output to prevent it from being interpreted as active content. Depending on the output context, this might require applying combinations of HTML, URL, JavaScript, and CSS encoding.

  Additional Reference
https://github.com/ImpressCMS/impresscms/issues/659
https://medium.com/@tehwinsam/impresscms-1-4-0-3aaf1825e6d5
https://nvd.nist.gov/vuln/detail/CVE-2020-17551
https://www.impresscms.org/modules/news/article.php?article_id=1034&title=impresscms-1-4-1-security-and-maintenance-release

## Impact

The impact of XSS, it could allow an attacker to execute malicious JavaScript so that the Cookies can send to attacker web via GET Method which could turn into account hijacking

## Attachments
No attachments
