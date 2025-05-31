# Local File Inclusion path bypass

## Report Details
- **Report ID**: 147570
- **URL**: https://hackerone.com/reports/147570
- **State**: Closed
- **Severity**: N/A
- **Submitted**: 2016-06-27T00:36:05.950Z
- **Disclosed**: 2016-08-19T00:17:46.666Z

## Reporter
- **Username**: paulos__
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: concretecms

## Vulnerability Information
Hey,

After reading egix's report #59665 and seeing your fix at https://github.com/concrete5/concrete5/commit/19d0cc81c7cd485b856289ac71ebc0389ea7c3da & https://github.com/concrete5/concrete5/commit/c646dd0defcfa79ef119dca8ba1beba2c5bc91ea I think the fixes are insufficient to stop lfi.

If you are going to stick with the `strpos()` trick, you missed something. 
```php
$path = $request->getPathInfo();
$path = rawurldecode($request->getPathInfo());
 if (substr($path, 0, 3) == '../' || substr($path, -3) == '/..' || strpos($path, '/../') ||
     substr($path, 0, 3) == '..\\' || substr($path, -3) == '\\..' || strpos($path, '\\..\\')) {
``` 
while that is one way to go. you forgot about "../\", " ..\/", "/\.." & "\/.." this works because some oses (unix like) parse the backslash to forward slash and proceed. add those and I think you should be fine. :)

Thanks,
P

## Attachments
No attachments
