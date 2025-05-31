# critical server misconfiguration lead to access to any user sensitive data which include user email and password

## Report Details
- **Report ID**: 1365738
- **URL**: https://hackerone.com/reports/1365738
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-10-11T16:21:15.843Z
- **Disclosed**: 2021-11-02T15:50:55.911Z

## Reporter
- **Username**: mr_robert
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: flickr

## Vulnerability Information
Hi flickr team,
I found a critical issue lead to access to any user sensitive data which include user hashed password and possibly can lead to takeover any user account on  flickr's main site, literally i can get all  user information from database with no restrictions ,
Let me explain how this happen:

As we know Flickr that it was belong to Yahoo and also it was  hosted on many servers, including Amazon servers,
And after Flickr reboot as an independent and separate organization from Yahoo
This servers still has full access to Flickr’s main server databases 
The attacker can use this old flickr server to get a lot of sensitive information belong to any user 
By using “published user image name” and search by it ,on Flickr yahoo old server

For example :
We have user x  and he posted a photo named “golden_arrow_img” 
Now let’s say the attacker know his victim user and now he know how to get all user sensitive data , he will go to misconfigured server  which it’s address is : https://34.235.208.201 But when he goes to this address, he only sees an error message and the logo of Flickr, and after a while of checking the available paths, I found that when I add the word start, all the content of the server appears,the address will be https://34.235.208.201/start , you will see a search box, go to search by the name of the published user image which is for example “golden_arrow_img”, but you will not see the results in The page, server will redirect you to the first error page , the request must be stopped by burp-suite proxy and send it to the repeater then repeat the request, you will see the results, search in the repeater results for the function called ==“Y.listData”==
You will see under this function all user sensitive data, which is will be like :

```
Y.listData = {
		"user": {
				"id": "193923944",
				"first_name": "robert",
				"last_name": "carlos",
				"email": "robert_d1999@yahoo.com",
				"date_creation": "1631706054",
				"date_modified": "0",
				"password": "d63b6d249dcc52ef335b0eeea167fef1",
				"city": "los angelos",
				"country": "United states",
				"check_code": "",
				"email_conf": "1",
				"email_conf_bounce": "0",
				"nsid": "194016757@N08",
				"character_name": "robert_d1999",
				"gender": "M",
				"magic_email": "",
				"is_admin": "0",
				"is_bad": "0",
				"prefs_main_1": "2056",
				"prefs_main_2": "262161",
				"mail_buffer": "",
				"deleted": "0",
				"kill": "0",
				"kill_from": "0",
				"refer_code": "",
				"date_limit": "0",
				"photo_id_limit": "0",
				"date_premium_end": "0",
				"is_paid_pro": "0",
				"has_order_history": "0",
				"gifts_to_give": "0",
				"path_alias": null,
				"date_iconchange": "0",
				"pref_default_license": "0",
				"upload_email_tags": "",
				"upload_email_size": "2",
				"upload_email_body": "0",
				"timezone_id": "5",
				"timezone_dst": "1",
				"buddyicon_server": "0",
				"unread_mail": "0",
				"yid": "ef29e4c8-ee47-45a1-8a26-32b2203b6d83",
				"yhid": "ef29e4c8-ee47-45a1-8a26-32b2203b6d83",
				"dot_yjid": null,
				"yintl": "eg",
				"lang": "1",
				"cluster_id": "39",
				"cluster_lock": "0",
				"adultness": "2",
				"commercial": "0",
				"last_activity": "1633964310",
				"bb_partner_id": "0",
				"stats_cluster_id": "1",
				"stats_cluster_lock": "0",
				"yreg": "0",
				"has_stats": "0",
				"contact_cluster_id": "1",
				"contact_cluster_lock": "0",
				"unread_mail_inbox": "0",
				"buddyicon_max_resolution": "0",
				"coverphoto_server": "0",
				"addons": "0",
				"yalias": "robert_d1999@yahoo.com",
				"ins_ts": "2021-09-15 11:40:54",
				"upd_ts": "2021-10-11 14:58:49",
				"has_csam": "0",
				"display_yhid": "robert_d1999@yahoo.com"
			},

```
==This is a summary, not all information, there is more fields==

##Steps to reproduce :
1. Go to https://34.235.208.201/start
2. Open burp suite 
3. Search by the name of the published user image which is for example “golden_arrow_img” 
4. Intercept the request and send it to repeater then repeat the request
5. search in the repeater results for the function called “Y.listData”
You will see under this function all user sensitive data

##Screenshots:
F1478270
F1478271

## Impact

The attacker can access to any user sensitive data which include user hashed password and possibly lead to takeover any flickr user account , literally the attacker can get all  user information from database with no restrictions

## Attachments
- flickr-yahoo-old-server.png
- user-data.png
