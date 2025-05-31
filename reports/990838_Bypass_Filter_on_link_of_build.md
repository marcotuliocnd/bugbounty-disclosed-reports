# Bypass Filter on link of build

## Report Details
- **Report ID**: 990838
- **URL**: https://hackerone.com/reports/990838
- **State**: Closed
- **Severity**: low
- **Submitted**: 2020-09-25T03:39:55.381Z
- **Disclosed**: 2020-09-28T08:36:06.336Z

## Reporter
- **Username**: khoabda1
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: cs_money

## Vulnerability Information
## Summary:
Hello team, I found that a valid build will have a link with the following format

```
https://3d.cs.money/item/0UkWN8vh2R
```

If you save a build with `/api/build/save`. It will return a link to sync with your save builds
The bug occurs when web app sync, you can custom the link of build with whatever you want with the format 

```
//YOUR_LINK/item/WHAT_EVER_YOU_WANT
```

## Steps To Reproduce:
[add details for how we can reproduce the issue]

- Make a build. Save build. Intercept request sync
- Edit request sync. For example:

```
POST /sync HTTP/1.1
Host: 3d.cs.money
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0
Accept: application/json, text/plain, */*
Accept-Language: vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3
Content-Type: application/json;charset=utf-8
Content-Length: 3455
Origin: https://3d.cs.money
Connection: close
Referer: https://3d.cs.money/item/0UkWN8vh2R
Cookie: __cfduid=dd4a5ae822200c2e5a6622942c8e9b5c61600828055; TEST_GROUP=6; UUID3D=z8yNnunP7rEULv4; _ga=GA1.1.123687832.1600828067; _ga_HY7CCPCD7H=GS1.1.1600999331.12.1.1600999740.56; _gid=GA1.2.745101638.1600828070; language=en; sellerid=2351662; theme=darkTheme; pro_version=false; tmr_reqNum=84; tmr_lvid=a86af86a1e546621ee998805dedf795e; tmr_lvidTS=1600829462593; _ym_uid=1600829464576681153; _ym_d=1600829464; prism_89846284=886529b3-1b72-491d-8e3e-fb061941ce6b; amplitude_id_222f15bd4f15cdfaee99c07bcc641e5fcs.money=eyJkZXZpY2VJZCI6ImJlNWM1YjhmLWE3OTQtNDZiNC1iMzg5LWU2MzljYThkZTNiNlIiLCJ1c2VySWQiOiI3NjU2MTE5ODM4OTQwODM5MiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMDk1MzY5NTUyOCwibGFzdEV2ZW50VGltZSI6MTYwMDk1Mzc5MzEyNywiZXZlbnRJZCI6NDAsImlkZW50aWZ5SWQiOjE4LCJzZXF1ZW5jZU51bWJlciI6NTh9; _fbp=fb.1.1600829468046.1736484188; csmoney_ga=GA1.2.348732095.1600829528; csmoney_ga_gid=GA1.2.929098124.1600829528; type_device=desktop; support_token=6f4a7515e3000799c5b9ffc20b3bdb808e065ec4a7d77c557bf14b72922136d9; amplitude_id_c14fa5162b6e034d1c3b12854f3a26f5cs.money=eyJkZXZpY2VJZCI6IjU0MTdhZjg4LTE0NDgtNDg3NC05YmNkLTFmMjczOGIwY2EyZFIiLCJ1c2VySWQiOiI3NjU2MTE5ODM4OTQwODM5MiIsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTYwMDk1MzYyMjg4MSwibGFzdEV2ZW50VGltZSI6MTYwMDk1MzYyMjg4MywiZXZlbnRJZCI6Mjk5LCJpZGVudGlmeUlkIjo0LCJzZXF1ZW5jZU51bWJlciI6MzAzfQ==; amp_d77dd0=nCXsKPRaEaZ_9OrPDjz6cM...1ej04bc91.1ej04d4lf.0.1.1; amp_d77dd0_cs.money=nCXsKPRaEaZ_9OrPDjz6cM...1ej04bc98.1ej04frr7.1p.2.1q; steamid=76561198389408392; avatar=https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/9e/9e972864d883f1b2e12cde94c8f83ef005c22438_medium.jpg; username=khoadeptrai; thirdparty_token=83a3e70e33f5a91ced64ee3a0fd005d80e119cb762c2d82449707c0eba6efcf1; trade_link=https%3A%2F%2Fsteamcommunity.com%2Ftradeoffer%2Fnew%2F%3Fpartner%3D429142664%26token%3DI1hTESVQ; _privy_undefined=%7B%22uuid%22%3A%22aa550b56-d1d7-425a-a4f8-28b3b53d6a71%22%7D; _privy_0A13181283E3DE28238D8AB1=%7B%22uuid%22%3A%22aa550b56-d1d7-425a-a4f8-28b3b53d6a71%22%2C%22variations%22%3A%7B%7D%2C%22country_code%22%3A%22VN%22%2C%22region_code%22%3A%22VN_35%22%2C%22postal_code%22%3A%22%22%7D

{"backgrounds":["/assets/images/back3.jpeg"],"builds":[{"href":"//asd.com/item1/cc","name":"AK-47 | Redline (Minimal Wear)\"","date":1601000408019}],"edition":1}
```

PoC
{F1002083}

## Impact

Bypass the format (regex?) on the link of  a build

## Attachments
- Screenshot_4.png
