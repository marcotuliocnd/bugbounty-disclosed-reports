# csrftoken not unique to session or specific user and csrfmiddlewaretoken  can be altered

## Report Details
- **Report ID**: 2513333
- **URL**: https://hackerone.com/reports/2513333
- **State**: Closed
- **Severity**: low
- **Submitted**: 2024-05-21T02:27:34.277Z
- **Disclosed**: 2024-11-20T11:31:31.433Z

## Reporter
- **Username**: bashbdeer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mozilla

## Vulnerability Information
Hello, while looking at the website i noticed 2 things when trying to delete a token

{F3285661}

assuming i click on Delete this token button (in picture above)
1. a post request will be sent  /api/tokens/delete/302 or /api/tokens/delete/some_number
and i see in burp that in the cookie's header csrftoken = vhHMjvtks3jwGkHikbY48d5gQR76yvPA and  i see in the params sent that csrfmiddlewaretoken= 8b9QkWMZgnqohp9R77Tu4m46PQW0YZRwtiGsth59ygzKNzGZh8Ho2pZcvxTWmkwW

what i noticed is that  changing csrfmiddlewaretoken's value to csrftoken 's value will still make the request work..
ie setting csrfmiddlewaretoken = vhHMjvtks3jwGkHikbY48d5gQR76yvPA  will still let the request work

this is the actual request
{F3285657}

this is the modified request which works!
{F3285659}

altered request successfully  deleted the api oken
{F3285662}

2. i noticed that the csrftoken sent in requests is not unique to the session id or user logged , meaning if im logged in as user1 and have csrftoken=x
then i can  login as user2 and send the request with csrftoken=x and csrfmiddlewaretoken=x and it will work!

for example in one of the users i logged in the csrft token was csrftoken= c7wq7XJaQq71Eump3tVwNJpOSHLbiqSC

lets say i want to delete a token again

this is the original request i get as user2

{F3285671}

i change the csrftoken and the csrfmiddlewaretoken to be the csrfttoken i got when logged as user1
ie im using a csrftoken of another user

{F3285673}

and as you can see this request works just fine and deleted the token api

{F3285677}


what does this mean?
1.this means csrfmiddlewaretoken  does not really add another layer of protection, i can easily change it the  csrftoken stored in the cookie and it will still work
2. given a valid csrftoken from any user (for example csrftoken=c7wq7XJaQq71Eump3tVwNJpOSHLbiqSC), its possible to create a csrf request that sends the POST  /api/tokens/delete/**index** request (where **index** can be enumerated ) with this valid csrftoken being sent as the csrfmiddlewaretoken value and with 
X-CSRF-Token set also as the valid csrf token as well and it will work and we can manage to delete user api tokens through csrf exploit( for example clicking on a website that sends such request) 
i also see that when sending an options request to /api/tokens/delete, access control allow headers are

access-control-allow-headers: accept, authorization, content-type, user-agent, x-csrftoken, x-requested-with
access-control-allow-methods: DELETE, GET, OPTIONS, PATCH, POST, PUT
access-control-allow-origin: *


{F3285690}

## Steps To Reproduce:


  1. log in as any user (user1), take the csrf token from the cookie and save it somewhere

  1.1.try to delete an existing api token (if you dont have create one), and intercept the request and change the csrfmiddlewaretoken  to the csrf token you took from the cookie, you should see that the request will still work.
  3. now logout from user1 and login as user2
  4. try to delete an existing api token (if you dont have create one), and intercept the request and change the csrfmiddlewaretoken  and the csrftoken to the first csrf token you got from when you were logged in user1, you will see that the request will work and will pass

## Impact

## Summary:
CSRF Exploit
1.this means csrfmiddlewaretoken  does not really add another layer of protection, i can easily change it the  csrftoken stored in the cookie and it will still work
2. given a valid csrftoken from any user (for example csrftoken=c7wq7XJaQq71Eump3tVwNJpOSHLbiqSC), its possible to create a csrf request that sends the POST  /api/tokens/delete/**index** request (where **index** can be enumerated ) with this valid csrftoken being sent as the csrfmiddlewaretoken value and with 
X-CSRF-Token set also as the valid csrf token as well and it will work and we can manage to delete user api tokens

## Attachments
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
- image.png
