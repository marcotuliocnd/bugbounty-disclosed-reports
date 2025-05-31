# Wordpress.com REST API oauth bypass via Cross Site Flashing

## Report Details
- **Report ID**: 176308
- **URL**: https://hackerone.com/reports/176308
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-17T13:26:12.658Z
- **Disclosed**: 2018-04-26T21:33:23.186Z

## Reporter
- **Username**: opnsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: automattic

## Vulnerability Information
Hello Automattic Security Team,

There is a vulnerability in `https://public-api.wordpress.com/crossdomain.xml`. This file allows `*.yahoo.com` and `*.yimg.com` to perform cross domain requests to `https://public-api.wordpress.com`. However, these domains are vulnerable to Cross-Site flashing. 
An attacker can inject his own Flash code in `yimg.com` and send requests to any `https://public-api.wordpress.com` URL and read response source code. This allows an attacker to bypass the Wordpress.com REST API oauth authorization flow and get authorization to access the victim Worpress.com account without user interaction.

POC link :
---------------------
http://opnsec.com/wp/hunger.html

Prerequisites :
---------------------
- Tested on Windows 7/8/10 with Chrome 49, Firefox 49 and IE 11/Edge
- Flash must be active 
- You must be logged in wordpress.com
- Note : The POC loads a quite noisy swf file so you should mute the system sound volume before opening it !

Instructions :
---------------------
1. Load the POC link 
2. Wait 10-20 sec
3. If you are logged in wordpress.com, the app "OauthBypasss" will have full authorization to access your Wordpress.com account.

Mitigation :
To solve this vulnerability, you should remove `https://public-api.wordpress.com/crossdomain.xml` file.
If you need to keep this file, you should do a redirection of `http://public-api.wordpress.com/oauth2/` to another subdomain that doesn't have a `crossdomain.xml` file. Like this the yahoo flash applications can still access your API but not the oauth authorization flow.

Regards,
Enguerran @opnsec


## Attachments
No attachments
