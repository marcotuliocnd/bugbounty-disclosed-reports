# upgrade Aspen on inside.gratipay.com to pick up CR injection fix

## Report Details
- **Report ID**: 143139
- **URL**: https://hackerone.com/reports/143139
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-06-04T23:05:22.989Z
- **Disclosed**: 2017-03-22T22:31:09.767Z

## Reporter
- **Username**: valievkarim
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gratipay

## Vulnerability Information
1) Using IE11, open DevTools and start network capture
2) visit the following URL:
http://inside.gratipay.com/assets/%0dSet-Cookie:%20qwe=qwe%0dq

3) find a 'qwe' cookie set in the response

There is a 0x0d character injected, which can be used as a header
delimiter in IE.
To see this behaviour using Curl, you can use the following command:
curl -s -v 'http://inside.gratipay.com/assets/%0dSet-Cookie:%20qwe=qwe%0dq' 2>&1|less

Screenshots of Curl output and DevTools are attached.


## Attachments
- img-2016-06-05-01-06-29.png
- img-2016-06-05-01-09-26.png
