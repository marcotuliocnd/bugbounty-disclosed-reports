# character limitation bypass can lead to DoS on Twitter App and 500 Internal Server Error

## Report Details
- **Report ID**: 819088
- **URL**: https://hackerone.com/reports/819088
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-03-14T05:13:10.468Z
- **Disclosed**: 2020-05-06T16:16:44.949Z

## Reporter
- **Username**: exit_n0de
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: x

## Vulnerability Information
**Summary:**

If you are creating a new moment on `https://twitter.com/{username}/moments` you get redirected to `https://twitter.com/i/moments/edit/{moments-id}`.
There you can set a title, a description and also you can add, if you want, a Tweet to your Moment.
The title and also the description are theoretically limited to 60 characters for the title and 250 characters for the description.
I was able to bypass this character limitation and cause an 500 Internal Server Error Response and, during this process of investigation, a heavy load on the Android App, while I'm sending over a lot of characters with the request to create Twitter Moments which, in the end, cause this heavy load.


**Description:**

I started up BurpSuite to investigate how the creation of this Moments work.
First of all, when you are on the `https://twitter.com/{username}/moments` page and you click on the tiny symbol in the middle right hand corner, I intercepted the following request for creating a moment: {F747462}
In this request is nothing set. No title, no description, nothing. Because you get redirected to `https://twitter.com/i/moments/edit/{moments-id}` where you can edit everything on a beautiful Web UI.

So at this point I can resend the request to create every single time a new empty moment with a new ID.
I thought "What would happen, if I fill in the empty quotes for the title and description params with tons of characters?!".
I tried one request after the other with more and more characters until I've got a 500 Internal Server Error Response. {F747468}
Nice!!
But... this wasn't everything.

During this investigation and re-sending of the create-a-moment-request I've flooded my Twitter Moments with Moments filled with tons of characters and I noticed things are getting veeeery slow. This page was very slow at this point. But before I deleted all this Moments I tried something different. I opened up my Twitter App for Android on my S7 Edge and tried to access the Moments Tab. The App hang up but didn't crashed. {F747458}
Not yet. So I've waited... and waited... and waited. I'm very impatient, so I closed the App and deleted all Moments via the Web Interface on my Computer except for one. {F747461}
I've tried to access it again with the Android App this time with success. It has loaded all the characters. I tapped a little bit around and found out that I'm able to share this Moment with others via Tweet, direct message or via external Apps. I've tried all of them. Via Tweet, App crashed and restarted to the Home Menu. Via DM, App didn't crashed but the message was not send(because of proper character limitation) and via external Apps, the App crashed: {F747460}
I have successfully crashed the Twitter App and I can recreate this process. I'm very proud of myself :D
But... that's still not all. I can copy the link to this Moment via Web UI on my Computer and Tweet or send this link to other people, so I'm able to crash or slow down other people Twitter App by sending them this link to my Moment I've created and demand to open this link (they shouldn't have any doubts because it's an official Twitter Link :p). I don't know how the iOS Version react to this flaw but I think resource consumption isn't that good no matter what OS I'm using.

During the redirection and within the editing there are several other requests. If you are on the editing page the changes you made are "live". So that what you typed in gets automatically saved. This is another method to set the title and the description. If you are not using too much characters and trigger the following response you are able to achieve nearly the same and slow down the Android App in this Tab.

On the following picture you can see that I've tried to get an 500 Internal Server Error with requesting 1.950.000 characters but without success. {F747464}
I've got the 413 response that the request entity was too large. Wow, too large... I didn't expect that... with 1.950.000 characters... *sarcastic laugh*
(There are two requests. One for the title and another one for the description. They are set within the field parameter. The picture PoC_request-entity-too-large.png shows only one req/resp because the other one have the same response.)

But this is one way to handle the flaw. Simply limit the request and respond an error 413 instead of an error 500 :p


**Proof of Concept:**

_Flaw #1 500 Internal Server Error:_

1. Start up BurpSuite
2. Intercept the requests on `https://twitter.com/{username}/moments` if you click on the tiny symbol in the middle right hand corner to create a new Moment
3. change the parameter title or description and fill the quotes with the payload_1.txt (1.950.000 characters, ~2MB): `{"title":"","description":"","is_production_only":true,"has_owner_granted_location_permission":true}`
4. send the request
5. Response code on server side is an 500 Internal Server Error {F747468}


_Flaw #2 DoS for Android(and maybe iOS):_

1. Start up BurpSuite
2. Intercept the requests on `https://twitter.com/{username}/moments` if you click on the tiny symbol in the middle right hand corner to create a new Moment
3. change the parameter title or description and fill the quotes with the payload_2.txt (200.001 characters, ~200kB): `{"title":"","description":"","is_production_only":true,"has_owner_granted_location_permission":true}`
4. send the request
5. send link to victim or tweet the link
6. if the victim click on the link he may have trouble with the twitter app(depends on the smartphone, old or new, android or ios, etc.)

**Attachments:**
- payload_1.txt
- payload_2.txt
- PoC_Android-App-not-responding.jpg
- PoC_crashed-Android-App.jpg
- PoC_Moment-with-tons-of-characters.png
- PoC_empty-request.png
- PoC_request-entity-too-large.png
- PoC_500.png

## Impact

In both cases an Attacker can perform a DoS Attack because there is no proper character limitation within the server requests.



I appreciate everyone who reads this long report <3
Also big thanks goes to the report from @meepmerp #768677, his payload helped me in this case to achieve both of this flaws(this is the reason I used %2Fa as payload characters).

## Attachments
- payload_2.txt
- PoC_Android-App-not-responding.jpg
- payload_1.txt
- PoC_crashed-Android-App.jpg
- PoC_Moment-with-tons-of-characters.png
- PoC_empty-request.png
- PoC_request-entity-too-large.png
- PoC_500.png
