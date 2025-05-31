# Email Spoofing Possible on djangoproject.com Email Domain

## Report Details
- **Report ID**: 418743
- **URL**: https://hackerone.com/reports/418743
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-03T22:19:36.475Z
- **Disclosed**: 2018-10-05T12:56:49.573Z

## Reporter
- **Username**: greenwolf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: django

## Vulnerability Information
**Summary:** Due to lacking a SPF and DMARC record it is possible to spoof emails from djangoproject.com. This could potentially be used to trick employees, customers or clients via phishing emails.  

**Description:** Mail servers rely on both SPF and DMARC to properly deal with email spoofing. SPF shows what servers are allowed to send emails for the current domain. However when a mail does not originate from one of the listed IP's or domains it does not automatically get rejected. What happens to the spoofed email relies of the DMARC policy of the domain. If there is no DMARC policy or the DMARC policy contains 'p=none;' then no action is taken and the email is accepted, even though SPF has failed. In this case there is neither a SPF or a DMARC record.

## Steps To Reproduce:

  1.  You can verify the missing SPF and DMARC policy with the following commands on Linux or OSX:
git clone https://github.com/BishopFox/spoofcheck
cd spoofcheck; python spoofcheck.py djangoproject.com
Verify the lines: 
[+] djangoproject.com has no SPF record!
[*] No DMARC record found. Looking for organizational record
[+] No organizational DMARC record
  2. You can test if spoofing is legitimate by sending a spoofed email using Send Grid. I have attached a small bash script which can do this for you, but you will need to provide a SendGrid username (SGUSER) and password (SGPASS) to use it. Also make sure to update the recipient email address (SGTO).


## Supporting Material/References:

  * I have attached an image of a spoofed email from vimeo.com to my outlook account called 'Vimeo-Spoofed-Email.png'. 
  * I have attached the output of spoofcheck showing the misconfigured DMARC record called 'misconfigured-dns.txt'. 
  * I have attached a small sendgrid script for you to test the spoofing called 'spooftest.sh'.

## Impact

By exploiting this issue, attackers can spoof emails from your domain, which could be used to target your customers or employees with phishing emails. 

As 90% of security breaches and compromises start with Phishing emails, allowing your domain to be spoofed removes an additional layer of protection for your customers, as they will see a legitimate from address at the top of a non legitimate email. This means an attacker doesn't have to rely on techniques such as character replacement which users have been trained to spot. E.g goggle.com or microsift.com

To fix the issue, a DMARC record containing 'p=reject;' should be added, which will cause spoofed emails to be rejected by the recipients mailbox.

## Attachments
- spooftest.sh
- Spoofed-Email.png
