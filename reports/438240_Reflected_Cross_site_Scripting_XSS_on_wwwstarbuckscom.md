# Reflected Cross site Scripting (XSS) on www.starbucks.com

## Report Details
- **Report ID**: 438240
- **URL**: https://hackerone.com/reports/438240
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-11-09T14:12:25.058Z
- **Disclosed**: 2019-03-08T14:04:25.604Z

## Reporter
- **Username**: cujanovic
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
**Summary:** Reflected Cross site Scripting (XSS) on https://www.starbucks.com/account/signin?ReturnUrl

**Description:** The attacker can execute javascript on  the victims account just after the authentication process.

**Platform(s) Affected:**
www.starbucks.com
www.starbucks.ca
www.starbucks.com.br
www.starbucks.co.uk
www.starbucks.de
www.starbucks.fr

## Steps To Reproduce:

1. Open the url: https://www.starbucks.com/account/signin?ReturnUrl=%19Jav%09asc%09ript%3ahttps%20%3a%2f%2fwww%2estarbucks%2ecom%2f%250Aalert%2528document.domain%2529
2. Login
3. The JS will execute on users(victims) account.

## Supporting Material/References:
Screenshot:
{F373210}

## How can the system be exploited with this bug?
The attacker can execute JS code.
  

## How did you come across this bug ?
I was testing for open redirect vulnerability.


## Recommendations for fix
Content based escaping on the users input, in this case the redirect parameter.

## Impact

The attacker can execute JS code.

## Attachments
- Screenshot_20181109_150007.png
