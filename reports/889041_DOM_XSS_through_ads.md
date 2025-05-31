# DOM XSS through ads

## Report Details
- **Report ID**: 889041
- **URL**: https://hackerone.com/reports/889041
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-06-02T04:34:12.942Z
- **Disclosed**: 2022-01-18T00:56:20.294Z

## Reporter
- **Username**: bemodtwz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: urbandictionary

## Vulnerability Information
Multiple ads hosted on www.urbandictionary.com make the www.urbandictionary.com origin vulnerable to DOM XSS.  Attached is an image of `alert(document.domain)` executing. The injection works in Firefox and Chrome.

Visiting the following URL will **probably** cause an alert box displaying the  document.domain as www.urbandictionary.com.
`https://www.urbandictionary.com/define.php?term=#asdf'-alert(document.domain)-'asdf`

I say "probably" because the exploit depends on the loading of certain ads. Doing this from a fresh browser session usually causes the alert box. If not refreshing the page a few times, allowing the page to fully load, usually causes the pop-up. It all depends on which ad loads.

It appears the `pwt.js` JavaScript file uses the `displayCreative` function to display a unique ad. This apparently is done by executing `document.write` in an anonymous function to write the ad into the  the www.urbandictionary.com page. Visiting the above link will cause one of the ads to execute `document.domain` with a string that contains the following:

```
<script type='text/javascript'>
url='https://vap3ord1.lijit.com/res/sovrn.containertag.new.min.js…252de1&loc=https://www.urbandictionary.com/define.php?term=#asdf'-alert(document.domain)-'',
```
Many ads want a reference to the website that is loading them, so they inject the URL of the hosting page into the ad source. Since the vulnerable inject the containing page into a JavaScript single quote string, a single quote can be used to escape out of the string. This results in the JavaScript alert function being called.

The stack trace for the above injection follows:
```
    <anonymous> (index):2
    displayCreative pwt.js:11048
    displayCreative pwt.js:13098
    displayCreative pwt.js:10759
    <anonymous> define.php:1
    apply define.php:347
    <anonymous> (index):2
    <anonymous> (index):2
    Caspr (index):2
    Caspr (index):2
    casprInvocation (index):3
    <anonymous> (index):8
    <anonymous> (index):8
```

Multiple ads contain the nearly the same vulnerability. The stack trace is always the same.  The string passed to `document.domain` is different depending on the ad. I will try to include a few examples by attaching files showing the entire content being passed to `document.write`.  

 I obtained the strings passed to `document.domain` using the Eval Villain extension for Firefox, which I developed. This extension may assist you in finding the cause of the vulnerability, or verifying it's existence.

## Impact

DOM XSS allows an attacker to run arbitrary JavaScript under you origin. Since users can authenticate to this origin, an attacker could use this to perform actions in behalf of a victim using the victim session. I  have not yet authenticated to the site, so I don't know exactly what all that would entail.

An attacker could use this vulnerability to add malicious or inappropriate content to your website or takeover the ads seen there. 

So far, it appears the urbandictionary.store does **not** grant the vulnerable origin any CORS privileges. This means an attacker most likely can NOT steal credit card information or modify purchases.

## Attachments
- ss_urban_xss.png
- adstring4.txt
- adstring2.txt
- adstring3.txt
- adstring1.txt
