# No Rate Limit in email leads to huge Mass mailings

## Report Details
- **Report ID**: 1185903
- **URL**: https://hackerone.com/reports/1185903
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2021-05-06T09:36:50.038Z
- **Disclosed**: 2021-12-09T17:52:55.072Z

## Reporter
- **Username**: sudhakarsurya
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: sifchain

## Vulnerability Information
steps to reproduce:
1.go to https://medium.com/sifchain-finance, click sign in.

2.click sign in with email,enter email and click continue

3.intercept the request in burp, 

POST /m/account/authenticate-email HTTP/2
Host: medium.com
Cookie: optimizelyEndUserId=lo_4bda3b4cea4e; _parsely_visitor={%22id%22:%22pid=13a75549c26a866722a51d135fa2b89c%22%2C%22session_count%22:3%2C%22last_session_ts%22:1620281603472}; _ga=GA1.2.1757937864.1616482301; __cfduid=d0a35a5ebe2e01682dde453715c6515fe1620281559; __cfruid=b11d97eb0fc5c3ee677572c61f2d084d8675c401-1620289698; _parsely_session={%22sid%22:3%2C%22surl%22:%22https://medium.com/sifchain-finance%22%2C%22sref%22:%22%22%2C%22sts%22:1620281603472%2C%22slts%22:1616564318272}; lightstep_guid/lite-web=22de58625d1cfa62; lightstep_session_id=345c4f5a2565f1b5; _gid=GA1.2.1621057179.1620283390; lightstep_guid/medium-web=bb0c0eec415c9462; sz=1349; pr=1; tz=-60; uid=lo_99337b8e9a5c; sid=1:l7Xj/X4Y4ywkRvuW4AtGejuh54gTE6EKvj0sx87VwldyYk6AnotlImzfa574rnW5; _parsely_slot_click={%22url%22:%22https://medium.com/sifchain-finance%22%2C%22x%22:1026%2C%22y%22:21%2C%22xpath%22:%22//*[@id=%5C%22_obv.shell._surface_1620288206500%5C%22]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/a[1]%22%2C%22href%22:%22https://medium.com/m/signin?redirect=https%253A%252F%252Fmedium.com%252Fsifchain-finance&source=--------------------------nav_reg&operation=login%22}
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0
Accept: application/json
Accept-Language: en-GB,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://medium.com/sifchain-finance
X-Obvious-Cid: web
X-Xsrf-Token: 1
X-Client-Date: 1620290904212
Content-Type: application/json
Content-Length: 161
Origin: https://medium.com
Te: trailers
Connection: close

{"email":"loyixac322@ffuqzt.com","redirect":"https://medium.com/sifchain-finance?source=--------------------------nav_reg","operation":"login","captchaValue":""}


4.now send the request to intruder and set as sending more than 50 mails.

5.see you will get 200 OK status coding & 50 plus emails in your inbox.

## Impact

IMMPACT:
    trouble to users on the website because huge email bombing can be done by because  of this bug.


attachments:

## Attachments
- bandicam_2021-05-06_09-56-39-426.jpg
- temp-mail.org_nl.png
