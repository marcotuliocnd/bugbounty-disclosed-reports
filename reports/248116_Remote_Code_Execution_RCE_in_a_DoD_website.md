# Remote Code Execution (RCE) in a DoD website

## Report Details
- **Report ID**: 248116
- **URL**: https://hackerone.com/reports/248116
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2017-07-10T22:22:00.839Z
- **Disclosed**: 2019-10-04T15:21:20.372Z

## Reporter
- **Username**: manoelt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Summary:**
One of the DoD applications uses a java library which is vulnerable to expression language injection. Using only an URL I was able to inject java code. I made a simple PoC that requests a name resolution to a DNS server.

**Description:**
The application at https://███ uses Primefaces version 5.3 which is vulnarable to Expression Language injection through DynamicContent generator.

To prove the injection I made a PoC that tries to submit a HTTP request, but the server blocks the outgoing packets on port 80, on the other hand the server still try to resolve the requested domain and so I receive DNS requests from DoD server. Also, I can delete and maybe read files using the File Java class, but I decided not to try to avoid leak of some private data.

## Impact
Critical.

## Step-by-step Reproduction Instructions

First you need to execute the program attached to generate the payload. To do that you just need the Primefaces-5.3.jar (https://www.primefaces.org/downloads/ ) in your class path.

1. With the code attached generate the payload encrypted with the default key "primefaces". Change the domain (String remoteMalJarUrl) to one that you have control or use one from http://dnsbin.zhack.ca/
2. With the payload from #1, append to the URL: https://████/javax.faces.resource/dynamiccontent.properties.xhtml?pfdrt=sc&ln=primefaces&pfdrid=
3. Send a GET request using curl (curl -vk https://████/javax.faces.resource/dynamiccontent.properties.xhtml?pfdrt=sc&ln=primefaces&pfdrid=<YOUR_PAYLOAD_HERE>
4. You will receive a name resolution request for remoteMalJarUrl from the DoD application

We could use this DNS request to exfiltrate data from the server. And as I said, theoretically I could also delete files from the server using the File class.

## Product, Version, and Configuration (If applicable)
Primefaces 5.3

## Suggested Mitigation/Remediation Actions
- Update Primefaces
- Alternatively by filtering incoming requests with pfdrid parameter (value longer than 16bytes and Base64 encoded) and "pfdrt=sc" is possible to mitigate the attack: "pfdrt=sc" calls the vulnerable StreamedContent Method and pfdrid contains the exploit payload. 

## References
http://blog.mindedsecurity.com/2016/02/rce-in-oracle-netbeans-opensource.html
https://github.com/primefaces/primefaces/issues/1152

## Attachments
No attachments
