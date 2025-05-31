# Subdomain takeover at info.hacker.one

## Report Details
- **Report ID**: 202767
- **URL**: https://hackerone.com/reports/202767
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-02-02T05:33:50.421Z
- **Disclosed**: 2017-03-27T03:37:25.860Z

## Reporter
- **Username**: ak1t4
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

Hi team,i've been able to takeover subdomain at __info.hacker.one__,
the CNAME entry in the subdomain is pointing to an external page service (app.unbounce.com). 

#### Actual Dns Entry:

{F156764}


#### Steps To Reproduce

1) I have claimed the domain and placed a page for PoC validation located under: 
Go to -> http://info.hacker.one/blank-page-123133617adasdasdsa/
2) You see the alert box and the subdomain takeover

{F156765}

Private & hide Video PoC at -> https://youtu.be/IcoGM65YyU4


#### How was this possible?

While testing UnbouncePage services i saw that they block any domain that was already claimed, but i decided go  deeper and I found an 0day in their API which allows any user to claim any domain with a DNS entry pointing to -> __unbouncepages.com__, i think this bug compromises All Customers Domains at UnbouncePage Services

#### Security Impact

An attacker can utilize this domain _info.hacker.one_ for targeting the organization by fake login hackerOne forms, or steal sensitive information of teams  (credentials, credit card information, etc)

#### FIX & MITIGATION

*You should immediately remove the DNS-entry for this domain or point it elsewhere if you don't use that service
*Contact vendor asap for patch or launch a Fix


Please let me know if more info needed or any help,

Best Regards,
@ak1t4


## Attachments
- Captura_de_pantalla_2017-02-02_a_las_2.12.09.png
- Captura_de_pantalla_2017-02-02_a_las_2.17.31.png
