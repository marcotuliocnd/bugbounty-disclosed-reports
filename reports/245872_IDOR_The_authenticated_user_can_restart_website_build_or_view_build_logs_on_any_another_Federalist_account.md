# [IDOR] The authenticated user can restart website build or view build logs on any another Federalist account

## Report Details
- **Report ID**: 245872
- **URL**: https://hackerone.com/reports/245872
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-07-04T16:11:10.631Z
- **Disclosed**: 2017-09-05T20:08:47.988Z

## Reporter
- **Username**: sp1d3rs
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gsa_bbp

## Vulnerability Information
##Description
Hi. I found an Insecure Direct Object Reference vulnerability on the `http://192.168.119.128:1337/v0/build/` endpoint.
{F200108}
When the user wants to restart the build, next request are sent to the endpoint:
```
{"site":<siteid>,"branch":"master"}
```
where siteid is numeric ID of the site.
However, this endpoint does not check, do this site ID belongs to this user. So the any user can restart the build of the site on any other user account. So it can be classified as partial authentication bypass.

##POC
I restarted the build on my localhost inscance on behalf of another user:
{F200109}

##Steps to reproduce
1. Login to the Federalist with your test account (we call it `user1`).
2. Restart the build on one of the sites belongs to you.
3. Catch the request to the 
```
http://192.168.119.128:1337/v0/build/
```
and change `site` parameter to the siteID, which was created on some other account (we call it `user2`).
4. Execute the request. It will be accepted.
5. Login as `user2` and go to this site's builds. You will notice that build was restarted by another user.

##Suggested fix
It looks like other endpoint (e.g. site settings modify) checks the site id correctly. The fix is add additional check too on this specific endpoint.


## Attachments
- vv.PNG
- x.PNG
