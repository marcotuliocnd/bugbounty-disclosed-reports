# Cache Posioning leading do Denial of Service on `www.█████████`

## Report Details
- **Report ID**: 1198434
- **URL**: https://hackerone.com/reports/1198434
- **State**: Closed
- **Severity**: high
- **Submitted**: 2021-05-15T17:00:17.139Z
- **Disclosed**: 2021-07-09T18:20:57.220Z

## Reporter
- **Username**: brumens
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
*Hey!
To be clear. This was not an test for Denial of service (DOS). I accidentally come a cross this vulnerability when I was testing for Server side request forgery (SSRF). I have read you policy well and I was not preforming any type of activity that harmed or slowed you system in anyway. You can read why below when I explain the cache poisoning vulnerability that is the core of the impact.*

# Vulnerability Cache Posioning (CPDoS)

**C**ache **P**osioning **D**enial **O**f  **S**ervice (CPDoS) [1] is taking advantage of *301* redirects by storing an false value of either domain, port or header that effect the response in any way. This makes the cache server store the false value and later delivery it to all users that view the domain page.

This vulnerability is in fact an Cache poisoning [2] in the ground which makes it possible to not harm the system in any way when testing. This is because it's possible to add random URL path to the domain that make only that path exploited under *x* time.

An attacker will use intruder to update the cache server every x sec, min or hours to make the domain down. 

# Summary

The vulnerability was discovered when I was testing for SSRF in the host header field.  I notice that it was behaving weard so I added an random parameter in the URL field of the domain that made it redirect with code *301*. This ended up in an reflection of the URL bar in the response.

When the URL of the redirect was reflected I was able to add an random port number and store it into the cache server.

#Proof Of Concept
███

**Supported link**
[1] https://cpdos.org/ - "What is CPDoS?", *Vulnerability explained*
[2]  https://portswigger.net/research/responsible-denial-of-service-with-web-cache-poisoning - "Responsible denial of service with web cache poisoning", *James Kettle*

Best regards,
Alex

## Impact

An attacker is able to Cache posioning the host header. This makes the cache server to store an incorrect port number from the server response and deliver out that incorrect domain and port combined to all users that try access the domain. This make the domain crash and unable to view for users.

**Attackers view**
*For an real attacker to take use of this he/she will disable the random paramter at the url and send it to the home direcly. This will make the domain crash fully*

## System Host(s)
www.███

## Affected Product(s) and Version(s)
/███████

## CVE Numbers


## Steps to Reproduce
**WARNING!** Do not send the request until the step to send the request comes. Otherwise you can by mistage crash the whole domain.

1. Open an browser that is connected to Burp suite
2. Visit: *https://www.███/█████?█████████*
3. Intercept the request with Burp suite and add it to the repeater.
4. **IMPORTEN** Add an random parameter at the end as example: *&CPDoS=1* in the url bar. (*See video POC*).
4. Add an nonexcisting port at the host header domain. Ex: *1234* Your request raw data should look like below:
{F1302641}
5. If an random paramter is added at the end *AND* the port is added to the host header. You can now send the request in Burp suite repeater tab.
The data will look similary to:
```
GET /████████?███████CPDoS=1 HTTP/1.1
Host: www.██████:1234
```
6. You will see an 301 that do redirect and reflect the port you gave inside the request.
7. In the request raw data. Delete the port number inside the host header.
8. Send the request now one more time. You will see the port you added before is still reflecting in the 301 redirect code.
This indicates that it's now cache poisoned and the domain path is down. Image: * FullRequest.png*
████████ <- Might not render...

## Suggested Mitigation/Remediation Actions
Configure the cache server to not store the host header.



## Attachments
No attachments
