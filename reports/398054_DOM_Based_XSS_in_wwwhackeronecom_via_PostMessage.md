# DOM Based XSS in www.hackerone.com via PostMessage

## Report Details
- **Report ID**: 398054
- **URL**: https://hackerone.com/reports/398054
- **State**: Closed
- **Severity**: low
- **Submitted**: 2018-08-22T08:43:35.166Z
- **Disclosed**: 2019-02-21T04:51:45.159Z

## Reporter
- **Username**: adac95
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: security

## Vulnerability Information
**Summary:**

The Marketo contact form available on the www.hackerone.com website is affected by a cross-site scripting vulnerability, caused by an insecure 'message' event listener installed on the page. Whilst this could allow an attacker to execute JavaScript in the context of the www.hackerone.com application, there were some restrictions which reduced the overall risk presented by the vulnerability.

**Description:**

The Marketo contact form, which can be used by visiting /contact or '#contact/' is implemented using message events sent between the hackerone.com window an embedded Marketo iframe. When the 'submit' button is clicked, a message containing the form data and some other configuration information is sent to the Marketo iframe, which then submits the data to the server. Once this process is complete, the Marketo iframe sends another message back to the hackerone.com window, reporting the success or failure of the submission.

The JavaScript functions used to handle the message events inside the hackerone.com window have been included below. (Note that this code and all other code examples are taken from the unminified version of the Marketo forms2.js script. www.hackerone.com uses the minified version):

```javascript
$(window).on("message", onMessage);
function onMessage (e){
  if(e.originalEvent && e.originalEvent.data){
    var d;
    try {
      d = $.parseJSON(e.originalEvent.data);
    }catch(ex){
      return;
    }
    if(d.mktoReady){
      onReady();
    }else if(d.mktoResponse){
      onResponse(d.mktoResponse)   
    }
  }
}
```

The 'message' event listener is instantiated using JQuery, and is configured to call the onMessage function, which parses the data from a string to an Object and then checks for a 'mktoReady' or a 'mktoResponse' property. If the 'mktoResponse' property is found, the following function is called with the property's value as an argument:

```javascript
function onResponse(mktoResponse){
  var requestId = mktoResponse["for"];
  var request = inflight[requestId];
  if(request){
    if(mktoResponse.error){
      request.error(mktoResponse.data);
    }else{
      request.success(mktoResponse.data);
    }
  }
  delete inflight[requestId];
}
```

Here, a variable 'requestId' is created and set to the value of the 'for' property of the 'mktoResponse' object, and this is then used to retrieve another object from the 'inflight' array. Inspection of the code revealed that the inflight object is created when the form is submitted, and contains two methods which will be called when the form submission is either successful, or when an error has occurred. If the 'mktoResponse' object contains a property named 'error', the inflight 'error' method will be called. Otherwise, the 'success' method is called with the data property as an argument:

```javascript
var success = function (data){
  if(data.error){
    onError(data);
  }else if(data.formId){
    var u = findCorrectFollowUpUrl(data);
    if(false === onSuccess(values, u)){
      return;
    }
    cookieHelper.removeCookieAllDomains("_mkto_purl");
    location.href = u;
  }
}
```

The success function is fairly simple - if there is no error set in the response, it creates a variable named 'u' and sets it to the return value of the 'findCorrectFollowUpUrl' method. This performs some processing on a property named 'followUpUrl' in the response object, which seemed to be a URL to redirect to after the form submission was complete. This was not used by the HackerOne form, but by setting it to an absolute URL, it was possible to control the value of the 'u' variable, which was later used to change the location.href of the window. When the following mktoResponse message was sent to the Hackerone window, the window was redirected to the JavaScript URI, and the code 'alert(document.domain)' was executed by the web browser (screenshot attached):

```javascript
{"mktoResponse":{"for":"mktoFormMessage0","error":false,"data":{"formId":"1013","followUpUrl":"javascript:alert(document.domain);//","aliId":17144124}}}
```

However, there were some limitations to this vulnerability which meant that it was not immediately exploitable. First, redirections to a JavaScript URI are considered equivalent to the execution of inline JavaScript, meaning this redirection was blocked by HackerOne's Content Security Policy. Ordinarily, this type of issue would still be exploitable in a browser which does not support CSP (such as Internet Explorer 11), however there appear to be some functional issues, which mean that the site does not work in IE11. I received the following errors in the developer console, which reported that the JavaScript made use of the 'includes' function, which is not available in IE11, causing an error:

```javascript
SCRIPT438: Object doesn't support property or method 'includes'
js_gSD6OxivXJVJaZwXxHUQz15yz9xczqXghcBxuRO0Ieo.js (43,5)
```

Another limitation was that the user was required to first visit an attacker's website, and submit the contact form (in order for the inflight object to be populated with the success and error functions). However, based on this report (which required the same conditions) I think it is reasonable to assume that this is accepted as a possible scenario: https://hackerone.com/reports/207042

I was able to get this to execute in Firefox, after disabling CSP using a Burp match and replace on response headers (removing ^Content-Security-Policy: .*$), and a PoC which I have attached to this report. The PoC works by convincing the user to open the Hackerone window by clicking a button (the attacker may include some text here asking that the user fill in the form and submit it). The JavaScript SetInterval function is then used to send a message containing the mktoResponse payload to the window every 250 milliseconds - this is necessary because, when the user submits the form, Marketo will respond with its own message. Repeatedly sending messages will ensure that the attacker's payload is processed by the success function before the legitimate Marketo message.

Another potential 'exploit' via this vulnerability, which does not trigger CSP but could allow for phishing attacks to occur, would be the following message:

```javascript
{"mktoResponse":{"for":"mktoFormMessage0","error":false,"data":{"formId":"1013","followUpUrl":"https://attacker.sometld/401.php","aliId":17144124}}}
```

The 401.php page should contain the following content, causing a basic authentication request to show:

```php
<?php
header('WWW-Authenticate: Basic realm="Log in to HackerOne"');
header('HTTP/1.0 401 Unauthorized');
?>
```

In Firefox and Microsoft Edge, when the authentication prompt is shown the www.hackerone.com page is still visible in the background, making it possible that a user may not realise that the authentication prompt is related to a different application. I have attached a screenshot of this behaviour in Firefox.

It should be noted that this could still be exploited in older versions of web browsers which do not support CSP (Chrome/Firefox ~2013 and earlier, for example). Additionally, if changes are made to the www.hackerone.com application which fix the functional issues, allowing the contact form to be used in IE11, this vulnerability could be immediately used to execute XSS against users of IE11.

To fix this, Marketo should add a check in the listener which ensures that all messages received from another window were sent by a trusted origin. In my testing, I only saw messages sent from a subdomain of 'marketo.com', so I would suggest that they either whitelist the subdomains used to host their messaging iframes, or allow messages from all Marketo subdomains. The value of the followUpUrl property should also be validated, to ensure that it is a HTTP/HTTPS URL, to prevent redirection to to a JavaScript URI.

## Impact

An attacker could be able to execute JavaScript in the context of the www.hackerone.com application, if the victim user makes use of a browser which does not support CSP. The attacker could also perform a limited phishing attack in Firefox or Microsoft Edge.

## Attachments
- postMessageXSS.html
- firefox401.PNG
- XSS2.PNG
