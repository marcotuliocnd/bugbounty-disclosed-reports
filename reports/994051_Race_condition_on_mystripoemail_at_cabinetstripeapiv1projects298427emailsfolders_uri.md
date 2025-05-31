# Race condition on my.stripo.email at /cabinet/stripeapi/v1/projects/298427/emails/folders uri

## Report Details
- **Report ID**: 994051
- **URL**: https://hackerone.com/reports/994051
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-29T13:38:45.659Z
- **Disclosed**: 2020-11-09T15:12:51.458Z

## Reporter
- **Username**: zeroc00i
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: stripo

## Vulnerability Information
## Summary:
Hi! I hope you all are pretty good =)
We have discovered a race condition endpoint

## Steps To Reproduce:
```
POST /cabinet/stripeapi/v1/projects/298427/emails/folders HTTP/1.1
Host: my.stripo.email
Connection: close
Content-Length: 23
Accept: application/json, text/plain, */*
Pragma: no-cache
Expires: Sat, 01 Jan 2000 00:00:00 GMT
Cache-Control: no-cache
X-XSRF-TOKEN: 704b458b-c5bd-4ff1-9610-da193b987cb7
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: https://my.stripo.email
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://my.stripo.email/cabinet/
Accept-Encoding: gzip, deflate
Accept-Language: pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6
Cookie: G_AUTHUSER_H=1; _ga=GA1.2.1350209788.1601383605; _gid=GA1.2.1199907309.1601383605; G_ENABLED_IDPS=google; __stripe_mid=5c31e871-7c0e-48a1-809a-e499e39a3dcaa15e57; __stripe_sid=0bcd042d-752e-43c8-877d-83f63b1fa64ddb3e7e; _ga=GA1.3.1350209788.1601383605; _gid=GA1.3.1199907309.1601383605; JSESSIONID=81E11E33CF9ABA02A4AB3D68A29BC4F8; token=eyJhbGciOiJSUzUxMiJ9.eyJhdXRoX3Rva2VuIjoie1widXNlckluZm9cIjp7XCJpZFwiOjI5NDA3NyxcImVtYWlsXCI6XCJqYWFhaGJvdW50eUBnbWFpbC5jb21cIixcImxvY2FsZUtleVwiOlwicHRcIixcImZpcnN0TmFtZVwiOlwiYm91bnR5MVwiLFwibGFzdE5hbWVcIjpcImJvdW50eVwiLFwiZmFjZWJvb2tJZFwiOm51bGwsXCJuYW1lXCI6bnVsbCxcInBob25lc1wiOltdLFwiYWN0aXZlXCI6dHJ1ZSxcImd1aWRcIjpudWxsLFwiYWN0aXZlUHJvamVjdElkXCI6Mjk4NDI3LFwic3VwZXJVc2VyVjJcIjpmYWxzZSxcImdhSWRcIjpcImNiZTljMzIyLTAzYTUtNDc0MS05ZDI2LTU3NzE3NTBiNDNjMFwiLFwib3JnYW5pemF0aW9uSWRcIjoyOTM4MTQsXCJvd25lZFByb2plY3RzXCI6WzI5ODQyN10sXCJmdWxsTmFtZVwiOlwiYm91bnR5MSBib3VudHlcIn0sXCJpc3N1ZWRBdFwiOjE2MDEzODQxNTY3NDEsXCJhcGlLZXlcIjpudWxsLFwicHJvamVjdElkXCI6bnVsbCxcInhzcmZUb2tlblwiOlwiNzA0YjQ1OGItYzViZC00ZmYxLTk2MTAtZGExOTNiOTg3Y2I3XCIsXCJyb2xlXCI6XCJDQUJJTkVUX1VTRVJcIixcImF1dGhvcml0aWVzXCI6W119IiwiZXhwIjoxNjAxNDcwNTU2fQ.v5AkWczH5NwzUvTNhKEYYLhBoL3If9GCb-TkJcCrY_UJN0zFOP0_R7inBRFfwwikVj0GDgTu5YrXCOsy4tge1ug-vemWzEKN5fCC_1qBjN3bWNMKwaL_73VDXvWaFFJGH7o78L5AJI5561bYPTTKFUoq1pn0WooP2K-mepsKblh9SHcN8_VuKjlXx7LbqqrrA9JWSvFOYJgIGfNODr4NfkMBvMrfVxTmPm1CsAvBNKC4sAc02xbuOmWDx0Pvw23RhQHUAHNNPwGKIYYBPsHaqcSQBVtxqs-mtIT0gzVeBUmPXK9t3E82m_aAUBYEEXYwnVdb9lsVPytrYC3wMj-cva-BZLcfC_Lji9NqcVH9LeQXof3JCTtsKnqSSn3rxAdQeGqPIo9Pc-3y1oXJAgGGGMXmZ2DiYIQ24EQUrNwManvWlLLS4OGaKX5XIC5WvT0N-iwaeDcCw-2OCS5sElK1hN0CbhJ4u7i8k_6tK6rFFRWP2OVqayC55dhCeaCmdgwYqAnfc7cJ44kmeYhP-9Jg2h8tHEYnV172llmGQE2UrYlMy3x1FT3yKyU-knWMFrUSI6kXG-oc_ScPJV9JDaSOsBjdXoHfG8MyuH6R6JxEC7qAo4fm6UV25MQIzMXLNZmhbR-RvKIRK-o9l9wDsT4-PxpTmUB8_LVU8Mji9qm5NXQ; amplitude_id_246810a6e954a53a140e3232aac8f1a9stripo.email=eyJkZXZpY2VJZCI6ImRkMjI1YzcwLTEzMTktNDU5NC04ZGZjLTdmODhkYTNhZGJlMVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMTM4MzYwNTA0NiwibGFzdEV2ZW50VGltZSI6MTYwMTM4NDE0NzIzNSwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MCwic2VxdWVuY2VOdW1iZXIiOjB9; intercom-session-b1m243ec=REUyV2F2UnAveGI2blZHVjRpeTFDKy9KZ1J5SHNBcXBIcjlOdjdybW9kODVQdFpESDZ5NUt1Y0twTjdxNHJMcS0tc0x0SkEwNWp4UHdMaWpCSFE5bkZSQT09--c213f9f6b9e06e876f19bb76bdef398b2e5f7787

{"name":"Nova Pasta 2"}
```

  1. Create a new email
  2. Create a new folder
  3. There isnt any x-rate-limit header to prevent repeatedly requests

## Screenshots 
Please check the attachments

## Impact

An atacker could make use of this atack vector to make API unavailable to another users if this request was strongly repeated.

## Attachments
- photo_2020-09-29_10-14-14.jpg
- photo_2020-09-29_10-14-33.jpg
