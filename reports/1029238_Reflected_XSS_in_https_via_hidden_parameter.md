# Reflected XSS in https://███████ via hidden parameter "████████"

## Report Details
- **Report ID**: 1029238
- **URL**: https://hackerone.com/reports/1029238
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-07T23:07:53.989Z
- **Disclosed**: 2022-01-19T19:30:22.449Z

## Reporter
- **Username**: supr4s
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi everyone :)

I found a Reflected XSS on https://███████ via hidden parameter "████████" on the following authentication page : https://███████/██████████


## Steps To Reproduce:

- Use your favorite web browser
- Go to : 
```
https://███████/███████&███=TEST%22%3E%3Cscript%3Ealert(%27Reflected%20XSS%27)%3C/script%3E
```

An XSS is triggered !

The initial page was https://█████████/█████████

With a little research, you can find a hidden parameter "████████" which is directly reflected in the source code **without sanitize user entries**. Then just close the tag and inject our malicious code.

## Supporting Material/References:
Work on every browser (Firefox, Chrome ..)

## Suggested Mitigation/Remediation Actions

- Never trust user inputs, and therefore sanitize them.
- If the parameter "███" is useless in this page and in the authentication process, then it should be deleted.

## Impact

The damages of a reflexive XSS flaw are numerous: executing malicious javascript code, phishing, defacing ... We can also inject HTML code and mislead the user when displaying the web page.

From [OWASP](https://owasp.org/www-community/attacks/xss/) :

>Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user. Flaws that allow these attacks to succeed are quite widespread and occur anywhere a web application uses input from a user within the output it generates without validating or encoding it.

## Attachments
No attachments
