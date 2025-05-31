# Confirmed #2118458: Intentional redirect from www.hackerone.com to domain which is up for sale

## Report Details
- **Report ID**: 2476149
- **URL**: https://hackerone.com/reports/2476149
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-04-23T17:16:28.761Z
- **Disclosed**: 2024-05-09T21:38:31.890Z

## Reporter
- **Username**: sarthakbhingare015
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
P.S.: Actually I submitted this issue back in August 2023 (#2118458), but the domain was just displaying an error. So, I contacted the domain owner for the deal to sell the domain to me and showed you the screenshot of our conversation, but it wasn't considered a valid bug (Even I realized later that it was not a valid proof 😀).

**Summary:**
There is this endpoint- https://www.hackerone.com/node/9386 which automatically redirects to https://www.iotna.com/. But the domain- **iotna.com** is on sale.

### Steps To Reproduce

1. Open any browser.
2. Visit [this](https://www.hackerone.com/node/9386) link.
3. You will be automatically redirected to https://www.iotna.com/.
4. Observe that the domain is up for sale.

{F3218688}
{F3218689}

## Impact

1. If anybody obtains the domain, it may use Hackerone as a starting point of the attack and trick users to perform unintended actions, make them download malwares, compromise their systems, etc.
1. Also, it may use this to bypass **External link warning** on hackerone.com submission form ([demo](https://www.hackerone.com/node/9386)) as there is no external warning for https://www.hackerone.com. This is the reason I have set the **Scope** in CVSS to **Changed**.

(The domain price is very high, which is why I couldn't provide you with working POC 😃)

## Attachments
- godaddy.png
- website.png
