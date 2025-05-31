# Fix for self-DoS in Security-txt Chrome Extension.

## Report Details
- **Report ID**: 299460
- **URL**: https://hackerone.com/reports/299460
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-12-19T19:53:35.691Z
- **Disclosed**: 2017-12-19T20:11:04.415Z

## Reporter
- **Username**: karel_origin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
@sp1d3rs found a self-DoS vulnerability in the Security-txt Chrome Extension. He was also kind enough to provide a fix wich you can find on [GitHub](https://github.com/securitytxt/chrome-extension/pull/2). We merged @sp1d3rs' fix when he submitted a PR. We later decided that it was better to stop using XHR and use Fetch instead, a newer API. This was the result:

background.js
========
~~~diff
     }
 }
 
-function getSecuritytxt(domain, protocol, wk, tabid) {
-    xhr = new XMLHttpRequest;
-    xhr.open("GET", protocol + domain + wk + 'security.txt');
-    xhr.timeout = 10000;
-    xhr.onreadystatechange = function() {
-        if (xhr.status != 404 && xhr.getResponseHeader('content-type').startsWith('text/plain') && xhr.responseText.indexOf('Contact:') != -1) {
-            UpdateStorage('hasSecuritytxt', 'set', domain + ':' + wk);
-            changeIcon(tabid, true);
-        } else {
-            changeIcon(tabid, false);
-            return false
+function getSecuritytxt(url, domain, tabid, i, messaged) {
+    const consume = responseReader => {
+    return responseReader.read().then(result => {
+        if (result.done || chunks == 1) { return; }
+        const chunk = result.value;
+        chunks++
+
+        if(chunk.length > 500){
+            UpdateStorage("blacklist", "add", domain)
+            setTimeout(function(){chrome.runtime.reload()}, 2000)
+            console.warn("Detected a large security.txt file, reloading the extension and blacklisting the domain.")
+        }
+
+        if (new TextDecoder("utf-8").decode(chunk).indexOf("Contact:") > -1) {
+            response_string = new TextDecoder("utf-8").decode(chunk)
+        }
+
+        if (typeof messaged == "undefined"){
+            if (typeof response_string != "undefined") {
+                changeIcon(tabid, true)
+                obj = new Object; obj[domain] = locations[i]
+                UpdateStorage("hasSecuritytxt", "set", obj)
+            } else if(i == locations.length - 1) {
+                changeIcon(tabid, false)
+            }
+        }else{
+            chrome.runtime.sendMessage({"content": response_string})
         }
-    };
-    xhr.send();
+
+        return consume(responseReader);
+        });
+    }
+    if(storage.blacklist.indexOf(domain) == -1) {
+        fetch(url).then(response => {
+            chunks = 0
+            if (response.status == 200 && response.headers.get("content-type").indexOf("text/plain") > -1 && response.redirected == false) {
+                setTimeout(function(){return consume(response.body.getReader())}, 200)
+            } else {
+                changeIcon(tabid, false)
+            }
+        }
+    )}
 }
 
 function UpdateStorage(path, action, value) {
     chrome.storage.local.get(function(callback) {
         storage = callback;
         if (Object.keys(storage).length == 0) {
             chrome.storage.local.set({
-                "hasSecuritytxt": [],
-                "location": []
+                "hasSecuritytxt": {},
+                "blacklist": []
             })
         };
-        if (path == 'hasSecuritytxt') {
-            if (action == 'set' && storage.hasSecuritytxt.indexOf(value.split(':')[0]) < 0) {
-                storage.hasSecuritytxt.push(value.split(':')[0]);
-                storage.location.push(value.split(':')[1])
+        if (path == "hasSecuritytxt") {
+            if(action == "set") {
+                storage.hasSecuritytxt[Object.keys(value)[0]] = value[Object.keys(value)[0]]
             }
-        };
+        }else if (path == "blacklist") {
+            if (action == "add") {
+                storage.blacklist.push(value)
+            }
+        }
         chrome.storage.local.set(storage);
     })
 }
 
 chrome.runtime.onMessage.addListener(function(message, sender, response) {
-    if (message.securityTxt != undefined && message.securityTxt) {
-        if (getSecuritytxt(message.securityTxt[0].domain, message.securityTxt[0].protocol, "/", sender.tab.id) == false) {
-            getSecuritytxt(message.securityTxt[0].domain, message.securityTxt[0].protocol, "/.well-known/", sender.tab.id)
+    locations = ["/security.txt", "/.well-known/security.txt"]
+    if (message.securityTxt != undefined && message.securityTxt.popup == undefined) {
+        for(i = 0; i < locations.length; i++) {
+            getSecuritytxt(message.securityTxt.root.concat(locations[i]), message.securityTxt.root.split('/')[2], sender.tab.id, i)
+        }
+    }else if (message.securityTxt != undefined && message.securityTxt.popup) {
+        for(i = 0; i < locations.length; i++) {
+            getSecuritytxt(message.securityTxt.root.concat(locations[i]), message.securityTxt.root.split('/')[2], null, i, true)
         }
     }
 })
 
 chrome.storage.onChanged.addListener(function() {
     UpdateStorage()
 });
-UpdateStorage();
+
+UpdateStorage(); 
~~~

Let me explain everything a bit more for those of you who don't know/understand JavaScript very well (you really should learn it! :)). XHR is the root cause of this issue because of the way it handles responses. 

New features in the Fetch API:
>We are now able to buffer data as it comes in, and we don’t have to wait until it’s all there. Streaming the response body improves the site’s memory usage and gives a greater perception of speed when trying to show content over slow connections. In XHR, the whole response would be buffered, rather than being able to operate on the data in chunks.

Source: [blogs.windows.com](https://blogs.windows.com/msedgedev/2016/05/24/fetch-and-xhr-limitations/)

The buffering of XHR requires a lot of the available system resources, especially on lower-end PCs/laptops, potentially causing crashes with large files. You can see how I'm reading the data chunk-by-chunk in the `getSecuritytxt` function.

```
function getSecuritytxt(url, domain, tabid, i, messaged) {
    const consume = responseReader => {
    return responseReader.read().then(result => {
        //Only handle the first chunk.
        if (result.done || chunks == 1) { return; }
        const chunk = result.value;
        chunks++
        //Reload the extension if the chunk is larger than 500 bytes and blacklist the domain.
        if(chunk.length > 500){
            UpdateStorage("blacklist", "add", domain)
            setTimeout(function(){chrome.runtime.reload()}, 2000)
            console.warn("Detected a large security.txt file, reloading the extension and blacklisting the domain.")
        }
        //Convert the Uint8Array to a string.
        if (new TextDecoder("utf-8").decode(chunk).indexOf("Contact:") > -1) {
            response_string = new TextDecoder("utf-8").decode(chunk)
        }

        if (typeof messaged == "undefined"){
            if (typeof response_string != "undefined") {
                changeIcon(tabid, true)
                obj = new Object; obj[domain] = locations[i]
                UpdateStorage("hasSecuritytxt", "set", obj)
            } else if(i == locations.length - 1) {
                changeIcon(tabid, false)
            }
        }else{
            chrome.runtime.sendMessage({"content": response_string})
        }
...
```

`if (result.done || chunks == 1) { return; }` makes sure that we only handle one chunk, because one chunk will be big enough for the entire security.txt file.

```
if(chunk.length > 500){
     UpdateStorage("blacklist", "add", domain)
     setTimeout(function(){chrome.runtime.reload()}, 2000)
     console.warn("Detected a large security.txt file, reloading the extension and blacklisting the domain.")
 }
```
This will check if the chunk is larger than 500 bytes, it will also add it to a blacklist if it is. I used `chrome.runtime.reload()` because at this moment, there's no way to cancel a Fetch request in Chrome, only in FireFox and Edge, so I'm reloading the entire extension to cancel it which seems to work fine. Otherwise, the request will just keep on going, even if I'm not doing anything with the received data.

```
if (typeof messaged == "undefined"){
     if (typeof response_string != "undefined") {
          changeIcon(tabid, true)
          obj = new Object; obj[domain] = locations[i]
          UpdateStorage("hasSecuritytxt", "set", obj)
      } else if(i == locations.length - 1) {
          changeIcon(tabid, false)
      }
} else {
    chrome.runtime.sendMessage({"content": response_string})
}
```

This saves the domain to a list of domains with security.txt files, if it is valid, and passes the contents of the file to the extension popup (the window you see after clicking on an extension's icon).

The changes made to content.js and popup.js aren't required to fix this issue, but they are required for the extension to function correctly after implementing the fix.

Thank you @sp1d3rs for reporting this issue, and helping me fix it. Also thanks to @edio (@edoverflow) for his kind words and compliments. :)

I hope that this motivates others to test this extension and look at Ed's program
Happy hacking!

~ Karel.

## Impact

.

## Attachments
No attachments
