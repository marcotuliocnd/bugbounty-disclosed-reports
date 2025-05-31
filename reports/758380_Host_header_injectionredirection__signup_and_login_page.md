# Host header injection/redirection | signup and login page

## Report Details
- **Report ID**: 758380
- **URL**: https://hackerone.com/reports/758380
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-12-14T06:19:36.707Z
- **Disclosed**: 2020-02-21T11:27:12.055Z

## Reporter
- **Username**: hassancypher
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
Hey Team.

There's a host header injection vulnerability in  signup and login page.

If possible, the application should avoid incorporating user-controllable data into redirection targets. In many cases, this behavior can be avoided in two ways:
Remove the redirection function from the application, and replace links to it with direct links to the relevant target URLs.
Maintain a server-side list of all URLs that are permitted for redirection. Instead of passing the target URL as a parameter to the redirector, pass an index into this list.

Vulnerable URL:
https://affiliates.nordvpn.com/signup

Payload: " Host: constitutionclub.in"

How to reproduce this vulnerability:

1.Open this URL "https://affiliates.nordvpn.com/signup" 
2.Send it to the repeater in burp suite add the payload to the header request and forward the request.
3.It will directly redirect to constitutionclub.in

## Impact

Whenever a user visits this URL, it will redirect them to site.com. It is used in phishing attacks.

## Attachments
- bandicam_2019-12-13_22-59-14-360.mp4
