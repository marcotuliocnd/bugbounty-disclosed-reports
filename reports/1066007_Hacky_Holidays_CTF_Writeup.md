# Hacky Holidays CTF Writeup

## Report Details
- **Report ID**: 1066007
- **URL**: https://hackerone.com/reports/1066007
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-24T21:12:24.418Z
- **Disclosed**: 2021-01-12T18:00:18.407Z

## Reporter
- **Username**: w--
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Intro:

12 days of challenges - some more challenging than others!  This holiday CTF had all 12 challenges hosted on the website https://hackyholidays.h1ctf.com/

{F1129112}

## Challenge 1:

I started by *significantly* overthinking all of the early challenges in this competition.  When this CTF started the home page did not have the "apps" button as seen in the screenshot above, and simply had the "Keep Out" image and the falling snow.

I checked the HTML source and didn't find anything much.  After checking a couple more obvious things, I started looking into the "falling snow" background, which was a `.mp4` file.  Perhaps there was a single frame with the flag in it?  Examining the file showed some interesting details like the file paths used for creating the animation (`H:\NahamSec\Grinch\Grinch Launch.aep`):

{F1129111}

Unfortunately, this challenge had nothing to do with the webpage source code, images or movie file.  The flag turned out to be in `robots.txt`!  The contents of robots.txt was:

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```

This provided the first flag, and the path to the second day's challenge

## Challenge 2

The path `/s3cr3t-ar3a` returned a message "Come back tomorrow" until day 2 started.  Once the challenge kicked off, the following page could be seen:

{F1129110}

This challenge, similar to the last, was even easier than it looked.  The HTML source for the page included an innocent looking reference to `/assets/js/jquery.min.js`.  Examining this file showed that data was obfuscated into the Javascript:

{F1129109}

There was no need to deobfuscate the data however.  Examining the Javascript showed that it would write the data into the DOM of the page.  Which means that the Web Developer Inspector built in to the browser could be used to simply view the data.  This revealed the following:

```
<div class="alert alert-danger text-center" id="alertbox" data-info="flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}" next-page="/apps">
```

Once again, we now have the flag for the challenge and the page for the next day.

## Challenge 3 - People Rater

The `/apps` page was used to host the next 8 challenges.  The first one (challenge 3) was the "People Rater" challenge.  This challenge displayed a list of people and the Grinch's rating of them.  Clicking a person would display the rating, which was always "Disgusting".

An intercepting proxy was used and showed that when a person was clicked, an API request similar to the following was made:

```
https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6NH0=
```

The `id` parameter clearly contains Base64 encoded data.  Decoding it shows:

```
{"id":4}
```

ID 1 never appears in the list to click on, so we can manually encode it and call this API with the following URL:

https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=

This returns the following result, which includes the flag for this challenge:

```
{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}
```

## Challenge 4 - Swag Shop

Challenge 4 was a fake web store.  There were 3 items for sale, but a login was required to purchase any items.  Attempting to brute force the login was not successful.  After trying several ways to break the web store, `wfuzz` was used with a small word list to attempt to find other pages that might not be linked.  This revealed the following page:

```
https://hackyholidays.h1ctf.com/swag-shop/api/sessions
```

This page returned a list of sessions as Base64 data:

{F1129108}

The Base64 data included a value, "Cookie" when decoded.  I initially tried to use the session data to populate my own login cookie, however this was not successful.  I even tried every single session ID!  

One of the session data strings also had the value "user": `"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043"`.  After *more* wfuzz scans I identified an endpoint `user` that accepted a parameter `uuid`.  This then allowed for a user to be looked up with the following URL:

```
https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043
```

The response had the flag:

```
{"uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","username":"grinch","address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},"flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}
```

## Challenge 5 - Secure Login

This challenge started off very straightforward.  The challenge started with a "login" page.  Entering a test login (admin/admin) returned the error:

```
Invalid Username
```

This strongly indicates that we need to first find the correct username.  I tried an LDAP injection as a test, but this did not uncover anything.  Next I moved to a brute force attack.  This quickly showed that the username `access` could be used.  With that username, the server now returned `Invalid Password` as the message.  Bruteforcing the password field showed the password was `computer`.  

The challenge was not done here however!  After logging in, the website simply said `No Files To Download`.  Brute forcing API paths did not reveal anything.  Examining the cookie that was set after login however revealed the next step.  The cookie value was `eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D`.  Base64 decoded this becomes: `{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}`.  I quickly changed "admin" to "true", and reencoded the cookie.  Now when accessing the file list, one file was available for download:

```
my_secure_files_not_for_you.zip
```

We still are not done!  After downloading this zip file I discovered that it is password protected.  The password turned out to be pretty easy, John The Ripper quickly found it to be `hahahaha`:

{F1129107}

This allowed flag.txt to be extracted and its value was: `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`

## Challenge 6 - My Diary

This challenge starts on the page: `https://hackyholidays.h1ctf.com/my-diary/?template=entries.html`.  The page displays a list of "diary" entries for the Grinch.  I ended up stuck on this one for waaay longer than I should have been.  The `?template=entries.html` parameter was the obvious target for attack, but changing it to any other value simply returned a `404`.  Accessing `entries.html` directly was successful, but only returned the exact same contents as the regular page.

I ran wfuzz several times with no results.  I tried path traversal attacks with some success (`?template=../` returned a blank page instead of a 404).  But still nothing.  Finally with an expanded wordlist for wfuzz I hit the parameter `?template=index.php`.  No other challenges had referenced pages with a `.php` extension, so I had not tried this for any of them.  I also ran in to an issue where Burp Intruder's filter function had a bug (which it has had forever).  The filter functionality of it incorrectly hides results while the scan is running.  It only works properly after an intruder run has completed.  Using wfuzz instead of intruder finally revealed the correct page.  The contents of the `index.php` page can be seen below:

{F1129106}

This PHP script is filtering input to block access to `secretadmin.php`  We can defeat this filter by using the following URL:

https://hackyholidays.h1ctf.com/my-diary/?template=secretadmsecretadmadmin.phpin.phpin.php

This reveals the calendar entry for the Grinch (Launch DDOS against Santa's Workshop), and the flag: `flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`

## Challenge 7 - Hate Mail Generator

The Hate Mail Generator app allows users to view or create new email campaigns.  The emails can make use of a template, and the app allows users to preview templates before they are used.  This challenge immediately appeared to require a template injection attack.  The example email template had the following value in it: `{{template:cbdj3_grinch_header.html}}`.  This template directive would cause the server to return the contents of that file when loaded.

After trying several template engine attacks, I switched to instead looking at the `cbdj3_grinch_header.html` page.  I found that this was stored in a directory that could be listed:

{F1129105}

This showed there was another file `38dhs_admins_only_header.html`.  Including this file in a template was not successful however!  The server returned an error `You do not have access to the file 38dhs_admins_only_header.html`.  After trying a few different things (injecting characters that were stripped out to bypass a filter - didn't work), I found that the template file could be referenced from the template *data*.  The following `POST` request was used to reveal the contents of the file:

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackyholidays.h1ctf.com/hate-mail-generator/new
Content-Type: application/x-www-form-urlencoded
Content-Length: 209
Origin: https://hackyholidays.h1ctf.com
Connection: close
Upgrade-Insecure-Requests: 1

preview_markup=yes{{template:cbdj3_/*grinch*/_header.html}}{{77}}&preview_data={"name":"admin","email":"admin@admin.com","admin":true,"administrator":true,"77":"{{template:38dhs_/*admins_only*/_header.html}}"}
```

The file contained the flag `flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`

## Challenge 8 - Forum

The goal for this challenge was to get admin access to the web forum.  I tore my hair out on this one - it was super frustrating!  After doing some testing and recon on the forum I discovered the page: `https://hackyholidays.h1ctf.com/forum/phpmyadmin/`.  Brute forcing logins for the forum and the phpmyadmin page was not successful.  There was a forum user `max`.  I thought, "how strong of a password can a dog really have".  Turns out, pretty strong.

After trying *everything* (SQL injection, password brute force, hidden files, LDAP injection, more password brute force), I was ready to give up.  It turns out that the key to this challenge was not on the `hackyholidays.h1ctf.com` website at all.  There was nothing to indicate this though, and I only discovered it when looking for info on some of the later challenges.  The challenge author had uploaded the source code for the `forum` software on to Github.  This included the password for the phpmyadmin page, although it was only visible in previous commits:

https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae

Logging in with the phpmyadmin credentials (forum/6HgeAZ0qC9T6CQIqJpD) was successful.  This allowed reading of the `users` table:

{F1129103}

Cracking the Grinch's password hash (35d652126ca1706b59db02c93e0c9fbf) revealed his password to be: `BahHumbug`.  Thanks to the Crackstation wordlist :)

Logging in as the Grinch showed the flag: `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`.  It also showed the Grinch's plans - to launch a DDOS once he obtains the IP for Santa's workshop.

## Challenge 9 - Evil Quiz

The evil quiz challenge was possibly the first challenge where what I thought the solution would be actually was exactly correct right from the beginning!  There are three "pages" in the quiz app which allow a user to enter their name, enter their answers, and check their score.  I correctly guessed that this would a "second order" SQL injection vulnerability.

I *attempted* to exploit this one using the `--second-req` parameter of Sqlmap.  But in true Sqlmap fashion it just never worked :(  So I ended up debating spending an hour doing it by hand or an hour battling Sqlmap.  Not sure which was the better way to go, but I just did it by hand.

A "second order" SQL injection means that one page saves the SQL injection data, and a second page returns the data or triggers the injection to actually take place.  We can inject our data on the page `https://hackyholidays.h1ctf.com/evil-quiz` with a `POST` request.  The injection takes place in the `name` parameter.  The result can be seen on the page `https://hackyholidays.h1ctf.com/evil-quiz/score`.  

Testing showed that any `sleep` command was removed from the input, probably to stop the CTF server from dying :)  I was only successful in exploiting this vulnerability as a "Boolean Based Blind" attack, which was somewhat slow going.  It appears that the server runs a SQL query to determine how many other users have the same username.  Since a "count" is returned, extracting data directly does not appear possible.  Instead we can craft SQL queries which either return "true" or "false" to affect the count output.  The following request is an example of the `POST` request used to trigger this attack:

```
POST /evil-quiz HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackyholidays.h1ctf.com/evil-quiz
Content-Type: application/x-www-form-urlencoded
Content-Length: 121
Origin: https://hackyholidays.h1ctf.com
Connection: close
Cookie: session=b0e2497adfcffb94cadce208c7aff1c3
Upgrade-Insecure-Requests: 1

name=test'+union+select+9,9,9,9+union+select+username,password,7,7+from+admin+where+password+like+'s3creT%25'#
```

The `union` statement in the above request causes the SQL result to either show a count of either 2 or 3.  A count of 3 will only be returned if the statement `select username,password,7,7 from admin where password like 's3creT%'` is true (which it is):

{F1129102}


Character by character the results were extracted until the full password for the `admin` user was discovered: `S3creT_p4ssw0rd-$`.  The special characters in the password threw me off for a bit - turns out MySQL doesn't know how to compare whether a `_` is lower or higher than the letter `a`.  I *also* discovered that a MySQL `like` statement does a case-insensitive compare. 

Logging in with the extracted credentials revealed the flag: `flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`

## Challenge 10 - Signup Manager

Even thought this was challenge number 10 it ended up being pretty quick to complete.  The system allows for new users to be registered, but only admin users have full access.  Examining the page source showed a reference to: `https://hackyholidays.h1ctf.com/signup-manager/README.md`.  This revealed that the full source code for this challenge could be downloaded.  It also showed that a user would only be marked as `admin` if there was a `Y` in the correct user field.  By default there would be a `N`.

Examining the PHP files used for the challenge showed that `index.php` did all the main work.  Each user field (first name, last name, etc) would have a fixed size.  Anything larger would be truncated.  The exception to this was the `age` field which would take an integer value instead of a fixed length string.  Checks were in place to ensure that the age value could only be a maximum of 3 digits.  The following code handled this:

```
if (!is_numeric($_POST["age"])) {
                $errors[] = 'Age entered is invalid';
            }
            if (strlen($_POST["age"]) > 3) {
                $errors[] = 'Age entered is too long';
            }
            $age = intval($_POST["age"]);
```

After a couple of tests, I confirmed that long age values were indeed blocked.  The PHP page describing the `intval` function had the hint needed however: https://www.php.net/manual/en/function.intval.php

This page indicates that `intval(1e10);` would return `1410065408`.  Checking on PHP type handling showed that `1e10` also passes the `is_numeric` check.  Since we need only 3 digits, the value `9e9` was used instead.  This was combined with a first and last name of all `Y`, which would overflow their normal fixed position and create our account as an `admin`.  The full `POST` request used was:

```
POST /signup-manager/ HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://hackyholidays.h1ctf.com/signup-manager/
Content-Type: application/x-www-form-urlencoded
Content-Length: 123
Origin: https://hackyholidays.h1ctf.com
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0

action=signup&username=grinch1337&password=test99&age=9e9&firstname=YYYYYYYYYYYYYYYYY&lastname=YYYYYYYYYYYYYYYYY&admin=true
```

This revealed the flag for this challenge as `flag{99309f0f-1752-44a5-af1e-a03e4150757d}`.  It also gave the URL for the next challenge:

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59

## Challenge 11 - Grinch Recon

The Grinch Recon challenge was *by far* the hardest challenge in this competition.  The difficulty went from 0 to 100 with no warning!  Rather than go through the million false attempts I made, here were the steps to successfully complete this challenge:

 1. The `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album` API has a SQL injection vulnerability.  This can easily be exploited, however *nothing* sensitive is stored in the database.
2. The SQL injection can instead be used to cause the server to calculate the hash for an arbitrary image file (described below)
3. A path traversal can be used with the image file URL to target the `/api` pages instead.
4. Only two API endpoints exist, `ping` and `user`.  The `user` endpoint accepts the parameters `username` and `password`.
5. No data can be retrieved using the `image` function due to content type errors.  Instead, we can determine if the API request returns no data (code 204), or data (code 200).
6. The `user` API endpoint appears to be using a `LIKE` statement to look up users.  We can insert a `%` symbol to do a wildcard match, and then character by character extract the valid username and password.

If the above steps sound simple enough, let me assure you, *they weren't*.  At each step along the way I ended up trying at least 10 different things all of which failed.  The initial SQL injection vulnerability was super cool I thought.  Since nothing is in the database, and we need a valid "authentication hash" for the `image` function, we need to use the SQL injection to completely rewrite the SQL query output.  I used the following SQL injection to accomplish this:

`jdh34p'+union+select+'4''+union+select+3,3,''../api/user''+--+','jdh349',user()--+'`

This would result in the value `../api/user` being returned from the SQL query, and would cause the server to calculate the authentication hash needed for this value:

{F1129104}

In the above SQL injection statement there is actually a nested SQL injection.  The first injection is a `union` statement targeting the `album` table query.  The second injection is a `union` statement targeting the `photo` table query.  The server itself is first looking up the album `id` value from the album `hash` input.  The `id` is then used with a second SQL query by the server to look up the `photo` data.  Our injection to the `photo` query ends up being the value:

```
' union select 3,3,'../api/user'
```

The quotes are double encoded so that they survive the first SQL injection and make it to the second.  The end result is that we can obtain an authentication hash for any server path.  

I thought this would be the end of it, but it was the start of much more frustration.  After scripting requests using the SQL injection to obtain a value file hash, I discovered the `/api/user` endpoint.  Unfortunately the server would not return any data:

{F1129101}

Eventually I discovered that a `%` could be added to the username and password fields to extract their values character by character.  This gave:

```
username: grinchadmin
password: s4nt4sucks
```

The flag after logging in to the attack box with these credentials was: `flag{07a03135-9778-4dee-a83c-7ec330728e72}`

## Challenge 12 - Grinch Network Attack Server

This was probably the most fun challenge.  Similar to challenge 11, an "authentication hash" is needed to submit requests to the server with a target IP address.  One of the thousand things I attempted in challenge 11 was brute forcing the shared secret that might have been used with the hash creation.  While this entirely failed for challenge 11, it worked great for challenge 12:

{F1129100}

I used the following John the Ripper rules to add the input text to a wordlist and see if it matched the known hash:

```
[List.Rules:ExampleGrinch]
Az"203.0.113.53"
A0"203.0.113.53"
```

The prefix `mrgrinch463` was in the `rockyou.txt` wordlist, which for some reason remains to be an awesome wordlist for password cracking.  Now that the prefix is known, it is trivial to create a valid MD5 authentication hash for any target value.  This challenge had a super cool "attack console", but unfortunately it wasn't just as easy as attacking `localhost`:

{F1129098}

Input that resolves to `127.0.0.1` is blocked.  I correctly guessed that a DNS rebinding attack might be needed to overcome this.  An awesome, free rebinding service already exists, which is https://github.com/taviso/rbndr

Using the example DNS of `7f000001.c0a80001.rbndr.us` I tried this challenge again.  This DNS server will return `127.0.0.1` half of the time (using the subdomain listed), and `192.168.0.1` the other half of the time.  Since each time the server is called a different IP is given, my first attempt failed.  The second time was successful however!  The attack check passed, and then the DDOS targeted localhost bringing down the Grinch server:

{F1129099}


## Conclusion and Flag Summary

Overall I had a lot of fun with this CTF.  There really was only "easy/medium" and "super hard" web challenges, but it was great to complete them all!

List of flags:

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

Took down the Grinch!

## Attachments
- writeup13.png
- writeup14.png
- writeup12.png
- writeup11.png
- writeup9.png
- writeup8.png
- writeup10.png
- writeup7.png
- writeup6.png
- writeup5.png
- writeup4.png
- writeup3.png
- writeup2.png
- writeup1.png
- writeup0.png
