# XSS and cache poisoning via upload.twitter.com on ton.twitter.com

## Report Details
- **Report ID**: 84601
- **URL**: https://hackerone.com/reports/84601
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-08-25T10:42:44.552Z
- **Disclosed**: 2019-05-01T23:05:34.697Z

## Reporter
- **Username**: filedescriptor
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi,
I would like to report an issue where attackers can bypass the upload restriction on upload.twitter.com to cause XSS on ton.twitter.com and cache poisoning.

##Detail
When using upload.twitter.com to upload audience data, it checks if the file type is allowed and rejects any harmful files (e.g. .html). However it fails to reject files with unknown file type. For example, ```foobar.html``` is rejected while ```foobar.test``` is passed. Since the server does not recognize the file type, it outputs the file without sending the ```Content-Type``` header in the response. The lack of such header results in browser sniffing for the document type. In this case, attackers can insert HTML to perform XSS. Normally the file uploaded is only accessible to the uploader which makes it a self-XSS, but with signed requests attackers can force victims to be able to view the file, thus triggering XSS on behalf of the victim.

###Cache poisoning
Attackers can take this attack further and perform cache poisoning on victim's browser. Since it allows uploading files, attackers can upload a cache manifest file (HTML5 AppCache) to control the cache behaviors over ton.twitter.com. There are two things the attacker can achieve:

1. Attacker can force victim's browser to cache the XSS file. That means it creates a persistent XSS on victim's browser even if the XSS file on the server is removed. 
2. Attacker can control all returning contents on the domain. For example, attacker can replace contents of any file on ton.twitter.com (in victim's perspective)

##Repo step
1. Go to Twitter Ads > Tools > Audience manager > Create new list audience
2. Upload a normal file under "Upload your data file." and intercept the request
3. Change the parameter *blobstore_url* with an unknown suffix (e.g. 1440354519600.txt => 1440354519600.test)
4. Replace the parameter *content* with any XSS vector (e.g. <script>alert(1)</script>)
5. The uploaded file now contains XSS
6. To make it accessible to others, sign it with OAuth token

##PoC
You may also visit http://innerht.ml/pocs/twitter-upload-xss to see the attack in action.

Video demo: https://vimeo.com/137155736 (password: appcache)

The PoC demonstrates the XSS. It also shows how it can influence contents of other pages (poisoning http://ton.twitter.com/).

## Attachments
No attachments
