# Incorrect Type Conversion in interpreting IPv4-mapped IPv6 addresses and below `curl` results in indeterminate SSRF vulnerabilities.

## Report Details
- **Report ID**: 2493548
- **URL**: https://hackerone.com/reports/2493548
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2024-05-07T15:11:55.706Z
- **Disclosed**: 2024-05-08T07:17:29.462Z

## Reporter
- **Username**: z3r0yu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Octal Type Handling of Errors in IPv4 Mapped IPv6 Addresses in curl  allows unauthenticated remote attackers to perform indeterminate SSRF, RFI, and LFI attacks on many programs that rely on curl. 

[RFC 4291](https://datatracker.ietf.org/doc/html/rfc4291#section-2-5-5) defines ways to embed an IPv4 address into IPv6 addresses. One of the methods defined in the RFC is to use IPv4-mapped IPv6 addresses, that have the following format:

```
   |                80 bits               | 16 |      32 bits        |
   +--------------------------------------+--------------------------+
   |0000..............................0000|FFFF|    IPv4 address     |
   +--------------------------------------+----+---------------------+
```

In IPv6 notation, the corresponding mapping for `127.0.0.1` is `::ffff:127.0.0.1` ([RFC 4038](https://datatracker.ietf.org/doc/html/rfc4038)). Although curl correctly converts octal numbers starting with 0 in IPv4 format, such as recognizing 0177.0.0.1 as 127.0.0.1, it fails to properly identify the data format of 0127.0.0.1 in IPv4-mapped IPv6 addresses. The curl command automatically removes the leading zeros from IP addresses in the format ::ffff:0127.0.0.1, and sends requests to 127.0.0.1 instead. This behavior can undermine defensive strategies that restrict access to 127.0.0.1, potentially leading to security threats such as Server-Side Request Forgery (SSRF) and Remote Code Execution (RCE) on the server.

## Steps To Reproduce:

### 2.1 Affected components

The vulnerable component is:

- curl: https://github.com/curl/curl
- 8.7.1 and below

### 2.2 Attack scenario

A typical attack scenario is illustrated in the diagram below. The Validator checks whether the attacker-supplied URL is on the blocklist. If not, the URL is passed to the Requester for processing. The Requester is responsible for sending requests to the hostname specified by the URL.

{F3251582}

### 2.3 PoC

payloads:

```
http://[::ffff:0127.000.0.1]/
```

You can verify this issue using the sample program below. Simply replace the payload variable in the verify function with the above payload to conduct the test.

```python
curl http://[::ffff:0127.000.0.1]/
```

I set up an HTTP server on my local machine using port 80 with the following Python code. Upon a successful request, the server will return the string "FindVuln".

```Python
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "FindVuln"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, threaded=True)

```

Figure 1 illustrates how curl handles IPv4 addresses, while Figure 2 demonstrates curl's processing of IPv4-mapped IPv6 representations.

Figure 1:

{F3251583}

Figure 2:

{F3251584}

## Mitigation

Please refer to [RFC 4291](https://datatracker.ietf.org/doc/html/rfc4291#section-2-5-5) and [RFC 4038](https://datatracker.ietf.org/doc/html/rfc4038) to fix this function.

## Supporting Material/References:

This security issue has also been identified in other libraries, and CVE IDs have been assigned. For more information, refer to [1], [2], [3] and [4]. 

[1] https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-24329

[2] https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22243

[3] https://sick.codes/sick-2021-015/

[4] https://sick.codes/sick-2021-016/

## Impact

The impact of this vulnerability is huge because the `curl`  is widely used. In many cases, developers need a blocklist to block on some IPs. However, the vulnerability will help attackers bypass the protection developers have set up for schemes and hosts. The vulnerability will lead to SSRF[1] and RCE[2] vulnerabilities in several cases. 

[1] https://cwe.mitre.org/data/definitions/918.html
[2] https://cwe.mitre.org/data/definitions/94.html

## Attachments
- image-20240507225530596.png
- image-20240507230111068.png
- image-20240507230208127.png
