# If the website does not impose additional defense against CSRF attacks, failing to use the 'Lax' or 'Strict' values could increase the risk of exposur

## Report Details
- **Report ID**: 1707680
- **URL**: https://hackerone.com/reports/1707680
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-09-21T16:53:40.646Z
- **Disclosed**: 2022-11-30T15:15:02.499Z

## Reporter
- **Username**: shubhangirathore836
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
## Summary:
[Cookies are typically sent to third parties in cross-origin requests. This can be
abused to do CSRF attacks. Recently a new cookie attribute named SameSite was
proposed to disable third-party usage for some cookies, to prevent CSRF attacks.
Same-site cookies allow servers to mitigate the risk of CSRF and information leakage
attacks by asserting that a particular cookie should only be sent with requests
initiated from the same registrable domain.]

## Platform(s) Affected:
[website :-   This may lead to Cross-Site-Request-Forgery (CSRF) attacks if there are no additional protections in place (such as Anti-CSRF tokens). 
Technical Impact: Modify Application Data ]

## Steps To Reproduce:
[Go to website www.yelp.com/ and inspect the website and go application and cookie.  and check Sensitive Cookie with Improper SameSite Attribute.
]

  1. [Cookie "myCookie" rejected because it has the "SameSite=None" attribute but is missing the "secure" attribute.

This Set-Cookie was blocked because it had the "SameSite=None" attribute but did not have the "Secure" attribute, which is required in order to use "SameSite=None".]
  2. [The server can set a same-site cookie by adding the SameSite=...attribute to the Set-Cookie
header. There are three possible values for the SameSite attribute:
• Set-Cookie: key=value; SameSite=Lax
• Set-Cookie: key=value; SameSite=Strict
• Set-Cookie: key=value; SameSite=None; Secure]
  

## Supporting Material/References:
[ https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite, https://owasp.org/www-community/SameSite, https://web.dev/samesite-cookies-explained/ (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

Technical Impact: Modify Application Data
If the website does not impose additional defense against CSRF attacks, failing to use the 'Lax' or 'Strict' values could increase the risk of exposure to CSRF attacks. The likelihood of the integrity breach is Low because a successful attack does not only depend on an insecure SameSite attribute. In order to perform a CSRF attack there are many conditions that must be met, such as the lack of CSRF tokens, no confirmations for sensitive actions on the website, a "simple" "Content-Type" header in the HTTP request and many more.

## Attachments
No attachments
