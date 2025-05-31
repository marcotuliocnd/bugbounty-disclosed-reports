# Information Disclosure through Sentry Instance ███████

## Report Details
- **Report ID**: 697512
- **URL**: https://hackerone.com/reports/697512
- **State**: Closed
- **Severity**: high
- **Submitted**: 2019-09-18T21:54:35.038Z
- **Disclosed**: 2019-09-19T09:27:08.719Z

## Reporter
- **Username**: chajer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: zomato

## Vulnerability Information
Hello team 


I found a bug (sensitive information ) can be used from attackers to perfom attack in youre server 
I don't know if this in scope so i'm sorry if i'm wrrong 

withou spending youre time 
 here the steps how i found this bug :

1-Please use burp suite to reproduce the same result 
2-i notice you have as tool for track errors (sentry) 
3- i send the request to ███ via /api/20/store█████████

4-change request from get to post 
Request:
==
POST /api/20/store██████ HTTP/1.1
Host: ███
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
██████
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Sec-Fetch-Site: none
Accept-Encoding: gzip, deflate
Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
5-go to response and click in the [Render ] to view disclosure UI 
6- i get alot of information disclosure ███(see my screenns) i think the server behind this is [███] with ███

## Impact

Please see the screens for more information 
best regards 
let me know if you need more information.

## Attachments
No attachments
