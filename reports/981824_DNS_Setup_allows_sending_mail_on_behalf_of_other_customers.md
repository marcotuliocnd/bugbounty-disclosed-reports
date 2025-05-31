# DNS Setup allows sending mail on behalf of other customers

## Report Details
- **Report ID**: 981824
- **URL**: https://hackerone.com/reports/981824
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-14T16:41:04.206Z
- **Disclosed**: 2021-02-21T16:02:32.495Z

## Reporter
- **Username**: aisforarray
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: basecamp

## Vulnerability Information
# Sent on your behalf

I knew basecamp themselves had used helpscout for support, so I was
curious to see if hey was doing the same.  A quick DNS lookup gave me the answer
I was looking for:

```
dig hey.com txt                     

; <<>> DiG 9.10.6 <<>> hey.com txt
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 48297
;; flags: qr rd ra; QUERY: 1, ANSWER: 4, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;hey.com.			IN	TXT

;; ANSWER SECTION:
hey.com.		60	IN	TXT	"cyssd1dn8z15bmffrprj1hzycw436gzh"
hey.com.		60	IN	TXT	"google-site-verification=k7w8RY2bLljThqEsIGQOoQlclHp19HawwdiHTq2nJpw"
hey.com.		60	IN	TXT	"google-site-verification=VH8KKQzQ7gWsKxSsibqBexLteqs254PwGFS37Hf22MQ"
hey.com.		60	IN	TXT	"v=spf1 include:_spf.hey.com include:helpscoutemail.com -all"

;; Query time: 39 msec
;; SERVER: 192.168.42.1#53(192.168.42.1)
;; WHEN: Fri Jun 26 17:20:34 PDT 2020
;; MSG SIZE  rcvd: 315
```

Ok.  That's interesting.  helpscoutemail.com has permissions to send email on
behalf of hey.com.  For completeness let's look at helpscoutmail.com spf
records:

```
dig helpscoutemail.com txt

; <<>> DiG 9.10.6 <<>> helpscoutemail.com txt
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47004
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
;; QUESTION SECTION:
;helpscoutemail.com.		IN	TXT

;; ANSWER SECTION:
helpscoutemail.com.	300	IN	TXT	"v=spf1 ip4:54.173.229.38 ip4:52.0.20.102 ip4:54.174.116.32 ip4:52.2.238.96 ip4:52.20.146.34 ip4:34.198.122.65 ~all"

;; Query time: 42 msec
;; SERVER: 192.168.42.1#53(192.168.42.1)
;; WHEN: Fri Jun 26 17:32:45 PDT 2020
;; MSG SIZE  rcvd: 174
```

### How can we exploit this?

First, let's go ahead and create an account over at helpscout.  It can be
anything.  Let's setup an inbox.  Again, it can be anything, doesn't really
matter.  What **does** matter is that we setup a custom address for the inbox.
Of course, helpscout makes sure we have access to the email address we're
acting as.  

So let's go ahead and setup an email as dhhracing@hey.com.  First, we sign up
for a trial on hey.com with that email.  All good.  Now, let's enter that into
helpscout.  Once we get the verification email in hey, we enter the verification
in helpscout.  But... generally there is another step.  Helpscout needs to have
permission to send on our behalf.  How do they do that?  With DNS records for
SPF, DKIM and DMARC.  But... hey.com has already done that as they themselves
are helpscout customers.

Now here is where the trouble comes in.  hey.com has a recycle policy.  If you
create a trial but never pay, or as for a refund, then after 30 days the email
address becomes available again.  So let's go ahead and cancel our
dhhracing@hey.com account (in hey, not in sendgrid).  Now we wait 30 days.  Now,
DHH realizes he needs an address for his racing.  So he goes to hey.com and
creates an account under dhhracing@hey.com.  And what do you know, it's
available!

But now, not only can DHH send email from dhhracing@hey.com, but SO CAN I.  From
my helpscout account.  Of course, I won't receive mail from that account, but I
could always just send out mail and CC another address that I own and hope for a
reply-all.  But really, the options for scamming are limitless.

I've suggested a few options to hey.com:

1. Don't use the primary domain on helpscout.  Setup heysupport.com or
   something similar.
2. Don't ever recycle accounts.  I can only ever see this causing issues.
3. Get helpscout to treat hey.com as a mail provider and don't allow sending
   from their domain.

## Impact

An attacker could spoof any hey.com email address that they had originally created an address for (and had been recycled).  This could allow them to appear to be a high-profile individual or company.  By CCing an address that they currently own they could receive replies from the correspondence as well.

## Attachments
No attachments
