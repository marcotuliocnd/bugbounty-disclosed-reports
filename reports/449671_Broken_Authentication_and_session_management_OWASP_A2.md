# Broken Authentication and session management OWASP A2

## Report Details
- **Report ID**: 449671
- **URL**: https://hackerone.com/reports/449671
- **State**: Closed
- **Severity**: none
- **Submitted**: 2018-11-26T04:02:50.027Z
- **Disclosed**: 2018-11-26T07:08:51.693Z

## Reporter
- **Username**: sameerphad72
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: liberapay

## Vulnerability Information
Hello @liberapay,

**Description**:
It seems now if attacker has csrf token & victim cookies then attacker can easily login to victim account without any login details. (No need Of Any Username/Password)

**Theory Proof-Of-Concept**:
- Go to https://liberapay.com/admin.101/edit/username (*any username/Self Account)
- Refresh Current Page & Copy Cookies By Burp Proxy
- Send Cookie Request to Repeater (Burp Proxy)
- Now, Delete Browsers Cookies Data/Logout/Open Private Mode (Logged Out)
- Go to https://liberapay.com/admin.101/edit/username Again with New Private Window Of Chrome 
- Refresh Current Page that says please log in to continue
- Now, Paste That Our Old Cookies & Forward Request
- Bom! You will logged into old account & able to edit username/mail/password or other info.

**Video Proof-Of-Concept**:
{F380556}

**Impact**:
Attacker Can Login To Victim Account Without Any Login Details Via Cookies. :-)

**Patch**:
Cookies need to change after logout... This bug doesnot works on facebook,hackerone,google or other platforms.

**Reference/Same Report Tested On HackerOne.com**:
https://hackerone.com/reports/284

**Live Example**:
You can also login to my account (admin.101) temp account via this cookies/request.
```GET /admin.101/edit/username HTTP/1.1
Host: liberapay.com
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: __cfduid=dd3ba661a9dc150157d3da058ecda83d31543203235; csrf_token="r6WR9u6fAZPDcfU4/3gP2OygIm1uh177"; session="1509265:1:YBAa_gGPtb0x1m_CjoNf4MgBhDG2mDJG.em"```



Thanks,
@sameerphad72

## Impact

Attacker Can Login To Victim Account Without Any Login Details Via Cookies. :-)

## Attachments
- liberapay.mp4
