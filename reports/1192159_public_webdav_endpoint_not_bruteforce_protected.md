# public webdav endpoint not bruteforce protected

## Report Details
- **Report ID**: 1192159
- **URL**: https://hackerone.com/reports/1192159
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-05-11T14:23:29.744Z
- **Disclosed**: 2021-08-11T09:19:29.295Z

## Reporter
- **Username**: rtod
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: nextcloud

## Vulnerability Information
Again related to https://hackerone.com/reports/1173684

I am having some trouble finding the code.
However if you do

```
curl -u "RANDOM1:RANDOM2" -X PROPFIND https://server/public.php/webdav
```

And then check your `oc_bruteforce_attempts` table. You'll see there is no entry registered.

## Impact

Low just like on the other report. But should be fixed non the less.

## Attachments
No attachments
