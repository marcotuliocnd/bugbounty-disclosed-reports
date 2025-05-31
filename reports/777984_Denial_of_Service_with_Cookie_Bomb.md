# Denial of Service with Cookie Bomb

## Report Details
- **Report ID**: 777984
- **URL**: https://hackerone.com/reports/777984
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-01-19T19:48:09.167Z
- **Disclosed**: 2020-04-03T09:42:56.060Z

## Reporter
- **Username**: bihari_web
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nordsecurity

## Vulnerability Information
## Summary:
This is Denial of Service attack by using which an attacker can make an user unable to access nordvpn.com website.
For more information you can read this article.
[https://blog.innerht.ml/tag/cookie-bomb/]

## Steps To Reproduce:
This will usually work on  user's fresh session for which we can use inconginito tab.

  1. Open fresh user session to website (Or Incognito Tab)
  1. First visit this link 
https://nordvpn.com/xxxxx.....xxxxxxx_up_to_4kb_in_size

When we visit this link or the home page of the website two cookies are set i.e *FirstSession* and *CurrentSession*
For every session, **FirstSession** Cookie is only set once and the **CurrentSession** cookies keeps on updating based on some **path** values.
Note: These cookies are set by javascript.

Cookie format for both of them is like this 
**FirstSession: source=(direct)&campaign=(direct)&medium=(none)&term=&content=&hostname=nordvpn.com&pathname=/&date=20200119**
**CurrentSession: source=(direct)&campaign=(direct)&medium=(none)&term=&content=&hostname=nordvpn.com&pathname=/&date=202019**
Here the **pathname** parameter is path to the website that we are on.
Since the pathname is directly set into  these cookie from the visited url, and there is no size limit on the url path.
Hence we can make a request to long random path up to of 4 Kb (Max size of a cookie) and both of the cookies will contain 4kb of randome data.
But the **CurrentSession** cookies will change on each path followed, hence it will change it's payload size.
For this attack to be successful we need aprox 8Kb of Cookies size. (Atleast we have 4Kb now from *FirstSession*)


  3 . Now Visit this final link
https://nordvpn.com/order/?2year&coupon=anything&ref=xxxxx.....xxxxxxx_up_to_4kb_in_size
This will set a cookie **n_ref** with the value of **ref** parameter.
And Now we have appox 8Kb of cookies and most of the webservers don't accept this large size of request and hence we now have a persistent Denial Of Service Attack.

## Supporting Material/References:
  * F689645
  * https://drive.google.com/file/d/1bgLTJd3ZNK9S7gHAz3g0Ksiz78BYWXOV/view?usp=sharing 
Video PoC Link

## Impact

User will not we able to access the website, and will have persistent DoS attack untill he deletes all the cookies manually.

## Attachments
- poc.html
