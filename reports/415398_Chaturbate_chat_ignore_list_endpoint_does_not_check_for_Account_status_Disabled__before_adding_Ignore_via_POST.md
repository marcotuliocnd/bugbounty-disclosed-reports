# Chaturbate "/chat_ignore_list/" endpoint does not check for Account status: Disabled  before adding Ignore via POST

## Report Details
- **Report ID**: 415398
- **URL**: https://hackerone.com/reports/415398
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-09-27T19:12:45.320Z
- **Disclosed**: 2018-10-31T22:02:30.938Z

## Reporter
- **Username**: nismo
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
##Summary##
Chaturbate.com provides the ability for its users when in chat to ignore other users in chat rooms via DM etc by adding their camhandle name  to ignore_list via HUI

Actually this is just a POST to  `/chat_ignore_list/` getting as a parameter the `username` which is the *camhandle* name in order to add the user to the ignore_list

The same can endpoint is used to unignore the username, by adding the boolen **remove** parameter set as true `remove=1`


Although the endpoint checks for the availability of the account to be ingoned or unignored, the  endpoint does not check for status: **Disabled** Accounts before the POST method, as all the endpoints in Chaturbate do.

Also as said on Hint,  this can be used to add and username even if not participating at Chaturbate room at the time or being online

## Steps To Reproduce:

* Create an account and disable it (in this POC the disabled **airbornh3** was used as a demo) 

* Make a POST to `/chat_ignore_list/` endpoint as

```
username=airbornh3&csrfmiddlewaretoken=XXX
```
{F352078}

* To verify this is actually happening make a call via GET to `/api/ignored_user_list/`

{F352077}

* Make a POST to `/chat_ignore_list/` endpoint as

```
username=airbornh3&remove=1&csrfmiddlewaretoken=XXX
```

{F352076}

You can also verify that the user was unignored via a GET method to `/api/ignored_user_list/` as shown above

##Hint (..get me that POST command in GUI :) )

You can use Burp or any HTTP interceptor to grab and replay an `ignore command` while inside a chatroom to get the POST command as well. Then you can use it to POST and ignore any user even if he is not connected to any room or not Online at all 

##Solution
While checking the account availability you should also check account status Disabled as well as doing on all other endpoints as well

Thanks and keep up the great work
@nismo

## Impact

Misconfiguration, Inappropriate check in endpoint usage

## Attachments
- unignore.png
- checklist.png
- ignore.png
