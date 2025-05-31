# Cache Posioning leading to denial of service at `█████████` - Bypass fix from report #1198434	

## Report Details
- **Report ID**: 1322732
- **URL**: https://hackerone.com/reports/1322732
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-08-29T14:50:58.926Z
- **Disclosed**: 2021-10-13T22:15:38.530Z

## Reporter
- **Username**: brumens
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
#Vulnerability Cache Posioning (CPDoS)
**C**ache **P**osioning **D**enial **O**f **S**ervice (CPDoS) [1] is taking advantage of 301 redirects by storing an false value of either domain, port or header that effect the response in any way. This makes the cache server store the false value and later delivery it to all users that view the domain page.
This vulnerability is in fact an Cache poisoning [2] in the ground which makes it possible to not harm the system in any way when testing. This is because it's possible to add random URL path to the domain that make only that path exploited under x time.
An attacker will use intruder to update the cache server every x sec, min or hours to make the domain down.

#Summary
The vulnerability was discovered when  was retesting the vulnerability and discovered that the domain still was vulnerable for cache poisoning. I did some tests and I was able to re poisoning the domains cache server again in different paths. It looks like the fix from report *#1198434* only fixed one path in the domain but other paths remain vulnerable.

# Proof of concept
*Can be used as step by step if you like*

█████████

Supported link
[1] https://cpdos.org/ - "What is CPDoS?", Vulnerability explained
[2] https://portswigger.net/research/responsible-denial-of-service-with-web-cache-poisoning - "Responsible denial of service with web cache poisoning", James Kettle

Best regards,
Brumens

## Impact

An attacker is able to crash most of the paths related to the domain.

## System Host(s)
████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
**WARNING!** Do not send the request until the step to send the request comes. Otherwise you can by mistage crash the whole domain.
1. Open an browser that is connected to Burp suite
2. Visit: https://██████████/██████████ (*More path are vulnerable but this is an example*)
3. Intercept the request with Burp suite and add it to the repeater.
**IMPORTEN** Add an random parameter at the end as example: &CPDoS=1 in the url bar at *Repeater*. (*See image at step 4.*)
4. Add an nonexcisting port at the host header domain. Ex: 1234 Your request raw data should look like below:
█████ 
If an random paramter is added at the end AND the port is added to the host header. You can now send the request in Burp suite repeater tab. The data will look similary to:

5. You will see an 301 that do redirect and reflect the port you gave inside the request.
In the request raw data. Delete the port number inside the host header.
Send the request now one more time. You will see the port you added before is still reflecting in the 301 redirect code. This indicates that it's now cache poisoned and the domain path is down. Try visit the url and you can see you won't be able to load it.

## Suggested Mitigation/Remediation Actions
Configure the cache server on all paths and locations on the domain.



## Attachments
No attachments
