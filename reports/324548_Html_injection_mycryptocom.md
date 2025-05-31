# Html injection mycrypto.com

## Report Details
- **Report ID**: 324548
- **URL**: https://hackerone.com/reports/324548
- **State**: Closed
- **Severity**: high
- **Submitted**: 2018-03-12T09:13:00.824Z
- **Disclosed**: 2018-03-16T17:51:25.344Z

## Reporter
- **Username**: w2w
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: mycrypto

## Vulnerability Information
Hello. I remembered that a couple of months ago I found an HTML injection vulnerability on myetherwallet.com, I sent it, but my message was ignored.
Since you have the same interface, I decided to check this vulnerability on your site and it was reproduced. The vulnerability works both on www.mycrypto.com and on mycrypto.com.
Html injection is in a pop-up message

 <div class = "alert-message ng-binding" ng-bind-html = "alert.message"> You are successfully connected
<br> URL: <strong> https://www.mycrypto.com/?txHash=qwqwq%3C%20SRC=%22jav
ascript: alert (0); "& gt; <a href="https://securityz.net"> <img src =" https://securityz.net/mycrypto.jpeg "> </a> qwqw # check- tx-status </ strong> <br> Network: <strong> ETH </ strong> provided by <strong> mycryptoapi.com </ strong> </ div>

Unfortunately, you have filtering there, I could not execute js and could hardly display a picture with href on the page. 
## PoC
 https://mycrypto.com/?txHash=qwqwq%3C%20SRC=%22jav&#x0D;ascript:alert(0);"> <a href="https://securityz.net"><img src="https://securityz.net/mycrypto.jpeg"></a>qwqw#check-tx-status 

##PoC video
 https://www.youtube.com/watch?v=JmP9AU8sX5k .
##Impact
Since your site and myetherwallet are often subjected to phishing attacks, this vulnerability is dangerous. You can put in the href url of the phishing site, then you can steal the private key of the victim. Perhaps you can upload js to the site, but I could not do it.

## Impact

Since your site and myetherwallet are often subjected to phishing attacks, this vulnerability is dangerous. You can put in the href url of the phishing site, then you can steal the private key of the victim. Perhaps you can upload js to the site, but I could not do it.

## Attachments
- hh.png
