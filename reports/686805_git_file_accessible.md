# .git file accessible

## Report Details
- **Report ID**: 686805
- **URL**: https://hackerone.com/reports/686805
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-09-03T11:15:22.234Z
- **Disclosed**: 2019-09-13T14:56:45.003Z

## Reporter
- **Username**: nitrozeus0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: makerdao_bbp

## Vulnerability Information
Hi,
Your .git file accessible. Thats information disclosure.
URL: https://blog.makerdao.com/wp-content/themes/makerDAO/.git/config

REQUEST:
GET /wp-content/themes/makerDAO/.git/config HTTP/1.1
Host: blog.makerdao.com
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-us,en;q=0.5
Cache-Control: no-cache
Cookie: __cfduid=dc0c2f50dd600bfac5f4cb2fee9380e181567508867; wordpress_test_cookie=WP+Cookie+check; pll_language=en
Referer: https://blog.makerdao.com/wp-content/themes/makerDAO/.git/config
User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36

REGARDS.

## Impact

GIT repository files can disclose GIT repository usernames and file lists. While disclosures of this type do not provide direct attack vectors, they can be useful for an attacker when combined with other vulnerabilities discovered within the application.

## Attachments
- git.png
