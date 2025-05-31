# XSS trigger via HTML Iframe injection in ( https://██████████ ) due to unfiltered HTML tags

## Report Details
- **Report ID**: 1200770
- **URL**: https://hackerone.com/reports/1200770
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-05-18T11:08:34.308Z
- **Disclosed**: 2022-02-14T21:23:22.209Z

## Reporter
- **Username**: basant0x01
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi team,
I found an Iframe injection issue where I chained it and formed an XSS. I found the issue in the text editor area while ███████ing the account.
There is a place in the registration area where we have to give a reason for █████████. We can write our reason and edit to show more beautifully.
URL: https://██████████/█████/
████████

In this edit area, there are two buttons 1. ████ and 2. ███████. We can use both fields to edit our text. As an analyst, I analyze both fields and found the text area is vulnerable to injection, where we can able to inject iframe injections.
<iframe src="https://google.com"></iframe>

And after clicking on the visual button, it's reflecting on the page. But the problem is it's showing the error, it's because the page is already secured by the clickjacking issue.
██████████

But got an idea where I can chain the iframe injection issue to fire the XSS into the page of https://██████████.
I uploaded the XSS image into my NETLIFY sandbox server. Here's a Link: https://█████

Then I create the payload like: 
<iframe src="https://███████"></iframe>

And boom!! I can see the XSS firing into the page of https://███.
████████

*It's definitely not allowing to injection directly iframe page but it's allowing the image to reflect. In this way, an attacker cannot able to steal session cookies but can able to perform attacks like phishing on a genuine site.*

**VIDEO POC:**
███████

## Impact

An attacker cannot able to steal a session's cookies because it's not an XSS  but attackers can able to perform attacks like phishing on a genuine site.

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Visit https://██████/█████████/,
2. Scroll below you will see the area like ( Reason for ██████ (required) )
3. Click the text button and inject : <iframe src="https://█████████"></iframe> 
payload
4. Again click on the ██████████ button,

(Instently, You will see the xss is firing into the page of https://███ )

## Suggested Mitigation/Remediation Actions
Filter every data before displaying it into the page and only whitelist the limited HTML tags.



## Attachments
No attachments
