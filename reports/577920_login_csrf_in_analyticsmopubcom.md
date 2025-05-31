# login csrf in analytics.mopub.com

## Report Details
- **Report ID**: 577920
- **URL**: https://hackerone.com/reports/577920
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-05-12T05:02:52.817Z
- **Disclosed**: 2019-10-02T23:05:07.239Z

## Reporter
- **Username**: protostar0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Description:** There is no csrf_token validation while logging in which leads to csrf.
**base request :**
>
POST /login HTTP/1.1
Host: analytics.mopub.com
Connection: close
Content-Length: 37
Accept: application/json, text/plain, */*
Origin: https://analytics.mopub.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36
Content-Type: application/json;charset=UTF-8
Referer: https://analytics.mopub.com/
Accept-Encoding: gzip, deflate
Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
Cookie: _ga=██████; _gid=███████; mp_mixpanel__c=0

>{"name":"username","pass":"password"}

** bypass content type & CORS**
we cant send it with simple html  form , because the **Content-Type: application/json;charset=UTF-8**
we can send it with ajax request and edit the Content-Type to json
and add this link https://cors-anywhere.herokuapp.com/ to  bypass   CORS 
ps: more about bypass cors 
https://medium.com/netscape/hacking-it-out-when-cors-wont-let-you-be-great-35f6206cc646


## Steps To Reproduce with :
1. download F488813 and edit  the username and password.

2.open it with browser .

3.with web development tools in browser open Network and look response .

if response status 401 means thats login failed;
F488816 ████
else if response status 400  means its bad request   with reflected input in json error can get  **Cross site scripting (content-sniffing):** {  the response header without  X-Content-Type-Options: nosniff }
████
else means login success
{i dont have account in analytics.mopub.com}





## References & semilar report : 

https://medium.com/netscape/hacking-it-out-when-cors-wont-let-you-be-great-35f6206cc646
https://hackerone.com/reports/293016
https://hackerone.com/reports/339352

## Impact

1-Log any victim into the attacker account, the attacker can create a similar account profile as the victim 2- with some information missing, and then social-engineering (e.g. email) user to provide personal information or current password and can also monitor the victim activities.
3- Also the victim may add his paymet info in the attackers account unknowingly using your wallet feature.
4-Cross site scripting (content-sniffing)  (not tested)

## Attachments
- csrfinlogin.html
- poc1.jpg
