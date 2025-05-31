#  The vulnerabilities found were XSS, Public disclosure, Network enumeration via CSRF, DLL hijacking.

## Report Details
- **Report ID**: 927413
- **URL**: https://hackerone.com/reports/927413
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-07-19T16:36:54.858Z
- **Disclosed**: 2020-07-21T16:30:17.762Z

## Reporter
- **Username**: b71728d7009b6664f0e2350
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Summary
IP found using ping command- 52.77.124.190 Then I used nmap tool to find the indepth information. I used burp suite and DNS scanner but it was not fruitful. Then I
explored some GitHub repositories to perform thorough web-application testing. Using
Aquatone I found some hidden domains. The results of Maltego tool and Aquatone
differed a lot. The vulnerabilities found were XSS, Public disclosure, Network
enumeration via CSRF, DLL hijacking.

**Platform(s) Affected:** Website

Details:
1. We found a domain which compiles on auth.zomato.com which is running 443
TCP as is well understood that 443 is for SSH and it is brute forcible on the IP
address
2. The next utility which I used is gitSploit. It is basically is used to find the
vulnerability and I found around 10 of them, the category varies from low to
critical.

## Impact

Information Disclosure, Server Can be Hijacked although it is not updated

## Attachments
- ZomatoReport.pdf
