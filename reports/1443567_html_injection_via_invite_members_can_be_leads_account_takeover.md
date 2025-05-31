# html injection via invite members can be leads account takeover 

## Report Details
- **Report ID**: 1443567
- **URL**: https://hackerone.com/reports/1443567
- **State**: Closed
- **Severity**: low
- **Submitted**: 2022-01-07T17:24:01.509Z
- **Disclosed**: 2022-03-22T10:15:21.944Z

## Reporter
- **Username**: unnamedx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mattermost

## Vulnerability Information
Hi team,
I have found an vulnerability on your website .
step to reproduce :
1.navigate to : yourworkspace.cloud.mattermost.com
2.create new channel F1571445
3.there you will find a functionality invite members F1571448
4.click on invite members 
5 input your email address 
6.scroll down & click on invite as guest F1571456
7. on Add to channels input your channel name 
8.click on set a custom message , input this html payloads : <a href=evil.com>click</a>
<input type=x>
9. invite 
10.open inbox of  email that you have invited
as you can see  html injected & there's an input field & click button 

follow my video poc for better understanding & if you need any info let me know .
thanks for reading my report .God bless you

## Impact

As HTML injection worked in email an attacker can trick victim to click on such hyperlinks to redirect him to any malicious site and also can host a XSS page. All this will surely cause some damage to victim. This could lead to users being tricked into giving logins away to malicious attackers.

## Attachments
- Screenshot_from_2022-01-07_23-10-23.png
- Screenshot_from_2022-01-07_23-15-57.png
- Screenshot_from_2022-01-07_23-10-40.png
- cloud.mattermost.com_html_injection.mkv
