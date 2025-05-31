# Email Spoofing Possible on torproject.org Email Domain

## Report Details
- **Report ID**: 423336
- **URL**: https://hackerone.com/reports/423336
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-13T13:52:20.135Z
- **Disclosed**: 2018-10-16T08:26:23.333Z

## Reporter
- **Username**: greenwolf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: torproject

## Vulnerability Information
**Summary:** Due to a missing SPF and DMARC record it is possible to spoof emails from torproject.org. This could potentially be used to trick employees or users via phishing emails.  

**Description:** Mail servers rely on both SPF and DMARC to properly deal with email spoofing. SPF shows what servers are allowed to send emails for the current domain. However when a mail does not originate from one of the listed IP's or domains it does not automatically get rejected. What happens to the spoofed email relies of the DMARC policy of the domain. If there is no DMARC policy or the DMARC policy contains 'p=none;' then no action is taken and the email is accepted, even though SPF has failed. 

## Steps To Reproduce:

  1.  You can verify there is no SPF or DMARC policy with the following commands on Linux or OSX:
$ dig torproject.org txt
Verify there is not SPF record.
$ dig _dmarc.torproject.org txt
Verify there is no DMARC record.

## Supporting Material/References:

  * I have attached an image of a spoofed email from security@torproject.org to my outlook account called 'Spoofed-Email.png'. 
  * I have attached an image of some OSINT output, showing that a number of [company] employees use this email domain. 'OSINT-Showing-Primary-Domain.png'
  * I have attached a small sendgrid script for you to test the spoofing called 'spooftest.sh'.

## Impact

By exploiting this issue, attackers can spoof emails from your domain, which could be used to target your customers or employees with phishing emails. 

As 90% of security breaches and compromises start with Phishing emails, allowing your domain to be spoofed removes an additional layer of protection for your customers, as they will see a legitimate from address at the top of a non legitimate email. This means an attacker doesn't have to rely on techniques such as character replacement which users have been trained to spot. E.g goggle.com or microsift.com.

To fix the issue, a DMARC record containing 'p=reject;' should be added, which will cause spoofed emails to be rejected by the recipients mailbox. 

Further Reading: https://blog.detectify.com/2016/06/20/misconfigured-email-servers-open-the-door-to-spoofed-emails-from-top-domains/
https://posts.specterops.io/gathering-open-source-intelligence-bee58de48e05
> This may sound like a small thing, but it can be a severe issue when misunderstood. Once, while working with a client, they had to respond to a nasty phishing incident. The attacker was, very convincingly, spoofing their email addresses to employees and other organizations. This simple check for DMARC and SPF records helped them understand what had happened. They thought SPF and vendor-provided email security solutions had spoofing on lockdown, so they moved to the next logical assumption, that the accounts had been compromised. However, they had never setup a DMARC record. Spoofing is a deceitfully difficult thing for many organizations because email security is so frequently misunderstood and so many exceptions are made for marketing, PR, automated alert emails, and other situations where spoofed emails are being used legitimately.

## Attachments
- OSINT-Showing-Primary-Email-Domain.png
- Spoofed-Email.png
- spooftest.sh
