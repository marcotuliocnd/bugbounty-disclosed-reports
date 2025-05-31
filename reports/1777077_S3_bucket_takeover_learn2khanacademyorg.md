# S3 bucket takeover [learn2.khanacademy.org]

## Report Details
- **Report ID**: 1777077
- **URL**: https://hackerone.com/reports/1777077
- **State**: Closed
- **Severity**: high
- **Submitted**: 2022-11-17T16:57:14.561Z
- **Disclosed**: 2022-12-29T06:12:13.014Z

## Reporter
- **Username**: fdeleite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
The subdomain learn2.khanacademy.org was pointed  to Amazon S3, but no bucket with that name was registered [learn2.khanacademy.org]. This meant that anyone could sign up for Amazon S3, claim the bucket as their own and then serve content.

## Steps to reproduce
 
Check the following url:
http://learn2.khanacademy.org

Also

```
>  curl -k http://learn2.khanacademy.org/
<!doctype html>
<html>
  <head>
    <title>S3 takeover POC</title>
  </head>
  <body>
    <p>This is S3 takeover POC </p>
  </body>
</html>
```

## Impact

It's extremely vulnerable to attacks as a malicious user could create any web page with any content and host it on the `ford.com` domain. This would allow them to post malicious content which would be mistaken for a valid site. 

They could perform several attacks like:
 - Cookie Stealing
 - Phishing campaigns. 
 - Bypass Content-Security Policies and CORS.
 
## Recommendations for fix

* Remove the affected DNS record
 

### Supporting Material/References:

 - https://0xpatrik.com/subdomain-takeover/
 - https://hackerone.com/reports/661751

## Attachments
No attachments
