# Reflected cross site scripting (XSS) attacks Reflected XSS attacks, 

## Report Details
- **Report ID**: 1799197
- **URL**: https://hackerone.com/reports/1799197
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2022-12-10T15:23:07.328Z
- **Disclosed**: 2024-08-30T23:13:54.039Z

## Reporter
- **Username**: 0xmekky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:
[Reflected XSS attacks, also known as non-persistent attacks, occur when a malicious script is reflected off of a web application to the victim’s browser.

The script is activated through a link, which sends a request to a website with a vulnerability that enables execution of malicious scripts. The vulnerability is typically a result of incoming requests not being sufficiently sanitized, which allows for the manipulation of a web application’s functions and the activation of malicious scripts.

To distribute the malicious link, a perpetrator typically embeds it into an email or third-party website (e.g., in a comment section or in social media). The link is embedded inside an anchor text that provokes the user to click on it, which initiates the XSS request to an exploited website, reflecting the attack back to the user.]

## Steps To Reproduce:
[add details for how we can reproduce the issue]

  1. open the url [https://102.176.160.119:10443/remote/error?errmsg=]
  1.  in this pramiter  inject the xss pyload  in ?errmsg = [https://102.176.160.119:10443/remote/error?errmsg=ABABAB--%3E%3Cscript%3Ealert(1337)%3C/script%3E]
  1. final url ===    https://102.176.160.119:10443/remote/error?errmsg=--%3E%3Cscript%3Ealert(document.domain)%3C/script%3E

## Supporting Material/References: 
https://medium.com/@Steiner254/reflected-cross-site-scripting-xss-7aae0f4343c3
https://portswigger.net/web-security/cross-site-scripting
https://www.imperva.com/learn/application-security/reflected-xss-attacks/

## Impact

~ When attackers can control scripts that are executed in the victims’ browsers, then they stand at chances of typically compromising those users. These attackers can do the following:
a. Perform any kinds of actions within the applications that the users can perform.

b. View all kinds of data that the users have abilities to view.

c. Modify data that the users have abilities to modify.

d. Initiation of interactions with other application’ users.

## Attachments
- xss_poc_mtn.mp4
