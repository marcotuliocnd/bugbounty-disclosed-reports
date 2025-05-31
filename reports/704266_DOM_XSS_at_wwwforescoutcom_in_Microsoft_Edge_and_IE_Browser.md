# DOM XSS at www.forescout.com in Microsoft Edge and IE Browser

## Report Details
- **Report ID**: 704266
- **URL**: https://hackerone.com/reports/704266
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-09-30T13:12:39.890Z
- **Disclosed**: 2020-04-07T08:37:19.705Z

## Reporter
- **Username**: enesdexh1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: forescout_technologies

## Vulnerability Information
## Summary:
I've found an DOM Based XSS on homepage 

## Steps To Reproduce:
1.Go to this url and you'll see alert pop
`https://www.forescout.com/#<img src=x onerror=alert('XSS')>`

But this will work just on ME/IE browsers because chrome and firefox have default encode system hash url

And vulnerable code is on your directly source code within jquery code. As you can see there is no encode in ==window.location.hash== code so when we open the page with #<img src=x onerror=alert(1)> it executes code.

`jQuery(window).load(function() {
    jQuery('a.fancybox-inline[href="' + window.location.hash + '"]:first').each(function() {
        jQuery(this).delay(700).trigger('click');
    });
});`

## Supporting Material/References:
I have uploaded a picture to show you POC


Regards 
Enesdex

## Impact

--Hacker can execute malicious codes in victim's browser
--Hacker can redirect user to malicious website
--Hacker can steal victim's cookies etc.

## Attachments
- DOM_XSS.PNG
