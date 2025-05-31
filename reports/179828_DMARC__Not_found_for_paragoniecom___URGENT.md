# DMARC  Not found for paragonie.com   URGENT

## Report Details
- **Report ID**: 179828
- **URL**: https://hackerone.com/reports/179828
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2016-11-03T05:28:37.727Z
- **Disclosed**: 2016-11-03T05:30:49.574Z

## Reporter
- **Username**: not_hackerone_hero
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: paragonie

## Vulnerability Information
#Hi sir, ,

I am  new hacker in hackerone platform  I am glad to join paragonie bounty program  ..i  want to report a very critical bug that is i found DMARC   missing for your domain paragonie.com

Add DMARC record as soon as  possible ..


DMARC description 

Background

Email authentication technologies SPF and DKIM were developed over a decade ago in order to provide greater assurance on the identity of the sender of a message. Adoption of these technologies has steadily increased but the problem of fraudulent and deceptive emails has not abated. It would seem that if senders used these technologies, then email receivers would easily be able to differentiate the fraudulent messages from the ones that properly authenticated to the domain. Unfortunately, it has not worked out that way for a number of reasons.

Many senders have a complex email environment with many systems sending email, often including 3rd party service providers. Ensuring that every message can be authenticated using SPF or DKIM is a complex task, particularly given that these environments are in a perpetual state of flux.
If a domain owner sends a mix of messages, some of which can be authenticated and others that can’t, then email receivers are forced to discern between the legitimate messages that don’t authenticate and the fraudulent messages that also don’t authenticate. By nature, spam algorithms are error prone and need to constantly evolve to respond to the changing tactics of spammers. The result is that some fraudulent messages will inevitably make their way to the end user’s inbox.
Senders get very poor feedback on their mail authentication deployments. Unless messages bounce back to the sender, there is no way to determine how many legitimate messages are being sent that can’t be authenticated or even the scope of the fraudulent emails that are spoofing the sender’s domain. This makes troubleshooting mail authentication issues very hard, particularly in complex mail environments.
Even if a sender has buttoned down their mail authentication infrastructure and all of their legitimate messages can be authenticated, email receivers are wary to reject unauthenticated messages because they cannot be sure that there is not some stream of legitimate messages that are going unsigned.
The only way these problems can be addressed is when senders and receivers share information with each other. Receivers supply senders with information about their mail authentication infrastructure while senders tell receivers what to do when a message is received that does not authenticate.

{F132000}

In 2007, PayPal pioneered this approach and worked out a system with Yahoo! Mail and later Gmail to collaborate in this fashion. The results were extremely effective, leading to a significant decrease in suspected fraudulent email purported to be from PayPal being accepted by these receivers.

The goal of DMARC is to build on this system of senders and receivers collaborating to improve mail authentication practices of senders and enable receivers to reject unauthenticated messages.

DMARC and the Email Authentication Process


{F131994}

DMARC is designed to fit into an organization’s existing inbound email authentication process. The way it works is to help email receivers determine if the purported message “aligns” with what the receiver knows about the sender. If not, DMARC includes guidance on how to handle the “non-aligned” messages. For example, assuming that a receiver deploys SPF and DKIM, plus its own spam filters, the flow may look something like this:

DMARC authentication flowIn the above example, testing for alignment according to DMARC is applied at the same point where ADSP would be applied in the flow. All other tests remain unaffected.

At a high level, DMARC is designed to satisfy the following requirements:

Minimize false positives.
Provide robust authentication reporting.
Assert sender policy at receivers.
Reduce successful phishing delivery.
Work at Internet scale.
Minimize complexity.
It is important to note that DMARC builds upon both the DomainKeys Identified Mail (DKIM) and Sender Policy Framework (SPF) specifications that are currently being developed within the IETF. DMARC is designed to replace ADSP by adding support for:

{F131999}


wildcarding or subdomain policies,
non-existent subdomains,
slow rollout (e.g. percent experiments)
SPF
quarantining mail
Anatomy of a DMARC resource record in the DNS

DMARC policies are published in the DNS as text (TXT) resource records (RR) and announce what an email receiver should do with non-aligned mail it receives.

{F131994}

Consider an example DMARC TXT RR for the domain “sender.dmarcdomain.com” that reads:

"v=DMARC1;p=reject;pct=100;rua=mailto:postmaster@dmarcdomain.com"
In this example, the sender requests that the receiver outright reject all non-aligned messages and send a report, in a specified aggregate format, about the rejections to a specified address. If the sender was testing its configuration, it could replace “reject” with “quarantine” which would tell the receiver they shouldn’t necessarily reject the message, but consider quarantining it.
DMARC records follow the extensible “tag-value” syntax for DNS-based key records defined in DKIM. The following chart illustrates some of the available tags:



How Senders Deploy DMARC in 5-Easy Steps

DMARC has been designed based on real-world experience by some of the world’s largest email senders and receivers deploying SPF and DKIM. The specification takes into account the fact that it is nearly impossible for an organization to flip a switch to production. There are a number of built-in methods for “throttling” the DMARC processing so that all parties can ease into full deployment over time.

Deploy DKIM & SPF. You have to cover the basics, first.
Ensure that your mailers are correctly aligning the appropriate identifiers.
Publish a DMARC record with the “none” flag set for the policies, which requests data reports.
Analyze the data and modify your mail streams as appropriate.
Modify your DMARC policy flags from “none” to “quarantine” to “reject” as you gain experience.

{F131998}




Spammers can sometimes forge the "From" address on email messages so the spam appears to come from a user in your domain. To help prevent this sort of abuse, Google is participating in DMARC.org, which gives domain owners more control over what Gmail does with spam email messages from their domain.

G Suite follows the DMARC.org standard and allows you to decide how Gmail treats unauthenticated emails coming from your domain. Domain owners can publish a policy telling Gmail and other participating email providers how to handle unauthenticated messages sent from their domain. By defining a policy, you can help 
combat phishing to protect users and your reputation.






Prerequisites
You must send all email messages through your own domain for DMARC to be effective. Messages sent on your behalf through third-party providers will appear unauthenticated and therefore can be rejected, depending upon your policy disposition. To authenticate messages sent from third-party providers, either share your DKIM key with them for inclusion on messages or have them relay messages through your network.

If you're a domain owner, you'll first need to configure SPF records and DKIM keys on all outbound email streams. DMARC relies upon these technologies to ensure signature integrity. A message that fails SPF and/or DKIM checks will trigger the DMARC policy. A single check failure using either technology allows the message to pass DMARC. See the corresponding SPF and DKIM sections of the DMARC specification for example messages filtered by these tools.

{F131997}

Considerations
Here are some things to keep in mind:

You'll receive a daily report from each participating email provider so you can see how often your messages are authenticated, how often invalid messages are identified, and policy actions requested and taken by IP address.
You can adjust your policy as you learn from the data in these reports. For example, you can adjust your actionable policies from “monitor” to “quarantine” to “reject” as you become more confident that your own messages will all be authenticated.
Your policy can be strict or relaxed. For example, eBay and PayPal publish a policy requiring all of their messages to be authenticated in order to appear in someone's inbox. In accordance with their policy, Google rejects all messages from eBay or PayPal that aren’t authenticated.
Recipients don't have to do anything, because Google is conducting the DMARC check for you.
See the DMARC Overview for other considerations. See these related articles for additional details:

{F131995}

#I am thankful to hackerone platform

##I want yout to fix this as soon as possible !!

Thanks.
Hackerone_hero

## Attachments
- DMARC_author-to-recipient_flow.jpg
- antispam-para-paginas-web.png
- Blog_Ads_Ebook_DMARCSavingEmail_082813.jpg
- Capture1-1.jpg
- DMARC-2015-logo-small-202x110.png
- dmarc-infographic.png
- SpamPost.jpg
