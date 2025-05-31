# Invading Grinch Network and Saving Christmas

## Report Details
- **Report ID**: 1065829
- **URL**: https://hackerone.com/reports/1065829
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-24T13:43:13.248Z
- **Disclosed**: 2021-01-12T17:56:36.997Z

## Reporter
- **Username**: w31rd0
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
#How we saved Christmas

As usual with H1 CTF challenges we are provided with a target URL. In our case it is the following:
https://hackyholidays.h1ctf.com/

We started by visiting the URL and see what is going on. All we could see is a page with an image with a warning message. 

{F1125722}

We quickly view the source code, for any potential hidden hint as a comment. All we could find was some URLs for the hosted content pointing to /assets/ but access there was Forbidden

##**Day 1**

1) We start our enumeration via running a directory enumeration tool.

```shell
./dirsearch -u https://hackyholidays.h1ctf.com/ -e php,txt,jsp
```

2) We get the file /robots.txt in the results. By visiting it we can see the first flag.
`flag{48104912-28b0-494a-9995-a203d1e261e7}`
We also notice a new directory named `s3cr3t-ar3a`. Once we try to visit it, we see that we have to wait for the second day of the event.

{F1115429}

##**Day 2**

1) Day 2 starts and the secret area  page is now updated, with a message indicating that the page has been moved. Therefore we start some subdomain enumeration in the background, just in case and take a closer look into the page.

2) In the source code we can see after a bit the 2nd flag hiding, as also a hint for the next part of the challenge  hinting that there will be an`/apps` directory
`flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}`

{F1115427}

##**Day 3**

1) Third day and we visit the home page, we now see a button that leads as to the following URL as expected based on day2's "awesome" recon.
https://hackyholidays.h1ctf.com/apps

We see a button and once clicked we open a new URL 
https://hackyholidays.h1ctf.com/people-rater

There are some buttons on the page that once clicked pop up an alert box with some *evil* message.

2) We open developer tools to have a closer look and on the network tab we see that for each button a request is sent containing an `id` parameter which includes a base64 encode JSON value such as the following:
https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6Mn0=

3) Once decode we can see that it is a id numeric value. Going through multiple buttons and decoding the URL we can see that they are incremental values.  However we notice that the values start from `id:2` and go up, id of value 1 is missing. 

4) We therefore create a new JSON value with `{"id":1}` and base64 encode it and pass it as a parameter to the above request.
https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=

We can now see the third flag.
flag{b705fb11-fb55-442f-847f-0931be82ed9a}

{F1117733}

##**Day 4**

1) We see a new application at the following URL
https://hackyholidays.h1ctf.com/swag-shop

We notice that in order to purchase an item, we need to authenticate. However it is not possible to perform username enumeration or bypass the login via SQLi, so we need another approach.

2) We start fuzzing the /api endpoint to see if there is something hidden and not present in the source code. which exposes some API endpoints We discover the following endpoints which look interesting
```
/sessions
/user
```
3) By visiting the  URL [sessions](https://hackyholidays.h1ctf.com/swag-shop/api/sessions) we get multiple JWT looking values. We can decode them since the are base 64 encoded and see their content. One of the values stands out since it is longer than all others.  Following command can be used to see that one value contains a UID and rest are NULL

```shell
curl https://hackyholidays.h1ctf.com/swag-shop/api/sessions | jq -r '.sessions[]' | base64 -d | jq -r '.user'
```
The following uid is extracted ` C7DCCE-0E0DAB-B20226-FC92EA-1B9043` and noted down

4)  Trying to use the session values and the cookie values within them doesn't wield any result. Therefore we go back to the /user endpoint. Once we visit it we get the following message

`{"error":"Missing required fields"}`

This is a good hint that we need to discover something more and we are on a right track.

5) We start fuzzing possible parameters on the URL below until we get a hit for the `uuid` parameter. We can then use the identified id from step 3 above and obtain the final flag.

https:////hackyholidays.h1ctf.com/swag-shop/api/user?=FUZZ

{F1117744}

**Url of 4th flag:** https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043
`flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`

{F1117735}

##**Day 5**

1) We visit our new target https://hackyholidays.h1ctf.com/secure-login
2) We start by investigating the login page. By providing some random credentials we notice that the login page returns an error message such as 
`Invalid Username` . This is a good indication of potential username enumeration.
3) We start fuzzing the username with a wordlist with name [1](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/Names/names.txt). After a while we can notice that one response does not contain the `Invalid Username` error. Therefore we have identified a valid username for the application, which is the following
**Username:** access
4) Now we can attempt to bruteforce the password, hoping no rate limit/account lockout is in place. We can use a password list [2](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-100.txt) 
We quickly get a hit and  a redirect for the following password
**Password:** computer
Therefore the following credentials allow access `access:computer`
However on the new screen we see that they are no files to download.
5) We notice though that the cookie set is base64 encoded and once decoded it contains the following values.
`{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}`
6) Admin is set to false, however there is no integrity validation, which might allow tampering with the cookie. We set admin to true and base64 encode the cookie. which gives us the following value. We then can set it as our cookie(securelogin) value in the browser
`eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==`
7) Once page is refreshed we have access to a zip file which we can download. When we try to unzip the file though, we are asked to provide a password.

{F1121043}
8) We can use multiple approaches to this, but I used fcrackzip to perform a dictionary attack.
```shell
fcrackzip -v -D -u -p /rockyou.txt my_secure_files_not_for_you.zip
````
Instantly we get the password for the zip file which is `hahahaha`

{F1121044}
We can now unzip the file and obtain the flag, as also a naughty grinch image ;)
`flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`

##**Day 6**

1) Once new application button is clicked we are directed to https://hackyholidays.h1ctf.com/my-diary/?template=entries.html
2) Any attempt for LFI or to use php filters seems to fail, so we proceed enumerating potential files. We notice that we can get a different response for index.php since it redirects to the page in step 1, while all other files return 404.
3) By trying to play a bit with the `template` parameter, hoping to get LFI we notice after a few attempt that the following URL will disclose source code 
`https://hackyholidays.h1ctf.com/my-diary/?template=index.php`
4) We notice that some filtering is happening with the following preg_replace lines
```php
$page = preg_replace('/([^a-zA-Z0-9.])/','',$page);
$page = str_replace("admin.php","",$page);
$page = str_replace("secretadmin.php","",$page);
```
5) So we see that special characters are removed, besides alphanumeric and the dot. Also if the keyword admin.php is detected its stripped, same for the secretadmin.php afterwards. The order of processing is important here, to craft a valid payload, which will bypass the checks and allow us to access
`secretadmin.php`
6) To do so we crafted the following URL  
https://hackyholidays.h1ctf.com/my-diary/?template=secretasecretadmadmin.phpin.phpdmin.php
Below a representation is show of how the filtering will strip out parts of the provided input in the templates parameter, to allow us to convert our payload to the valid target file

{F1121060}
7) Now we can use the above URL and access the admin protected page and grab our flag (as also see grinch's evil plan)
`flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`

{F1121062}

##**Day 7**

1) New target is [Hate Mail Generator]( https://hackyholidays.h1ctf.com/hate-mail-generator)

2) We proceed with enumerating the application. 
We can see that there is a created email, which has some references to templates  via the following format `{{template:cbdj3_grinch_header.html}}` This can be a hint for later on so we note it down
We can also create our own emails. However when trying to send, we notice that we do not have enough credits. We can only preview the message. We  discover that XSS is possible via the body of the preview request. Example below

`preview_markup=Hello {{name}} ....&preview_data={"name":"<script>alert</script>","":"@test.com"}`

Since though we can not send this data it will not be possible to achieve XSS for now, if we do not bypass the credit check somehow.

3) We also run a directory enumeration and we discover the following endpoint which has also directory listing enabled.
https://hackyholidays.h1ctf.com/hate-mail-generator/templates/
Within that directory a specific template stands out which is our potential target `38dhs_admins_only_header.html `

4) We attempt to create an email and include the payload, but we notice that the application returns the following message

`You do not have access to the file 38dhs_admins_only_header.html`

5) We need to bypass this somehow and access the template.  We notice that the `preview_markup` parameter applies some filtering, striping out special characters like `/` etc

6) Since the `preview_data` parameter has not filtering we decide to fuzz and attempt to tamper with it. We finally discover that we can include templates from the `preview_data` with a reference in the `preview_markup`. 
Therefore we can use a payload like the following to bypass the access restriction and get the flag. 

```http
POST /hate-mail-generator/new/preview HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 100
<--Redacated-->

preview_markup=Hello {{name}}....&preview_data={"name":"{{template:38dhs_admins_only_header.html}}"
```
`flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`

{F1121586}

##**Day 8**
1) New target is [Evil Forum](https://hackyholidays.h1ctf.com/forum/)
2) We start our enumeration and we discover a few usernames
- grinch
- max

Two login pages
- https://hackyholidays.h1ctf.com/forum/login
- https://hackyholidays.h1ctf.com/forum/phpmyadmin

Attempting to bruteforce both does not wield any successful result
3) We progress with further enumeration and we perform some OSINT also. We end up using the challenge creator's name in github to find his profile
https://github.com/adamtlangley

Under that and towards the bottom of the page we can see a repository:
https://github.com/Grinch-Networks/forum

4) We visit the repository and after examining the code for a while we can not see anything sensitive leaked, So we check the commit history. We can find after a whie the following commit [Initial Code Commit](https://github.com/Grinch-Networks/forum/commit/07799dce61d7c3add39d435bdac534097de404dc) which leaks some credentials

```php
self::$write = new DbConnect( true,  'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' );
```
5) We can now use the credentials above and connect to the /phpmyadmin endpoint. Within it we discover  a table named `user` which has the two users discovered befored and their hashed md5 passwords. User grinch also has administrative privileges, therefore can view any post in the forum.

{F1122501}
6) By visiting [crackstation](https://crackstation.net/) we can attempt to see if the hash already exists and we are able to obtain the actual password of the user.
**Password:** BahHumbug

{F1122503}
7) We can now login as the grinch user and view the hidden post and obtain the flag

**Login credentials**
- grinch:BahHumbug

**Flag post:**
- https://hackyholidays.h1ctf.com/forum/3/2

`flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`

{F1122502}

##**Day 9**

1) New target is [Evil Quiz](https://hackyholidays.h1ctf.com/evil-quiz)

2) We see an input field with a username, once submitted we have to answer 3 questions and then we end up seeing results for our questions, as also a message about how many other users use that exact username. XSS payloads will not work here, since special characters are encoded and it would be a self-XSS most likely.
Since there is a comparison with a Database of usernames we proceed with attempting a simple SQL injection payload.
**Plain Username Result**
With our username `w31rd0` we receive a result of 1 user sharing the same username

{F1123369}

**Username Evaluates to TRUE**
With the following payload `w31rd0' OR 1=1-- -` the SQL query will evaluate to TRUE, since we can break the initial query and insert a statement that always evaluates to TRUE

{F1123373}

The above evidence is sufficient enough to confirm the existence of SQL injection. However it is boolean-based second order, since our results can not be viewed directly when submitted and the validity of the query is based on the string returned.

3) After identifying the database type/version, we proceed with attempting to identify the table names.
To do so we can use an injection like the following
```sql
' AND (ascii(substr((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1))) = 113-- -
```

**Apporach Methodology:**
- The above query will attempt to compare the first letter of the first database with an ASCII value (in our case 113 is equivalent to character **r**)
- To decrease the number of request we can try to use different comparison operators (e.g. we can do
```sql
' AND (ascii(substr((SELECT schema_name FROM information_schema.schemata LIMIT 0,1),1,1))) > 113-- -
```
- Then by querying the [score](https://hackyholidays.h1ctf.com/evil-quiz/score) endpoint, we can see if the query evaluates to TRUE or not, based on the result for the usernames
- If the result gives `0 other player(s) `, the query is FALSE. On the contrary if we get a value higher that zero, the query is TRUE, therefore we have identified the first letter of the first database.
- We can continue with the next letter (or by adapting our request if we used the <, > operators) until we get the entire name of our target.
- Move to the next entry (for the databases)

Proceeding with this approach we can get the name for the second database which looks interesting
`Target DB name: quiz`

4) We then can proceed with identifying the tables within the database with a similar approach as with the database names.
We obtain the following table name which seems the one we need
`Target Table name: admin`

5) Next we enumerate the column names for the admin table.
We obtain the following columns names which seem interesting
`Target Column names: username, password`

6) Now having knowledge of the table structure we can exfiltrate data with a query like the following
```sql
test' AND (ascii(substr((SELECT password FROM quiz.admin LIMIT 0,1),1,1))) = 112--  -
```
Injection Request:

{F1123397}

Injected query for password letter exfiltration evaluates to TRUE:

{F1123399}

After a while we obtain the following credentials
`admin:S3creT_p4ssw0rd-$`

Sadly my programming skills are totally bad, however i attempted to make a script that will automate the extraction of each letter (F1123459).
Its not efficient enough, however it will display the first letter of the username. By editing the script we can continue bruteforcing the remaining letters.
The script include also the payloads for the tables, columns which are commented out

7) We can now login in the admin panel [Admin](https://hackyholidays.h1ctf.com/evil-quiz/admin)
And obtain the flag.
`flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`

##**Day10**

1) New target is [Signup-Manager](https://hackyholidays.h1ctf.com/signup-manager/)

2) We poke around a bit to examine the application. We notice in the while inspecting element a comment on the top
`<!-- See README.md for assistance -->`

3) Visiting the [README.md](https://hackyholidays.h1ctf.com/signup-manager/README.md) we get a file. Once opened we can see a few hints with the following stadning out
```
2) Move signupmanager.zip into the new directory and unzip it.
6) You can make anyone an admin by changing the last character in the users.txt file to a Y
7) Default login is admin / password
```
4) Default credentials will not work, therefore they have been probably changed. We try to visit the descriptibed location for the .zip file and we manage to access it and download it.  [signupmanager.zip](https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip)

5) Extracting the contents we see multiple .php files. However the most interesting one is the index.php
Within the file we can see all the processing that happens during the signup and creation o user accounts which is the functionality that has the most potential to be vulnerable.

What we notice is that the username, firstname and lastname are filtered and only a substring of the provided input is used (first 15 characters after all special characters have been removed and only alphanumerics remain)
```php
$username = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["username"]), 0, 15);
$firstname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["firstname"]), 0, 15);
$lastname = substr(preg_replace('/([^a-zA-Z0-9])/', '', $_POST["lastname"]), 0, 15);
```

Also the following function is the one of interest since it checks if the account has administrative privileges. The most important part is the last line. It will check the 112 character and if if matches a Y it will be validated to TRUE.
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
Also the following code is responsible for constructing the string that will be ented in the users.txt file once a user registers and will be checked with the  above function.

```php
function addUser($username,$password,$age,$firstname,$lastname){
    $random_hash = md5( print_r($_SERVER,true).print_r($_POST,true).date("U").microtime().rand() );
    $line = '';
//Pads parameters to reach 15chars by adding # and start concatinating the parameters
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

From analyzing the above code its apparent that we can not use the username, firstname, lastname in a malicious way since they are heavily sanitised.
We see though that the age parameter has less strict checks such as:
```php
if (!is_numeric($_POST["age"]))
if (strlen($_POST["age"]) > 3)
```

Once those check are passed the following happens
```php
$age = intval($_POST["age"]);
```

This is interesting based on this post [intval processing PHP 7](https://www.php.net/manual/en/function.intval.php#120543)
we can notice that  `intval('1e5');` will return 100000.
This fits perfectly our purpose. Since now by adding the additional values, we can overide the  ` $line .= 'N';` which is set by default and change it to Y which will grant us administrative privilleges.

**Signup Request to Obtain Admin Privileges**
```http
POST /signup-manager/ HTTP/1.1
Host: hackyholidays.h1ctf.com
Connection: close
Content-Length: 105
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: https://hackyholidays.h1ctf.com
Content-Type: application/x-www-form-urlencoded
<--REDACTED-->

action=signup&username=w31rdtest&password=password&age=1e5&firstname=loadsofys&lastname=abcdefgabcdeYYY
```
Then we can login with the above credentials and access the hidden message with the flag.

{F1124657}

##**Day 11**

1) New target is [Recon Server](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59) based on the message from Day 10.

2) After a lot of recon and attempts we discover that an SQLinjection exists on the following URL on the `hash` parameter
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=

3) Also we have identified that the images hosted on the server are retrievable via a base64 value, which include an auth token that validates the file. If the authentication token is off, the file retrieval will fail, with a message that the authentication token is wrong.

**Encoded File Retrieval object:**
```
eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzMyZmViYjE5NTcyYjEyNDM1YTZhMzkwYzA4ZThkM2RhLmpwZyIsImF1dGgiOiI3NmJhMDYxZDM1NmM2MjY0YTYwMDUyMTZlMTc3NmJhNiJ9
```
**Decoded Object**
```json
{"image":"r3c0n_server_4fdk59\/uploads\/32febb19572b12435a6a390c08e8d3da.jpg","auth":"76ba061d356c6264a6005216e1776ba6"}
```

4) Furthermore the challenge mentions the /api/* endpoint. However once we try to enumerate API endpoints we see a message.
```json
"error":"This endpoint cannot be visited from this IP address"
```
This is a strong indication of SSRF to be required to access API endpoints.

5) After a lot of trial and error (and then Adam's hint), trying to reverse the auth MD5 creation is not possible. Also dumping the content via the SQLi does not give any additional information, besides what we already have.
After tampering with our injection (and brainstorming with all the  other troubled players), it seems that we can use the SQLi to nest additional queries, once the query is processed by the server it will also be singed with an MD5 hash that is generated and create the image object. Now the image object can successfully retrieve the desired files

6) Based also on the API response [codes](https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/api), we can identify if endpoints and parameters exist or not. Based on that we are able to identify that the `/user` endpoint exists and that it also accepts two parameters `username` and `password`

An example injection is the one below which will return the following message
`Expected HTTP status 200, Received: 204`

SQL Query
```sql
' UNION SELECT "' union select 1,2,'../api/user?username=grinch'#",1,2# 
```

Injected URL
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%27+UNION+SELECT+%22%27+union+select+1%2C2%2C%27..%2Fapi%2Fuser%3Fusername%3Dgrinch%27%23%22%2C1%2C2%23
```
The above URL as described creates the signed image that can be accessed by the following URL where the `data` parameter contains the base64 encoded JSON data with the URL and the auth MD5 hash.
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3VzZXI/dXNlcm5hbWU9Z3JpbmNoIiwiYXV0aCI6IjEzYTVjMDg4NTFiNjdmNTg5ZDQ1NDBjZGJhMzE2NDhiIn0=
```

7)After a lot of additional fails, and attempting to identify more API endpoints and parameters, we had no luck. So we went back to the /api/user endpoint. We started fuzzing the username parameter and we identified some strange behavior.

 We run our fuzzer (we can adapt the one from day10) against the username, and we notice that  by injecting into the username parameter payloads it would return `Invalid content type detected` for one 1 specific character. We have also included the % character which can be interpreted as  `anything` in database queries. Therefore we can assume that this is a TRUE clause, so we might be able to brute-force the username character by character based on boolean based SQLinjection.

On the below injection, we can inject between the $$ symbols (those are removed in the script just added here to highlight the injection point).

Injection URL:
```sql
' UNION SELECT "' union select 1,2,'../api/user?username=grincha$$%&password=%25'#",1,2#
```
Below we can observe that a TRUE clause is confirmed via the error message and that the next letter on grincha is `d`.

{F1127289}

We can perform the same brute-force for the password value, since we have already identified that its one of the parameters accepted by the user API endpoint. After a while we can end up with the final set of credentials.

`grinchadmin:s4nt4sucks`

8) We can now go to https://hackyholidays.h1ctf.com/attack-box/login and login to obtain the flag
`flag11=flag{07a03135-9778-4dee-a83c-7ec330728e72}`

{F1127290}

##**Day 12**

1) New target is https://hackyholidays.h1ctf.com/attack-box

2) We can see that there are some buttons that will send a request with a base64 encoded parameter. Once decoding the value we notice the following content
```json
{"target":"203.0.113.213","hash":"5aa9b5a497e3918c0e1900b2a2228c38"}
```
So the above object sets the target, but also hash a sanity check for tampering (the hash value). If we try to edit that value, the validation will fail and the attack will not start.

3) After fuzzing and trying for hours, we decide to attempt to crack the hash. Since its not in any public database, it most likely uses a salt.
Due to the nature of the challenge, most parts of it use passwords/content related to santa, grinch etc.
We therefore decide to filter out such keyword from the rockyou.txt password list and attempt to see if we can get a valid hash.
What we did is

**Wordlist Generation based on Keywords**
```bash
cat /usr/share/wordlists.rockyou.txt | grep $keyword > keyword-salts.txt
```
**Creation of Crackable Hash**
```bash
for i in $(cat keyword-salts.txt); do echo "5aa9b5a497e3918c0e1900b2a2228c38:$i >>saltedhashes.txt
```
**Cracking with Hashcat**
```bash
hashcat -m 20 saltedhashses.txt pass
```

**Additional Information for Cracking Process**
- Content of pass is the IP from above `203.0.113.213`
- Instead of mode 20 for hashcat we tried mode 10 also, since we can not be sure about the method the salting happened.
- Method 20 in hashcat worked at the end and it is md5($salt.$pass)
- The $keyword to grab content from rockyou.txt wordlist that worked was **grinch**
- The final salt discovered was **mrgrinch463**

4) We can now attempt to forge a valid hash for a target of our choosing. 
```
Target: 127.0.0.1
Salted Hash: 3e3f8df1658372edf0214e202acb460b
New Payload: {"target":"127.0.0.1","hash":"3e3f8df1658372edf0214e202acb460b"}
Attack URL:
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==
```

But once we submit that, we get the following

{F1128273}

5) We keep trying different representations of the 127.0.0.1 such as localhost, 127.1, hex and decimal representation of IP etc. But either they are blocked, or not valid IPs.
While providing hostnames we see that it also does a DNS lookup for the IP, so there might be a DNS related attack.
We move on attempting to go with DNS rebinding.
The following resource can be used [rebinder](https://lock.cmpxchg8b.com/rebinder.html) to craft a domain that will resolve to the selected IPs.
We can put in one spot a random IP and in the second 127.0.0.1 as below

{F1128398}

We now produce the MD5 of the hostname, we can use this web app [MD5 computation](http://md5.my-addr.com/md5_salted_hash-md5_salt_hash_generator_tool.php) to craft a salted MD5 value

6) We can now submit a new attack with the crafted payload.

**Final Payload**
```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiI3ZjAwMDAwMS4xNDE0MTQxNC5yYm5kci51cyIsImhhc2giOiIxZmEyZjM0NjA2YjlkMjFhNzNjZDYyNDI1OTVhOGNlZSJ9
```

We might need to submit this a couple of times to resolve to the desired local address. But once that happens we notice

{F1128403}

7) Once attack is complete we can see the win message page and grab the final flag.
`flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`

{F1128405}


##**Message to the Grinch**

{F1128426}

##**Message to Everyone Else**

Thanks for this CTF. Merry Christmas to you all and a Happy New Year!! Keep Safe.

##**FLAGS**
Here is a small Christmas Gift
```
flag1 = flag{48104912-28b0-494a-9995-a203d1e261e7}
flag2 = flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
flag3 = flag{b705fb11-fb55-442f-847f-0931be82ed9a}
flag4 = flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}
flag5 = flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
flag6 = flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}
flag7 = flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}
flag8 = flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}
flag9 = flag{6e8a2df4-5b14-400f-a85a-08a260b59135}
flag10=flag{99309f0f-1752-44a5-af1e-a03e4150757d}
flag11=flag{07a03135-9778-4dee-a83c-7ec330728e72}
flag12=flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}
```

## Impact

We can share cookies with Santa! :)

## Attachments
- flag2.png
- flag1.png
- 3rd-flag.png
- flag4.png
- uuid-param.png
- zip-day5.png
- frack.png
- php-filter-bypass.png
- flag-6.png
- flag7.png
- access-to-phpmyadmin.png
- flag8.png
- hash-cracked.png
- false-statement.png
- paylod-sqli-true.png
- flag-9.png
- payload-for-pass-extraction.png
- query-evaluates-to-true.png
- sqli-bruteforcer.py
- flag10.png
- welcome.png
- bf-username.png
- flag11.png
- localattack.png
- rinder.png
- attack-locahost.png
- flag12.png
- Studio_Project.jpeg
