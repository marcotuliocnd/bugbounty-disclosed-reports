# Content Spoofing/Text Injection in https://support.cs.money and JS file not minified and uglyfied which makes it clearly readable 

## Report Details
- **Report ID**: 997198
- **URL**: https://hackerone.com/reports/997198
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-10-03T16:41:07.880Z
- **Disclosed**: 2020-11-12T13:18:11.591Z

## Reporter
- **Username**: rootishere
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Issue 1:
Greetings,

Hello Team,
I have found a Content Spoofing/Text Injection on this domain https://support.cs.money
Using the below link the attacker can trick any genuine user to go to the attacker's phishing site.

The attacker could craft the URL by providing discounts which will tempt the user to visit the attacker URL mentioned, as the site displaying the message still belongs to https://support.cs.money

## Steps To Reproduce

POC URL
[support cs money url](https://support.cs.money//.cs.money(!has-moved-to-[www.support.cs.money.in]).Please-visit__[www.cs.money.in]___present__resource)

## Issue 2 - worker.js file is user-readable 
https://cs.money/js/worker.js?language=en&v=1331&csrf_token=[removed]
The worker.js contains a lot of business logic which is deployed in production whiteout being minified or uglified. This might lead an attacker to craft attacks in future as it uses 
1. location.href`
2. eval
  in the below code snipped 
```
case 'method':
            try {
                postMessage({
                    cbid: data.cbid,
                    result: eval(`(${data.method})`)()
                });
            } catch (err) {
                console.warn(err);
            }
            break;
```

PoC Screenshots attached.

Let me know if you need more information.

Cheers!

## Impact

Crafted phishing attacks on cs.money

## Attachments
- Phising_attack.png
- plain_text_workerjs_file.png
