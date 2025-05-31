# account.ubnt.com CSRF

## Report Details
- **Report ID**: 101909
- **URL**: https://hackerone.com/reports/101909
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2015-11-24T21:58:43.155Z
- **Disclosed**: 2016-12-05T23:50:51.984Z

## Reporter
- **Username**: benkhlifafahmi
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Good Evening Sir, 
I want to inform you that i have successfully discovered a problem on  the API (django Restfull API) you used to manage the security of 
https://account.ubnt.com
The vulnerability type : CSRF
Vulnerability description : 
An attacker create a web page with the code attached to this  report : "hacking_code.html"
then transfer the link of the file to the  victim (note victim need to be logged in to his account)
once the victim visit the link , his password will be changed immediatly to the password set by the hacker 
Note: an attacker can also change user information (name , email , etc...).
You can watch this video as proof of concept : 
Link : https://mega.nz/#!JZ1DxYyb
and to make this video private you may need to be asked for decryption key : 
the key is :  !██████

Impact : Critical as the account.ubnt.com is the site that manage all acounts on the ubnt.com (ex: community.ubnt.com , store.ubnt.com) , i see this require a quick fix and i am ready to help

How to fix this : 1st you need to enable the csrf_token of Django ; 2nd when change user information you may ask the user for his current password.


PS: if you need any help coding a solution i am ready to do this for you , I have a great knowledge on  DJango Development and i am ready to this for you for free :p 

if you need any thing urgent feel free to call me +█████████ , or mail me ! ███████

Thank you for your time
Best Regards , 
Ben khlifa Fahmi 
CO-Founder & Pentester at Tunisian Whitehats Security

## Attachments
- exploit_csrf_poc.html
