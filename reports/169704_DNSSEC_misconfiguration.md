# DNSSEC misconfiguration

## Report Details
- **Report ID**: 169704
- **URL**: https://hackerone.com/reports/169704
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-09-16T01:05:56.852Z
- **Disclosed**: 2016-09-30T18:39:56.872Z

## Reporter
- **Username**: fabiothebest89
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: skyliner

## Vulnerability Information
First of all I will start with some theory.
DNS is a system to translate a domain name to an ip address. Normally a computer automatically trust a DNS server and connects to the IP provided by the DNS server. This is prone to security issues because a malicious wifi network, an attacker on your router, a compromised ISP, or any other man-in-the-middle attack can redirect a DNS request to a server of their choice (a fake one) and this can allow phishing, malware spreading, botnets and can also cause Denial of Service in a way because the original server will become unreachable unless you know its IP address and you use it for establishing a TCP connection. An attacker can do domain hijacking, create forged DNS updates, unauthorised zone transfers, cache poisoning and DoS.
How can we solve all these problems? The answer is: implementing DNSSEC.
And you did it, but you did it wrong.
If you want to read about the DNSSEC standard check RFC4034(https://www.ietf.org/rfc/rfc4034.txt) and RFC4035(https://www.ietf.org/rfc/rfc4035.txt). Besides I recommend you to read the NIST Secure Domain Name System (DNS) Deployment Guide, (NIST Special Publication 800-81-2) (http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-81-2.pdf).
DNSSEC validates the source of the DNS response, ensures the response hasn't been altered in transit and authenticates replies of non-existence. It works by adding digital signatures to DNS responses, adding chan of trusts to validate responses and identifying bogus responses.
To facilitate signature validation, DNSSEC adds a few new DNS record types:

**RRSIG** – Contains a cryptographic signature
**DNSKEY** – Contains a public signing key
**DS** – Contains the hash of a DNSKEY record
**NSEC** and **NSEC3** – For explicit denial-of-existence of a DNS record
**CDNSKEY** and **CDS** – For a child zone requesting updates to DS record(s) in the parent zone.

**RRsets**
The first step towards securing a zone with DNSSEC is to group all the records with the same type into a resource record set (RRset). For example, if you have three AAAA records in your zone, they would all be bundled into a single AAAA RRset and it's the whole RRset that will be digitally signed.
**Zone Signing Keys**
Each zone in DNSSEC has a zone-signing key pair (ZSK): the private portion of the key digitally signs each RRset in the zone, while the public portion verifies the signature. To enable DNSSEC, a zone operator creates digital signatures for each RRset using the private ZSK and stores them in their name server as RRSIG records. 
However, these RRSIG records are useless unless DNS resolvers have a way of verifying the signatures. The zone operator also needs to make their public ZSK available by adding it to their name server in a DNSKEY record.
When a DNSSEC resolver requests a particular record type (e.g., AAAA), the name server also returns the corresponding RRSIG. The resolver can then pull the DNSKEY record containing the public ZSK from the name server. Together, the RRset, RRSIG, and public ZSK can validate the response. If we trust the zone-signing key in the DNSKEY record, we can trust all the records in the zone. But, what if the the zone-signing key was compromised? We need a way to validate the public ZSK.
**Key-Signing Keys**
In addition to a zone-signing key, DNSSEC name servers also have a key-signing key (KSK). The KSK validates the DNSKEY record in exactly the same way as our ZSK secured the rest of our RRsets in the previous section: It signs the public ZSK (which is stored in a DNSKEY record), creating an RRSIG for the DNSKEY. Just like the public ZSK, the name server publishes the public KSK in another DNSKEY record, which gives us the DNSKEY RRset shown above. Both the public KSK and public ZSK are signed by the private KSK. Resolvers can then use the public KSK to validate the public ZSK. We separate zone-signing keys and key-signing keys because it’s difficult to replace an old or compromised KSK instead changing the ZSK is much easier. 
We’ve now established trust within our zone, but DNS is a hierarchical system, and zones rarely operate independently. Complicating things further, the key-signing key is signed by itself, which doesn’t provide any additional trust. We need a way to connect the trust in our zone with its parent zone.
**Delegation Signer Records**
DNSSEC introduces a delegation signer (DS) record to allow the transfer of trust from a parent zone to a child zone. A zone operator hashes the DNSKEY record containing the public KSK and gives it to the parent zone to publish as a DS record. Every time a resolver is referred to a child zone, the parent zone also provides a DS record. This DS record is how resolvers know that the child zone is DNSSEC-enabled. To check the validity of the child zone’s public KSK, the resolver hashes it and compares it to the DS record from the parent. If they match, the resolver can assume that the public KSK hasn’t been tampered with, which means it can trust all of the records in the child zone. This is how a chain of trust is established in DNSSEC. Note that any change in the KSK also requires a change in the parent zone’s DS record. Changing the DS record is a multi-step process that can end up breaking the zone if it’s performed incorrectly. First, the parent needs to add the new DS record, then they need to wait until the TTL for the original DS record to expire before removing it. This is why it’s much easier to swap out zone-signing keys than key-signing keys.
**The Chain of Trust**
We have a way to establish trust within a zone and connect it to its parent zone, but how do we trust the DS record? Well, the DS record is signed just like any other RRset, which means it has a corresponding RRSIG in the parent. The whole validation process repeats until we get to the parent’s public KSK. To verify that, we need to go to that parent’s DS record, and on and on we go up the chain of trust. However, when we finally get to the root DNS zone(https://www.internic.net/domain/root.zone), we have a problem: there’s no parent DS record to validate against. Signing of the root zone is done personally by people who work at ICANN {F120684}

So, to summarize we all need to trust ICANN people who signs the root zone, the root zone signs the TLD domains (.io in the case of skyliner.io), the .io domain allows to trust skyliner.io and skyliner.io allows to trust its subdomains, if any.

Now take a look at the 2 DNSSEC reports that I included as attachments. {F120685} 
 {F120686}

**THE PROBLEM OF SKYLINER.IO DNSSEC IMPLEMENTATION**
The problem is that it appears there isn't a DS record in the .io zone, so the signer of the skyliner.io zone should send a DS record to the .io zone . 
Besides no DNSKEY records were found in skyliner.io. It means that the skyliner.io zone isn't signed with DNSSEC or the zone maintainer didn't include the DNSKEY records before signing it. 
Finally no RRSIGs were found in the skyliner.io zone. It means that the skyliner.io zone isn't signed with DNSSEC or that some RRSIG records are missing or not available from all the nameservers.

The delegation from the root zone to the .io zone is secure, trusted, verified.
The delegation from the .io zone to the skyliner.io zone is insecure.  The NS, TXT, SOA, A and MX records of skyliner.io aren't correctly verified. So the chain of trust is broken.

The implementation of DNSSEC depends also on if you manage a DNS server yourself (i.e. Bind) or you use another company for that. It can be complex as you saw in my long message and there are some tools to ease the task but there aren't fully automated solutions. Also remember that it's important to store your private keys offsite or if you really want to keep them on the server, they should be encrypted. I also like to a nice OWASP presentation that can give you further details on how to implement DNSSEC correctly. (https://www.owasp.org/images/6/63/OWASP_Atlanta_Feb_12_2010.pdf)
I hope it helps and I hope to hear from you soon. In case you need further assistance do not hesitate to ask, anyway I tried to provide as much information as possible for your convenience.
Best regards,

Fabio Baroni

 

## Attachments
- root-signing-ceremony.jpg
- skyliner.io-1.JPG
- skyliner.io-2016-09-15-22-32-42-UTC.png
