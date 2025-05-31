# Window.opener protection  Bypass

## Report Details
- **Report ID**: 306414
- **URL**: https://hackerone.com/reports/306414
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2018-01-18T19:32:10.878Z
- **Disclosed**: 2018-02-17T20:25:25.864Z

## Reporter
- **Username**: ranjit_p
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: phabricator

## Vulnerability Information
SUMMURY
========
If you create a post/comment with a link  like http://x.com in fabricator then server add ```rel="norefferrer"``` to anchor tag . So child window dont have access to parent window.
But it can be bypassed with url like ```/\x.com/index.php``` and child window can change the location property of parent window.

STEP TO REPRODUCE
========================
1. goto http://domain/w/  and create new document.

2. Now paste  this code in content
```
[[ /\jackluru02.000webhostapp.com/tabnabbing.html | click_me ]]
```

code of this my url is
 ```
<script>
window.opener.location.replace('http://example.com');
</script>
```

3. now save it and share this document to other user.

4. When user click this click , malicious link opened in new window and parent window location will be changed.

{F255328}

## Impact

attacker can perform malicious activity to other user using this attack.

```
mongoose
```

## Attachments
- Screenshot_-_Jan_18__2018_2.23_PM.png
