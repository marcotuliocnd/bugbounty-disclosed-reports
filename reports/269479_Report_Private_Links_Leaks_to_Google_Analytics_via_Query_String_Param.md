# Report Private Links Leaks to Google Analytics via Query String Param

## Report Details
- **Report ID**: 269479
- **URL**: https://hackerone.com/reports/269479
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-09-19T14:01:25.564Z
- **Disclosed**: 2017-10-25T23:45:14.669Z

## Reporter
- **Username**: r3y
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hello HackerOne Team,

According to HackerOne privacy

>>HackerOne sometimes partners with third-party services which may use various tracking technologies to provide certain services or features, including targeted online marketing. These technologies allow a partner to recognize your computer or mobile device each time you visit HackerOne, __but do not allow access to Your Information from HackerOne.__ For a list of current partners, please contact us at support@hackerone.com.

### Summary:

When the report is still private, no one will get access to any of the report contents aside from the reporter (participants) and security team members.

But i have found that when the report contents have a link URLs and any participants clicks the link, the link was being leaked to external domain which is Google Analytics.

### Impact:

Most of the researcher provides a link/url as a PoC pointing to some video reproduction steps, that link is private only for the sec team to reproduce the issue, but security teams didn't know that the link provided by the researcher already leak upon clicking the link.

Please note that most of the link for PoC video contains sensitive information such steps to reproduce the bug.

### Steps to reproduce:

  1. Click any url/link on the private report and capture the request using burp.
  2. Observe that there is a `POST` that leaks the private link to google analytics before after redirecting to the external link warning page.

__PoC Screenshot:__

{F222163}

### Scenario:

  1. Look at my vimeo public profile there is no video uploaded yet: https://vimeo.com/user70143644
  2. But in reality i have uploaded a private video with a private link: https://vimeo.com/232320359/fa452a0137
  3. Now the private link is for the security team to reproduce the issue.
  4. When i create a report with this content: https://vimeo.com/232320359/fa452a0137 and the sec team clicks that, the below PoC POST request was being called and it will redirect to external domain warning page.

```
POST /r/collect HTTP/1.1
Host: www.google-analytics.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:55.0) Gecko/20100101 Firefox/55.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Content-Type: text/plain
Referer: https://hackerone.com/
Content-Length: 428
Origin: https://hackerone.com
DNT: 1
Connection: close

v=1&_v=j62&a=2078508761&t=pageview&_s=1&dl=https%3A%2F%2Fhackerone.com%2Fredirect%3Fsignature%3D336dc1060a5ccbf5ef7063cabbfa33873202c35e%26url%3Dhttps%253A%252F%252Fvimeo.com%252F232320359%252Ffa452a0137&ul=en-us&de=UTF-8&dt=Leaving%20HackerOne...&sd=24-bit&sr=1600x900&vp=1600x743&je=0&_u=SCCAAUAjI~&jid=346100484&gjid=1015600924&cid=1626748485.1504716574&uid=78347&tid=UA-49905813-1&_gid=545891595.1505791144&_r=1&z=1287598365
```

Observe the __dl__ and __url__ parameter:

__dl:__ Contains the hackerone signature
__url:__ Contains the private PoC link

`dl=https%3A%2F%2Fhackerone.com%2Fredirect%3Fsignature%3D336dc1060a5ccbf5ef7063cabbfa33873202c35e%26url%3Dhttps%253A%252F%252Fvimeo.com%252F232320359%252Ffa452a0137`

Let me know if anything else is needed.

Regards
@reydd


## Attachments
- private_link_leaked.png
