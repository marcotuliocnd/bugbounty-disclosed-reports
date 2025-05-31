# [H1-2006 2020]  "Swiss Cheese" design style leads to helping Mårten Mickos pay poor hackers

## Report Details
- **Report ID**: 890272
- **URL**: https://hackerone.com/reports/890272
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-06-03T16:59:48.340Z
- **Disclosed**: 2020-06-18T15:30:44.604Z

## Reporter
- **Username**: al-madjus
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Summary:
Several vulnerabilities in the bountypay application leads to unauthorised access, information disclosure, SSRF and other fun stuff. 

# Steps To Reproduce:

This is how I helped Mårten Mickos pay the poor hackers who had been waiting so long for their bounties. 

## First part: Web 

I started by finding all subdomains for challenge: 
https://bountypay.h1ctf.com
https://app.bountypay.h1ctf.com
https://staff.bountypay.h1ctf.com
https://api.bountypay.h1ctf.com
https://www.bountypay.h1ctf.com
https://software.bountypay.h1ctf.com

Fuzzing the subdomains, I found this: `https://app.bountypay.h1ctf.com/.git/HEAD`
Checking `/.git/config` showed the link to the github repo and an interesting file: 
`https://github.com/bounty-pay-code/request-logger/blob/master/logger.php`
which referenced the file `bp_web_trace.log` which could be found here: 
`https://app.bountypay.h1ctf.com/bp_web_trace.log`

Decoding the contents of that file gave: 
`{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}`
This looked like a server log which included credentials for the user 'brian.oliver', plus a challenge_answer. 

Logging in to `app.bountypay.h1ctf.com` which this user resulted in a 2fa challenge.
{F854022}
Supplying the answer from the log did not pass the 2fa, apparently that answer had expired. 
Looking at the source of the challenge, the `challenge_value` is 32 chars long, which could indicate an MD5sum. Trying to bruteforce this value did not give any result, apparently it is now a common word. 
Maybe it's the MD5sum of the challenge answer? The md5sum of `bD83Jk27dQ` is `5828c689761cce705a1c84d9b1a1ed5e` and intercepting the 2fa POST request and putting those 2 values in resulted in passing the 2fa! 

I was now presented with the BountyPay Dashboard. Loading all transactions through the past few years and into the future
returned empty responses. However the reply included an API URL that the backend used to look up the transactions. Qeueing the API directly gave "Missing or invalid Token", apparently I was not authenticated on that subdomain so I'd have to fuzz the API through `app.bountypay`. 
At this point I noticed that putting a path traversal in the cookie (which is base64 encoded JSON) like this: 
`{"account_id":"F8gHiqSdpK/../F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}`
resulted in the same result as the original cookie. Maybe I could exploit this?

Earlier I had noticed how `api.bountypay` had a redirect function that only allowed redirecting to a limited subset of URLs, including many of the `*.bountypay` subdomains. One of those subdomains, `https://software.bountypay.h1ctf.com` returned `401 Unauthorized` telling me I was not allowed to access it from my IP. Maybe I could use SSRF to access it
from `api.bountypay`? 
After some trial and error I constructed the following payload: 
`{"account_id":"F8gHiqSdpK/../../../redirect?url=https://software.bountypay.h1ctf.com/#","hash":"de235bffd23df6995ad4e0930baac1a2"}`
which used path traversal to back up to the index page, redirected to `software.bountypay` and included a trailing `#` to get rid of the `statements` parameter added by the bountypay dashboard. 

With this I could now view the contents of software.bountypay which presented a login portal. 
Seeing no way past this (it only accepted POST requests, GET requests did not work) I resorted to fuzzing the subdomain, writing a quick python script to do this.
With this I found an /uploads folder that contained a file called `BountyPay.apk`. 
{F854027}
Luckily getting this file was possible from any IP, as it wasn't possible to get it via SSRF. 

## Second part: Mobile
This part presented me with a lot of trouble, mainly because I have very little experience with mobile hacking. 
After solving a lot of problems with Android Studio specific to my system I was able to get an Android virtual device running with the BountyPay apk and also attached a logger. 
I also decompiled the apk using `jadx-gui` and found the three main activities for the app. The application uses intents but I was not able to make those work in the virtual device, so I logged into it via `adb` and launched them via the shell. 
Launching the application and logging in (it didn't seem to matter which username I used) I looked at the decompiled code to see what was required to pass Part One (which presented the hints "Deep Links" and "Params").
`if (getIntent() != null && getIntent().getData() != null && (firstParam =
getIntent().getData().getQueryParameter("start")) != null &&
firstParam.equals("PartTwoActivity") && settings.contains("USERNAME"))`

So I needed to pass an intent with one parameter containing "PartTwoActivity": 
`am start -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity"`
With this I was presented with Part Two, which gave these hints: "Currently invisible" and "Visible with the right params". 
Again from the decompiled code: 
`String firstParam = data.getQueryParameter("two");
String secondParam = data.getQueryParameter("switch");
    if (firstParam != null && firstParam.equals("light") &&
      secondParam != null && secondParam.equals("on"))`

So this time we needed 2 parameters, "two=light" and "switch=on", which I passed like this: 
`am start -a android.intent.action.VIEW -d "two://part?two=light&switch=on"`

Now I saw the 'invisible' thing, a hash value and an input box to check a header value (the hash value?). 
{F854035}
Writing down the hash thinking it would be useful later, I started submitting header values. It wasn't the hash, so I again looked at the decompiled code.  
`if (str.equals("X-" + ((String) dataSnapshot.getValue())))`
So it had to start with "X-" and then the value of `dataSnapshot`. I couldn't really identify that value so I just tried different values and happened upon "X-Token" - and it worked! I was now on Part Three! 

This part required 3 parameters according to the source code, the first 2 being base64 encoded values and the last the value of the X-Token: 
`if (str != null && decodedFirstParam.equals("PartThreeActivity") && str2 != null && decodedSecondParam.equals("on") && (str = secondParam2) != null) {
                        if (str.equals("X-" + value)) `
Again I thought that this token would be the hash leaked before, but no, once again it was just "X-Token"! 
Passing that with `adb` the application crashed. I had to go through the process several times, sometimes it would crash, other times it would go back to Part Two instead of advancing until I URL-encoded the equal signs in the base64: 
`am start -a android.intent.action.VIEW -d
"three://part?three=UGFydFRocmVlQWN0aXZpdHk%3D\&switch=b24%3D\&header=X-Token"`

With this I advanced and got a screen asking to input a hash. Again it wasn't the hash from before but looking in the attached logger I saw the following token: 
`X-Token: 8e9998ee3137ca9ade8f372739f062c1`
Putting this in the input box I was presented with a screen saying I had completed all Android challenges! 
{F854039}
{F854040}


## Third part: PrivEsc
Using the newly found X-Token I went to `api.bountypay` where it authorised me. I could now query the API and found the `/api/staff` endpoint which listed staff names and ids. Trying to make a POST request to this endpoint gave `409
Conflict "Staff Member already has an account"`. Interesting! 
Earlier an official hint was posted on Twitter for a new staff hire showing her staff card with this staff ID (never do that kids!): `8FJ3KFISL3`
Putting this in the request with a ficticious name resulted in this: 
{F854043}
Trying these credentials on the staff login portal worked, I now had staff access! 

Going through the staff application I found 4 important clues: 
+ `website.js` referred to 2 interesting functions: `upgradeToAdmin` and a
report URL, plus `#tab{1,4}` which were queried in the location hash. 
+ Using the parameter `username` I could populate the login screen like this: 
`https://staff.bountypay.h1ctf.com/?template=login&username=sandra.allison`
+ Using arrays, I was able to chain templates together in the same site like
this: 
`https://staff.bountypay.h1ctf.com/?template[]=login&template[]=ticket&ticket_id=3582`
+ There was an injection in the upgrade avatar functionality, but any non-alphanumerics were stripped away. 

Playing around with each of these functionalities didn't really get me anywhere. I was unable to get upgraded to admin just by reporting the upgrade URL, and I couldn't really get XSS or anything else interesting via the injection vulnerability. 

For this step I'd like to credit Clos2100 and Simone Bovi who I was collaborating with; they helped me put all the above clues together. 
Turns out there exists something called "Event Bubbling", where by passing one JavaScript event together with another associated function, causes them both to execute. Chaining the above clues together like this resulted in getting
upgraded to admin privileges: 
Injecting a `tab1` event into the avatar name together with the `upgradeToAdmin` function caused this function to execute too. 
`profile_avatar=tab1+upgradeToAdmin`
However, since `upgradeToAdmin` required a username`'input[name="username"]'` I needed to supply the username via the parameter mentioned earlier, and chain both  pages together (the avatar is reflected in the Support Tickets page) and finally supply the `#tab1` event in the URL:
`https://staff.bountypay.h1ctf.com/?template[]=login&username=sandra.allison&template[]=ticket&ticket_id=3582#tab1`

Sending this link to the admin via the report link, and intercepting the request and adding `#tab1` and again base64 encoding (the #... part gets removed by the report functionality) I was able to get admin privileges. 

Going to the admin area I got Mårten Mickos' login credentials: 
`marten.mickos:h&H5wy2Lggj*kKn4OD&Ype`
{F854048}


## Fourth part: 2FA 
Mårten's login credentials worked on `app.bountypay`, which again required me to bypass the same 2fa challenge as before. 
Going to the dashboard I loaded the transactions for 05/2020 and clicked pay.
After spending hours and hours trying to funnel the 210.300$ into my own account I gave up and instead focused on completing the CTF (hackers gotta be hackers...). 

Clicking 'Pay' lead to another 2fa (at first I thought it was the same as before and said "Why do they even bother?") - but of course this was 1000x more difficult! Loading the challenge caused the client to make a POST request with a css file, I could change the link to the file and have it contact my server (though only HTTPS servers which caused me some trouble). I served a slightly altered css file that simply changed the background colour, but this resulted in no change. Inspecting the file closer lead me to believe it was used server side for the 2fa functionality. Interesting: maybe this was where the codes were displayed? 

I started looking into css injection techniques and read an interesting blog post by D0nut. I tried creating a similar attack to extract the challenge codes out-of-band, supposing them to be visible server side. 
Once again I must credit Clos2100 as well as FersingB for helping me with this step. After a lot of trial and error I came up with a css attack script that queried each character of the code letter for letter, sending back the correct character to my server. The script is attached below (F854056). 
Sending this malicious css file to the server and then looking in my server log I saw all 7 characters (though out of order) and had 2 minutes to input them. This passed the final 2fa challenge and all the hackers finally got paid!

^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$

{F854058}

# Supporting material
Blog post by D0nut referenced for the css attack: 
https://medium.com/@d0nut/better-exfiltration-via-html-injection-31c72a2dae8b

## Impact

Hackers could get paid. Who would want that? :-p

## Attachments
- first_2fa.png
- apkfile.png
- parttwo.png
- x-token.png
- congrats.png
- staff_created.png
- mickos.png
- uni_2fa_style.css
- flag.png
