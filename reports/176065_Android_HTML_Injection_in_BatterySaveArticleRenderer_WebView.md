# [Android] HTML Injection in BatterySaveArticleRenderer WebView

## Report Details
- **Report ID**: 176065
- **URL**: https://hackerone.com/reports/176065
- **State**: Closed
- **Severity**: high
- **Submitted**: 2016-10-16T00:14:18.358Z
- **Disclosed**: 2018-10-22T19:51:14.435Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:

HTML Injection in BatterySaveArticleRenderer WebView.

## Products affected: 

 * Android Brave Browser 1.9.56

## Steps To Reproduce:

 * Open https://blackfan.ru/brave or html

```html
<script>
location="https://www.google.com/search?q=</title><h1><marquee><s>Injection<!--"
</script>
```
* Wait for a full load
* Click on ArticleModeButton

## Supporting Material/References:

Vulnerable code:
```java
public class aot
...
// s7 == title
if(s7 != null)
{
  s4 = (new StringBuilder()).append(s5).append("<title>").append(s7).append("</title>").toString();
  s1 = (new StringBuilder()).append(s6).append("<p style=\"font-size:").append(s1).append(";line-height:120%;font-weight:bold;margin:").append(s3).append(" 0px 12px 0px\">").append(s7).append("</p>").toString();
...
// s8 == authorName
if(s8 != null)
  s1 = (new StringBuilder()).append("<span class=\"nowrap\"><b>").append(s8).append("</b>,</span> ").toString();
```


## Attachments
- Screenshot_20161016-041209.png
- Screenshot_20161016-041215.png
