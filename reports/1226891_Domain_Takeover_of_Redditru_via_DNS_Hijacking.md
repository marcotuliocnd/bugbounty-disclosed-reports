# Domain Takeover of Reddit.ru via DNS Hijacking

## Report Details
- **Report ID**: 1226891
- **URL**: https://hackerone.com/reports/1226891
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-15T04:41:49.877Z
- **Disclosed**: 2021-10-21T19:52:55.126Z

## Reporter
- **Username**: indianajson
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: reddit

## Vulnerability Information
## Summary

I discovered that Reddit.ru  was vulnerable to DNS hijacking via DNS provider, Reg.ru. This would allow a malicious attacker to control the content on this domain, as well as, create email addresses associated with it... I'm going to be totally honest and say that any of us ethical hackers would have nerded out giving ourselves `@reddit.ru` emails. 

## Explanation

Reviewing the WHOIS records for [Reddit.ru](https://www.whois.com/whois/Reddit.ru) you will see that this is a Reddit-owned domain and that Reg.ru nameservers are listed as the authority for the domain. However, if you had run a DIG request on Reddit.ru you would have gotten a [SERVFAIL error](https://toolbox.googleapps.com/apps/dig/#A/Reddit.ru). This is because, despite having Reg.ru set as the authoritative nameserver with the domain's registrar, the hosted zone in Reg.ru had been deleted, allowing anyone to create the missing hosted zone and take control of the domain's content, including creating email accounts.

## Proof of Concept / Verified Takeover

I created the missing Hosted Zone within Reg.ru as a proof of concept and to keep any malicious actors from hijacking the domain before Reddit could take corrective action. For a visible proof of concept, please check the [TXT records](https://toolbox.googleapps.com/apps/dig/#TXT/Reddit.ru) for Reddit.ru, which will display:

```javascript
reddit.ru.		86400	IN	TXT	"faberge@wearehackerone"
```

## Mitigation

Removing the Reg.ru nameservers for Reddit.ru from your registrar will remove the ability for someone to take control of the domain and will remove my control of the domain. No `@reddit.ru` email for me... how sad.

## Impact

First, DNS hijacking of domains has a higher severity because this vulnerability allows a malicious attacker to completely control all aspects of a domain opening the door to a variety of sophisticated attacks including phishing attacks, and malware distribution. Worse yet, domains owned by reputable companies typically receive greater leniency for spam emails from email providers, thus allowing a malicious attacker to more widely distribute spam than would otherwise be possible.

Second, similar to subdomain takeovers, DNS hijacking has become a more severe issue with the advent of open source tools such as [Modlishka](https://github.com/drk1wi/Modlishka), which would allow a malicious actor to invisibly operate a high fidelity spoof of Reddit. Simply put, nothing would indicate to a user that the site was being controlled by someone else, however, a malicious attacker would be able to invisibly siphon sensitive information without any way to identify the domain as compromised. This would be a highly effective way to siphon Russian user's Reddit credentials.  An ideal option would be to run advertisements on Google Ads targeting  Russian searches for `reddit`. 

Third, since this is a primary domain of Reddit (reddit.ru) the value of this takeover is substantially higher for its ability to negatively impact the brand and would have proven more useful had any of the attack vectors listed above to be executed against it compared to any of the other ~1,000 domains owned by Reddit. 

Overall, this takeover presents a real and present danger to Reddit, Inc.

## Attachments
No attachments
