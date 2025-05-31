# subdomain takeover at news-static.semrush.com

## Report Details
- **Report ID**: 294201
- **URL**: https://hackerone.com/reports/294201
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-12-01T10:04:40.130Z
- **Disclosed**: 2018-01-10T13:08:29.070Z

## Reporter
- **Username**: 0ways
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
**Summary:** The subdomain news-static.semrush.com can be taken over by attackers and abuse it for further attacks (Phishing, XSS Cross origin, malware, etc..).

**Description:** The subdomain news-static.semrush.com was pointed using CNAME to Amazon S3, but no bucket with that name was registered. This meant that anyone could sign up for Amazon S3, claim the bucket as their own and then serve content on news-static.semrush.com

**Browsers Verified In:**
  * Google Chrome v62.0.3202.94 
  * FireFox ESR v52.5.0

**Steps To Reproduce:** 
  1. Open AWS account
  2. Create s3 bucket and claim the subdomain news-static.semrush.com
  3. upload poc.html file to the bucket

**Supporting Material/References:**

```
$ dig A news-static.semrush.com @8.8.8.8

; <<>> DiG 9.8.3-P1 <<>> A news-static.semrush.com @8.8.8.8
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 35678
;; flags: qr rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;news-static.semrush.com.	IN	A

;; ANSWER SECTION:
news-static.semrush.com. 59	IN	CNAME	s3.amazonaws.com.
s3.amazonaws.com.	3459	IN	CNAME	s3-1.amazonaws.com.
s3-1.amazonaws.com.	4	IN	A	52.216.21.165
```

**POC**
http://news-static.semrush.com/POC_2313521212.html

This means that nobody else can claim the bucket and add content.

**Mitigation/Fix** 
I have claimed the bucket on my account so no one can claimed it before I release it.
Remove the news-static.semrush.com DNS entry. Alternatively, if you wish to use news-static.semrush.com with S3, tell me in a comment and I will remove the bucket from my Amazon account.

## Impact

The attacker will own the subdomain and can do whatever he want with it, such as Phishing, XSS that can affect all *.semrush.com to bypass cross origin policy and upload malwares. etc..

## Attachments
- Screen_Shot_2017-12-01_at_1.04.23_PM.png
