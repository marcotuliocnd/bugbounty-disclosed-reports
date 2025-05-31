# [api.tumblr.com] Denial of Service by cookies manipulation

## Report Details
- **Report ID**: 1005421
- **URL**: https://hackerone.com/reports/1005421
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-10-11T22:46:29.275Z
- **Disclosed**: 2020-11-29T10:48:55.466Z

## Reporter
- **Username**: fuzzme
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello

## Summary:

I have found at api.tumblr.com two parameters ```consumer_key ``` &&  ```consumer_secret``` allow to modify ```oa-consumer_key```  && ```oa_consumer_secret```  cookies values and property.

An attacker can send a malicious link to reset the cookies of api.tumblr.com, this lead to DOS.
To trigger the DOS, the target/victim account need to click a malicious link.

To restore the account, the victim need to delete all cookies on api.tumblr.com.

Similar issues :  https://hackerone.com/reports/583819

##Vulnerable Url

```
https://api.tumblr.com/console/auth?
```

##Vulnerable Paramater(s)

```
$_GET['consumer_key'];
$_GET['consumer_secret'];
$_POST['consumer_key'];
$_POST['consumer_secret'];
```
## Steps To Reproduce:

1. Login at https://www.tumblr.com/

2. Go to https://www.tumblr.com/oauth/apps and create a random application

/!\ if the cookies "oa-consumer_key" && "oa_consumer_secret" already exist the attack doesn't  work /!\

3. After, create your application, click to this malicious following link 
```
https://api.tumblr.com/console/auth?consumer_key=x;%20domain=tumblr.com;%20Max-Age=1000000000000000000000&consumer_secret=x;%20domain=tumblr.com;%20Max-Age=1000000000000000000000
```

4. Go back to https://www.tumblr.com/oauth/apps and try to connect to api.tumblr.com by clicking in "Explore API".
You will be redirected to https://www.tumblr.com/oauth/authorize?oauth_token=*&source=console and click to authorize

5. loggout and login at tumblr.com

6. Try again to connect to your application

You can follow me in the video POC.

Thanks, good bye.

## Impact

Denial of Service and cookies manipulation

## Attachments
- poc.mp4
