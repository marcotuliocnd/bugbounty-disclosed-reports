# Grinch-Networks taken down - hacky holidays CTF 

## Report Details
- **Report ID**: 1069189
- **URL**: https://hackerone.com/reports/1069189
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-31T09:09:51.900Z
- **Disclosed**: 2021-01-11T22:06:08.809Z

## Reporter
- **Username**: pirateducky
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
## Summary:
CTF Submission

```
Day 1: flag{48104912-28b0-494a-9995-a203d1e261e7} 
Day 2: flag{b7ebcb75-9100-4f91-8454-cfb9574459f7} 
Day 3: flag{b705fb11-fb55-442f-847f-0931be82ed9a} 
Day 4: flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6} 
Day 5: flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004} 
Day 6: flag{18b130a7-3a79-4c70-b73b-7f23fa95d395} 
Day 7: flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd} 
Day 8: flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}
Day 9: flag{6e8a2df4-5b14-400f-a85a-08a260b59135}
Day 10: flag{99309f0f-1752-44a5-af1e-a03e4150757d}
Day 11: flag{07a03135-9778-4dee-a83c-7ec330728e72}
Day 12: flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}
```

{F1139188}

## Steps To Reproduce:

- Day 1: /robots.txt
- Day 2: /s3cr3t-ar3a
  - inspect html
  - the flag is dynamically built
- Day 3: /people-rater
  - [https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=](https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=)
- Day 4: /swag-shop
  - [https://hackyholidays.h1ctf.com/swag-shop/api/sessions](https://hackyholidays.h1ctf.com/swag-shop/api/sessions)
  - One of the sessions has a user value `C7DCCE-0E0DAB-B20226-FC92EA-1B9043` 
  - [https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043](https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043)
- Day 5:  Secure Login
  - bruteforce the username: `access` & password: `computer`
  - Edit the cookie to make ourselves admin
  - `/my_secure_files_not_for_you.zip` 
  - password for zip: hahahaha
  - {F1139213}
- Day 6: /my-diary/?template=entries.html
  - `/my-diary/?template=index.php` discloses the source
  - [ https://hackyholidays.h1ctf.com/my-diary/?template=secretadsecretaadmin.phpdmin.phpmin.php]( https://hackyholidays.h1ctf.com/my-diary/?template=secretadsecretaadmin.phpdmin.phpmin.php)
- Day 7: /hate-mail-generator
  -  `curl 'https://hackyholidays.h1ctf.com/hate-mail-generator/new/preview' -H 'Content-Type: application/x-www-form-urlencoded' --data-raw 'preview_markup=Hello+%7B%7Bname%7D%7D+....&preview_data=%7B%22name%22%3A%22%7B%7Btemplate%3A38dhs_admins_only_header.html%7D%7D%22%2C%22email%22%3A%22alice%40test.com%22%7D'`
- Day 8: /forum
  - Github recon: search for "grinch-networks"
  - One username is found [https://github.com/Grinch-Networks](https://github.com/Grinch-Networks)
  - Commit history reveals password [here](https://github.com/Grinch-Networks/forum/commit/efb92ef3f561a957caad68fca2d6f8466c4d04ae)
  - Log into the [phpmyadmin](https://hackyholidays.h1ctf.com/forum/phpmyadmin) with username: `forum` & password: `6HgeAZ0qC9T6CQIqJpD`
  - Get username `grinch` & password `35D652126CA1706B59DB02C93E0C9FBF` which is a hash
  - Use [crackstation](https://crackstation.net/) to get the value `BahHumbug` 
  - Log into the forum with the username: `grinch` & password:`BahHumbug`
  - `curl 'https://hackyholidays.h1ctf.com/forum/3/2' -H 'Cookie: phpmyadmin=98ac2709d3d94e8ba1afefab300deb8e; token=9F315347A655FFDAF70CD4A3529EE8A6`
- Day 9: /evil-quiz
  - Second Order SQLi in `name` parameter
  - use a name like `hax" OR (select 1 from admin)#` to verify the existence of the `admin` table
  - use a name like `hax" OR (select count(password) from admin)#` to verify the column password
 - I decided to bruteforce the password
 - {F1139240} username: `admin` password: `S3creT_p4ssw0rd-$`
- Day 10 /signup-manager
  - [https://hackyholidays.h1ctf.com/signup-manager/README.md](https://hackyholidays.h1ctf.com/signup-manager/README.md) from html source
  - Download [https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip](https://hackyholidays.h1ctf.com/signup-manager/signupmanager.zip)
  - Source Code!
  - Need a username that gets us admin `username#password#cookie#age#firstname#lastname#Y` - note the `Y` at the end
  - If we submit a number that "expands" after being evaluated by `$age = intval($_POST["age"]);` we can "overflow" our `lastname` and end up with an admin account
  - `action=signup&username=1337&password=password&age=1e5&firstname=YYYYYYYYYYYYYYY&lastname=YYYYYYYYYYYYYYY` 
- Day 11: /r3c0n_server_4fdk59
  - SQLi insde more SQLi
  - There's a SQL injection in the hash param: `/r3c0n_server_4fdk59/album?hash=3dir42`
  - {F1139250} - script to bruteforce the username & password: `grinchadmin` : `s4nt4sucks`
  - `curl 'https://hackyholidays.h1ctf.com/attack-box' -H 'Cookie: attackbox=d09d508e78f3975e0199a5e91dde9687`
- Day 12: /attack-box
  - The only thing to try to attack is the hash inside the base64 encoded value that maps the target's ip address
  - Use `hashcat` with the hashes we have alongside some guesses for the salt and the ip addresses we have, our guesses will look like `hash:salt:ip`
  - Use some Christmas keywords like `santa, grinch` from wordlists
  - `5f2940d65ca4140cc18d0878bc398955:mrgrinch463:203.0.113.33` 
  - Now we can sign our payloads with the correct salt, but using `127.0.0.1` stops the attack
  - Use DNS rebinding! - [https://lock.cmpxchg8b.com/rebinder.html](https://lock.cmpxchg8b.com/rebinder.html)
  - `https://hackyholidays.h1ctf.com/attack-box/launch?payload=eyJ0YXJnZXQiOiI3ZjAwMDAwMS43ZjAwMDAwMi5yYm5kci51cyIsImhhc2giOiI1MzE4NDcxODU0MDBhYjkzOWE5Yzc5NzA3NTAzOGIwYiJ9` 
- https://hackyholidays.h1ctf.com/attack-box/challenge-completed-a3c589ba2709

Thanks to everyone who put this together, it was a ton of fun & thanks to the people I asked questions to - ya'll are awesome.

## Impact

HUGE

## Attachments
- ctf.png
- secure-login.rb
- evil-quiz.rb
- r3c0n_server_4fdk59.rb
