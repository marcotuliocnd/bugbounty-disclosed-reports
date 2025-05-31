# Multiple XSS on account settings that can hijack any users in the company. 

## Report Details
- **Report ID**: 503298
- **URL**: https://hackerone.com/reports/503298
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-02-28T12:27:15.103Z
- **Disclosed**: 2019-04-01T16:40:27.104Z

## Reporter
- **Username**: giddsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
### Note:
Hello Twitter Team, I just noticed that my report #485748 is already fixed, can you confirm? but my other duplicate reports aren't and still exists. #492444 #492913 are you sure it's on the **same root cause**? because I think the broad fix is already released but didn't fix the other issues.
I will make a report here so you'll notice. I will merge #492444 #492913 here. I'm also thinking for Twitter Security. I'm monitoring MoPub since report #485748 was set on triage. 

*The broad fix didn't really fixed all issues, that's why I'm resubmitting these issues.*

##Description: 
An issue that can be performed **vice versa**. That a member can hijack a admin or admin hijack a member by injecting a malicious scripts in the **accounts settings**.

##Steps to reproduce:

1. Login to MoPub: https://app.mopub.com/account/login/
2. Go to **account settings** (*almost everything here is vulnerable to XSS*)
3. Inject on **currency**
4. You can also inject on **company's information** (*every input is vulnerable to XSS*) 

**Cases of injecting on company's name** 
- When the victim go to **report's tab** XSS will trigger. (*even if the victim is on his/her original company, attacker's company still visible on email drop down menu.*)  
- When the victim go to **account settings** XSS will trigger.  
- When the victim go to **edit user settings** XSS will trigger.  

**Cases of injecting on currency**(vice versa attack)
- Administrator can inject malicious payload in **currency** can hijack member's session. (XSS triggers on member's end) 
- Member can inject malicious payload in **currency** can hijack administrator's session. (XSS triggers on administrator's end)

I provided a **Full Demonstration of the vulnerability**
F432851

**Based on Roles and Permissions:**
(Vice Versa Attack)

- Members can make changes in the account, but they cannot add new users, change other users' roles or view payment information. F432849

## Impact

This vulnerability can impact other users invited by the attacker. And it is Stored XSS that every time the victim visits the vulnerable endpoints, XSS will trigger. The impact here is the attacker can hijack the victim's session.

It's also a vice versa attack. the attacker could be the administrator or the member.

## Attachments
- pic.PNG
- Full_PoC.webm
