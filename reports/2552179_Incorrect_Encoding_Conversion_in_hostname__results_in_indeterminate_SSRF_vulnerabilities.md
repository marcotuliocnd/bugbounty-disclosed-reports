# Incorrect Encoding Conversion in hostname  results in indeterminate SSRF vulnerabilities

## Report Details
- **Report ID**: 2552179
- **URL**: https://hackerone.com/reports/2552179
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-06-14T08:39:47.217Z
- **Disclosed**: 2024-06-18T10:52:09.175Z

## Reporter
- **Username**: z3r0yu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: curl

## Vulnerability Information
## Summary:
Best-Fit is a character mapping strategy designed to resolve the issue when characters in the source code page lack a direct equivalent in the target code page. During the conversion of characters from a Unicode code page to a non-Unicode code page, if a corresponding character cannot be located, the conversion is carried out using a predefined Best-Fit conversion table.

For instance, the Best-Fit Mapping conversion table for GBK encoding (cp936) can be found at: https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit936.txt

This table contains some intriguing character conversions, such as 0xb9 being mapped to 1 and 0xb2 being mapped to 2. By exploiting this conversion feature, it is possible to construct a hostname that causes curl to initiate network requests to unintended locations, potentially resulting in an SSRF vulnerability.

Initially, this parsing feature was utilized by orange from the DEVCORE team to circumvent the defenses in [CVE-2012-1823](https://www.kb.cert.org/vuls/id/520827) and subsequently discover the vulnerability [CVE-2024-4577](https://devco.re/blog/2024/06/06/security-alert-cve-2024-4577-php-cgi-argument-injection-vulnerability-en/). However, our research team’s testing has revealed that curl supports partial best-fit conversion features on all Chinese operating systems. By exploiting this parsing issue, it is possible to create certain security impacts.

## Details

### Affected components

The vulnerable component is:

- curl: https://github.com/curl/curl
- 8.7.1 and below

The operating systems affected are:

This feature is supported on Windows, macOS, and Ubuntu (Linux) operating systems with Traditional Chinese, Simplified Chinese, and Japanese language settings.

## Steps To Reproduce:
We constructed the following payload:

```
http://¹²7.0.0.1
```

The character mapping relationships are as follows:

0xb9 --> displayed as ¹ --> parsed by curl as 1

0xb2 --> displayed as ² --> parsed by curl as 2

The parsing behavior of curl clearly adheres to  [CODEPAGE 936](https://www.unicode.org/Public/MAPPINGS/VENDORS/MICSFT/WindowsBestFit/bestfit936.txt)

{F3357294}

We are uncertain whether the display of ¹² varies across different operating systems, but here is a comparison result provided by Python, demonstrating that ¹² != 12.

{F3357295}

### Test

The PoC used for testing here is shown below.

```python
curl -g 'http://¹²7.0.0.1' -v -o /dev/null
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

Figure 1 illustrates the parsing behavior of curl on a Chinese Ubuntu system. It can be observed that a request was successfully made to 127.0.0.1, even though the input hostname was different [¹²7.0.0.1].

{F3357297}

Figure 2 illustrates the parsing behavior of curl on an English Ubuntu system. It shows that the best-fit encoding conversion was not followed, which is expected since the English operating system does not support GBK encoding.

{F3357298}

Figure 3 illustrates the parsing behavior of curl on a Chinese macOS system.

{F3357299}

Figure 4 illustrates the parsing behavior of curl on a Chinese Windows system.

{F3357301}


##  Impact
The impact of this vulnerability is huge because the `curl`  is widely used. In many cases, developers need a blocklist to block on some IPs. However, the vulnerability will help attackers bypass the protections that developers have set up for schemes and hosts. The vulnerability will lead to SSRF[1] and RCE[2] vulnerabilities in several cases.

## Impact

Attackers can exploit this parsing difference to initiate requests to unexpected locations, thereby causing potential SSRF vulnerability threats.

## Attachments
- image-20240614154339276.png
- image-20240614154930952.png
- image-20240614155923543.png
- image-20240614161214560.png
- image-20240614161157157.png
- image-20240614161119610.png
