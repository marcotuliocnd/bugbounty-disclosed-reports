# Incoming email hijacking on sc-cdn.net

## Report Details
- **Report ID**: 168476
- **URL**: https://hackerone.com/reports/168476
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-15T02:13:20.493Z
- **Disclosed**: 2016-09-23T22:53:53.259Z

## Reporter
- **Username**: rubyroobs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: snapchat

## Vulnerability Information
Hey guys!

Really interesting find here.

### Summary
These dangling MX records on `sc-cdn.net` have allowed me to purchase an email account with GoDaddy (owner of these servers) and send/receive email from an account on this domain.

```
sc-cdn.net.		3599	IN	MX	0 smtp.secureserver.net.
sc-cdn.net.		3599	IN	MX	10 mailstore1.secureserver.net.
```

### Reproduction
As I now "own" this email URL on GoDaddy, in theory you can't register another email address yourself. To prove that I've taken it over, feel free to email me on `rubyroobs@sc-cdn.net` and I'll be able to paste the message I receive into here to prove ownership of it.

### Mitigation
Delete these DNS records to avoid mail being hijacked on this domain.

### Impact
I believe impact of hijacking incoming emails on this address far outweighs the smaller consequences of missing SPF records. This would allow me to setup accounts on this email and in some cases allow me to prove control of the domain or impersonation of Snapchat staff.

Been super fun investigating this - not my typical find honestly :D. Let me know if you need any help triaging!

Cheers,
@rubyroobs

## Attachments
No attachments
