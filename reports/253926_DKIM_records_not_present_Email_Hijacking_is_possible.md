# DKIM records not present, Email Hijacking is possible.....

## Report Details
- **Report ID**: 253926
- **URL**: https://hackerone.com/reports/253926
- **State**: Closed
- **Severity**: none
- **Submitted**: 2017-07-27T14:18:15.793Z
- **Disclosed**: 2017-09-16T13:39:46.220Z

## Reporter
- **Username**: kaamakya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Your SPF record is present (attachments : spf)

Which very well shows that you don't want spoofed email to be sent from your domains, but you just forget one thing:

DKIM (DomainKeys Identified Mail) is an important authentication mechanism to help protect both email receivers and email senders from forged and phishing email. Forged email is a serious threat to all parties in an email exchange.

DomainKeys Identified Mail (DKIM) is an email validation system designed to detect email spoofing by providing a mechanism to allow receiving mail exchangers to check that incoming mail from a domain is authorized by that domain's administrators and that the email (including attachments) has not been modified during transport. A digital signature included with the message can be validated by the recipient using the signer's public key published in the DNS. In technical term, DKIM is a technique to authorize the domain name which is associated with a message through cryptographic authentication.

DKIM was aimed at:

Reducing false negatives
Provide authentication reporting
Apply sender policies at the receiving end
Reduce phishing
Be scalable

Advantages:

Use with spam filtering
DKIM is a method of labeling a message, and it does not itself filter or identify spam. However, widespread use of DKIM can prevent spammers from forging the source address of their messages, a technique they commonly employ today. If spammers are forced to show a correct source domain, other filtering techniques can work more effectively. In particular, the source domain can feed into a reputation system to better identify spam. Conversely, DKIM can make it easier to identify mail that is known not to be spam and need not be filtered. If a receiving system has a whitelist of known good sending domains, either locally maintained or from third party certifiers, it can skip the filtering on signed mail from those domains, and perhaps filter the remaining mail more aggressively.

Anti-phishing
DKIM can be useful as an anti-phishing technology. Mailers in heavily phished domains can sign their mail to show that it is genuine. Recipients can take the absence of a valid signature on mail from those domains to be an indication that the mail is probably forged. The best way to determine the set of domains that merit this degree of scrutiny remains an open question; DKIM has an optional feature called ADSP that lets authors that sign all their mail self-identify, but the effectiveness of this approach is questionable, and ADSP was demoted to historic status in November 2013

Compatibility
Because it is implemented using DNS records and an added RFC 5322 header field, DKIM is compatible with the existing e-mail infrastructure. In particular, it is transparent to existing e-mail systems that lack DKIM support

Protocol overhead
DKIM requires cryptographic checksums to be generated for each message sent through a mail server, which results in computational overhead not otherwise required for e-mail delivery. This additional computational overhead is a hallmark of digital postmarks, making sending bulk spam more (computationally) expensive.his facet of DKIM may look similar to hashcash, except that the receiver side verification is not a negligible amount of work.

Generate your DKIM easily here: http://dkimcore.org/tools/keys.html

You can read more about DKIM records and their uses here: http://www.gettingemaildelivered.com/dkim-explained-how-to-set-up-and-use-domainkeys-identified-mail-effectively.

Now, to check if the DKIM record is present or not in weblate run below command

 "nslookup -querytype=TXT google._domainkey.weblate.org"

The DKIM record is not present in weblate.org (attachments : poc), Which shows that you are missing this security feature.

You should publish a valid DKIM record for your domain to prevent any misunderstanding and to prevent hackers from using your email.

DKIM for hackerone is attached below (attachments : hackerone):

## Attachments
- spf.JPG
- hackerone.JPG
- poc.JPG
