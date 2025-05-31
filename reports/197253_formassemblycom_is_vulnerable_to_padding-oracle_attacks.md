# formassembly.com is vulnerable to padding-oracle attacks.

## Report Details
- **Report ID**: 197253
- **URL**: https://hackerone.com/reports/197253
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-10T13:38:12.460Z
- **Disclosed**: 2017-03-17T16:53:51.058Z

## Reporter
- **Username**: edoverflow
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: formassembly

## Vulnerability Information
Dear Formassembly bug bounty team,

# Summary
---

formassembly.com is vulnerable to CVE-2016-2107, allowing remote attackers to obtain sensitive information via padding-oracle attacks.

~~~
$ git clone https://github.com/FiloSottile/CVE-2016-2107.git
$ go run main.go www.formassembly.com
... Vulnerable: true
~~~

The code above checks whether the TLS alert is `DATA_LENGTH_TOO_LONG` (vulnerable) or `BAD_RECORD_MAC` (not vulnerable).

# What is CVE-2016-2107?
---

Filippo Valsorda, the author of the tool I used to discover this issue, wrote a fantastic article on CVE-2016-2107 here: https://blog.cloudflare.com/yet-another-padding-oracle-in-openssl-cbc-ciphersuites/

# What are padding-oracle attacks?
---

During the decryption and the HMAC verification process the length of the padding is revealed. Padding-oracle attacks iterate over the padding of the cryptographic message, revealing the contents of the message.

# More information
---

While I am at it I may as well let you know that you also support 1024-bit Diffie-Hellman keys. I would recommend using a 2048-bit Diffie-Hellman group.

Link to GitHub repo: https://github.com/FiloSottile/CVE-2016-2107
Link to online test: https://filippo.io/CVE-2016-2107/

Yours sincerely,
Ed



## Attachments
No attachments
