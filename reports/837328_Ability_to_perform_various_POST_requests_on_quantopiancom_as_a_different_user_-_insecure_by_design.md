# Ability to perform various POST requests on quantopian.com as a different user - insecure by design.

## Report Details
- **Report ID**: 837328
- **URL**: https://hackerone.com/reports/837328
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-04-02T16:36:50.708Z
- **Disclosed**: 2022-12-21T20:13:05.961Z

## Reporter
- **Username**: irisrumtub
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quantopian

## Vulnerability Information
##Summary:
Due to excessive control of victim's UI over algorithm collaboration feature one is able to force algorithm collaborator to issue malicious POST requests.
##Description:
Hello again my favorite VDP! WebSockets again. Following vulnerability can be abused to attack a person that we collaborate on same algorithm with. 
To understand underlying root of the bug we should review 2 features.

----------------------------------------------------
**First feature** is "Build algorithm" button that checks code for mistakes and quickly builds your algo in IDE.
{F770716}
When you press this button, you issue POST request to `https://quantopian.com/algorithms/ALGO-ID/validate` like this
{F770723}
This request body contains code of algorithm, algorithm id, runtime and dates of backtest. It is meant to check if code contains errors, i think. 
**What is important about this feature?**
Important thing is, it takes user-supplied parameter into URL. To be precise, algorithm IDE page's HTML contains such element - `algo-id`:
{F770728}
When we press aforementioned button, "Build Algorithm", URL is taking ALGO-ID from this element. So if we manually switch this  `algo-id` html element's value to "abracadabra" and press the "Build Algorithm" button, we will automatically issue POST request to `https://quantopian.com/algorithms/abracadabra/validate`. We will get back to this soon.

----------------------------------------------------
**Second feature** is collaboration websockets library's event called `form-update`. We can issue this event when we update any input fields, like algorithm code or backtest dates. For example, when we switch algo from US Futures to US Equities here:
{F770751}
we automatically issue websocket request like this:
{F770754}
By fuzzing with this form-update evenet i found out that with this websocket command we can set our own value to any html element that has `value` attribute. For example, if we issue such WS reuqest (take a look at "value" key):
```json
{"type":"form-update","element":"#algo-id","value":"hello","clientId":"x","roomId":"5ce6e50b298f7c6e0acb68c6"}
```
it will result in following HTML:
{F770767}
Note: since this is a request we issue over websockets, such HTML will be in all collaborators' pages
----------------------------------------------------
**Chaining two features together**
We can chain these 2 features to achieve some results here. For example we'll take security feature that is located at https://www.quantopian.com/account#security - email notification when your account is logge into from a new browser
{F770788}
This is how request would look if we wanted to turn it on:
{F770801}
Actually, the payload doesn't have to be in request body, it can also be in URL of the request. So request like this will return HTTP 200 OK code as well:
{F770805}
Moreover, URL takes first place when server analyzes request, so even if there is uninterpretable garbage in POST request body, if POST request's url parameters are correct, they will be parsed properly.
This is crucial for this bug.

Now, let's remember that:
-  ../../../../ on linux means previous directories.
- # will mean like comment in code - if it's wrong, just skip it :)

And finally, **exploit**:
Let's issue websockets request like this:
```json
{"type":"form-update","element":"#algo-id","value":"/../../../../../users/update_preferences?prefs%5Bsend_login_detected_email%5D=false","clientId":"x","roomId":"5ce6e50b298f7c6e0acb68c6"}
```
Our HTML (and our victim's) will look like this:
{F770819}
And when we our our victim will press on "Build algorithm", he will issue this request
{F770822}
We don't care about request's body since the url and supplied parameters are working properly. This will result in our victim himself turning off email notifications of new logins.

Another example, but with several parameters:
```json
{"type":"form-update","element":"#algo-id","value":"/../../../../../users/update_profile?firstname=h1&lastname=test&bio=hi#","clientId":"x","roomId":"5ce6e50b298f7c6e0acb68c6"}
```
If we issue such request and victim presses "build algorithm", he will rename himself to h1 test, with bio "hi"

By using /../../../ and putting request parameters from body in URL we can do all sorts of stuff. Basically, we can do ANY POST request on https://quantopian.com since we control url of request and its parameters, excluding those requests that require knowing passwords (like change password or email) or require knowledge of private strings like when you want to publish a topic, you need to know previously generated topic ID. More info on this in impact section. 

## Steps To Reproduce:



  1. engage in collaboration with someone
  2. craft malicious websocket request, like examples above, and issue it
  3. wait for victim to press "Build algorithm".


## Test account information

tvburis+hackerone@gmail.com
irisrumtub+hackerone@mail.ru

## Impact

So far i found that we can:
- rename user, as described above
- disable email notifications when logged in from new browser, as described above
- delete any of his public posts on forum (especially that would hurt contestants if we have any of those in our collaboration, we can delete their submissions) (the thing here is that deleting posts isn't using DELETE http method, but rather uses POST request to `/posts/delete_post`, and as a parameter it takes public post's ID that we can look up in html.
- comment on any existing topic on his behalf. (the endpoint is /posts/submit_reply, and it takes 2 parameters: `parent_post_id` and `text`, where parent post is OP post's ID which is publicly visible, and text is what we wish to write. Important stealth information here is - since victim issued those requests himself, it will be hard to trace the real attacker here.

## Attachments
- screen_1.png
- screen_2.png
- screen_3.png
- screen_4.png
- screen_5.png
- screen_6.png
- screen_7.png
- screen_8.png
- screen_9.png
- screen_10.png
- screen_11.png
