# JavaScript URL Issues in the latest version of Brave Browser

## Report Details
- **Report ID**: 176083
- **URL**: https://hackerone.com/reports/176083
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2016-10-16T04:20:48.479Z
- **Disclosed**: 2016-10-17T20:10:50.552Z

## Reporter
- **Username**: smelt
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: brave

## Vulnerability Information
## Summary:
* The URL javascript: can redirect users to any site, instead of executing JavaScript.

## Additional Notes
* Found as partners by @kicker (http://hackerone.com/kicker) and myself (@smelt).

## Products affected: 
* The current version of Brave Browser on Windows.
* The current mobile version of Brave Browser.

## Steps To Reproduce:
* Open Brave Browser
* Go to javascript:javascript: or javascript:javascript:hackerone.com in the Brave Browser.
* If using the **javascript:javascript:** link, the browser should redirect to your search engine's homepage.
* If using the **javascript:javascript:hackerone.com** link, the browser should redirect to HackerOne. (HackerOne was just an option, you can redirect to any URL.)

* This bug is different than the redirection bug previously disclosed, allowing addresses after @ to redirect to that site. The site can be redirected using simply the javascript: URL in this bug.

## Supporting Material/References:
* See attached video files.

Thanks for reviewing this report, and let me cross my fingers, that it's not a duplicate! :)


## Attachments
- Brave_Javascript_Redirect_Bug.mp4
- Brave_Browser_Javascript_Bug.mp4
