# suppress version in Server header on gratipay.com or grtp.co

## Report Details
- **Report ID**: 123742
- **URL**: https://hackerone.com/reports/123742
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-03-17T00:52:23.891Z
- **Disclosed**: 2016-07-14T16:31:42.608Z

## Reporter
- **Username**: caffeine
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
Summary:
Server version information is returned in the response headers.

Estimated severity: Low

More info:
Any page requested on the site returns a lot of information in the response headers. This information includes specific version information for the server and proxy. The following version information is revealed: gunicorn 18.0 and vegur 1.1. While neither of these version have known, published vulnerabilities available but updates are available for both.

Impact:
An attacker can use the information provided to find known vulnerabilities, if they exist. If known vulns do not exist, the site is still at risk of being targeted when an issue is discovered.

Recreation:
1. Proxy all traffic through Burp.
2. Request any page.
3. Examine the response for exposed version information

Vulnerable request:
>GET / HTTP/1.1
>Host: gratipay.com:443
>Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
>Accept-Encoding: gzip, deflate, sdch
>Accept-Language: en-US,en;q=0.8
>Cookie: csrf_token=f8wF2Qs0pUGuRd857KNhiSDMDfbPtZUW
>DNT: 1
>Upgrade-Insecure-Requests: 1
>User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36

Response:
>HTTP/1.1 200 OK
>Cache-Control: no-cache
>Connection: keep-alive
>Content-Type: text/html; charset=UTF-8
>Date: Thu, 17 Mar 2016 00:31:50 GMT
>Server: gunicorn/18.0
>Set-Cookie: csrf_token=f8wF2Qs0pUGuRd857KNhiSDMDfbPtZUW; expires=Thu, 24 Mar 2016 00:31:50 GMT; Path=/; secure
>Transfer-Encoding: chunked
>Via: 1.1 vegur
>X-Content-Type-Options: nosniff
>X-Frame-Options: SAMEORIGIN
>X-Gratipay-Version: 1943
>X-Xss-Protection: 1; mode=block

Recommendation: 
1. The server should be configured to reveal less information. Instructions: http://stackoverflow.com/questions/16010565/how-to-prevent-gunicorn-from-returning-a-server-http-header
2. Out-of-date components should be updated immediately and a patch/update management should be implemented and followed.

## Attachments
No attachments
