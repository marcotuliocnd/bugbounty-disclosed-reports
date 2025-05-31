# Cross-Site Scripting (XSS) on www.starbucks.com | .co.uk login pages

## Report Details
- **Report ID**: 881115
- **URL**: https://hackerone.com/reports/881115
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-05-23T04:57:34.672Z
- **Disclosed**: 2020-06-30T22:44:06.701Z

## Reporter
- **Username**: cdl
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi team,

**Summary:** 
There is a cross-site scripting vulnerability on the login page of  www.starbucks.com and various regions, due to improper escaping on the URL path.

**Description:**
The login page at https://www.starbucks.com/account/signin builds several links by the relative URL path. An attacker can actually control the relative path: 

{F839656}

Furthermore, the application does not escape certain characters –  allowing us to break out of the tags and inject a malicious event handler.

**Platform(s) Affected:** 
- https://www.starbucks.com/account/signin
- https://www.starbucks.co.uk/account/signin

## Steps To Reproduce:

  1. Open Chrome or Firefox
  2. Visit `https://www.starbucks.com/account/(A(%22%20%252fonmouseover=%22alert%25%32%38%64%6f%63%75%6d%65%6e%74.%64%6f%6d%61%69%6e%25%32%39%22))/signin` and in the upper right-hand corner, move your mouse over the "Find the Store" button.

The XSS will trigger and you'll get an `alert()` with the value of `document.domain`

{F839657}


## Exploitation: 
Since this is on the **login page**, it is absolutely trivial to steal user credentials.

Here's a simple proof-of-concept, this will just alert() your password back to you:

- `https://www.starbucks.com/account/(F(%22%20%252fonmouseover=%22%2561%256c%2565%2572%2574%2528%2564%256f%2563%2575%256d%2565%256e%2574%252e%2567%2565%2574%2545%256c%2565%256d%2565%256e%2574%2573%2542%2579%254e%2561%256d%2565%2528%2527%2541%2563%2563%256f%2575%256e%2574%252e%2550%2561%2573%2573%2557%256f%2572%2564%2527%2529%255b%2530%255d%252e%2576%2561%256c%2575%2565%2529%22))/signin`

{F839660}


## How can the system be exploited with this bug?
  An attacker can easily abuse this bug to steal user passwords, inject malicious javascript into the context of `www.starbucks.com`, etc.

## Suggested Mitigation
Implement HTML encoding / escaping on the path.

## Impact

This is a high impact vulnerability as this affects the login page.

Best,
@cdl

## Attachments
- Screen_Shot_2020-05-22_at_11.45.25_PM.png
- starbucks.com-loginpagexss.gif
- starbucks-password-theft-xss.gif
