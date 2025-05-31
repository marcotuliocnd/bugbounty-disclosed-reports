# redirect_to(["string"]) remote code execution

## Report Details
- **Report ID**: 1106652
- **URL**: https://hackerone.com/reports/1106652
- **State**: Closed
- **Severity**: low
- **Submitted**: 2021-02-18T16:40:59.177Z
- **Disclosed**: 2021-05-07T23:01:09.877Z

## Reporter
- **Username**: gmcgibbon
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: rails

## Vulnerability Information
For example, `redirect_to(params[:user_input])`  with a URL of `?user_input[]=something` calls the method `something_url` and tries to redirect the return value of the method. If this call is on an unauthenticated route, it would allow an external user to test if a route name exists by determining if the app 500s  (the method does not exist) or successfully redirects.

## Impact

Any public method defined on a controller ending with `_url` could be remotely executed.

## Attachments
No attachments
