# Possible (we need to wait for some time) takeover of subdomain badootech.badoo.com which is pointing to Medium servers

## Report Details
- **Report ID**: 1034023
- **URL**: https://hackerone.com/reports/1034023
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-11-13T16:16:19.046Z
- **Disclosed**: 2020-12-30T11:23:45.196Z

## Reporter
- **Username**: w2w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: bumble

## Vulnerability Information
##Description:
Hello, team! Recently I found a new subdomain pushed; it's https://badootech.badoo.com/.
The site's content contains a Medium icon with the text "Oops! We couldn’t find that page. Sorry about that.", DNS records are:
badootech.badoo.com.	21399	IN	A	52.1.173.203
badootech.badoo.com.	21399	IN	A	52.4.225.124
badootech.badoo.com.	21399	IN	A	52.0.16.118
badootech.badoo.com.	21399	IN	A	52.1.147.205
badootech.badoo.com.	21399	IN	A	52.4.145.119
badootech.badoo.com.	21399	IN	A	52.4.240.221
badootech.badoo.com.	21399	IN	A	52.4.38.70
badootech.badoo.com.	21399	IN	A	52.4.175.111
badootech.badoo.com.	21399	IN	A	52.6.3.192
badootech.badoo.com.	21399	IN	A	52.6.46.142
badootech.badoo.com.	21399	IN	A	52.1.119.170
badootech.badoo.com.	21399	IN	A	52.5.181.79

This is a classic pointing to the Medium as a part of claiming custom domain. The thing here is that you haven't claim badootech.badoo.com host in the medium but added DNS records that could lead to subdomain takeover. Let's look at the process of how custom domains are linked with Medium's blogs at https://medium.com/feedium/how-to-set-up-a-custom-domain-on-medium-fbcb4041a1b9. https://extranewsfeed.com/ is an example of the Medium custom domain, and it has identical DNS records as your subdomain does! According to the article, steps to registering a custom domain on Medium are as following:
1. Inform Medium you want to turn your publication into a custom domain.
2. You’ll have to send Medium your: Publication URL, your registered domain URL, your domain registrar site (ex. GoDaddy)
3. At one point, Medium charged a $75 fee for doing this service to account for extra costs on their side. I’m not sure if they will restart this or make it free yet.
4. If Medium approves, they will send you: a CNAME and A Records.
5. You have to log in to your domain registrar (ex. GoDaddy) and adjust the CNAME and A Record values to match the ones Medium gave you.
6. Wait 4 to 24 hours, and your new domain should be up and running!

Since DNS records were added already, we can skip the 5th step. All we have to do is to send to the Medium team a link to your domain, a link to my blog on medium, and the hosting name (it's "register" according to whois). Here is my request, along with the answer :

{F1077184}

As you can see, Medium paused, providing the "custom domains" service but will relaunch it soon. When it is available, it'd be possible to take over a domain. I decided to send a report right away and let you know about it before the subdomain will be taken over by someone.

## Impact

Impact here is the phishing as with the "Shopify" subdomain takeover, severity at your discretion. I'd recommend removing DNS records.

## Attachments
- Screenshot_2020-11-13_at_18.09.07.png
