# URl redirection 

## Report Details
- **Report ID**: 642876
- **URL**: https://hackerone.com/reports/642876
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-14T11:16:53.599Z
- **Disclosed**: 2019-08-28T15:31:37.871Z

## Reporter
- **Username**: ziel
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: kartpay

## Vulnerability Information
In the following post HTTP request while registering for merchant


POST /register HTTP/1.1
Host: merchant.kartpay.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://merchant.kartpay.com/register
Content-Type: application/x-www-form-urlencoded
Content-Length: 189
DNT: 1
Connection: close
Cookie: XSRF-TOKEN=eyJpdiI6IjFKUXdMQlhcL3Z0Ynh1c1dcL3gyeEpiZz09IiwidmFsdWUiOiIya3U5RUlwM0RuMUI5dGpQT0tWQ1Vwaml2bXgrYTk2aGM3UW03T3ZKM1ZYYnlnV2tOblg4eHhpR3lVM01xVzBjIiwibWFjIjoiYmMxNGNjYTY1N2MyMWIwMmYzYWZjNTczZWE0YTViNGQ0ZGVmNDBmYjkzYWFlNWEyN2Q4NGJhYjlkNDNlY2YzZCJ9; laravel_session=eyJpdiI6InJ2ZzByUm44aWFlUm5jSE1XRDV3clE9PSIsInZhbHVlIjoick1rVnRaNWw1YXVzMWJBWDFTaUJadm1pVTdXUHFrcks2Q0t4cmtqbXZGd3J5bTBuQW1MM2hyUXpodGV3R0M1ZyIsIm1hYyI6IjgxZmI2MDM0NmViNTNjYzQxOTI2MmE4OTIwOGZjZTI3ZjFmMmExNmQ0ZmM5NzZjNDkxZTQyNGFhNjczYTAwN2YifQ%3D%3D; __tawkuuid=e::kartpay.com::wQWbHoNu5pztKvKlrrxFMmm76vfDDCsNlhIe6kmIiM0OGKmL14t07iKcuOcjGIjy::2
Upgrade-Insecure-Requests: 1

verification_code=&type=merchant&_token=2zCgjrNgztgRCMhm4cDScrbTARxEmwn4z16Fjnpe&first_name=ahcvcv&last_name=jbshchjs&email=jbcjhsbcbsb%40baxjbj.com&country_code=%2B91&contact_no=9090909090



The referrer header is vulnerable to open url redirection


## Steps To Reproduce:
[add details for how we can reproduce the issue]

1. make above http request in burp suit
  2. change the referrer header to any site say bing.com
3. it gets redirected to bing.com

Poc : attached screenshot

## Impact

An attacker can construct a URL within the application that causes a redirection to an arbitrary external domain

## Attachments
- kart.png
