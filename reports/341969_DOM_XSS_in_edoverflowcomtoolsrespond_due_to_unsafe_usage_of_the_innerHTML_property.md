# DOM XSS in edoverflow.com/tools/respond due to unsafe usage of the innerHTML property.

## Report Details
- **Report ID**: 341969
- **URL**: https://hackerone.com/reports/341969
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-04-23T11:01:15.691Z
- **Disclosed**: 2018-04-23T11:28:11.422Z

## Reporter
- **Username**: karel_origin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: ed

## Vulnerability Information
Hi,

There's a DOM XSS vulnerability on [edoverflow.com](https://edoverflow.com/tools/respond/). This cannot be exploited without user-interaction so I had to make a clickjacking PoC to trick the user in triggering the payload her/himself.

#Reproduction Steps
1. Open the attached HTML document in FireFox.
2. Drag Frog 1 to the other (two) frogs.
3. Click on the "Make friends!" button.

Result: 
{F289573}

# Vulnerable JavaScript

```
<html>
<script>
/* ===========================================
  Allow users to submit usernames and store 
  them in localStorage for future use.
============================================*/
document.getElementById("form").addEventListener("submit", function(){
    var triager = document.getElementById("triager").value;
    var hacker = document.getElementById("hacker").value;
    console.log(hacker); // Why is this not executing?
    document.body.innerHTML = document.body.innerHTML.replace('{{triager}}', triager);
    document.body.innerHTML = document.body.innerHTML.replace('{{username}}', hacker);
    //localStorage.setItem("triager", triager);

//var retrieve = localStorage.getItem("triager"); // Why does this return "null"?
//document.body.innerHTML = document.body.innerHTML.replace('{{triager}}', retriev
document.getElementById("remove").addEventListener("click", function(){
    localStorage.removeItem("triager");
});
</script>
</html>
```

#Fix

~~~diff
- <input type="submit" name="submit" class="button">
+ <input type="button" class="button" id="submit">
~~~

~~~diff
       Allow users to submit usernames and store 
       them in localStorage for future use.
     ============================================*/
-    document.getElementById("form").addEventListener("submit", function(){
-        var triager = document.getElementById("triager").value;
-        var hacker = document.getElementById("hacker").value;
+       elem = document.getElementsByTagName("pre")[0].children[0];
+
+    document.getElementById("submit").addEventListener("click", function(){
+        var trger = document.getElementById("triager").value;
+        var hckr = document.getElementById("hacker").value;
         console.log(hacker); // Why is this not executing?
-        document.body.innerHTML = document.body.innerHTML.replace('{{triager}}', triager);
-        document.body.innerHTML = document.body.innerHTML.replace('{{username}}', hacker);
-        //localStorage.setItem("triager", triager);
+               elem.innerText = elem.innerText.replace("{{username}}", trger).replace("{{triager}}", hckr);
+        localStorage.setItem("triager", trger);
     });
 
-    //var retrieve = localStorage.getItem("triager"); // Why does this return "null"?
-    //document.body.innerHTML = document.body.innerHTML.replace('{{triager}}', retrieve);
+    if(localStorage.getItem("triager") != null) {
+       var trger = localStorage.getItem("triager"); // Why does this return "null"?
+       elem.innerText = elem.innerText.replace("{{triager}}", trger);
+    }
 
     document.getElementById("remove").addEventListener("click", function(){
         localStorage.removeItem("triager");
     });

~~~

Raw (JS attached)

## Impact

There is not much that can be done because it looks like most pages don't require authentication, I also don't think that the owner of this website would fall for something like this. ;)


Thanks,
Karel.

The hacker selected the **Cross-site Scripting (XSS) - DOM** weakness. This vulnerability type requires contextual information from the hacker. They provided the following answers:

**URL**
https://edoverflow.com/tools/respond/

**Verified**
Yes



## Attachments
- fix.js
- screenshot.PNG
- Clickjacking-XSS.html
