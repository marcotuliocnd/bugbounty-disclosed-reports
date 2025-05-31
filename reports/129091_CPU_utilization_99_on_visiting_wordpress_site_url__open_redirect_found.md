# CPU utilization 99% on visiting wordpress site url & open redirect found

## Report Details
- **Report ID**: 129091
- **URL**: https://hackerone.com/reports/129091
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-04-07T19:41:31.604Z
- **Disclosed**: 2017-07-23T10:30:48.394Z

## Reporter
- **Username**: csanuragjain
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
**Working POC for making CPU 99% for wordpress user**
+ Login to wordpress account
+ Visit any of the below url's which are sent by attacker to victim (since these are wordpress url so victim will accept & open)
1.https://wordpress.com/post/20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
2.https://wordpress.com/design/1000000000000000000000
3.https://wordpress.com/pages/anurag.wordpress.com/-10000000000000000000000000000000000000000000000
+ Check your CPU usage in task manager. It would go to 99% as shown in attached.
+ This happens since these pages continues to send unlimited requests to https://pixel.wp.com/g.gif?v=wpcom-no-pv&x_newdash_pageviews=route&t=0.1642450245826501
+ Unlimited request are send since I think the variable holding the Post id cannot hold a value as long as 20000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 which throws an exception.
+ **Problem:** User CPU goes 99% causing the browser to go very very slow & unresponsive. Negative impact on customer.

**Working POC for open redirect**
+ Access wordpress using url https://wordpress.com/wp-login.php?redirect_to=https%3A%2F%2Fgoogle.com%2Fsearch?q=myFakeSite&reauth=1
+ After login you will be redirected to https://www.google.co.in/search?q=myFakeSite&gws_rd=cr&ei=WLYGV8fUHIq8uATj56uIBA which is incorrect. Wordpress should not allow redirecting to external websites like google,yahoo.
+ **Problem:** In future if there is any bug in these external site then this open redirect from wordpress could cause harm to users.

## Attachments
- wordpress.png
