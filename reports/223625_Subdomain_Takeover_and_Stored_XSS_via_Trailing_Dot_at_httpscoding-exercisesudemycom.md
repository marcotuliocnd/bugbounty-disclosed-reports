# Subdomain Takeover (and Stored XSS) via Trailing Dot at https://coding-exercises.udemy.com

## Report Details
- **Report ID**: 223625
- **URL**: https://hackerone.com/reports/223625
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-04-25T02:02:54.095Z
- **Disclosed**: 2018-05-10T18:51:56.450Z

## Reporter
- **Username**: cha5m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: udemy

## Vulnerability Information
Hello @Udemy!

Summary
=====
I previously reported a cross-site scripting vulnerability ( #222337 ) at coding-exercises.udemy.com. I recently discovered that GitBook-hosted sites are also vulnerable to subdomain takeovers due to a trailing dot vulnerability in the GitBook "Custom Domain" feature (seen below).

{F179119}

Proof of Concept
=====
The taken-over subdomain can be found here: `https://coding-exercises.udemy.com.` (notice the trailing dot).

First, we will look at the ```dig``` results for ```coding-exercises.udemy.com.``` (with the trailing dot)

```
Chases-MacBook-Air:~ chase$ dig coding-exercises.udemy.com.

; <<>> DiG 9.8.3-P1 <<>> coding-exercises.udemy.com.
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38225
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;coding-exercises.udemy.com.	IN	A

;; ANSWER SECTION:
coding-exercises.udemy.com. 1	IN	CNAME	www.gitbooks.io.
www.gitbooks.io.	3301	IN	CNAME	cdn.gitbook.com.
cdn.gitbook.com.	2494	IN	A	138.197.194.9

;; Query time: 342 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Mon Apr 24 21:24:39 2017
;; MSG SIZE  rcvd: 115
```
And now the ```dig``` results for ```coding-exercises.udemy.com```
```
Chases-MacBook-Air:~ chase$ dig coding-exercises.udemy.com

; <<>> DiG 9.8.3-P1 <<>> coding-exercises.udemy.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 1203
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;coding-exercises.udemy.com.	IN	A

;; ANSWER SECTION:
coding-exercises.udemy.com. 267	IN	CNAME	www.gitbooks.io.
www.gitbooks.io.	3268	IN	CNAME	cdn.gitbook.com.
cdn.gitbook.com.	2461	IN	A	138.197.194.9

;; Query time: 785 msec
;; SERVER: 192.168.1.1#53(192.168.1.1)
;; WHEN: Mon Apr 24 21:25:12 2017
;; MSG SIZE  rcvd: 115
```

Mitigation
=====
I noticed that this service is hosted by GitBook, however, your bug bounty brief does not state that third-party hosted services being out of scope. I have also reported these issues directly to GitBook in an attempt to get them resolved ASAP. However, it might be worthwhile for you, an actual GitBook customer, to reach out directly to get them resolved quicker.

Example
=====
Here is an example of another report with a trailing dot causing a subdomain takeover in a service:
* https://hackerone.com/reports/174417

Please let me know if you have any other questions. I would be more than happy to help! :)

Thank you and best regards,
n0rb3r7

## Attachments
- Screen_Shot_2017-04-24_at_9.24.06_PM.png
