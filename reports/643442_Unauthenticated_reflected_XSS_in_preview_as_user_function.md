# Unauthenticated reflected XSS in preview_as_user function

## Report Details
- **Report ID**: 643442
- **URL**: https://hackerone.com/reports/643442
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2019-07-15T11:36:41.063Z
- **Disclosed**: 2019-12-06T15:48:41.839Z

## Reporter
- **Username**: arcturian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
An unauthenticated, reflected cross-site-scripting attack is possible due to the unsanitised `cID` parameter in the preview_as_user functionality.

Example URL: `https://LOCAL-CONCRETE-INSTALL/ccm/system/panels/page/preview_as_user/preview?cID=%22%3E%3C/iframe%3E%3Cscript%3Ealert(1)%3C/script%3E%3C!--`

The error is in the `concrete/views/panels/page/preview_as/frame.php` file, line 4:
```
[..]
src="<?= URL::to('/ccm/system/panels/page/preview_as_user/render') . '?&cID=' . Request::request('cID') ?>
[..]
```

Solutions would be to either cast this value to an int with `intval()`, or pass the value through `htmlentities()` before rendering it. Or both!

## Impact

An attacker could steal cookies or perform actions on other users behalf.

## Attachments
- xss-example.PNG
