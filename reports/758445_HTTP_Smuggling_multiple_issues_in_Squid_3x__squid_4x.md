# HTTP Smuggling multiple issues in Squid 3.x & squid 4.x

## Report Details
- **Report ID**: 758445
- **URL**: https://hackerone.com/reports/758445
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-12-14T11:11:17.654Z
- **Disclosed**: 2021-08-26T23:57:28.217Z

## Reporter
- **Username**: regilero
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ibb

## Vulnerability Information
Hello, as can be seen on a recent public security update by Squid I reported several smuggling issues.
If you want some background on impact of Smuggling issues You can check the current works of James Keetle or my own previous published works.

* https://www.youtube.com/watch?v=upEMlJeU_Ik  HTTP Desync Attacks: Smashing Into The Cell Next Door - James Kettle
* https://www.youtube.com/watch?v=dVU9i5PsMPY  DEF CON 24 - regilero - Hiding Wookiees in HTTP: HTTP smuggling

But I'm quite sure that the recent additions of Smuggling tools in Burp suite is making Smuggling impacts issues more easy to understand now.

# CVE-2019-18678
 
* http://www.squid-cache.org/Advisories/SQUID-2019_10.txt

current score (5 / 5.3) available at :
* https://www.suse.com/fr-fr/security/cve/CVE-2019-18678/

> --------------------------
> Advisory ID:        SQUID-2019:10
> Date:               November 05, 2019
> Summary:            HTTP Request Splitting issue
>                     in HTTP message processing.
> Affected versions:  Squid 3.0 -> 3.5.28
>                     Squid 4.x -> 4.8
> Fixed in version:   Squid 4.9
> ---------------------------->
> 
> http://www.squid-cache.org/Advisories/SQUID-2019_10.txt
> 
> (...)
> 
> Credits:
> 
>  This vulnerability was discovered by by Régis Leroy (regilero
>  from Makina Corpus).
>
> Fixed by Amos Jeffries of Treehouse Networks Ltd.
>  Revision history:
>
>  2019-07-24 11:52:51 UTC Initial Report
>  2019-09-11 02:52:52 UTC Patches Released
>  2019-11-04 13:43:22 UTC CVE Assignment

I can give more details than what is publicly available.
On the initial report from 2019-07-24 there were 4 issues. Only 1 of these issues is currently covered by the CVE-2019-18678.

## Issue 1 : undisclosed Squid 3 issue

There is also an undisclosed Security filter bypass for Squid 3.x. This is a wonfix for Squid because Squid 3.x is not maintained anymore.
Without complete details this is an abuse of separators characters which allows access to urls where a security filter in Squid is present to prevent such locations from being accessed.

Project maintainer response:

> Please be aware that Squid-3 has been deprecated for several years now.
> Several of the problems you are pointing out are well-known issues with
> the HTTP protocol design from RFC2616 itself not being clear. Squid-3
> primarily implements that specification, with only sprinkling of RFC7230.
>
> Squid-4 increases the upgrade to RFC7230 specification with
> implementation of the majority of message parsing updates. Though that
> is still an ongoing work.
>
> (...)
> As do Squid-4 releases. The fix is to upgrade the proxy to a version
> where the problem has been fixed.

## Issue 2 : HTTP Response Splitting issue on bad withespaces before header's colon

Squid allowed bad withespaces characters between the header title and the colon (before value).
This is forbidden in RFC 7230.

> 3.2.  Header Fields
>
> Each header field consists of a case-insensitive field name followed
> by a colon (":"), optional leading whitespace, the field value, and
> optional trailing whitespace.
> header-field   = field-name ":" OWS field-value OWS
> field-name     = token
> (...)
> 
> 3.2.4.  Field Parsing
> (...)
> **No whitespace is allowed between the header field-name and colon**.  In
> the past, differences in the handling of such whitespace have led to
> security vulnerabilities in request routing and response handling.  **A**
> **server MUST reject any received request message that contains**
> **whitespace between a header field-name and colon** with a response code
> of 400 (Bad Request).  A proxy MUST remove any such whitespace from a
> response message before forwarding the message downstream.

This could be used to perform HTTP Smuggling attacks (if you want more details on exploitations I can add some very detailled examples, I'll just give you a short version).

Various invalid syntax where a space or pseudo space is added before ':' in the header line could be used against Squid to obtain an HTTP Response splitting attack:

* Transfer-Encoding : chunked\r\n
* Transfer-Encoding\t: chunked\r\n
* Transfer-Encoding\f: chunked\r\n
* Transfer-Encoding\f: chunked\r\n
* Transfer-Encoding\r: chunked\r\n
* Transfer-Encoding\x0b: chunked\r\n
* Transfer-Encoding\t\x0b \r\f: chunked\r\n

Squid would give 3 response for this request (it should see only 2 requests, one from 01 to 12, and one from 13 to 15, but Squid saw one from 01 to 08, one from 09 to 12 and one from 14 to 15):

01 POST /?t=41 HTTP/1.1\r\n
02 Host: dummy-host.example.com\r\n
03 X-REQUEST-IDENTIFIER: 41\r\n
04 Content-Length: 92\r\n
05 Transfer-Encoding\x0b: chunked\r\n
06 \r\n
07 0\r\n
08 \r\n
09 GET /foo.html?t=42 HTTP/1.1\r\n
10 Host: dummy-host.example.com\r\n
11 X-REQUEST-IDENTIFIER: 42\r\n
12 \r\n
13 GET /bar.html?t=43 HTTP/1.1\r\n
14 Host: dummy-host.example.com\r\n
15 X-REQUEST-IDENTIFIER: 43\r\n
15 \r\n

Impacts are quite high, like HTTP Cache poisoning for any actor set in front of Squid, and security filter bypass for this previous actor also. Adding extra responses from the Squid stream is definitively a good way for adding choas on the HTTP chain (Dos, Xss, etc).

## Issue 3 : Undisclosed SeverSide Request Forgery issue

This one is only fixed on master. The fix is not present on any published version of Squid. So we may talk about it later.


## Issue 4 : Undisclosed HTTP Request Splitting

This one is still present and not yet fixed. So we may talk about it later, because I think it will be fixed one day.
I'm pretty sure this issue will soon be discovered by other bounty hunters. So I don't know if I should already give more details to claim precedence, currently I'll keep the details undisclosed and let the project maintainers act on that.

## Summary

Issue `#2` is the one covered by the published CVE.
For issues `#3` & `#4` I'm pretty sure that I will make reports later.
For issue `#1` I'm not sure this can be covered by this program, I could give you more details if you want.

## Impact

Like most HTTP Smuggling issue impact is not always directly targeted on Squid, here (if we only talk about issue #2) the impact is very important for HTTP actors set in front of squid (like an SSL terminator).

Cache poisoning,  DOS, XSS, etc.

## Attachments
No attachments
